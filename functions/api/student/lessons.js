// Word Play Student API — Get lessons for enrolled classes
// GET /api/student/lessons
// Query params: ?class_id=<optional> to filter by specific class
// Response: { lessons: [{id, class_id, date, time_start, time_end, title, type, level, location}, ...] } or { error }


import { verifyTokenId as verifyToken } from '../_shared.js';
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
    if (userRole !== 'student') {
      return json({ error: 'Student access required' }, 403);
    }

    // Get the student record for this user
    const student = await context.env.DB.prepare(
      'SELECT id FROM students WHERE user_id = ?'
    )
      .bind(userId)
      .first();

    if (!student) {
      return json({ lessons: [] }, 200);
    }

    // Parse optional class_id filter from query params
    const url = new URL(context.request.url);
    const classIdParam = url.searchParams.get('class_id');
    const classIdFilter = classIdParam ? parseInt(classIdParam) : null;

    let query;
    let bindings;

    if (classIdFilter) {
      // Filter by specific class AND verify enrollment
      query = `
        SELECT
          l.id,
          l.class_id,
          l.date,
          l.time_start,
          l.time_end,
          l.title,
          l.type,
          l.level,
          l.location
        FROM lessons l
        INNER JOIN class_enrollments ce ON l.class_id = ce.class_id
        WHERE ce.student_id = ? AND l.class_id = ?
        ORDER BY l.date ASC, l.time_start ASC
      `;
      bindings = [student.id, classIdFilter];
    } else {
      // Fetch lessons from all enrolled classes
      query = `
        SELECT
          l.id,
          l.class_id,
          l.date,
          l.time_start,
          l.time_end,
          l.title,
          l.type,
          l.level,
          l.location
        FROM lessons l
        INNER JOIN class_enrollments ce ON l.class_id = ce.class_id
        WHERE ce.student_id = ?
        ORDER BY l.date ASC, l.time_start ASC
      `;
      bindings = [student.id];
    }

    const result = await context.env.DB.prepare(query).bind(...bindings).all();

    const lessons = (result.results || []).map(l => ({
      id: l.id,
      class_id: l.class_id,
      date: l.date,
      time_start: l.time_start || null,
      time_end: l.time_end || null,
      title: l.title,
      type: l.type || '1on1',
      level: l.level || null,
      location: l.location || null
    }));

    return json({ lessons }, 200);
  } catch (error) {
    console.error('Get lessons error:', error);
    return json({ error: 'Failed to fetch lessons' }, 500);
  }
}
