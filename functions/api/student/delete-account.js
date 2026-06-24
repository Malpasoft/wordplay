// DELETE /api/student/delete-account
// Body: { password } — requires password confirmation to prevent accidental/malicious deletion.
// Cascades: auth_tokens, chapter_results, user_xp, student_progress, password_resets (via FK),
// student_teachers, class_enrollments, students (linked record). (GDPR Art. 17)

import { verifyToken, json } from '../_shared.js';

async function hashPassword(password, salt) {
  const encoder = new TextEncoder();
  const keyMaterial = await crypto.subtle.importKey(
    'raw', encoder.encode(password), { name: 'PBKDF2' }, false, ['deriveBits']
  );
  const bits = await crypto.subtle.deriveBits(
    { name: 'PBKDF2', hash: 'SHA-256', salt: encoder.encode(salt), iterations: 100000 },
    keyMaterial, 256
  );
  return Array.from(new Uint8Array(bits)).map(b => b.toString(16).padStart(2, '0')).join('');
}

export async function onRequestDelete(context) {
  try {
    const authHeader = context.request.headers.get('Authorization');
    if (!authHeader?.startsWith('Bearer ')) return json({ error: 'Unauthorized' }, 401);

    const user = await verifyToken(authHeader.replace('Bearer ', ''), context.env);
    if (!user) return json({ error: 'Invalid or expired token' }, 401);

    // Only students can self-delete; admin/teacher accounts need manual handling
    if (user.role !== 'student') {
      return json({ error: 'Only student accounts can be self-deleted.' }, 403);
    }

    const { password } = await context.request.json();
    if (!password) return json({ error: 'Password confirmation required.' }, 400);

    const db = context.env.DB;
    const userRow = await db.prepare('SELECT password_hash FROM users WHERE id = ?')
      .bind(user.id).first();

    if (!userRow) return json({ error: 'User not found.' }, 404);

    // Guard against null/malformed hash (legacy or passwordless accounts)
    if (!userRow.password_hash || userRow.password_hash.indexOf(':') === -1) {
      return json({ error: 'This account has no password set; cannot confirm deletion.' }, 400);
    }

    const [hash, salt] = userRow.password_hash.split(':');
    const computed = await hashPassword(password, salt);
    if (computed !== hash) {
      return json({ error: 'Incorrect password.' }, 403);
    }

    // Delete all data — FKs with ON DELETE CASCADE handle most; others explicit
    await db.prepare('DELETE FROM auth_tokens WHERE user_id = ?').bind(user.id).run();
    await db.prepare('DELETE FROM password_resets WHERE user_id = ?').bind(user.id).run();
    await db.prepare('DELETE FROM chapter_results WHERE user_id = ?').bind(user.id).run();
    await db.prepare('DELETE FROM user_xp WHERE user_id = ?').bind(user.id).run();
    await db.prepare('DELETE FROM student_progress WHERE user_id = ?').bind(user.id).run();
    await db.prepare('DELETE FROM student_teachers WHERE student_id = ?').bind(user.id).run();
    // students table may have a linked record
    await db.prepare('DELETE FROM students WHERE user_id = ?').bind(user.id).run();
    // Finally delete the user
    await db.prepare('DELETE FROM users WHERE id = ?').bind(user.id).run();

    return json({ ok: true });
  } catch (err) {
    console.error('[student/delete-account]', err);
    return json({ error: 'Internal server error.' }, 500);
  }
}
