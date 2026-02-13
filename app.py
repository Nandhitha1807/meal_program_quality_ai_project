"""
School Meal Quality Monitor - Landing Page
"""

import streamlit as st
from pathlib import Path
import sys

# Add src to path
sys.path.append(str(Path(__file__).parent))

from src.auth import is_logged_in, get_current_user

# Page config
st.set_page_config(
    page_title="School Meal Quality Monitor",
    page_icon="🍽️",
    layout="wide",
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
        padding: 0;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .hero-section {
        text-align: center;
        padding: 6rem 2rem 4rem 2rem;
        color: white;
    }
    
    .hero-title {
        font-size: 5rem;
        font-weight: 900;
        margin-bottom: 1rem;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
        animation: fadeInDown 1s ease-in-out;
    }
    
    .hero-subtitle {
        font-size: 1.8rem;
        font-weight: 400;
        opacity: 0.95;
        margin-bottom: 3rem;
        animation: fadeInUp 1s ease-in-out;
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .feature-card {
        background: white;
        padding: 2.5rem;
        border-radius: 25px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        margin: 1rem;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        height: 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-15px) scale(1.02);
        box-shadow: 0 25px 50px rgba(0,0,0,0.25);
    }
    
    .feature-icon {
        font-size: 4rem;
        margin-bottom: 1.5rem;
        display: inline-block;
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    .feature-title {
        font-size: 1.6rem;
        font-weight: 800;
        color: #1e293b;
        margin-bottom: 1rem;
    }
    
    .feature-desc {
        color: #64748b;
        line-height: 1.8;
        font-size: 1.05rem;
    }
    
    .stats-container {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(15px);
        border-radius: 25px;
        padding: 2.5rem;
        margin: 3rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .stat-item {
        text-align: center;
        color: white;
    }
    
    .stat-number {
        font-size: 4rem;
        font-weight: 900;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .stat-label {
        font-size: 1.1rem;
        opacity: 0.95;
        font-weight: 600;
    }
    
    .cta-section {
        background: white;
        padding: 4rem 2rem;
        border-radius: 30px 30px 0 0;
        margin-top: 4rem;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        border-radius: 50px;
        padding: 1.2rem 4rem;
        font-size: 1.3rem;
        font-weight: 800;
        border: none;
        box-shadow: 0 15px 35px rgba(16, 185, 129, 0.4);
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton>button:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 45px rgba(16, 185, 129, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# Check if logged in
if is_logged_in(st.session_state):
    user_info = get_current_user(st.session_state)
    
    # Show logged in navigation in corner
    col1, col2 = st.columns([6, 1])
    with col2:
        if st.button("🚪 Logout", key="logout_btn"):
            from src.auth import logout
            logout(st.session_state)
            st.rerun()

# Hero Section
st.markdown("""
    <div class="hero-section">
        <div class="hero-title">
            🍽️ School Meal<br>Quality Monitor
        </div>
        <div class="hero-subtitle">
            AI-Powered Quality Assessment for Better Student Nutrition
        </div>
    </div>
""", unsafe_allow_html=True)

# Stats Section
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div class="stats-container">
            <div class="stat-item">
                <div class="stat-number">5</div>
                <div class="stat-label">Quality Dimensions</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="stats-container">
            <div class="stat-item">
                <div class="stat-number">100%</div>
                <div class="stat-label">Explainable AI</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="stats-container">
            <div class="stat-item">
                <div class="stat-number">$0</div>
                <div class="stat-label">Hardware Cost</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="stats-container">
            <div class="stat-item">
                <div class="stat-number">5s</div>
                <div class="stat-label">Analysis Time</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# White Section for Features
st.markdown('<div class="cta-section">', unsafe_allow_html=True)

# Features
st.markdown("""
    <h2 style='text-align: center; color: #1e293b; font-size: 3rem; font-weight: 900; margin-bottom: 4rem;'>
        ✨ Key Features
    </h2>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Multi-Dimensional</div>
            <div class="feature-desc">
                Evaluates nutrition, waste, hygiene, taste, and menu compliance
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <div class="feature-title">AI-Powered</div>
            <div class="feature-desc">
                Intelligent alerts and prioritized recommendations
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📈</div>
            <div class="feature-title">Real-Time Analytics</div>
            <div class="feature-desc">
                Interactive dashboards with live visualizations
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">💡</div>
            <div class="feature-title">Actionable Insights</div>
            <div class="feature-desc">
                Specific recommendations, not just data
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔒</div>
            <div class="feature-title">Secure</div>
            <div class="feature-desc">
                MySQL database with encrypted storage
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Lightning Fast</div>
            <div class="feature-desc">
                Process data in seconds
            </div>
        </div>
    """, unsafe_allow_html=True)

# CTA
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
    <h2 style='text-align: center; color: #1e293b; font-size: 2.5rem; font-weight: 800; margin-bottom: 3rem;'>
        Ready to Get Started?
    </h2>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if is_logged_in(st.session_state):
        if st.button("🚀 Go to Dashboard", use_container_width=True, type="primary"):
            st.switch_page("pages/2_upload_data.py")
    else:
        if st.button("🔐 Login to Start", use_container_width=True, type="primary"):
            st.switch_page("pages/1_login.py")

st.markdown('</div>', unsafe_allow_html=True)