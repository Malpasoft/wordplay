// Word Play Teacher API — Individual student deletion
// DELETE /api/teacher/students/[student_id] — remove student from teacher's class


import { verifyTokenId as verifyToken } from '../../_shared.js';
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

export async function onRequestDelete(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return json({ error: 'Missing authorization token' }, 401);
    }

    const token = authHeader.replace('Bearer ', '');
    const teacherId = await verifyToken(token, context.env.DB);
    if (!teacherId) {
      return json({ error: 'Invalid or expired token' }, 401);
    }

    const userRole = await getUserRole(teacherId, context.env.DB);
    if (userRole !== 'teacher' && userRole !== 'admin') {
      return json({ error: 'Teacher access required' }, 403);
    }

    const { student_id } = context.params;
    const studentId = parseInt(student_id);

    if (!studentId) {
      return json({ error: 'Student ID is required' }, 400);
    }

    // Verify teacher owns this student before removal
    const relationship = await context.env.DB.prepare(
      'SELECT id FROM student_teachers WHERE student_id = ? AND teacher_id = ?'
    )
      .bind(studentId, teacherId)
      .first();

    if (!relationship) {
      return json({ error: 'Student not found or not assigned to this teacher' }, 404);
    }

    // Remove student from teacher's class (don't delete user, just unlink)
    await context.env.DB.prepare(
      'DELETE FROM student_teachers WHERE student_id = ? AND teacher_id = ?'
    )
      .bind(studentId, teacherId)
      .run();

    return json({ message: 'Student removed from class' });
  } catch (error) {
    console.error('Student deletion error:', error);
    return json({ error: 'Failed to remove student' }, 500);
  }
}
