// Word Play Analytics API — Class-level insights (normalized schema)
// GET /api/analytics/class/[teacher_id] — fetch class performance data (teacher only)
// Now uses normalized chapter_results + user_xp tables for O(1) queries (was O(n))

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
    const { teacher_id } = context.params;
    const authHeader = context.request.headers.get('Authorization');

    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return json({ error: 'Missing authorization token' }, 401);
    }

    const token = authHeader.replace('Bearer ', '');
    const tokenUserId = await verifyToken(token, context.env.DB);

    if (!tokenUserId) {
      return json({ error: 'Invalid or expired token' }, 401);
    }

    const userRole = await getUserRole(tokenUserId, context.env.DB);
    const teacherId = parseInt(teacher_id);

    if (userRole !== 'admin' && tokenUserId !== teacherId) {
      return json({ error: 'Cannot view another teacher\'s analytics' }, 403);
    }

    // ONE QUERY: fetch all students + their XP
    const allStudents = await context.env.DB.prepare(
      `SELECT u.id, u.email, COALESCE(x.xp, 0) as xp, COALESCE(x.streak, 0) as streak
       FROM users u
       LEFT JOIN user_xp x ON u.id = x.user_id
       WHERE u.role = 'student'
       ORDER BY u.email`
    ).all();

    // ONE QUERY: fetch all chapter results for all students
    const allResults = await context.env.DB.prepare(
      `SELECT user_id, level, chapter_slug, pct
       FROM chapter_results
       ORDER BY user_id, pct ASC`
    ).all();

    // Aggregate in memory: group chapters by student, calculate averages
    const studentMap = {};
    for (const student of allStudents.results || []) {
      studentMap[student.id] = {
        id: student.id,
        email: student.email,
        name: student.email.split('@')[0],
        xp: student.xp,
        streak: student.streak,
        level: 'a1', // default; will be updated from first chapter's level
        scores: [],
        chapters: {}
      };
    }

    // Populate chapters, calculate average score per student
    for (const result of allResults.results || []) {
      const student = studentMap[result.user_id];
      if (!student) continue;

      student.level = result.level; // last level wins (most recent)
      student.scores.push(result.pct);
      if (!student.chapters[result.level]) student.chapters[result.level] = [];
      student.chapters[result.level].push({
        slug: result.chapter_slug,
        label: result.chapter_slug.replace(/-/g, ' ').split('_').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' '),
        pct: result.pct
      });
    }

    // Build final output with weakest chapters per student
    const students = Object.values(studentMap).map(s => ({
      id: s.id,
      email: s.email,
      name: s.name,
      level: s.level,
      avgScore: s.scores.length > 0 ? Math.round(s.scores.reduce((a, b) => a + b, 0) / s.scores.length) : 0,
      xp: s.xp,
      weakestChapters: []
        .concat(...Object.values(s.chapters))
        .sort((a, b) => a.pct - b.pct)
        .slice(0, 5)
    }));

    return json({ students: students });
  } catch (error) {
    console.error('Analytics fetch error:', error);
    return json({ error: 'Failed to fetch analytics' }, 500);
  }
}
