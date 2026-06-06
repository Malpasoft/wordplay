// Word Play Auth API — Signup endpoint
// POST /api/auth/signup
// Request: { email, password, level }
// Response: { token, user_id, email, role, level } or { error }

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

// Generate random 32-byte hex token
function generateToken() {
  const bytes = crypto.getRandomValues(new Uint8Array(32));
  return Array.from(bytes).map(b => b.toString(16).padStart(2, '0')).join('');
}

// Validate email format
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

// Rate limiting via D1: max 5 signups per IP per hour (persistent across restarts)
async function checkRateLimit(ip, db) {
  const now = Date.now();
  const oneHourAgo = now - 3600000;

  // Count attempts in the last hour
  const result = await db.prepare(
    'SELECT COUNT(*) as count FROM rate_limit_log WHERE ip = ? AND endpoint = ? AND timestamp > ?'
  )
    .bind(ip, 'signup', oneHourAgo)
    .first();

  const recentCount = result?.count || 0;

  if (recentCount >= 5) {
    return false; // Rate limit exceeded
  }

  // Log this attempt
  try {
    await db.prepare(
      'INSERT INTO rate_limit_log (ip, endpoint, timestamp) VALUES (?, ?, ?)'
    )
      .bind(ip, 'signup', now)
      .run();
  } catch (e) {
    // If logging fails, don't block the request (fail open for availability)
    console.warn('Rate limit logging failed:', e.message);
  }

  return true;
}

// Get client IP from request
function getClientIP(request) {
  return (
    request.headers.get('cf-connecting-ip') ||
    request.headers.get('x-forwarded-for') ||
    'unknown'
  ).split(',')[0].trim();
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' }
  });
}

export async function onRequestPost(context) {
  try {
    const body = await context.request.json();
    const { email, password, level } = body;

    // Validate inputs
    if (!email || !password || !level) {
      return json({ error: 'Email, password, and level are required.' }, 400);
    }

    if (!isValidEmail(email)) {
      return json({ error: 'Invalid email format.' }, 400);
    }

    if (password.length < 8) {
      return json({ error: 'Password must be at least 8 characters.' }, 400);
    }

    // Validate level
    const validLevels = ['a1', 'a2', 'b1', 'b2', 'c1', 'c2'];
    if (!validLevels.includes(level.toLowerCase())) {
      return json({ error: 'Invalid level.' }, 400);
    }

    // Rate limiting by IP (persistent in D1)
    const clientIP = getClientIP(context.request);
    const rateLimitOK = await checkRateLimit(clientIP, context.env.DB);
    if (!rateLimitOK) {
      return json(
        { error: 'Too many signup attempts. Please try again in an hour.' },
        429
      );
    }

    const emailLower = email.toLowerCase();

    // Check if email already exists (prevent enumeration by not revealing)
    const existingUser = await context.env.DB.prepare('SELECT id FROM users WHERE email = ?')
      .bind(emailLower)
      .first();

    if (existingUser) {
      // Don't reveal that email exists; return generic message
      return json({ error: 'That email is already in use.' }, 400);
    }

    // Generate salt and hash password
    const saltChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let salt = '';
    const saltBytes = crypto.getRandomValues(new Uint8Array(8));
    for (let i = 0; i < 8; i++) {
      salt += saltChars[saltBytes[i] % saltChars.length];
    }

    const hash = await hashPassword(password, salt);
    const passwordHash = hash + ':' + salt;

    // Create user (always as 'student' role)
    const userResult = await context.env.DB.prepare(
      'INSERT INTO users (email, password_hash, role) VALUES (?, ?, ?)'
    )
      .bind(emailLower, passwordHash, 'student')
      .run();

    const userId = userResult.meta.last_row_id;

    // Initialize XP record (uses normalized schema, not legacy blob)
    await context.env.DB.prepare(
      'INSERT INTO user_xp (user_id, xp, streak) VALUES (?, ?, ?)'
    )
      .bind(userId, 0, 0)
      .run();

    // Generate token (7 days = 604800 seconds)
    const token = generateToken();
    const expiresAt = Date.now() + 7 * 24 * 60 * 60 * 1000;

    // Store token in auth_tokens table
    await context.env.DB.prepare(
      'INSERT INTO auth_tokens (user_id, token, expires_at) VALUES (?, ?, ?)'
    )
      .bind(userId, token, expiresAt)
      .run();

    // Return success
    return json({
      token: token,
      user_id: userId,
      email: emailLower,
      role: 'student',
      level: level.toLowerCase()
    }, 201);
  } catch (error) {
    console.error('Signup error:', error);
    return json({ error: 'Internal server error.' }, 500);
  }
}
