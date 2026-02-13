"""
Login Page
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent to path
sys.path.append(str(Path(__file__).parent.parent))

from src.auth import authenticate, is_logged_in

# Page config
st.set_page_config(
    page_title="Login - School Meal Monitor",
    page_icon="🔐",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .login-container {
        background: white;
        padding: 3rem;
        border-radius: 25px;
        box-shadow: 0 25px 50px rgba(0,0,0,0.3);
        max-width: 450px;
        margin: 2rem auto;
    }
    
    .login-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .login-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #1e293b;
        margin-bottom: 0.5rem;
    }
    
    .login-subtitle {
        color: #64748b;
        font-size: 1rem;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        padding: 0.8rem 2rem;
        font-weight: 700;
        border: none;
        width: 100%;
        font-size: 1.1rem;
    }
    
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #e2e8f0;
        padding: 0.8rem 1rem;
        font-size: 1rem;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    .demo-credentials {
        background: #f8fafc;
        padding: 1rem;
        border-radius: 10px;
        margin-top: 1.5rem;
        border-left: 4px solid #3b82f6;
    }
    </style>
""", unsafe_allow_html=True)

# Check if already logged in
if is_logged_in(st.session_state):
    st.success("✅ Already logged in!")
    if st.button("Go to Upload Page"):
        st.switch_page("pages/2_upload_data.py")
    st.stop()

# Login Container
st.markdown('<div class="login-container">', unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="login-header">
        <div style="font-size: 4rem; margin-bottom: 1rem;">🔐</div>
        <div class="login-title">Welcome Back</div>
        <div class="login-subtitle">Login to access the dashboard</div>
    </div>
""", unsafe_allow_html=True)

# Login Form
with st.form("login_form"):
    username = st.text_input(
        "Username",
        placeholder="Enter your username",
        help="Default: admin"
    )
    
    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password",
        help="Default: admin123"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    submit = st.form_submit_button("🚀 Login", use_container_width=True)
    
    if submit:
        if not username or not password:
            st.error("❌ Please enter both username and password")
        else:
            success, result = authenticate(username, password)
            
            if success:
                # Store in session
                st.session_state['logged_in'] = True
                st.session_state['user_info'] = result
                st.session_state['username'] = username
                
                st.success(f"✅ Welcome, {result['full_name']}!")
                st.balloons()
                
                # Redirect
                st.switch_page("pages/2_upload_data.py")
            else:
                st.error(f"❌ {result}")

# Demo Credentials
st.markdown("""
    <div class="demo-credentials">
        <strong>📝 Demo Credentials</strong><br>
        Username: <code>admin</code><br>
        Password: <code>admin123</code>
    </div>
""", unsafe_allow_html=True)

# Back to home
st.markdown("<br>", unsafe_allow_html=True)
if st.button("← Back to Home", use_container_width=True):
    st.switch_page("app.py")

st.markdown('</div>', unsafe_allow_html=True)