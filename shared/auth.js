// Word Play Auth Utility — Client-side helpers for authentication
// Stores: wp_token (session), wp_user (user info)

var AUTH_TOKEN_KEY = 'wp_token';
var AUTH_USER_KEY = 'wp_user';

// Get the current auth token from localStorage
function getAuthToken() {
  return localStorage.getItem(AUTH_TOKEN_KEY);
}

// Get the current user object from localStorage
function getCurrentUser() {
  var user = localStorage.getItem(AUTH_USER_KEY);
  if (!user) return null;
  try {
    return JSON.parse(user);
  } catch (e) {
    return null;
  }
}

// Check if user is logged in
function isLoggedIn() {
  return getAuthToken() && getCurrentUser();
}

// Check if current user is admin
function isAdmin() {
  var user = getCurrentUser();
  return user && user.role === 'admin';
}

// Check if current user is teacher (or admin)
function isTeacher() {
  var user = getCurrentUser();
  return user && (user.role === 'teacher' || user.role === 'admin');
}

// Check if current user is student
function isStudent() {
  var user = getCurrentUser();
  return user && user.role === 'student';
}

// Set auth state after login
function setAuthState(token, user) {
  localStorage.setItem(AUTH_TOKEN_KEY, token);
  localStorage.setItem(AUTH_USER_KEY, JSON.stringify(user));
}

// Clear auth state (logout)
function clearAuthState() {
  localStorage.removeItem(AUTH_TOKEN_KEY);
  localStorage.removeItem(AUTH_USER_KEY);
}

// Redirect to login if not authenticated
function requireAuth() {
  if (!isLoggedIn()) {
    location.href = '/login.html';
  }
}

// Redirect to login if not admin
function requireAdmin() {
  if (!isAdmin()) {
    location.href = '/login.html';
  }
}

// Redirect to login if not teacher
function requireTeacher() {
  if (!isTeacher()) {
    location.href = '/login.html';
  }
}

// Redirect to login if not student
function requireStudent() {
  if (!isStudent()) {
    location.href = '/login.html';
  }
}

// Make authenticated API request (adds Authorization header)
function authenticatedFetch(url, options) {
  options = options || {};
  var token = getAuthToken();
  if (!token) {
    return Promise.reject(new Error('Not authenticated'));
  }
  options.headers = options.headers || {};
  options.headers['Authorization'] = 'Bearer ' + token;
  return fetch(url, options);
}

// Logout: clear auth state and call logout API
function logout() {
  var token = getAuthToken();
  if (token) {
    fetch('/api/auth/logout', {
      method: 'POST',
      headers: { 'Authorization': 'Bearer ' + token }
    }).catch(function() {});
  }
  clearAuthState();
  location.href = '/login.html';
}
