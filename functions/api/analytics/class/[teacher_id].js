// Word Play Analytics API — Class-level insights
// GET /api/analytics/class/[teacher_id] — fetch class performance data (teacher only)

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

function parseProgress(progressJson) {
  try {
    return JSON.parse(progressJson);
  } catch (e) {
    return {};
  }
}

function getWeakestChapters(progress) {
  const chapters = [];

  // Iterate through all levels
  for (const level in progress) {
    if (!level || level === 'xp' || level === 'streak' || level === 'updated_at' || level === 'lastDay') continue;

    const levelData = progress[level];
    if (typeof levelData !== 'object') continue;

    // Find all chapter results (non-game entries)
    for (const key in levelData) {
      if (!key.startsWith('wordplay_game_')) {
        const result = levelData[key];
        if (result && typeof result === 'object' && result.pct !== undefined) {
          chapters.push({
            slug: key,
            label: key.replace(/-/g, ' ').split('_').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' '),
            pct: result.pct,
            level: level
          });
        }
      }
    }
  }

  // Sort by percentage and return top 5 weakest
  return chapters.sort((a, b) => a.pct - b.pct).slice(0, 5);
}

function getAverageScore(progress) {
  const scores = [];

  for (const level in progress) {
    if (!level || level === 'xp' || level === 'streak' || level === 'updated_at' || level === 'lastDay') continue;

    const levelData = progress[level];
    if (typeof levelData !== 'object') continue;

    for (const key in levelData) {
      const result = levelData[key];
      if (result && typeof result === 'object' && result.pct !== undefined) {
        scores.push(result.pct);
      }
    }
  }

  return scores.length > 0 ? Math.round(scores.reduce((a, b) => a + b, 0) / scores.length) : 0;
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

    // Only teacher or admin can view class analytics
    const userRole = await getUserRole(tokenUserId, context.env.DB);
    const teacherId = parseInt(teacher_id);

    if (userRole !== 'admin' && tokenUserId !== teacherId) {
      return json({ error: 'Cannot view another teacher\'s analytics' }, 403);
    }

    // For now, return aggregated data for all students
    // In a future phase, we'll add student-teacher relationships
    // For MVP, teachers can see all student data if they're logged in
    const allStudents = await context.env.DB.prepare(
      `SELECT u.id, u.email FROM users u WHERE u.role = 'student' ORDER BY u.email`
    ).all();

    const students = [];

    for (const student of allStudents.results || []) {
      const progress = await context.env.DB.prepare(
        'SELECT progress_data FROM student_progress WHERE user_id = ?'
      ).bind(student.id).first();

      const progressData = progress ? parseProgress(progress.progress_data) : {};
      const weakest = getWeakestChapters(progressData);
      const avgScore = getAverageScore(progressData);

      // Extract level from first available result
      let level = 'a1';
      for (const levelKey in progressData) {
        if (levelKey && !['xp', 'streak', 'updated_at', 'lastDay'].includes(levelKey)) {
          level = levelKey;
          break;
        }
      }

      students.push({
        id: student.id,
        email: student.email,
        name: student.email.split('@')[0],
        level: level,
        avgScore: avgScore,
        xp: progressData.xp || 0,
        weakestChapters: weakest
      });
    }

    return json({ students: students });
  } catch (error) {
    console.error('Analytics fetch error:', error);
    return json({ error: 'Failed to fetch analytics' }, 500);
  }
}
