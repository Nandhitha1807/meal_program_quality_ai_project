"""
Authentication Module
Simple user authentication for the application
"""

import hashlib
import json
import os
from pathlib import Path

# User database file
USER_DB_FILE = Path(__file__).parent.parent / "data" / "users.json"

# Default admin credentials
DEFAULT_ADMIN = {
    "username": "admin",
    "password_hash": hashlib.sha256("admin123".encode()).hexdigest(),
    "role": "Admin",
    "full_name": "System Administrator"
}

def init_user_db():
    """Initialize user database if it doesn't exist"""
    USER_DB_FILE.parent.mkdir(exist_ok=True)
    
    if not USER_DB_FILE.exists():
        users = {
            "admin": DEFAULT_ADMIN
        }
        save_users(users)

def load_users():
    """Load users from database"""
    init_user_db()
    
    try:
        with open(USER_DB_FILE, 'r') as f:
            return json.load(f)
    except:
        return {"admin": DEFAULT_ADMIN}

def save_users(users):
    """Save users to database"""
    with open(USER_DB_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    """Hash a password"""
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username, password):
    """Authenticate user"""
    users = load_users()
    
    if username not in users:
        return False, "User not found"
    
    password_hash = hash_password(password)
    
    if users[username]['password_hash'] == password_hash:
        return True, users[username]
    else:
        return False, "Invalid password"

def create_user(username, password, full_name, role="User"):
    """Create a new user"""
    users = load_users()
    
    if username in users:
        return False, "Username already exists"
    
    users[username] = {
        "username": username,
        "password_hash": hash_password(password),
        "role": role,
        "full_name": full_name
    }
    
    save_users(users)
    return True, "User created successfully"

def is_logged_in(session_state):
    """Check if user is logged in"""
    return 'logged_in' in session_state and session_state['logged_in']

def get_current_user(session_state):
    """Get current logged-in user"""
    if is_logged_in(session_state):
        return session_state.get('user_info', None)
    return None

def logout(session_state):
    """Logout user"""
    keys_to_delete = ['logged_in', 'user_info', 'username']
    for key in keys_to_delete:
        if key in session_state:
            del session_state[key]