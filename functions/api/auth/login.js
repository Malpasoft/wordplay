// Word Play Auth API — Login endpoint
// POST /api/auth/login
// Request: { email, password }
// Response: { token, user_id, email, role } or { error }

import { verifyPassword, generateToken } from '../_lib/crypto.js';

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

    // Account may have no password set (e.g. teacher-created student, or a
    // legacy account). Return a clean 401 and point at the password-reset flow.
    if (!user.password_hash || user.password_hash.indexOf(':') === -1) {
      return new Response(
        JSON.stringify({ error: 'This account has no password set. Use "Forgot password?" to create one.' }),
        { status: 401, headers: { 'Content-Type': 'application/json' } }
      );
    }

    // Verify password (stored as "hash:salt" in password_hash column)
    const isValid = await verifyPassword(password, user.password_hash);

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
