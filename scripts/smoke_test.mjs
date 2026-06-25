#!/usr/bin/env node
// B3: End-to-end API smoke test. Exercises the critical student journey against a
// live deployment and asserts status codes + response shapes. Self-cleaning (creates
// then deletes a throwaway account). Zero dependencies (Node 18+ global fetch).
//
// Usage:  node scripts/smoke_test.mjs [BASE_URL]
//         BASE_URL defaults to the production site.
// Exits non-zero on the first failed assertion.

const BASE = process.argv[2] || process.env.SMOKE_BASE_URL || 'https://wordplay-38t.pages.dev';
const EMAIL = `smoke_${Date.now()}@example.com`;
const PASS = 'smoketest12345';

let passed = 0, failed = 0;
function ok(name) { passed++; console.log(`  ✓ ${name}`); }
function bad(name, detail) { failed++; console.log(`  ✗ ${name}\n      ${detail}`); }
function assert(cond, name, detail) { cond ? ok(name) : bad(name, detail || 'assertion failed'); }

async function api(method, path, { token, body } = {}) {
  const headers = { 'Content-Type': 'application/json' };
  if (token) headers['Authorization'] = 'Bearer ' + token;
  const res = await fetch(BASE + path, { method, headers, body: body ? JSON.stringify(body) : undefined });
  let json = null;
  try { json = await res.json(); } catch { /* non-JSON */ }
  return { status: res.status, json };
}

async function main() {
  console.log(`Smoke test against ${BASE}\n`);
  let token = null;

  // 1. signup
  let r = await api('POST', '/api/auth/signup', { body: {
    email: EMAIL, password: PASS, level: 'a1', target_lang: 'en', l1: 'es', privacy_consent: true } });
  assert(r.status === 201 && r.json?.token, 'signup returns 201 + token', `got ${r.status} ${JSON.stringify(r.json)}`);
  token = r.json?.token;

  // 2. signup without consent → 400
  r = await api('POST', '/api/auth/signup', { body: { email: 'x'+EMAIL, password: PASS, level: 'a1' } });
  assert(r.status === 400, 'signup without consent rejected (400)', `got ${r.status}`);

  // 3. login
  r = await api('POST', '/api/auth/login', { body: { email: EMAIL, password: PASS } });
  assert(r.status === 200 && r.json?.token, 'login returns 200 + token', `got ${r.status}`);
  assert(r.json?.target_lang === 'en' && r.json?.l1 === 'es', 'login returns l1/target_lang', JSON.stringify(r.json));
  token = r.json?.token || token;

  // 4. wrong password → 401 (not 500)
  r = await api('POST', '/api/auth/login', { body: { email: EMAIL, password: 'nope' } });
  assert(r.status === 401, 'wrong password → clean 401', `got ${r.status}`);

  // 5. progress push + pull
  r = await api('POST', '/api/student/progress', { token, body: {
    chapters: [{ level: 'a1', slug: 'present-simple', score: 8, total: 10, pct: 80, date: '2026-06-25' }],
    xp: 80, streak: 1 } });
  assert(r.status === 200, 'progress push 200', `got ${r.status}`);
  r = await api('GET', '/api/student/progress', { token });
  assert(r.status === 200 && r.json?.chapters?.a1?.['present-simple']?.pct === 80, 'progress pull round-trips', JSON.stringify(r.json?.chapters?.a1));

  // 6. mistakes push + aggregate
  r = await api('POST', '/api/student/mistakes', { token, body: {
    mistakes: [{ level: 'a1', chapter_slug: 'present-simple', skill_tag: 'Present Simple', expected: 'goes', given: 'go', source: 'worksheet' }] } });
  assert(r.status === 200 && r.json?.inserted === 1, 'mistakes push 200 + inserted', JSON.stringify(r.json));
  r = await api('GET', '/api/student/mistakes', { token });
  assert(r.status === 200 && r.json?.total >= 1 && Array.isArray(r.json?.by_skill), 'mistakes aggregate report', JSON.stringify(r.json));

  // 7. booking without a teacher link → graceful 400 (not 500)
  r = await api('POST', '/api/bookings', { token, body: { date: '2099-01-05', start_time: '17:00', end_time: '18:00' } });
  assert(r.status === 400, 'booking w/o teacher → 400 (not 500)', `got ${r.status} ${JSON.stringify(r.json)}`);

  // 8. availability GET (student, no teacher) → 200
  r = await api('GET', '/api/availability', { token });
  assert(r.status === 200, 'availability GET 200', `got ${r.status}`);

  // 9. password reset request → always 200 ok (no enumeration)
  r = await api('POST', '/api/auth/request-reset', { body: { email: EMAIL } });
  assert(r.status === 200 && r.json?.ok, 'request-reset 200 ok', `got ${r.status}`);

  // 10. GDPR export → 200 (JSON download)
  r = await api('GET', '/api/student/export', { token });
  assert(r.status === 200 && r.json?.account?.email === EMAIL, 'GDPR export returns account', JSON.stringify(r.json?.account));

  // 11. delete account (password-confirmed) → 200, then login fails
  r = await api('DELETE', '/api/student/delete-account', { token, body: { password: PASS } });
  assert(r.status === 200 && r.json?.ok, 'delete-account 200', `got ${r.status}`);
  r = await api('POST', '/api/auth/login', { body: { email: EMAIL, password: PASS } });
  assert(r.status === 401, 'login fails after deletion', `got ${r.status}`);

  console.log(`\n${passed} passed, ${failed} failed`);
  if (failed) process.exit(1);
}

main().catch(e => { console.error('Smoke test crashed:', e); process.exit(1); });
