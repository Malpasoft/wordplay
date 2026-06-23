// Word Play Auth API — Signup endpoint
// POST /api/auth/signup
// Request: { email, password, level, privacy_consent }
// Response: { token, user_id, email, role, level } or { error }

import { sendEmail } from '../_lib/email.js';

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
    const { email, password, level, privacy_consent, target_lang, l1 } = body;

    // Validate inputs
    if (!email || !password || !level) {
      return json({ error: 'Email, password, and level are required.' }, 400);
    }

    if (!privacy_consent) {
      return json({ error: 'You must accept the Privacy Policy to create an account.' }, 400);
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

    // Create user (always as 'student' role).
    // Try the full insert (new profile columns); fall back to the minimal insert
    // if migrations 0009/0012 haven't been applied yet, so signup never 500s.
    const consentAt = Date.now();
    const targetLang = (target_lang === 'es' || target_lang === 'en') ? target_lang : 'en';
    const l1Lang = ['es', 'en', 'fr', 'other'].includes(l1) ? l1 : null;
    let userResult;
    try {
      userResult = await context.env.DB.prepare(
        'INSERT INTO users (email, password_hash, role, privacy_consent, consent_at, target_lang, l1) VALUES (?, ?, ?, ?, ?, ?, ?)'
      )
        .bind(emailLower, passwordHash, 'student', 1, consentAt, targetLang, l1Lang)
        .run();
    } catch (colErr) {
      console.warn('Full signup insert failed (migrations may be pending); falling back:', colErr.message);
      userResult = await context.env.DB.prepare(
        'INSERT INTO users (email, password_hash, role) VALUES (?, ?, ?)'
      )
        .bind(emailLower, passwordHash, 'student')
        .run();
    }

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

    // Send verification email (non-blocking — don't fail signup if email fails)
    try {
      const verifyToken = generateToken();
      const verifyExpiry = Date.now() + 72 * 60 * 60 * 1000; // 72 hours
      await context.env.DB.prepare(
        'INSERT INTO password_resets (user_id, token, expires_at) VALUES (?, ?, ?)'
      ).bind(userId, verifyToken, verifyExpiry).run();

      const baseUrl = context.env.SITE_URL || 'https://wordplay-38t.pages.dev';
      const verifyUrl = `${baseUrl}/api/auth/verify-email?token=${verifyToken}`;
      await sendEmail({
        to: emailLower,
        subject: 'Verify your Word Play email',
        html: `
          <div style="font-family:system-ui,sans-serif;max-width:480px;margin:0 auto;padding:32px 24px">
            <h2 style="font-size:1.4rem;margin:0 0 16px;color:#1A1A1A">Welcome to Word Play</h2>
            <p style="color:#444;line-height:1.6;margin:0 0 24px">
              Click below to verify your email address. This link expires in 72 hours.
            </p>
            <a href="${verifyUrl}" style="display:inline-block;padding:12px 24px;background:#B8860B;color:#fff;text-decoration:none;border-radius:4px;font-weight:600">
              Verify email
            </a>
          </div>
        `,
        env: context.env
      });
    } catch (emailErr) {
      console.warn('Verification email failed:', emailErr.message);
    }

    // Return success
    return json({
      token: token,
      user_id: userId,
      email: emailLower,
      role: 'student',
      level: level.toLowerCase(),
      target_lang: targetLang,
      l1: l1Lang
    }, 201);
  } catch (error) {
    console.error('Signup error:', error);
    return json({ error: 'Internal server error.' }, 500);
  }
}
