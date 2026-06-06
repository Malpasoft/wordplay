# Student Self-Signup API Test Examples

This document provides curl examples for testing the Student Self-Signup feature.

## Prerequisites

- Wordplay server running
- Teacher account with valid auth token
- Student account for testing (or create via signup)

## 1. Test Student Signup

### Create a new student account

```bash
curl -X POST http://localhost:8787/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{
    "email": "newstudent@example.com",
    "password": "SecurePassword123",
    "level": "b1"
  }'
```

**Expected Response (201):**
```json
{
  "token": "a1b2c3d4e5f6...",
  "user_id": 42,
  "email": "newstudent@example.com",
  "role": "student",
  "level": "b1"
}
```

### Test password validation (too short)

```bash
curl -X POST http://localhost:8787/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "short",
    "level": "a1"
  }'
```

**Expected Response (400):**
```json
{
  "error": "Password must be at least 8 characters."
}
```

### Test duplicate email

```bash
curl -X POST http://localhost:8787/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{
    "email": "existing@example.com",
    "password": "ValidPass123",
    "level": "a2"
  }'
```

**Expected Response (400):**
```json
{
  "error": "That email is already in use."
}
```

## 2. Test Teacher Invite Code Management

### Get list of teacher's invite codes

Replace `TEACHER_TOKEN` with actual teacher auth token.

```bash
curl -X GET http://localhost:8787/api/teacher/invite-code \
  -H "Authorization: Bearer TEACHER_TOKEN"
```

**Expected Response (200):**
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

### Generate a new invite code

```bash
curl -X POST http://localhost:8787/api/teacher/invite-code \
  -H "Authorization: Bearer TEACHER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "days_until_expiry": 14,
    "max_uses": 10
  }'
```

**Expected Response (201):**
```json
{
  "id": 2,
  "code": "XYZ789",
  "created_at": 1717689600000,
  "expires_at": 1720368000000,
  "max_uses": 10,
  "uses_count": 0,
  "expires_in_days": 14
}
```

### Generate unlimited-use code (valid for 60 days)

```bash
curl -X POST http://localhost:8787/api/teacher/invite-code \
  -H "Authorization: Bearer TEACHER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "days_until_expiry": 60,
    "max_uses": -1
  }'
```

### Revoke an invite code

```bash
curl -X DELETE http://localhost:8787/api/teacher/invite-code \
  -H "Authorization: Bearer TEACHER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "code_id": 1
  }'
```

**Expected Response (200):**
```json
{
  "message": "Code revoked"
}
```

### Test rate limiting (generate 11 codes in quick succession)

```bash
for i in {1..11}; do
  curl -X POST http://localhost:8787/api/teacher/invite-code \
    -H "Authorization: Bearer TEACHER_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"days_until_expiry": 30, "max_uses": -1}'
done
```

Expected: First 10 succeed (201), 11th fails with 429 rate limit.

## 3. Test Student Join Teacher

### Student uses invite code to join class

```bash
curl -X POST http://localhost:8787/api/student/join-teacher \
  -H "Authorization: Bearer STUDENT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "invite_code": "ABC123"
  }'
```

**Expected Response (200):**
```json
{
  "message": "Successfully joined the class.",
  "teacher_id": 5
}
```

### Test with invalid code

```bash
curl -X POST http://localhost:8787/api/student/join-teacher \
  -H "Authorization: Bearer STUDENT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "invite_code": "INVALID"
  }'
```

**Expected Response (400):**
```json
{
  "error": "Invalid invite code."
}
```

### Test with expired code

After creating a code and waiting for expiry (or manually setting expires_at to past):

```bash
curl -X POST http://localhost:8787/api/student/join-teacher \
  -H "Authorization: Bearer STUDENT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "invite_code": "EXPIRED"
  }'
```

**Expected Response (400):**
```json
{
  "error": "This invite code has expired."
}
```

### Test joining when already linked to teacher

```bash
# First call succeeds
curl -X POST http://localhost:8787/api/student/join-teacher \
  -H "Authorization: Bearer STUDENT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "invite_code": "ABC123"
  }'
# Response: 200 success

# Second call with same code fails
curl -X POST http://localhost:8787/api/student/join-teacher \
  -H "Authorization: Bearer STUDENT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "invite_code": "ABC123"
  }'
```

**Expected Response (400):**
```json
{
  "error": "You are already joined to this teacher's class."
}
```

## 4. End-to-End Workflow Test

### Step 1: Teacher generates invite code

```bash
# Get teacher token (via login)
TEACHER_TOKEN=$(curl -X POST http://localhost:8787/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"teacher@example.com","password":"TeacherPass123"}' \
  | jq -r '.token')

# Generate code
CODE_RESPONSE=$(curl -s -X POST http://localhost:8787/api/teacher/invite-code \
  -H "Authorization: Bearer $TEACHER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"days_until_expiry": 30, "max_uses": -1}')

INVITE_CODE=$(echo $CODE_RESPONSE | jq -r '.code')
echo "Generated code: $INVITE_CODE"
```

### Step 2: Student signs up with invite code

```bash
# Create account (simulating signup form submission)
SIGNUP_RESPONSE=$(curl -s -X POST http://localhost:8787/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{
    "email": "student123@example.com",
    "password": "StudentPass123",
    "level": "b1"
  }')

STUDENT_TOKEN=$(echo $SIGNUP_RESPONSE | jq -r '.token')
STUDENT_ID=$(echo $SIGNUP_RESPONSE | jq -r '.user_id')
echo "Student created: ID=$STUDENT_ID"

# Join teacher's class
JOIN_RESPONSE=$(curl -s -X POST http://localhost:8787/api/student/join-teacher \
  -H "Authorization: Bearer $STUDENT_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"invite_code\": \"$INVITE_CODE\"}")

echo "Join result: $(echo $JOIN_RESPONSE | jq '.message')"
```

### Step 3: Verify student is in teacher's class

```bash
# Fetch teacher's students list
curl -s -X GET http://localhost:8787/api/teacher/students \
  -H "Authorization: Bearer $TEACHER_TOKEN" \
  | jq '.students[] | select(.id == '$STUDENT_ID')'
```

Expected: Student should appear in teacher's class.

## 5. Edge Cases & Error Testing

### Test invalid auth token

```bash
curl -X GET http://localhost:8787/api/teacher/invite-code \
  -H "Authorization: Bearer INVALID_TOKEN"
```

**Expected Response (401):**
```json
{
  "error": "Invalid or expired token"
}
```

### Test non-teacher trying to generate code

```bash
# Use student token instead of teacher token
curl -X POST http://localhost:8787/api/teacher/invite-code \
  -H "Authorization: Bearer STUDENT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"days_until_expiry": 30}'
```

**Expected Response (403):**
```json
{
  "error": "Teacher access required"
}
```

### Test code with max_uses=1 and two students

```bash
# Create code with max_uses=1
CODE=$(curl -s -X POST http://localhost:8787/api/teacher/invite-code \
  -H "Authorization: Bearer $TEACHER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"days_until_expiry": 30, "max_uses": 1}' \
  | jq -r '.code')

# First student uses it
curl -s -X POST http://localhost:8787/api/student/join-teacher \
  -H "Authorization: Bearer STUDENT1_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"invite_code\": \"$CODE\"}" \
  | jq '.'
# Response: 200 success

# Second student tries to use same code
curl -s -X POST http://localhost:8787/api/student/join-teacher \
  -H "Authorization: Bearer STUDENT2_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"invite_code\": \"$CODE\"}" \
  | jq '.'
```

**Expected Response (400):**
```json
{
  "error": "This invite code has reached its use limit."
}
```

## 6. Browser Testing (Manual)

### Test signup flow in browser

1. Navigate to `http://localhost:8787/signup.html`
2. Fill in form:
   - Email: `test@example.com`
   - Password: `TestPass123`
   - Confirm: `TestPass123`
   - Level: `B1`
   - Teacher Code: (leave blank for first test)
3. Click "Create Account"
4. Should redirect to home page and be logged in
5. Check browser localStorage:
   - `wp_token` should exist
   - `wp_user` should contain user object

### Test with teacher code

1. Navigate to signup page
2. In teacher code field, enter: `ABC123` (or valid code)
3. Complete signup
4. Should auto-join teacher's class
5. Teacher's student list should include new student

### Test dark mode compatibility

1. Open signup page
2. Click "Dark" toggle in header
3. Page should properly theme (amber accent on dark background)
4. All form elements readable in both modes

### Test mobile responsiveness

1. Open signup page
2. Resize to 360px width (mobile)
3. Form should stack vertically
4. All inputs/buttons easily tappable
5. No horizontal scroll

## Bash Helper Script

```bash
#!/bin/bash
# save as test-signup.sh

API="http://localhost:8787"

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo "=== Student Self-Signup API Tests ==="

# Test 1: Basic signup
echo -e "\n${GREEN}Test 1: Basic Student Signup${NC}"
curl -s -X POST $API/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test'$(date +%s)'@example.com",
    "password": "TestPass123",
    "level": "b1"
  }' | jq '.'

# Test 2: Invalid password (too short)
echo -e "\n${GREEN}Test 2: Password Too Short${NC}"
curl -s -X POST $API/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "short",
    "level": "a1"
  }' | jq '.error'

# Test 3: Duplicate email
echo -e "\n${GREEN}Test 3: Duplicate Email${NC}"
curl -s -X POST $API/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "ValidPass123",
    "level": "a2"
  }' | jq '.error'

echo -e "\n${GREEN}All tests completed!${NC}"
```

Run with: `bash test-signup.sh`
