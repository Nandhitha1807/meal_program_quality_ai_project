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