// Word Play Auth API — Logout endpoint
// POST /api/auth/logout
// Request: { token } or Authorization header
// Response: { ok: true }

export async function onRequestPost(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    const token = authHeader ? authHeader.replace('Bearer ', '') : null;

    if (!token) {
      // Just clear client-side auth and return success
      // (token is already in localStorage; client will clear it)
      return new Response(
        JSON.stringify({ ok: true }),
        { status: 200, headers: { 'Content-Type': 'application/json' } }
      );
    }

    // Delete token from auth_tokens table
    await context.env.DB.prepare('DELETE FROM auth_tokens WHERE token = ?')
      .bind(token)
      .run();

    return new Response(
      JSON.stringify({ ok: true }),
      { status: 200, headers: { 'Content-Type': 'application/json' } }
    );
  } catch (error) {
    console.error('Logout error:', error);
    return new Response(
      JSON.stringify({ error: 'Logout failed' }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }
}
