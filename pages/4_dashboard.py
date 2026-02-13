"""
Page 4: Dashboard - Complete Analytics View
"""

import streamlit as st
import sys
from pathlib import Path
import pandas as pd

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from src.visualizations import Visualizer
from src.auth import is_logged_in, get_current_user, logout

# ========================================
# AUTHENTICATION CHECK
# ========================================
if not is_logged_in(st.session_state):
    st.error("🔒 Please login first!")
    if st.button("🔐 Go to Login"):
        st.switch_page("pages/1_login.py")
    st.stop()

# Get current user
current_user = get_current_user(st.session_state)

# Check if processing is complete
if 'processing_complete' not in st.session_state or not st.session_state['processing_complete']:
    st.error("❌ Please process data first!")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📤 Go to Upload", use_container_width=True):
            st.switch_page("pages/2_upload_data.py")
    with col2:
        if st.button("⏳ Go to Processing", use_container_width=True):
            st.switch_page("pages/3_processing.py")
    st.stop()

# Load data from session state
df = st.session_state['df_processed']
quality_df = st.session_state['quality_df']
alerts_df = st.session_state['alerts_df']
stats = st.session_state['stats']

# ========================================
# SIDEBAR
# ========================================
with st.sidebar:
    st.markdown(f"""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 1.5rem; border-radius: 15px; color: white; margin-bottom: 2rem;'>
            <h3 style='margin: 0; color: white;'>👤 {current_user['full_name']}</h3>
            <p style='margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 0.9rem;'>
                Role: {current_user['role']}
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚪 Logout", use_container_width=True):
        logout(st.session_state)
        st.success("Logged out!")
        st.switch_page("pages/1_login.py")
    
    st.markdown("---")
    
    st.markdown("### 📍 Current Page")
    st.success("**Dashboard**")
    
    st.markdown("### 🔄 Navigation")
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")
    if st.button("📤 Upload New Data", use_container_width=True):
        # Clear session state
        for key in ['data_loaded', 'processing_complete', 'meal_data', 'df_processed', 'quality_df', 'alerts_df', 'stats']:
            if key in st.session_state:
                del st.session_state[key]
        st.switch_page("pages/2_upload_data.py")

# [REST OF THE DASHBOARD CODE FROM PREVIOUS RESPONSE GOES HERE]