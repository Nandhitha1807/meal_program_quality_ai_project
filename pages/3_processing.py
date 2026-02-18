# # """
# # Page 3: Processing Data
# # Shows animated processing and calculates quality scores
# # """

# # import streamlit as st
# # import sys
# # from pathlib import Path
# # import time

# # # Add parent directory to path
# # sys.path.append(str(Path(__file__).parent.parent))

# # from src.data_processor import DataProcessor
# # from models.quality_rules import QualityAssessment
# # from src.auth import is_logged_in, get_current_user, logout

# # # ========================================
# # # AUTHENTICATION CHECK
# # # ========================================
# # if not is_logged_in(st.session_state):
# #     st.error("🔒 Please login first!")
# #     if st.button("🔐 Go to Login"):
# #         st.switch_page("pages/1_login.py")
# #     st.stop()

# # # Get current user
# # current_user = get_current_user(st.session_state)

# # # ========================================
# # # PAGE CONFIGURATION
# # # ========================================
# # st.set_page_config(
# #     page_title="Processing - School Meal Monitor",
# #     page_icon="⏳",
# #     layout="wide"
# # )

# # # ========================================
# # # CUSTOM CSS
# # # ========================================
# # st.markdown("""
# #     <style>
# #     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    
# #     * {
# #         font-family: 'Inter', sans-serif;
# #     }
    
# #     .processing-container {
# #         text-align: center;
# #         padding: 4rem 2rem;
# #     }
    
# #     .spinner-icon {
# #         font-size: 6rem;
# #         animation: spin 2s linear infinite;
# #     }
    
# #     @keyframes spin {
# #         0% { transform: rotate(0deg); }
# #         100% { transform: rotate(360deg); }
# #     }
    
# #     .progress-step {
# #         background: white;
# #         padding: 1.5rem;
# #         border-radius: 15px;
# #         margin: 1rem 0;
# #         box-shadow: 0 4px 6px rgba(0,0,0,0.1);
# #         transition: all 0.3s ease;
# #     }
    
# #     .step-complete {
# #         background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
# #         border-left: 5px solid #10b981;
# #     }
    
# #     .step-processing {
# #         background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
# #         border-left: 5px solid #3b82f6;
# #     }
    
# #     .step-pending {
# #         background: #f3f4f6;
# #         border-left: 5px solid #9ca3af;
# #     }
# #     </style>
# # """, unsafe_allow_html=True)

# # # ========================================
# # # SIDEBAR
# # # ========================================
# # with st.sidebar:
# #     st.markdown(f"""
# #         <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
# #                     padding: 1.5rem; border-radius: 15px; color: white; margin-bottom: 2rem;'>
# #             <h3 style='margin: 0; color: white;'>👤 {current_user['full_name']}</h3>
# #             <p style='margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 0.9rem;'>
# #                 Role: {current_user['role']}
# #             </p>
# #         </div>
# #     """, unsafe_allow_html=True)
    
# #     if st.button("🚪 Logout", use_container_width=True):
# #         logout(st.session_state)
# #         st.switch_page("pages/1_login.py")
    
# #     st.markdown("---")
    
# #     st.markdown("### 📍 Current Step")
# #     st.success("**Step 2:** Processing Data")
    
# #     st.markdown("### 🔄 Progress")
# #     st.write("1. ✅ Upload Data")
# #     st.write("2. ⏳ Processing (Current)")
# #     st.write("3. 📊 Dashboard")

# # # ========================================
# # # CHECK IF DATA EXISTS
# # # ========================================
# # if 'data_loaded' not in st.session_state or not st.session_state['data_loaded']:
# #     st.error("❌ No data found! Please upload data first.")
# #     if st.button("📤 Go to Upload Page", type="primary"):
# #         st.switch_page("pages/2_upload_data.py")
# #     st.stop()

# # # ========================================
# # # HEADER
# # # ========================================
# # st.markdown("""
# #     <div class="processing-container">
# #         <div class="spinner-icon">⚙️</div>
# #         <h1 style='color: #1e293b; font-size: 3rem; margin: 2rem 0;'>
# #             Processing Your Data
# #         </h1>
# #         <p style='color: #64748b; font-size: 1.2rem;'>
# #             Our AI is analyzing meal quality across multiple dimensions
# #         </p>
# #     </div>
# # """, unsafe_allow_html=True)

# # # ========================================
# # # PROGRESS STEPS
# # # ========================================
# # col1, col2, col3 = st.columns([1, 3, 1])

# # with col2:
# #     # Step 1: Loading Data
# #     step1 = st.empty()
# #     step1.markdown("""
# #         <div class="progress-step step-processing">
# #             <h3>🔄 Step 1: Loading Data...</h3>
# #             <p>Reading meal records from source</p>
# #         </div>
# #     """, unsafe_allow_html=True)
    
# #     progress_bar = st.progress(0)
# #     status_text = st.empty()
    
# #     # Load data
# #     df = st.session_state['meal_data']
    
# #     status_text.text(f"📊 Loaded {len(df)} records from {df['School_ID'].nunique()} schools")
# #     time.sleep(1)
# #     progress_bar.progress(20)
    
# #     step1.markdown("""
# #         <div class="progress-step step-complete">
# #             <h3>✅ Step 1: Data Loaded Successfully</h3>
# #             <p>All meal records validated and ready</p>
# #         </div>
# #     """, unsafe_allow_html=True)
    
# #     # Step 2: Calculating Metrics
# #     step2 = st.empty()
# #     step2.markdown("""
# #         <div class="progress-step step-processing">
# #             <h3>🔄 Step 2: Calculating Metrics...</h3>
# #             <p>Computing waste %, compliance %, hygiene scores</p>
# #         </div>
# #     """, unsafe_allow_html=True)
    
# #     status_text.text("🧮 Calculating derived metrics...")
# #     time.sleep(1.5)
# #     progress_bar.progress(40)
    
# #     processor = DataProcessor(df=df)
# #     df_processed = processor.calculate_metrics()
    
# #     progress_bar.progress(60)
    
# #     step2.markdown("""
# #         <div class="progress-step step-complete">
# #             <h3>✅ Step 2: Metrics Calculated</h3>
# #             <p>All performance indicators computed successfully</p>
# #         </div>
# #     """, unsafe_allow_html=True)
    
# #     # Step 3: AI Quality Assessment
# #     step3 = st.empty()
# #     step3.markdown("""
# #         <div class="progress-step step-processing">
# #             <h3>🔄 Step 3: Running AI Quality Assessment...</h3>
# #             <p>Applying intelligent rules across 5 dimensions</p>
# #         </div>
# #     """, unsafe_allow_html=True)
    
# #     status_text.text("🤖 AI analyzing quality: Nutrition, Waste, Hygiene, Taste, Menu...")
# #     time.sleep(1.5)
# #     progress_bar.progress(80)
    
# #     quality_checker = QualityAssessment(df_processed)
# #     quality_df = quality_checker.calculate_overall_quality()
# #     alerts_df = quality_checker.generate_alerts(quality_df)
    
# #     progress_bar.progress(90)
    
# #     step3.markdown("""
# #         <div class="progress-step step-complete">
# #             <h3>✅ Step 3: Quality Assessment Complete</h3>
# #             <p>AI analysis finished, quality scores generated</p>
# #         </div>
# #     """, unsafe_allow_html=True)
    
# #     # Step 4: Generating Insights
# #     step4 = st.empty()
# #     step4.markdown("""
# #         <div class="progress-step step-processing">
# #             <h3>🔄 Step 4: Generating Insights...</h3>
# #             <p>Creating alerts and recommendations</p>
# #         </div>
# #     """, unsafe_allow_html=True)
    
# #     status_text.text("💡 Generating insights and recommendations...")
# #     time.sleep(1)
# #     progress_bar.progress(100)
    
# #     stats = processor.get_summary_stats()
    
# #     step4.markdown("""
# #         <div class="progress-step step-complete">
# #             <h3>✅ Step 4: Insights Generated</h3>
# #             <p>Alerts and recommendations ready for review</p>
# #         </div>
# #     """, unsafe_allow_html=True)
    
# #     # Store in session state
# #     st.session_state['df_processed'] = df_processed
# #     st.session_state['quality_df'] = quality_df
# #     st.session_state['alerts_df'] = alerts_df
# #     st.session_state['stats'] = stats
# #     st.session_state['processing_complete'] = True
    
# #     status_text.success("✅ Processing Complete!")
    
# #     # Success message
# #     st.markdown("<br><br>", unsafe_allow_html=True)
# #     st.markdown("""
# #         <div style='background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%); 
# #                     padding: 2.5rem; border-radius: 20px; text-align: center;
# #                     box-shadow: 0 10px 25px rgba(16, 185, 129, 0.2);'>
# #             <h2 style='color: #065f46; margin: 0; font-size: 2.5rem;'>🎉 Analysis Complete!</h2>
# #             <p style='color: #047857; margin: 1rem 0; font-size: 1.2rem;'>
# #                 Your quality assessment is ready. View the interactive dashboard for detailed insights.
# #             </p>
# #         </div>
# #     """, unsafe_allow_html=True)
    
# #     st.markdown("<br>", unsafe_allow_html=True)
    
# #     # Quick Summary
# #     col_a, col_b, col_c = st.columns(3)
    
# #     with col_a:
# #         st.metric(
# #             "🏫 Schools Analyzed",
# #             stats['total_schools'],
# #             help="Total number of schools in dataset"
# #         )
    
# #     with col_b:
# #         st.metric(
# #             "🚨 Alerts Generated",
# #             len(alerts_df),
# #             help="Number of quality alerts detected"
# #         )
    
# #     with col_c:
# #         excellent = len(quality_df[quality_df['Overall_Quality_Score'] >= 85])
# #         st.metric(
# #             "⭐ Excellent Schools",
# #             excellent,
# #             help="Schools with score >= 85"
# #         )
    
# #     st.markdown("<br>", unsafe_allow_html=True)
    
# #     # Navigate to dashboard
# #     if st.button("📊 View Dashboard", use_container_width=True, type="primary"):
# #         st.balloons()
# #         time.sleep(0.5)
# #         st.switch_page("pages/4_dashboard.py")
# """
# pages/3_processing.py — Processing Page
# """
# import streamlit as st
# import sys, time
# from pathlib import Path

# sys.path.append(str(Path(__file__).parent.parent))
# from src.data_processor import DataProcessor
# from models.quality_rules import QualityAssessment
# from src.auth import is_logged_in, get_current_user, logout
# from src.styles import GLOBAL_CSS

# if not is_logged_in(st.session_state):
#     st.error("🔒 Please sign in first.")
#     if st.button("Go to Login →", type="primary"): st.switch_page("pages/1_login.py")
#     st.stop()

# current_user = get_current_user(st.session_state)

# st.set_page_config(page_title="Processing · School Meal Monitor", page_icon="⚙️", layout="wide")
# st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
# st.markdown("""
# <style>
# /* ── STEP CARD ── */
# .proc-step {
#     border-radius: var(--r-md);
#     padding: 1.3rem 1.6rem;
#     margin-bottom: 0.9rem;
#     border-left: 4px solid;
#     display: flex;
#     align-items: flex-start;
#     gap: 1.2rem;
#     transition: all 0.4s ease;
#     border-top: 1px solid var(--border);
#     border-right: 1px solid var(--border);
#     border-bottom: 1px solid var(--border);
# }
# .proc-step.pending {
#     border-left-color: rgba(148,163,184,0.3);
#     background: var(--surface-1);
#     opacity: 0.45;
# }
# .proc-step.running {
#     border-left-color: var(--c-blue);
#     background: var(--info-bg);
# }
# .proc-step.done {
#     border-left-color: var(--c-emerald);
#     background: var(--success-bg);
# }
# .proc-icon {
#     font-size: 1.5rem;
#     flex-shrink: 0;
#     width: 2.4rem;
#     text-align: center;
#     margin-top: .1rem;
# }
# .proc-title { font-size:.95rem; font-weight:700; margin:0 0 .25rem; }
# .proc-desc  { font-size:.82rem; opacity:.6; margin:0; }

# /* SUMMARY CARDS */
# .summary-card {
#     background: var(--surface-1);
#     border: 1px solid var(--border);
#     border-radius: var(--r-md);
#     padding: 1.5rem;
#     text-align: center;
# }
# .summary-card .sc-val {
#     font-family: 'Fraunces', serif !important;
#     font-size: 2.5rem; font-weight:700; margin:0 0 .3rem; line-height:1;
#     color: var(--c-blue);
# }
# .summary-card .sc-lbl {
#     font-size:.78rem; font-weight:700; text-transform:uppercase;
#     letter-spacing:.07em; opacity:.55; margin:0;
# }

# /* SUCCESS BANNER */
# .success-banner {
#     background: linear-gradient(135deg, rgba(16,185,129,0.12) 0%, rgba(6,182,212,0.08) 100%);
#     border: 1px solid rgba(16,185,129,0.3);
#     border-radius: var(--r-lg);
#     padding: 2.5rem;
#     text-align: center;
#     margin: 2rem 0;
# }
# .success-banner h2 {
#     font-family: 'Fraunces', serif !important;
#     font-size: 2rem; font-weight:700;
#     color: var(--c-emerald); margin:0 0 .6rem;
# }
# .success-banner p { opacity:.65; margin:0; font-size:.95rem; }
# </style>
# """, unsafe_allow_html=True)

# # ── SIDEBAR ──
# with st.sidebar:
#     st.markdown(f'<div class="sidebar-user-card"><h4>👤 {current_user["full_name"]}</h4><p>Role: {current_user["role"]}</p></div>', unsafe_allow_html=True)
#     if st.button("🚪 Sign Out", use_container_width=True):
#         logout(st.session_state)
#         st.switch_page("pages/1_login.py")
#     st.markdown("---")
#     st.markdown("""
#     <div class="step-bar">
#       <div class="step-item"><div class="step-dot done">✓</div><span class="step-text done">Upload</span></div>
#       <div class="step-connector done"></div>
#       <div class="step-item"><div class="step-dot active">2</div><span class="step-text active">Process</span></div>
#       <div class="step-connector"></div>
#       <div class="step-item"><div class="step-dot">3</div><span class="step-text">Dashboard</span></div>
#     </div>
#     """, unsafe_allow_html=True)

# # No data guard
# if 'data_loaded' not in st.session_state or not st.session_state['data_loaded']:
#     st.error("❌ No data found. Please upload data first.")
#     if st.button("← Go to Upload", type="primary"): st.switch_page("pages/2_upload_data.py")
#     st.stop()

# # ── HEADER ──
# st.markdown("""
# <div class="page-header">
#   <div class="header-badge">Step 2 of 3</div>
#   <h1>⚙️ Processing Data</h1>
#   <p>Our AI engine is analyzing meal quality across all five dimensions</p>
# </div>
# """, unsafe_allow_html=True)

# # ── PROCESSING AREA ──
# _, center, _ = st.columns([1, 3, 1])

# with center:
#     df = st.session_state['meal_data']

#     # ── STEP PLACEHOLDERS ──
#     s1 = st.empty()
#     s2 = st.empty()
#     s3 = st.empty()
#     s4 = st.empty()
#     progress = st.progress(0)
#     status   = st.empty()

#     def step_html(state, icon, title, desc):
#         return f'<div class="proc-step {state}"><div class="proc-icon">{icon}</div><div><p class="proc-title">{title}</p><p class="proc-desc">{desc}</p></div></div>'

#     # ── STEP 1 ──
#     s1.markdown(step_html("running","🔄","Loading Data","Reading meal records from source..."), unsafe_allow_html=True)
#     s2.markdown(step_html("pending","⏳","Calculating Metrics","Waiting..."), unsafe_allow_html=True)
#     s3.markdown(step_html("pending","⏳","AI Quality Assessment","Waiting..."), unsafe_allow_html=True)
#     s4.markdown(step_html("pending","⏳","Generating Insights","Waiting..."), unsafe_allow_html=True)

#     status.caption(f"📊 Found {len(df):,} records from {df['School_ID'].nunique()} schools")
#     time.sleep(0.9)
#     progress.progress(20)
#     s1.markdown(step_html("done","✅","Data Loaded","All records validated and ready"), unsafe_allow_html=True)

#     # ── STEP 2 ──
#     s2.markdown(step_html("running","🔄","Calculating Metrics","Computing waste %, compliance %, hygiene scores..."), unsafe_allow_html=True)
#     status.caption("🧮 Computing derived metrics...")
#     time.sleep(1.2)
#     processor = DataProcessor(df=df)
#     df_processed = processor.calculate_metrics()
#     progress.progress(50)
#     s2.markdown(step_html("done","✅","Metrics Calculated","All performance indicators computed"), unsafe_allow_html=True)

#     # ── STEP 3 ──
#     s3.markdown(step_html("running","🔄","AI Quality Assessment","Scoring across Nutrition · Waste · Hygiene · Taste · Menu..."), unsafe_allow_html=True)
#     status.caption("🤖 AI analysing all 5 quality dimensions...")
#     time.sleep(1.4)
#     checker    = QualityAssessment(df_processed)
#     quality_df = checker.calculate_overall_quality()
#     alerts_df  = checker.generate_alerts(quality_df)
#     progress.progress(80)
#     s3.markdown(step_html("done","✅","Quality Assessment Complete","Scores generated for all schools"), unsafe_allow_html=True)

#     # ── STEP 4 ──
#     s4.markdown(step_html("running","🔄","Generating Insights","Building alerts and recommendations..."), unsafe_allow_html=True)
#     status.caption("💡 Generating alerts and recommendations...")
#     time.sleep(0.9)
#     stats = processor.get_summary_stats()
#     progress.progress(100)
#     s4.markdown(step_html("done","✅","Insights Ready","Alerts and recommendations generated"), unsafe_allow_html=True)

#     # ── SAVE TO SESSION ──
#     st.session_state.update({
#         'df_processed': df_processed,
#         'quality_df':   quality_df,
#         'alerts_df':    alerts_df,
#         'stats':        stats,
#         'processing_complete': True
#     })

#     status.empty()

#     # ── SUCCESS BANNER ──
#     excellent = len(quality_df[quality_df['Overall_Quality_Score'] >= 85])
#     st.markdown(f"""
#     <div class="success-banner">
#       <h2>🎉 Analysis Complete!</h2>
#       <p>Your quality assessment is ready. View the interactive dashboard for full insights.</p>
#     </div>
#     """, unsafe_allow_html=True)

#     # ── QUICK SUMMARY ──
#     sc1, sc2, sc3 = st.columns(3)
#     with sc1:
#         st.markdown(f'<div class="summary-card"><p class="sc-val">{stats["total_schools"]}</p><p class="sc-lbl">Schools Analysed</p></div>', unsafe_allow_html=True)
#     with sc2:
#         st.markdown(f'<div class="summary-card"><p class="sc-val">{len(alerts_df)}</p><p class="sc-lbl">Alerts Generated</p></div>', unsafe_allow_html=True)
#     with sc3:
#         st.markdown(f'<div class="summary-card"><p class="sc-val">{excellent}</p><p class="sc-lbl">Excellent Schools</p></div>', unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)

#     if st.button("View Dashboard →", use_container_width=True, type="primary"):
#         st.switch_page("pages/4_dashboard.py")

"""
pages/3_processing.py — Processing Page
Animated step-by-step AI processing. Theme-safe.
"""
import streamlit as st, sys, time
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from src.data_processor import DataProcessor
from models.quality_rules import QualityAssessment
from src.auth import is_logged_in, get_current_user, logout
from src.styles import SHARED_CSS

if not is_logged_in(st.session_state):
    st.error("🔒 Please sign in first.")
    if st.button("Go to Login →", type="primary"):
        st.switch_page("pages/1_login.py")
    st.stop()

current_user = get_current_user(st.session_state)

st.set_page_config(page_title="Processing · School Meal Monitor", page_icon="⚙️", layout="wide")
st.markdown(SHARED_CSS, unsafe_allow_html=True)

# ── SIDEBAR ──
with st.sidebar:
    st.markdown(f'<div class="sb-user"><h4>👤 {current_user["full_name"]}</h4><p>{current_user["role"]}</p></div>', unsafe_allow_html=True)
    if st.button("🚪 Sign Out", use_container_width=True):
        logout(st.session_state)
        st.switch_page("pages/1_login.py")
    st.markdown("---")
    st.markdown("""
    <div class="steps">
      <div class="st-item"><div class="st-dot done">✓</div><span class="st-lbl done">Upload</span></div>
      <div class="st-line done"></div>
      <div class="st-item"><div class="st-dot active">2</div><span class="st-lbl active">Process</span></div>
      <div class="st-line"></div>
      <div class="st-item"><div class="st-dot">3</div><span class="st-lbl">Dashboard</span></div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")

# ── Guard: no data ──
if 'data_loaded' not in st.session_state or not st.session_state['data_loaded']:
    st.error("❌ No data found. Please upload data first.")
    if st.button("← Go to Upload", type="primary", use_container_width=True):
        st.switch_page("pages/2_upload_data.py")
    st.stop()

# ── HEADER ──
st.markdown("""
<div class="ph">
  <div class="ph-badge">Step 2 of 3</div>
  <h1>⚙️ Processing Data</h1>
  <p>Our AI engine is scoring meal quality across all five weighted dimensions</p>
</div>
""", unsafe_allow_html=True)

# ── PROCESSING ── (centered column)
_, center, _ = st.columns([1, 3, 1])

def step(state, icon, title, desc):
    return f'<div class="ps {state}"><div class="pi">{icon}</div><div><p class="pt">{title}</p><p class="pd">{desc}</p></div></div>'

with center:
    df = st.session_state['meal_data']

    s1 = st.empty(); s2 = st.empty(); s3 = st.empty(); s4 = st.empty()
    prog = st.progress(0)
    status = st.empty()

    # Render initial state
    s1.markdown(step("running","🔄","Loading Data","Reading records from uploaded file..."), unsafe_allow_html=True)
    s2.markdown(step("pending","⏳","Calculating Metrics","Waiting..."), unsafe_allow_html=True)
    s3.markdown(step("pending","⏳","AI Quality Assessment","Waiting..."), unsafe_allow_html=True)
    s4.markdown(step("pending","⏳","Generating Insights","Waiting..."), unsafe_allow_html=True)

    # Step 1
    status.caption(f"Loaded {len(df):,} records from {df['School_ID'].nunique()} schools")
    time.sleep(0.8)
    prog.progress(20)
    s1.markdown(step("done","✅","Data Loaded",f"{len(df):,} records · {df['School_ID'].nunique()} schools"), unsafe_allow_html=True)

    # Step 2
    s2.markdown(step("running","🔄","Calculating Metrics","Computing waste %, calorie compliance, protein compliance, hygiene score..."), unsafe_allow_html=True)
    status.caption("Computing derived metrics...")
    time.sleep(1.1)
    processor    = DataProcessor(df=df)
    df_processed = processor.calculate_metrics()
    prog.progress(50)
    s2.markdown(step("done","✅","Metrics Calculated","All performance indicators computed"), unsafe_allow_html=True)

    # Step 3
    s3.markdown(step("running","🔄","AI Quality Assessment","Scoring across Nutrition · Waste · Hygiene · Taste · Menu..."), unsafe_allow_html=True)
    status.caption("AI scoring all 5 quality dimensions...")
    time.sleep(1.3)
    checker    = QualityAssessment(df_processed)
    quality_df = checker.calculate_overall_quality()
    alerts_df  = checker.generate_alerts(quality_df)
    prog.progress(82)
    s3.markdown(step("done","✅","Quality Assessment Complete","Scores generated for all schools"), unsafe_allow_html=True)

    # Step 4
    s4.markdown(step("running","🔄","Generating Insights","Building alerts and recommendations..."), unsafe_allow_html=True)
    status.caption("Building alerts and recommendations...")
    time.sleep(0.8)
    stats = processor.get_summary_stats()
    prog.progress(100)
    s4.markdown(step("done","✅","Insights Ready","All alerts and recommendations prepared"), unsafe_allow_html=True)

    # Save to session
    st.session_state.update({
        'df_processed':        df_processed,
        'quality_df':          quality_df,
        'alerts_df':           alerts_df,
        'stats':               stats,
        'processing_complete': True,
    })
    status.empty()

    # ── SUCCESS ──
    excellent = len(quality_df[quality_df['Overall_Quality_Score'] >= 85])
    st.markdown(f"""
    <div class="suc-banner">
      <h2>🎉 Analysis Complete!</h2>
      <p>Your quality assessment is ready. Head to the dashboard to explore the results.</p>
    </div>
    """, unsafe_allow_html=True)

    # Summary
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="sc"><p class="sv">{stats["total_schools"]}</p><p class="sl">Schools Analysed</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="sc"><p class="sv">{len(alerts_df)}</p><p class="sl">Alerts Generated</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="sc"><p class="sv">{excellent}</p><p class="sl">Excellent Schools</p></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("View Full Dashboard →", use_container_width=True, type="primary"):
        st.switch_page("pages/4_dashboard.py")