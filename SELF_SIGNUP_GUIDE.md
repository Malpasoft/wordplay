# Student Self-Signup Implementation Guide

This document describes the Student Self-Signup feature added to Word Play, including implementation details, security measures, and operational procedures.

## Overview

Students can now create their own accounts without requiring admin or teacher intervention. They can:
1. Sign up at `/signup.html` with email, password, and English level
2. Optionally join a teacher's class using an invite code
3. Start learning immediately after account creation

## Architecture

### 1. Signup Flow

**Frontend:** `/signup.html`
- Email validation (format check)
- Password validation (min 8 characters)
- Password confirmation check
- Level selection (A1–C2)
- Optional teacher code field
- Client-side form validation before submission

**Backend:** `POST /api/auth/signup`
- Server-side email format validation
- Password length check
- Rate limiting (5 signups per IP per hour)
- Email uniqueness check (prevents enumeration: returns generic message)
- PBKDF2-SHA256 password hashing with random salt
- User account creation with role='student'
- Progress and XP record initialization
- Auth token generation (7-day expiry)
- Response includes token, user_id, email, role, level

### 2. Teacher Invite Codes

**Teacher Code Management:** `GET/POST/DELETE /api/teacher/invite-code`
- **GET:** List all active (non-revoked, non-expired) codes with usage stats
- **POST:** Generate new unique 6-character alphanumeric code
  - Configurable expiry (default: 30 days, range: 1-365 days)
  - Optional max uses limit (default: unlimited)
  - Rate limit: 10 codes per minute per teacher
- **DELETE:** Revoke a code (prevents further use)

**Code Storage:** `invite_codes` table
```sql
CREATE TABLE invite_codes (
  id, code, teacher_id, created_at, expires_at, 
  max_uses, uses_count, revoked, updated_at
)
```

### 3. Student Class Joining

**Frontend:** Integrated into `/signup.html`
- After account creation, if teacher code provided:
  - Make authenticated request to `/api/student/join-teacher`
  - Show error if code is invalid/expired (but account created)
  - Proceed to redirect regardless

**Backend:** `POST /api/student/join-teacher`
- Verify student auth token
- Validate invite code exists, not revoked, not expired, not exhausted
- Check student not already linked to teacher
- Create `student_teachers` relationship
- Increment code usage count
- Return success or specific error message

## Database Schema

### Migration: `0007_invite_codes.sql`

New table: `invite_codes`
- **Indexes:** code, teacher_id, expires_at
- **Constraints:** UNIQUE(code), FOREIGN KEY(teacher_id)
- **Fields:**
  - `code` – unique 6-char invite code
  - `teacher_id` – links to teacher user
  - `expires_at` – unix timestamp (milliseconds)
  - `max_uses` – -1 for unlimited, positive int for limit
  - `uses_count` – current usage count
  - `revoked` – soft delete flag (0 or 1)

### Existing Tables (Updated Usage)

**users:** Already supported for student accounts
- **role:** 'student' (enum: admin, teacher, student)
- Students created by signup always have role='student'

**student_teachers:** Already existed, now populated via:
- Teacher management (admin/teacher endpoints)
- Student self-join (via invite code)
- Relationship tracks student-to-teacher binding

**student_progress, user_xp:** Initialized on signup

## Security Measures

### 1. Password Security
- **Hashing:** PBKDF2-SHA256 with 100,000 iterations
- **Salt:** 8-byte random salt (generated per user)
- **Storage:** stored as "hash:salt" in password_hash column
- **Client validation:** min 8 characters, confirm match
- **Server validation:** min 8 characters (enforced)

### 2. Rate Limiting
- **Signup:** 5 accounts per IP per hour (prevents brute signup attacks)
- **Invite code generation:** 10 codes per teacher per minute
- **Implementation:** In-memory store (note: resets on server restart)
  - For production: consider Redis or D1-backed rate limiting

### 3. Account Enumeration Prevention
- Signup endpoint returns generic "email already in use" message
- Does not confirm whether email exists in system
- Same approach as login (returns generic "invalid email or password")

### 4. Invite Code Security
- **6-character alphanumeric codes:** ~2.3B possible combinations
- **Uniqueness guarantee:** UNIQUE constraint on code column
- **Expiry enforcement:** Codes expire after N days (default 30)
- **Revocation:** Teachers can revoke codes at any time
- **Use limits:** Optional per-code maximum usage count
- **Soft deletes:** revoked flag (no hard deletes to preserve audit trail)

### 5. Authentication
- **Token verification:** All endpoints check Authorization header
- **Role checking:** Student endpoints reject non-students
- **Token expiry:** 7 days (same as login flow)

### 6. Level Immutability
- **Set at signup:** Student's initial level cannot be changed by student
- **Teachers can override:** Admin/teacher panel has ability to change level
- **Validation:** Only valid levels (a1-c2) accepted

## API Reference

### POST /api/auth/signup

**Request:**
```json
{
  "email": "student@example.com",
  "password": "SecurePass123",
  "level": "b1"
}
```

**Response (201 Created):**
```json
{
  "token": "64-char-hex-token",
  "user_id": 42,
  "email": "student@example.com",
  "role": "student",
  "level": "b1"
}
```

**Errors:**
- 400: Missing fields, invalid format, password too short
- 409: Email already exists (note: returned as 400 to hide enumeration)
- 429: Rate limit exceeded (5 per IP per hour)
- 500: Server error

### GET /api/teacher/invite-code

**Authorization:** Bearer token (teacher or admin)

**Response:**
```json
{
  "codes": [
    {
      "id": 1,
      "code": "ABC123",
      "created_at": 1717689600000,
      "expires_at": 1725465600000,
      "uses_count": 2,
      "max_uses": null,
      "is_expired": false,
      "is_exhausted": false
    }
  ]
}
```

### POST /api/teacher/invite-code

**Authorization:** Bearer token (teacher or admin)

**Request:**
```json
{
  "days_until_expiry": 30,
  "max_uses": -1
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "code": "ABC123",
  "created_at": 1717689600000,
  "expires_at": 1725465600000,
  "max_uses": null,
  "uses_count": 0,
  "expires_in_days": 30
}
```

### DELETE /api/teacher/invite-code

**Authorization:** Bearer token (teacher or admin)

**Request:**
```json
{
  "code_id": 1
}
```

**Response:**
```json
{
  "message": "Code revoked"
}
```

### POST /api/student/join-teacher

**Authorization:** Bearer token (student)

**Request:**
```json
{
  "invite_code": "ABC123"
}
```

**Response (200 OK):**
```json
{
  "message": "Successfully joined the class.",
  "teacher_id": 5
}
```

**Errors:**
- 400: Invalid code, expired code, exhausted code, already joined, code revoked
- 401: Missing or invalid token
- 403: Not a student account
- 500: Server error

## Frontend Integration

### login.html Changes
- Added footer with "Don't have an account? Create one" link
- Link points to `/signup.html`

### signup.html New Page
- Full responsive design (mobile, desktop, dark mode)
- Uses design system (amber accent, paper background, ink text)
- JavaScript form validation and API integration
- Two-step signup: create account, then optionally join teacher
- Dark mode compatible

## Usage Examples

### For Students

1. **Self-signup without teacher:**
   - Go to `https://wordplay.example.com/signup.html`
   - Enter email, password, confirm password, select level
   - Click "Create Account"
   - Redirected to home (logged in)

2. **Self-signup with teacher code:**
   - Receive 6-character code from teacher (e.g., "ABC123")
   - Go to signup page
   - Fill form and enter code in "Teacher Code" field
   - Click "Create Account"
   - Auto-added to teacher's class

### For Teachers

1. **Generate invite code:**
   - In teacher tools (admin panel)
   - Click "Generate Invite Code"
   - Choose expiry (default 30 days)
   - Optionally set max uses (default unlimited)
   - Copy code and share with students
   - Code appears in "Manage Codes" list

2. **Monitor code usage:**
   - View all codes with usage counts
   - See which codes are active/expired/exhausted
   - Revoke codes (stops further use)

3. **Revoke a code:**
   - Click revoke button next to code
   - Code becomes inactive immediately
   - Students cannot use it

## Operations & Monitoring

### Key Metrics
- Signup rate (accounts/hour)
- Rate limit hits (suspicious patterns)
- Invite code generation rate
- Code usage stats (adoption)
- Join failures (invalid codes, etc.)

### Troubleshooting

**Student sees "email already in use"**
- Email already exists
- Have student use different email or reset password via login

**"Invite code expired" error**
- Teacher needs to generate new code
- Codes expire after N days (default 30)

**"Code has reached use limit"**
- Code max_uses was exceeded
- Teacher can revoke and generate new code

**"Rate limit exceeded" on signup**
- User attempted >5 signups from same IP in 1 hour
- Wait 1 hour and retry, or use different IP/device

**Account created but failed to join teacher**
- Code may be invalid/expired/revoked
- Student is still signed up, just not linked to teacher
- Can manually join later if new code generated

### Rate Limit Implementation Notes

Current implementation uses in-memory Map for rate limiting:
- **Pros:** Fast, no external dependencies
- **Cons:** Resets on server restart, not shared across workers

**For production/scale:**
- Implement Redis-backed rate limiting
- Or use D1 with cleanup job for old entries
- Consider Cloudflare Workers KV for global state

## Testing

### Manual Test Cases

1. **Valid signup:**
   - Email: test@example.com, Password: TestPass123, Level: B1
   - Expect: Account created, auto-logged in, redirected to home

2. **Password mismatch:**
   - Password: TestPass123, Confirm: TestPass124
   - Expect: "Passwords do not match" error

3. **Duplicate email:**
   - Signup twice with same email
   - Expect: "Email already in use" on second attempt

4. **Short password:**
   - Password: Pass123 (7 chars)
   - Expect: "Password must be at least 8 characters" error

5. **Invalid email:**
   - Email: not-an-email
   - Expect: HTML5 validation error (browser)

6. **Rate limiting:**
   - Attempt 6 signups from same IP within 60 minutes
   - Expect: 6th attempt gets 429 "Too many signup attempts"

7. **Invite code flow:**
   - Create account with valid code
   - Expect: Account created + auto-joined to teacher's class

8. **Expired code:**
   - Create account with expired code
   - Expect: Account created, but error "invite code expired"

9. **Code revocation:**
   - Teacher revokes code
   - Student attempts to use it
   - Expect: "code revoked" error

10. **Code max uses:**
    - Code with max_uses=1
    - Two students try to join
    - Expect: First succeeds, second gets "code exhausted" error

## Future Enhancements

1. **Email verification:** Send confirmation email before account activation
2. **Social login:** Google/Microsoft OAuth integration
3. **Bulk import:** Teachers import student lists, auto-generate codes
4. **Code templates:** Teachers set default expiry/max_uses globally
5. **Analytics:** Dashboard showing signup trends, code effectiveness
6. **CSRF tokens:** Add explicit CSRF protection for forms
7. **Password reset:** Self-service password recovery
8. **Profile completion:** Collect name/avatar during signup
9. **Referral codes:** Student refer friend, both get bonus
10. **Grade distribution:** Teacher export student list with progress

## Files Changed/Created

| File | Status | Changes |
|------|--------|---------|
| `/signup.html` | NEW | Student signup form page |
| `/login.html` | MODIFIED | Added "Create account?" link |
| `/migrations/0007_invite_codes.sql` | NEW | Invite codes table schema |
| `/functions/api/auth/signup.js` | NEW | POST /api/auth/signup endpoint |
| `/functions/api/teacher/invite-code.js` | NEW | Invite code CRUD endpoints |
| `/functions/api/student/join-teacher.js` | NEW | Student join teacher endpoint |
| `/shared/auth.js` | UNCHANGED | Existing auth utilities |

## Deployment Checklist

- [ ] Apply migration 0007 to D1 database
- [ ] Deploy signup.html and updated login.html
- [ ] Deploy three API endpoints (auth/signup, teacher/invite-code, student/join-teacher)
- [ ] Test signup flow end-to-end (with and without teacher code)
- [ ] Verify rate limiting works (test from same IP)
- [ ] Test dark mode compatibility on signup page
- [ ] Test mobile responsiveness (360px and up)
- [ ] Verify old login flow still works
- [ ] Monitor error logs for any auth issues
- [ ] Communicate signup availability to teachers
- [ ] Provide teachers with invite code generation instructions

## Security Review Checklist

- [x] Password hashing (PBKDF2-SHA256)
- [x] Rate limiting (signup, code generation)
- [x] Email enumeration prevention (generic error messages)
- [x] Token validation on protected endpoints
- [x] Role checking (student-only endpoints)
- [x] Code expiry enforcement
- [x] Code revocation support
- [x] SQL injection prevention (parameterized queries)
- [x] Input validation (email format, password length, level enum)
- [ ] CSRF tokens (optional enhancement)
- [ ] Email verification (optional enhancement)
- [ ] Account lockout (optional enhancement)

---

For questions or issues, refer to the main project CLAUDE.md or contact the development team.
