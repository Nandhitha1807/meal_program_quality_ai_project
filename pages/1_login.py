"""
Login Page - Authentication Gateway
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
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .login-container {
        background: white;
        padding: 3rem 2.5rem;
        border-radius: 25px;
        box-shadow: 0 25px 50px rgba(0,0,0,0.3);
        max-width: 500px;
        width: 100%;
        animation: slideIn 0.5s ease-out;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .login-header {
        text-align: center;
        margin-bottom: 2.5rem;
    }
    
    .login-icon {
        font-size: 5rem;
        margin-bottom: 1rem;
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    .login-title {
        font-size: 2.5rem;
        font-weight: 900;
        color: #1e293b;
        margin-bottom: 0.5rem;
    }
    
    .login-subtitle {
        color: #64748b;
        font-size: 1.1rem;
        font-weight: 500;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 12px;
        padding: 1rem 2rem;
        font-weight: 700;
        border: none;
        width: 100%;
        font-size: 1.15rem;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
    }
    
    .stTextInput>div>div>input {
        border-radius: 12px;
        border: 2px solid #e2e8f0;
        padding: 1rem 1.2rem;
        font-size: 1.05rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
    }
    
    .demo-credentials {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin-top: 2rem;
        border-left: 5px solid #3b82f6;
    }
    
    .demo-credentials strong {
        color: #1e40af;
        font-size: 1.05rem;
    }
    
    .demo-credentials code {
        background: white;
        padding: 0.3rem 0.8rem;
        border-radius: 6px;
        color: #667eea;
        font-weight: 700;
        font-size: 0.95rem;
    }
    
    .back-button {
        text-align: center;
        margin-top: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Check if already logged in
if is_logged_in(st.session_state):
    st.success("✅ You are already logged in!")
    st.info("Redirecting to upload page...")
    
    if st.button("📤 Go to Upload Page", use_container_width=True):
        st.switch_page("pages/2_upload_data.py")
    
    st.stop()

# Login Container
st.markdown('<div class="login-container">', unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="login-header">
        <div class="login-icon">🔐</div>
        <div class="login-title">Welcome Back</div>
        <div class="login-subtitle">Login to access School Meal Quality Monitor</div>
    </div>
""", unsafe_allow_html=True)

# Login Form
with st.form("login_form", clear_on_submit=False):
    username = st.text_input(
        "👤 Username",
        placeholder="Enter your username",
        help="Use 'admin' for demo access"
    )
    
    password = st.text_input(
        "🔑 Password",
        type="password",
        placeholder="Enter your password",
        help="Use 'admin123' for demo access"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        submit = st.form_submit_button("🚀 Login", use_container_width=True, type="primary")
    
    with col2:
        clear = st.form_submit_button("🔄 Clear", use_container_width=True)
    
    if submit:
        if not username or not password:
            st.error("❌ Please enter both username and password")
        else:
            with st.spinner("🔄 Authenticating..."):
                success, result = authenticate(username, password)
                
                if success:
                    # Store in session
                    st.session_state['logged_in'] = True
                    st.session_state['user_info'] = result
                    st.session_state['username'] = username
                    
                    st.success(f"✅ Welcome, {result['full_name']}!")
                    st.balloons()
                    
                    # Small delay for effect
                    import time
                    time.sleep(1)
                    
                    # Redirect
                    st.switch_page("pages/2_upload_data.py")
                else:
                    st.error(f"❌ {result}")
                    st.warning("💡 Hint: Use 'admin' / 'admin123' for demo")

# Demo Credentials Box
st.markdown("""
    <div class="demo-credentials">
        <strong>📝 Demo Login Credentials</strong><br><br>
        <strong>Username:</strong> <code>admin</code><br>
        <strong>Password:</strong> <code>admin123</code><br><br>
        <em style="color: #64748b; font-size: 0.9rem;">
            💡 Use these credentials to explore the system
        </em>
    </div>
""", unsafe_allow_html=True)

# Back to Home Button
st.markdown('<div class="back-button">', unsafe_allow_html=True)
if st.button("← Back to Home", use_container_width=True):
    st.switch_page("app.py")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='text-align: center; color: white; padding: 2rem; margin-top: 2rem;'>
        <p style='margin: 0; opacity: 0.9;'>
            🍽️ School Meal Quality Monitor | Powered by AI
        </p>
    </div>
""", unsafe_allow_html=True)