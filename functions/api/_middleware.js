// B4: API error-monitoring middleware. Runs for every /api/* request.
// - Catches unhandled exceptions (full message + stack) and returns a clean 500.
// - Logs any 5xx response (status + path) so endpoint-level failures are visible too.
// Logging is best-effort and never blocks or breaks a request.

async function logError(env, { path, method, status, message, stack }) {
  try {
    await env.DB.prepare(
      'INSERT INTO error_log (path, method, status, message, stack, created_at) VALUES (?, ?, ?, ?, ?, ?)'
    ).bind(
      path || null,
      method || null,
      status || null,
      message ? String(message).slice(0, 500) : null,
      stack ? String(stack).slice(0, 2000) : null,
      Date.now()
    ).run();
  } catch (e) {
    // error_log table may not exist yet — don't let monitoring break the API
    console.warn('[error-log] write failed:', e.message);
  }
}

export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  try {
    const res = await context.next();
    if (res && res.status >= 500) {
      // Fire-and-forget; don't await on the hot path
      context.waitUntil(logError(env, {
        path: url.pathname, method: request.method, status: res.status,
        message: 'HTTP ' + res.status
      }));
    }
    return res;
  } catch (err) {
    console.error('[api middleware] unhandled error:', err);
    context.waitUntil(logError(env, {
      path: url.pathname, method: request.method, status: 500,
      message: err && err.message, stack: err && err.stack
    }));
    return new Response(JSON.stringify({ error: 'Internal server error.' }), {
      status: 500, headers: { 'Content-Type': 'application/json' }
    });
  }
}
