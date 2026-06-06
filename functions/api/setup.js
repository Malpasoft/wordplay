// Word Play Setup Endpoint — Bootstrap initial admin account
// GET /api/setup?password=youradminpassword
// One-time use only. After setup, this endpoint should be deleted or disabled.
// Safety: Only works if users table is empty.

// PBKDF2 password hash using Web Crypto API
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

export async function onRequestGet(context) {
  try {
    const url = new URL(context.request.url);
    const password = url.searchParams.get('password');
    const email = url.searchParams.get('email') || 'admin@wordplay.local';

    if (!password || password.length < 8) {
      return new Response(
        JSON.stringify({ error: 'Password required (min 8 chars). Usage: /api/setup?email=admin@example.com&password=yoursecurepassword' }),
        { status: 400, headers: { 'Content-Type': 'application/json' } }
      );
    }

    // Check if any users exist
    const existingUser = await context.env.DB.prepare('SELECT COUNT(*) as cnt FROM users').first();

    if (existingUser && existingUser.cnt > 0) {
      return new Response(
        JSON.stringify({ error: 'Setup already completed. Users table is not empty. Delete /api/setup.js from your Workers to prevent re-initialization.' }),
        { status: 403, headers: { 'Content-Type': 'application/json' } }
      );
    }

    // Generate random salt (8 characters)
    const saltChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let salt = '';
    const saltBytes = crypto.getRandomValues(new Uint8Array(8));
    for (let i = 0; i < 8; i++) {
      salt += saltChars[saltBytes[i] % saltChars.length];
    }

    // Hash password with salt
    const hash = await hashPassword(password, salt);
    const passwordHash = hash + ':' + salt;

    // Insert admin user
    const result = await context.env.DB.prepare(
      'INSERT INTO users (email, password_hash, role) VALUES (?, ?, ?)'
    )
      .bind(email, passwordHash, 'admin')
      .run();

    return new Response(
      JSON.stringify({
        success: true,
        message: 'Admin account created successfully',
        email: email,
        userId: result.meta.last_row_id,
        instruction: 'Visit /login.html and sign in with your email and password. Then DELETE /api/setup.js from your Workers to prevent unauthorized access.'
      }),
      { status: 200, headers: { 'Content-Type': 'application/json' } }
    );
  } catch (error) {
    console.error('Setup error:', error);
    return new Response(
      JSON.stringify({ error: 'Setup failed: ' + error.message }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }
}
