"""
pages/3_processing.py — Processing Page
Uses background threading so the AI pipeline runs without blocking
the Streamlit server. The UI polls progress and updates live.
Skips processing if already done — shows results instantly.
"""
import streamlit as st, sys, time, threading
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from src.data_processor import DataProcessor
from models.quality_rules import QualityAssessment
from src.auth import is_logged_in, get_current_user, logout
from src.styles import SHARED_CSS
from src.db_saver import save_all_results

# ── AUTH ──
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

# ══════════════════════════════════════════════════════════════
# ── ALREADY PROCESSED CHECK ──
# If user comes back to this page after processing is done,
# skip the entire pipeline and show results instantly.
# ══════════════════════════════════════════════════════════════
if st.session_state.get('processing_complete'):

    quality_df = st.session_state['quality_df']
    alerts_df  = st.session_state['alerts_df']
    stats      = st.session_state['stats']
    db_result  = st.session_state.get('db_save_result', {})
    excellent  = len(quality_df[quality_df['Overall_Quality_Score'] >= 85])
    db_icon    = "✅" if db_result.get("success") else "⚠️"
    db_msg     = db_result.get("scores", {}).get("message", "Saved") if db_result.get("success") else "Session only"

    # ── HEADER ──
    st.markdown("""
    <div class="ph">
      <div class="ph-badge">Step 2 of 3</div>
      <h1>⚙️ Processing Data</h1>
      <p>AI pipeline runs in a background thread — server stays responsive during processing</p>
    </div>
    """, unsafe_allow_html=True)

    _, center, _ = st.columns([1, 3, 1])
    with center:

        def step_done(icon, title, desc):
            return (f'<div class="ps done">'
                    f'<div class="pi">{icon}</div>'
                    f'<div><p class="pt">{title}</p><p class="pd">{desc}</p></div>'
                    f'</div>')

        # Show all 5 steps as already done — instant, no loading
        st.markdown(step_done("✅", "Data Loaded",
            f"{len(st.session_state['meal_data']):,} records · "
            f"{st.session_state['meal_data']['School_ID'].nunique()} schools"),
            unsafe_allow_html=True)
        st.markdown(step_done("✅", "Metrics Calculated",  "All performance indicators computed"),     unsafe_allow_html=True)
        st.markdown(step_done("✅", "Quality Assessment",  "Scores generated for all schools"),        unsafe_allow_html=True)
        st.markdown(step_done("✅", "Insights Ready",      "All alerts and recommendations prepared"), unsafe_allow_html=True)
        st.markdown(step_done(db_icon, "Saved to Database", db_msg),                                   unsafe_allow_html=True)

        st.progress(100)

        # Success banner
        st.markdown("""
        <div class="suc-banner">
          <h2>✅ Already Processed!</h2>
          <p>Your data was already analysed. View the dashboard or re-process with new data.</p>
        </div>
        """, unsafe_allow_html=True)

        # Summary chips
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f'<div class="sc"><p class="sv">{stats["total_schools"]}</p><p class="sl">Schools Analysed</p></div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="sc"><p class="sv">{len(alerts_df)}</p><p class="sl">Alerts Generated</p></div>', unsafe_allow_html=True)
        with c3:
            st.markdown(f'<div class="sc"><p class="sv">{excellent}</p><p class="sl">Excellent Schools</p></div>', unsafe_allow_html=True)
        with c4:
            db_label = "Saved to DB" if db_result.get("success") else "Session Only"
            st.markdown(f'<div class="sc"><p class="sv">{db_icon}</p><p class="sl">{db_label}</p></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("View Full Dashboard →", use_container_width=True, type="primary"):
                st.switch_page("pages/4_dashboard.py")
        with col2:
            if st.button("🔄 Re-Process Data", use_container_width=True):
                for key in ['processing_complete', 'quality_df', 'alerts_df',
                            'stats', 'df_processed', 'db_save_result']:
                    st.session_state.pop(key, None)
                st.rerun()

    st.stop()   # ← pipeline code below never runs again
# ══════════════════════════════════════════════════════════════


# ── HEADER ──
st.markdown("""
<div class="ph">
  <div class="ph-badge">Step 2 of 3</div>
  <h1>⚙️ Processing Data</h1>
  <p>AI pipeline runs in a background thread — server stays responsive during processing</p>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# BACKGROUND THREAD FUNCTION
# ══════════════════════════════════════════════════════════════

def run_ai_pipeline(df, username: str, progress: dict):
    try:
        # ── Step 1: Load ──
        progress.update({"step": 1, "status": "running"})
        time.sleep(0.5)
        progress.update({
            "step": 1, "status": "done",
            "records": len(df),
            "schools": df['School_ID'].nunique()
        })

        # ── Step 2: Calculate Metrics ──
        progress.update({"step": 2, "status": "running"})
        processor    = DataProcessor(df=df)
        df_processed = processor.calculate_metrics()
        time.sleep(0.3)
        progress.update({"step": 2, "status": "done", "df_processed": df_processed})

        # ── Step 3: AI Quality Assessment ──
        progress.update({"step": 3, "status": "running"})
        checker    = QualityAssessment(df_processed)
        quality_df = checker.calculate_overall_quality()
        alerts_df  = checker.generate_alerts(quality_df)
        time.sleep(0.3)
        progress.update({
            "step": 3, "status": "done",
            "quality_df": quality_df,
            "alerts_df":  alerts_df
        })

        # ── Step 4: Summary Stats ──
        progress.update({"step": 4, "status": "running"})
        stats = processor.get_summary_stats()
        time.sleep(0.3)
        progress.update({"step": 4, "status": "done", "stats": stats})

        # ── Step 5: Save to MySQL ──
        progress.update({"step": 5, "status": "running"})
        db_result = save_all_results(quality_df, alerts_df, uploaded_by=username)
        time.sleep(0.3)
        progress.update({"step": 5, "status": "done", "db_result": db_result})

        progress["finished"] = True

    except Exception as e:
        progress["error"]    = str(e)
        progress["finished"] = True


# ══════════════════════════════════════════════════════════════
# MAIN THREAD — renders UI and polls background thread
# ══════════════════════════════════════════════════════════════

def step_html(state, icon, title, desc):
    return (
        f'<div class="ps {state}">'
        f'<div class="pi">{icon}</div>'
        f'<div><p class="pt">{title}</p><p class="pd">{desc}</p></div>'
        f'</div>'
    )

_, center, _ = st.columns([1, 3, 1])

with center:

    df       = st.session_state['meal_data']
    username = st.session_state.get('username', 'admin')

    progress = {
        "step": 0, "status": "pending",
        "finished": False, "error": None
    }

    thread = threading.Thread(
        target=run_ai_pipeline,
        args=(df, username, progress),
        daemon=True
    )
    thread.start()

    s1   = st.empty()
    s2   = st.empty()
    s3   = st.empty()
    s4   = st.empty()
    s5   = st.empty()
    prog = st.progress(0)
    msg  = st.empty()

    STEPS = {
        1: ("Loading Data",          "Reading records from uploaded file..."),
        2: ("Calculating Metrics",   "Computing waste %, calorie & protein compliance, hygiene score..."),
        3: ("AI Quality Assessment", "Scoring across Nutrition · Waste · Hygiene · Taste · Menu..."),
        4: ("Generating Insights",   "Building summary statistics and recommendations..."),
        5: ("Saving to Database",    "Writing quality scores and alerts to MySQL..."),
    }

    PROGRESS_PCT = [15, 35, 60, 80, 100]
    slots        = [s1, s2, s3, s4, s5]
    completed    = [False] * 5

    s1.markdown(step_html("running", "🔄", *STEPS[1]), unsafe_allow_html=True)
    for i in range(1, 5):
        slots[i].markdown(step_html("pending", "⏳", *STEPS[i + 1]), unsafe_allow_html=True)

    while not progress.get("finished"):

        current_step   = progress.get("step", 0)
        current_status = progress.get("status", "pending")

        for i in range(5):
            step_num = i + 1
            if completed[i]:
                continue

            if step_num < current_step or (step_num == current_step and current_status == "done"):
                label, _ = STEPS[step_num]
                if step_num == 1:
                    detail = f"{progress.get('records', 0):,} records · {progress.get('schools', 0)} schools"
                elif step_num == 5:
                    dr = progress.get("db_result", {})
                    detail = (dr.get("scores", {}).get("message", "Saved")
                              if dr.get("success")
                              else "Session only — DB unavailable")
                else:
                    detail = "Complete"

                slots[i].markdown(step_html("done", "✅", label, detail), unsafe_allow_html=True)
                prog.progress(PROGRESS_PCT[i])
                completed[i] = True

            elif step_num == current_step and current_status == "running":
                label, desc = STEPS[step_num]
                slots[i].markdown(step_html("running", "🔄", label, desc), unsafe_allow_html=True)
                msg.caption(f"⏳ Background thread — Step {step_num}: {label}")
                if i + 1 < 5:
                    next_label, next_desc = STEPS[step_num + 1]
                    slots[i + 1].markdown(
                        step_html("pending", "⏳", next_label, next_desc),
                        unsafe_allow_html=True
                    )

        time.sleep(0.3)

    thread.join(timeout=5)

    if progress.get("error"):
        st.error(f"❌ Processing failed in background thread: {progress['error']}")
        st.stop()

    for i in range(5):
        if not completed[i]:
            label, _ = STEPS[i + 1]
            slots[i].markdown(step_html("done", "✅", label, "Complete"), unsafe_allow_html=True)

    prog.progress(100)
    msg.empty()

    df_processed = progress["df_processed"]
    quality_df   = progress["quality_df"]
    alerts_df    = progress["alerts_df"]
    stats        = progress["stats"]
    db_result    = progress.get("db_result", {"success": False, "scores": {}, "alerts": {}})

    st.session_state.update({
        'df_processed':        df_processed,
        'quality_df':          quality_df,
        'alerts_df':           alerts_df,
        'stats':               stats,
        'processing_complete': True,
        'db_save_result':      db_result,
    })

    excellent = len(quality_df[quality_df['Overall_Quality_Score'] >= 85])
    st.markdown("""
    <div class="suc-banner">
      <h2>🎉 Analysis Complete!</h2>
      <p>Pipeline finished in background thread — server stayed responsive throughout.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f'<div class="sc"><p class="sv">{stats["total_schools"]}</p><p class="sl">Schools Analysed</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="sc"><p class="sv">{len(alerts_df)}</p><p class="sl">Alerts Generated</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="sc"><p class="sv">{excellent}</p><p class="sl">Excellent Schools</p></div>', unsafe_allow_html=True)
    with c4:
        db_icon  = "✅" if db_result.get("success") else "⚠️"
        db_label = "Saved to DB" if db_result.get("success") else "Session Only"
        st.markdown(f'<div class="sc"><p class="sv">{db_icon}</p><p class="sl">{db_label}</p></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("View Full Dashboard →", use_container_width=True, type="primary"):
            st.switch_page("pages/4_dashboard.py")
    with col2:
        if st.button("🔄 Re-Process Data", use_container_width=True):
            for key in ['processing_complete', 'quality_df', 'alerts_df',
                        'stats', 'df_processed', 'db_save_result']:
                st.session_state.pop(key, None)
            st.rerun()