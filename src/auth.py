# """
# Authentication Module
# Simple user authentication for the application
# """

# import hashlib
# import json
# import os
# from pathlib import Path

# # User database file
# USER_DB_FILE = Path(__file__).parent.parent / "data" / "users.json"

# # Default admin credentials
# DEFAULT_ADMIN = {
#     "username": "admin",
#     "password_hash": hashlib.sha256("admin123".encode()).hexdigest(),
#     "role": "Admin",
#     "full_name": "System Administrator"
# }

# def init_user_db():
#     """Initialize user database if it doesn't exist"""
#     USER_DB_FILE.parent.mkdir(exist_ok=True)
    
#     if not USER_DB_FILE.exists():
#         users = {
#             "admin": DEFAULT_ADMIN
#         }
#         save_users(users)

# def load_users():
#     """Load users from database"""
#     init_user_db()
    
#     try:
#         with open(USER_DB_FILE, 'r') as f:
#             return json.load(f)
#     except:
#         return {"admin": DEFAULT_ADMIN}

# def save_users(users):
#     """Save users to database"""
#     with open(USER_DB_FILE, 'w') as f:
#         json.dump(users, f, indent=4)

# def hash_password(password):
#     """Hash a password"""
#     return hashlib.sha256(password.encode()).hexdigest()

# def authenticate(username, password):
#     """Authenticate user"""
#     users = load_users()
    
#     if username not in users:
#         return False, "User not found"
    
#     password_hash = hash_password(password)
    
#     if users[username]['password_hash'] == password_hash:
#         return True, users[username]
#     else:
#         return False, "Invalid password"

# def create_user(username, password, full_name, role="User"):
#     """Create a new user"""
#     users = load_users()
    
#     if username in users:
#         return False, "Username already exists"
    
#     users[username] = {
#         "username": username,
#         "password_hash": hash_password(password),
#         "role": role,
#         "full_name": full_name
#     }
    
#     save_users(users)
#     return True, "User created successfully"

# def is_logged_in(session_state):
#     """Check if user is logged in"""
#     return 'logged_in' in session_state and session_state['logged_in']

# def get_current_user(session_state):
#     """Get current logged-in user"""
#     if is_logged_in(session_state):
#         return session_state.get('user_info', None)
#     return None

# def logout(session_state):
#     """Logout user"""
#     keys_to_delete = ['logged_in', 'user_info', 'username']
#     for key in keys_to_delete:
#         if key in session_state:
#             del session_state[key]
"""
Enhanced Authentication System with Role-Based Access Control
- Admin: Can see ALL schools
- School User: Can see ONLY their assigned school
"""
import json
import hashlib
from pathlib import Path

USER_DB_PATH = Path(__file__).parent.parent / "data" / "users.json"

def hash_password(password: str) -> str:
    """Hash password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

def init_user_db():
    """Initialize user database with default users"""
    USER_DB_PATH.parent.mkdir(exist_ok=True)
    
    default_users = {
        "admin": {
            "password_hash": hash_password("admin123"),
            "role": "admin",
            "full_name": "Administrator",
            "school_id": None  # Admin can see all schools
        },
        "sch001": {
            "password_hash": hash_password("sch001pass"),
            "role": "school",
            "full_name": "School 001 Manager",
            "school_id": "SCH001"  # Can only see SCH001
        },
        "sch002": {
            "password_hash": hash_password("sch002pass"),
            "role": "school",
            "full_name": "School 002 Manager",
            "school_id": "SCH002"  # Can only see SCH002
        },
        "sch003": {
            "password_hash": hash_password("sch003pass"),
            "role": "school",
            "full_name": "School 003 Manager",
            "school_id": "SCH003"  # Can only see SCH003
        }
    }
    
    if not USER_DB_PATH.exists():
        with open(USER_DB_PATH, 'w') as f:
            json.dump(default_users, f, indent=2)
    
    return default_users

def authenticate(username: str, password: str) -> tuple[bool, dict]:
    """
    Authenticate user and return user info
    Returns: (success: bool, user_info: dict or error_msg: str)
    """
    if not USER_DB_PATH.exists():
        init_user_db()
    
    with open(USER_DB_PATH, 'r') as f:
        users = json.load(f)
    
    if username not in users:
        return False, "User not found"
    
    user = users[username]
    password_hash = hash_password(password)
    
    if user['password_hash'] != password_hash:
        return False, "Invalid password"
    
    # Return user info (without password hash)
    return True, {
        'username': username,
        'role': user['role'],
        'full_name': user['full_name'],
        'school_id': user.get('school_id')  # None for admin, specific for school users
    }

def create_user(username: str, password: str, role: str, full_name: str, school_id: str = None):
    """Create a new user"""
    if not USER_DB_PATH.exists():
        init_user_db()
    
    with open(USER_DB_PATH, 'r') as f:
        users = json.load(f)
    
    if username in users:
        return False, "Username already exists"
    
    users[username] = {
        'password_hash': hash_password(password),
        'role': role,
        'full_name': full_name,
        'school_id': school_id
    }
    
    with open(USER_DB_PATH, 'w') as f:
        json.dump(users, f, indent=2)
    
    return True, "User created successfully"

def is_logged_in(session_state) -> bool:
    """Check if user is logged in"""
    return session_state.get('logged_in', False)

def get_current_user(session_state) -> dict:
    """Get current logged-in user info"""
    return session_state.get('user_info', {})

def logout(session_state):
    """Logout current user"""
    session_state['logged_in'] = False
    session_state['user_info'] = {}
    session_state['username'] = None
    
    # Clear data session
    for key in ['data_loaded', 'processing_complete', 'meal_data', 
                'df_processed', 'quality_df', 'alerts_df', 'stats']:
        if key in session_state:
            del session_state[key]

def can_view_school(session_state, school_id: str) -> bool:
    """
    Check if current user can view data for a specific school
    - Admin: can view all schools (returns True)
    - School user: can only view their assigned school
    """
    user_info = get_current_user(session_state)
    
    # Admin can see all schools
    if user_info.get('role') == 'admin':
        return True
    
    # School user can only see their own school
    return user_info.get('school_id') == school_id

def filter_data_by_role(session_state, df):
    """
    Filter dataframe based on user role
    - Admin: sees all data
    - School user: sees only their school's data
    """
    user_info = get_current_user(session_state)
    
    # Admin sees everything
    if user_info.get('role') == 'admin':
        return df
    
    # School user sees only their school
    school_id = user_info.get('school_id')
    if school_id and 'School_ID' in df.columns:
        return df[df['School_ID'] == school_id].copy()
    
    # Fallback: return empty dataframe if no school assigned
    return df.head(0)

def get_user_school_ids(session_state) -> list:
    """
    Get list of school IDs the current user can access
    - Admin: returns None (meaning all schools)
    - School user: returns [their_school_id]
    """
    user_info = get_current_user(session_state)
    
    # Admin can see all
    if user_info.get('role') == 'admin':
        return None  # None means "all schools"
    
    # School user can only see their school
    school_id = user_info.get('school_id')
    if school_id:
        return [school_id]
    
    return []