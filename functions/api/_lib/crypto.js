// Canonical auth crypto helpers. Byte-identical to the per-file copies they
// replace (PBKDF2-SHA256, 100k iterations, 256 bits, hex) so existing stored
// password hashes continue to verify. Import these instead of re-defining.

const SALT_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

export async function hashPassword(password, salt) {
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

// Generate an 8-char random salt.
export function generateSalt() {
  let salt = '';
  const bytes = crypto.getRandomValues(new Uint8Array(8));
  for (let i = 0; i < 8; i++) salt += SALT_CHARS[bytes[i] % SALT_CHARS.length];
  return salt;
}

// Hash a fresh password into the stored "hash:salt" form.
export async function makePasswordHash(password) {
  const salt = generateSalt();
  const hash = await hashPassword(password, salt);
  return hash + ':' + salt;
}

// Verify a password against a stored "hash:salt" value. Guards null/malformed.
export async function verifyPassword(password, stored) {
  if (!stored || stored.indexOf(':') === -1) return false;
  const [hash, salt] = stored.split(':');
  const computed = await hashPassword(password, salt);
  return computed === hash;
}

// 32-byte hex bearer/reset token.
export function generateToken() {
  const bytes = crypto.getRandomValues(new Uint8Array(32));
  return Array.from(bytes).map(b => b.toString(16).padStart(2, '0')).join('');
}

// Cryptographically-random alphanumeric code (uppercase + digits).
export function generateCode(len) {
  const chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  const bytes = crypto.getRandomValues(new Uint8Array(len));
  let out = '';
  for (let i = 0; i < len; i++) out += chars[bytes[i] % chars.length];
  return out;
}
