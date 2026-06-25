// Word Play Admin API — User management
// GET /api/admin/users — list all users
// POST /api/admin/users — create new user (admin only)

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

function verifyToken(token, db) {
  return db.prepare('SELECT user_id FROM auth_tokens WHERE token = ? AND expires_at > ?')
    .bind(token, Date.now())
    .first()
    .then(row => row ? row.user_id : null);
}

async function getUserRole(userId, db) {
  const user = await db.prepare('SELECT role FROM users WHERE id = ?')
    .bind(userId)
    .first();
  return user ? user.role : null;
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' }
  });
}

export async function onRequestGet(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return json({ error: 'Missing authorization token' }, 401);
    }

    const token = authHeader.replace('Bearer ', '');
    const userId = await verifyToken(token, context.env.DB);
    if (!userId) {
      return json({ error: 'Invalid or expired token' }, 401);
    }

    const userRole = await getUserRole(userId, context.env.DB);
    if (userRole !== 'admin') {
      return json({ error: 'Admin access required' }, 403);
    }

    const url = new URL(context.request.url);
    const limit = Math.min(200, Math.max(1, parseInt(url.searchParams.get('limit') || '100')));
    const offset = Math.max(0, parseInt(url.searchParams.get('offset') || '0'));

    const users = await context.env.DB.prepare(
      'SELECT id, email, role, created_at FROM users ORDER BY created_at DESC LIMIT ? OFFSET ?'
    ).bind(limit, offset).all();

    return json({ users: users.results || [], limit: limit, offset: offset });
  } catch (error) {
    console.error('User list error:', error);
    return json({ error: 'Failed to fetch users' }, 500);
  }
}

export async function onRequestPost(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return json({ error: 'Missing authorization token' }, 401);
    }

    const token = authHeader.replace('Bearer ', '');
    const userId = await verifyToken(token, context.env.DB);
    if (!userId) {
      return json({ error: 'Invalid or expired token' }, 401);
    }

    const userRole = await getUserRole(userId, context.env.DB);
    if (userRole !== 'admin') {
      return json({ error: 'Admin access required' }, 403);
    }

    const body = await context.request.json();
    const { email, password, role } = body;

    if (!email || !password || !role) {
      return json({ error: 'Email, password, and role are required' }, 400);
    }

    if (!['student', 'teacher', 'admin'].includes(role)) {
      return json({ error: 'Role must be student, teacher, or admin' }, 400);
    }

    if (password.length < 8) {
      return json({ error: 'Password must be at least 8 characters' }, 400);
    }

    const existingUser = await context.env.DB.prepare('SELECT id FROM users WHERE email = ?')
      .bind(email.toLowerCase())
      .first();

    if (existingUser) {
      return json({ error: 'Email already in use' }, 409);
    }

    const saltChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let salt = '';
    const saltBytes = crypto.getRandomValues(new Uint8Array(8));
    for (let i = 0; i < 8; i++) {
      salt += saltChars[saltBytes[i] % saltChars.length];
    }

    const hash = await hashPassword(password, salt);
    const passwordHash = hash + ':' + salt;

    const result = await context.env.DB.prepare(
      'INSERT INTO users (email, password_hash, role) VALUES (?, ?, ?)'
    )
      .bind(email.toLowerCase(), passwordHash, role)
      .run();

    return json({
      user_id: result.meta.last_row_id,
      email: email.toLowerCase(),
      role: role
    }, 201);
  } catch (error) {
    console.error('User creation error:', error);
    return json({ error: 'Failed to create user' }, 500);
  }
}
