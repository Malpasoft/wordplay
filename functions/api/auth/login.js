// Word Play Auth API — Login endpoint
// POST /api/auth/login
// Request: { email, password }
// Response: { token, user_id, email, role } or { error }

// PBKDF2 password hash using Web Crypto API (Cloudflare Workers)
async function hashPassword(password, salt) {
  const encoder = new TextEncoder();
  const keyMaterial = await crypto.subtle.importKey(
    'raw',
    encoder.encode(password),
    { name: 'PBKDF2' },
    false,
    ['deriveBits']
  );
  const bits = await crypto.subtle.deriveBits(
    {
      name: 'PBKDF2',
      hash: 'SHA-256',
      salt: encoder.encode(salt),
      iterations: 100000
    },
    keyMaterial,
    256
  );
  const view = new Uint8Array(bits);
  return Array.from(view).map(b => b.toString(16).padStart(2, '0')).join('');
}

// Verify password
async function verifyPassword(password, hash, salt) {
  const computed = await hashPassword(password, salt);
  return computed === hash;
}

// Generate random 32-byte hex token
function generateToken() {
  const bytes = crypto.getRandomValues(new Uint8Array(32));
  return Array.from(bytes).map(b => b.toString(16).padStart(2, '0')).join('');
}

export async function onRequestPost(context) {
  try {
    const body = await context.request.json();
    const { email, password } = body;

    if (!email || !password) {
      return new Response(
        JSON.stringify({ error: 'Email and password are required.' }),
        { status: 400, headers: { 'Content-Type': 'application/json' } }
      );
    }

    // Query user from D1
    const user = await context.env.DB.prepare(
      'SELECT * FROM users WHERE email = ?'
    )
      .bind(email.toLowerCase())
      .first();

    if (!user) {
      return new Response(
        JSON.stringify({ error: 'Invalid email or password.' }),
        { status: 401, headers: { 'Content-Type': 'application/json' } }
      );
    }

    // Verify password (stored as "hash:salt" in password_hash column)
    const [hash, salt] = user.password_hash.split(':');
    const isValid = await verifyPassword(password, hash, salt);

    if (!isValid) {
      return new Response(
        JSON.stringify({ error: 'Invalid email or password.' }),
        { status: 401, headers: { 'Content-Type': 'application/json' } }
      );
    }

    // Generate token (7 days = 604800 seconds)
    const token = generateToken();
    const expiresAt = Date.now() + 7 * 24 * 60 * 60 * 1000;

    // Store token in auth_tokens table
    await context.env.DB.prepare(
      'INSERT INTO auth_tokens (user_id, token, expires_at) VALUES (?, ?, ?)'
    )
      .bind(user.id, token, expiresAt)
      .run();

    // Return success
    return new Response(
      JSON.stringify({
        token: token,
        user_id: user.id,
        email: user.email,
        role: user.role,
        target_lang: user.target_lang || null,
        l1: user.l1 || null
      }),
      { status: 200, headers: { 'Content-Type': 'application/json' } }
    );
  } catch (error) {
    console.error('Login error:', error);
    return new Response(
      JSON.stringify({ error: 'Internal server error.' }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }
}
