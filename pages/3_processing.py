"""
Page 3: Processing Data
Shows animated processing and calculates quality scores
"""

import streamlit as st
import sys
from pathlib import Path
import time

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from src.data_processor import DataProcessor
from models.quality_rules import QualityAssessment
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

# ========================================
# PAGE CONFIGURATION
# ========================================
st.set_page_config(
    page_title="Processing - School Meal Monitor",
    page_icon="⏳",
    layout="wide"
)

# ========================================
# CUSTOM CSS
# ========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .processing-container {
        text-align: center;
        padding: 4rem 2rem;
    }
    
    .spinner-icon {
        font-size: 6rem;
        animation: spin 2s linear infinite;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .progress-step {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .step-complete {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        border-left: 5px solid #10b981;
    }
    
    .step-processing {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border-left: 5px solid #3b82f6;
    }
    
    .step-pending {
        background: #f3f4f6;
        border-left: 5px solid #9ca3af;
    }
    </style>
""", unsafe_allow_html=True)

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
        st.switch_page("pages/1_login.py")
    
    st.markdown("---")
    
    st.markdown("### 📍 Current Step")
    st.success("**Step 2:** Processing Data")
    
    st.markdown("### 🔄 Progress")
    st.write("1. ✅ Upload Data")
    st.write("2. ⏳ Processing (Current)")
    st.write("3. 📊 Dashboard")

# ========================================
# CHECK IF DATA EXISTS
# ========================================
if 'data_loaded' not in st.session_state or not st.session_state['data_loaded']:
    st.error("❌ No data found! Please upload data first.")
    if st.button("📤 Go to Upload Page", type="primary"):
        st.switch_page("pages/2_upload_data.py")
    st.stop()

# ========================================
# HEADER
# ========================================
st.markdown("""
    <div class="processing-container">
        <div class="spinner-icon">⚙️</div>
        <h1 style='color: #1e293b; font-size: 3rem; margin: 2rem 0;'>
            Processing Your Data
        </h1>
        <p style='color: #64748b; font-size: 1.2rem;'>
            Our AI is analyzing meal quality across multiple dimensions
        </p>
    </div>
""", unsafe_allow_html=True)

# ========================================
# PROGRESS STEPS
# ========================================
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    # Step 1: Loading Data
    step1 = st.empty()
    step1.markdown("""
        <div class="progress-step step-processing">
            <h3>🔄 Step 1: Loading Data...</h3>
            <p>Reading meal records from source</p>
        </div>
    """, unsafe_allow_html=True)
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Load data
    df = st.session_state['meal_data']
    
    status_text.text(f"📊 Loaded {len(df)} records from {df['School_ID'].nunique()} schools")
    time.sleep(1)
    progress_bar.progress(20)
    
    step1.markdown("""
        <div class="progress-step step-complete">
            <h3>✅ Step 1: Data Loaded Successfully</h3>
            <p>All meal records validated and ready</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Step 2: Calculating Metrics
    step2 = st.empty()
    step2.markdown("""
        <div class="progress-step step-processing">
            <h3>🔄 Step 2: Calculating Metrics...</h3>
            <p>Computing waste %, compliance %, hygiene scores</p>
        </div>
    """, unsafe_allow_html=True)
    
    status_text.text("🧮 Calculating derived metrics...")
    time.sleep(1.5)
    progress_bar.progress(40)
    
    processor = DataProcessor(df=df)
    df_processed = processor.calculate_metrics()
    
    progress_bar.progress(60)
    
    step2.markdown("""
        <div class="progress-step step-complete">
            <h3>✅ Step 2: Metrics Calculated</h3>
            <p>All performance indicators computed successfully</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Step 3: AI Quality Assessment
    step3 = st.empty()
    step3.markdown("""
        <div class="progress-step step-processing">
            <h3>🔄 Step 3: Running AI Quality Assessment...</h3>
            <p>Applying intelligent rules across 5 dimensions</p>
        </div>
    """, unsafe_allow_html=True)
    
    status_text.text("🤖 AI analyzing quality: Nutrition, Waste, Hygiene, Taste, Menu...")
    time.sleep(1.5)
    progress_bar.progress(80)
    
    quality_checker = QualityAssessment(df_processed)
    quality_df = quality_checker.calculate_overall_quality()
    alerts_df = quality_checker.generate_alerts(quality_df)
    
    progress_bar.progress(90)
    
    step3.markdown("""
        <div class="progress-step step-complete">
            <h3>✅ Step 3: Quality Assessment Complete</h3>
            <p>AI analysis finished, quality scores generated</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Step 4: Generating Insights
    step4 = st.empty()
    step4.markdown("""
        <div class="progress-step step-processing">
            <h3>🔄 Step 4: Generating Insights...</h3>
            <p>Creating alerts and recommendations</p>
        </div>
    """, unsafe_allow_html=True)
    
    status_text.text("💡 Generating insights and recommendations...")
    time.sleep(1)
    progress_bar.progress(100)
    
    stats = processor.get_summary_stats()
    
    step4.markdown("""
        <div class="progress-step step-complete">
            <h3>✅ Step 4: Insights Generated</h3>
            <p>Alerts and recommendations ready for review</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Store in session state
    st.session_state['df_processed'] = df_processed
    st.session_state['quality_df'] = quality_df
    st.session_state['alerts_df'] = alerts_df
    st.session_state['stats'] = stats
    st.session_state['processing_complete'] = True
    
    status_text.success("✅ Processing Complete!")
    
    # Success message
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style='background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%); 
                    padding: 2.5rem; border-radius: 20px; text-align: center;
                    box-shadow: 0 10px 25px rgba(16, 185, 129, 0.2);'>
            <h2 style='color: #065f46; margin: 0; font-size: 2.5rem;'>🎉 Analysis Complete!</h2>
            <p style='color: #047857; margin: 1rem 0; font-size: 1.2rem;'>
                Your quality assessment is ready. View the interactive dashboard for detailed insights.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Quick Summary
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        st.metric(
            "🏫 Schools Analyzed",
            stats['total_schools'],
            help="Total number of schools in dataset"
        )
    
    with col_b:
        st.metric(
            "🚨 Alerts Generated",
            len(alerts_df),
            help="Number of quality alerts detected"
        )
    
    with col_c:
        excellent = len(quality_df[quality_df['Overall_Quality_Score'] >= 85])
        st.metric(
            "⭐ Excellent Schools",
            excellent,
            help="Schools with score >= 85"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Navigate to dashboard
    if st.button("📊 View Dashboard", use_container_width=True, type="primary"):
        st.balloons()
        time.sleep(0.5)
        st.switch_page("pages/4_dashboard.py")