# # """
# # pages/3_processing.py — Processing Page
# # Animated step-by-step AI processing. Theme-safe.
# # """
# # import streamlit as st, sys, time
# # from pathlib import Path

# # sys.path.append(str(Path(__file__).parent.parent))
# # from src.data_processor import DataProcessor
# # from models.quality_rules import QualityAssessment
# # from src.auth import is_logged_in, get_current_user, logout
# # from src.styles import SHARED_CSS

# # if not is_logged_in(st.session_state):
# #     st.error("🔒 Please sign in first.")
# #     if st.button("Go to Login →", type="primary"):
# #         st.switch_page("pages/1_login.py")
# #     st.stop()

# # current_user = get_current_user(st.session_state)

# # st.set_page_config(page_title="Processing · School Meal Monitor", page_icon="⚙️", layout="wide")
# # st.markdown(SHARED_CSS, unsafe_allow_html=True)

# # # ── SIDEBAR ──
# # with st.sidebar:
# #     st.markdown(f'<div class="sb-user"><h4>👤 {current_user["full_name"]}</h4><p>{current_user["role"]}</p></div>', unsafe_allow_html=True)
# #     if st.button("🚪 Sign Out", use_container_width=True):
# #         logout(st.session_state)
# #         st.switch_page("pages/1_login.py")
# #     st.markdown("---")
# #     st.markdown("""
# #     <div class="steps">
# #       <div class="st-item"><div class="st-dot done">✓</div><span class="st-lbl done">Upload</span></div>
# #       <div class="st-line done"></div>
# #       <div class="st-item"><div class="st-dot active">2</div><span class="st-lbl active">Process</span></div>
# #       <div class="st-line"></div>
# #       <div class="st-item"><div class="st-dot">3</div><span class="st-lbl">Dashboard</span></div>
# #     </div>
# #     """, unsafe_allow_html=True)
# #     st.markdown("---")
# #     if st.button("🏠 Home", use_container_width=True):
# #         st.switch_page("app.py")

# # # ── Guard: no data ──
# # if 'data_loaded' not in st.session_state or not st.session_state['data_loaded']:
# #     st.error("❌ No data found. Please upload data first.")
# #     if st.button("← Go to Upload", type="primary", use_container_width=True):
# #         st.switch_page("pages/2_upload_data.py")
# #     st.stop()

# # # ── HEADER ──
# # st.markdown("""
# # <div class="ph">
# #   <div class="ph-badge">Step 2 of 3</div>
# #   <h1>⚙️ Processing Data</h1>
# #   <p>Our AI engine is scoring meal quality across all five weighted dimensions</p>
# # </div>
# # """, unsafe_allow_html=True)

# # # ── PROCESSING ── (centered column)
# # _, center, _ = st.columns([1, 3, 1])

# # def step(state, icon, title, desc):
# #     return f'<div class="ps {state}"><div class="pi">{icon}</div><div><p class="pt">{title}</p><p class="pd">{desc}</p></div></div>'

# # with center:
# #     df = st.session_state['meal_data']

# #     s1 = st.empty(); s2 = st.empty(); s3 = st.empty(); s4 = st.empty()
# #     prog = st.progress(0)
# #     status = st.empty()

# #     # Render initial state
# #     s1.markdown(step("running","🔄","Loading Data","Reading records from uploaded file..."), unsafe_allow_html=True)
# #     s2.markdown(step("pending","⏳","Calculating Metrics","Waiting..."), unsafe_allow_html=True)
# #     s3.markdown(step("pending","⏳","AI Quality Assessment","Waiting..."), unsafe_allow_html=True)
# #     s4.markdown(step("pending","⏳","Generating Insights","Waiting..."), unsafe_allow_html=True)

# #     # Step 1
# #     status.caption(f"Loaded {len(df):,} records from {df['School_ID'].nunique()} schools")
# #     time.sleep(0.8)
# #     prog.progress(20)
# #     s1.markdown(step("done","✅","Data Loaded",f"{len(df):,} records · {df['School_ID'].nunique()} schools"), unsafe_allow_html=True)

# #     # Step 2
# #     s2.markdown(step("running","🔄","Calculating Metrics","Computing waste %, calorie compliance, protein compliance, hygiene score..."), unsafe_allow_html=True)
# #     status.caption("Computing derived metrics...")
# #     time.sleep(1.1)
# #     processor    = DataProcessor(df=df)
# #     df_processed = processor.calculate_metrics()
# #     prog.progress(50)
# #     s2.markdown(step("done","✅","Metrics Calculated","All performance indicators computed"), unsafe_allow_html=True)

# #     # Step 3
# #     s3.markdown(step("running","🔄","AI Quality Assessment","Scoring across Nutrition · Waste · Hygiene · Taste · Menu..."), unsafe_allow_html=True)
# #     status.caption("AI scoring all 5 quality dimensions...")
# #     time.sleep(1.3)
# #     checker    = QualityAssessment(df_processed)
# #     quality_df = checker.calculate_overall_quality()
# #     alerts_df  = checker.generate_alerts(quality_df)
# #     prog.progress(82)
# #     s3.markdown(step("done","✅","Quality Assessment Complete","Scores generated for all schools"), unsafe_allow_html=True)

# #     # Step 4
# #     s4.markdown(step("running","🔄","Generating Insights","Building alerts and recommendations..."), unsafe_allow_html=True)
# #     status.caption("Building alerts and recommendations...")
# #     time.sleep(0.8)
# #     stats = processor.get_summary_stats()
# #     prog.progress(100)
# #     s4.markdown(step("done","✅","Insights Ready","All alerts and recommendations prepared"), unsafe_allow_html=True)

# #     # Save to session
# #     st.session_state.update({
# #         'df_processed':        df_processed,
# #         'quality_df':          quality_df,
# #         'alerts_df':           alerts_df,
# #         'stats':               stats,
# #         'processing_complete': True,
# #     })
# #     status.empty()

# #     # ── SUCCESS ──
# #     excellent = len(quality_df[quality_df['Overall_Quality_Score'] >= 85])
# #     st.markdown(f"""
# #     <div class="suc-banner">
# #       <h2>🎉 Analysis Complete!</h2>
# #       <p>Your quality assessment is ready. Head to the dashboard to explore the results.</p>
# #     </div>
# #     """, unsafe_allow_html=True)

# #     # Summary
# #     c1, c2, c3 = st.columns(3)
# #     with c1:
# #         st.markdown(f'<div class="sc"><p class="sv">{stats["total_schools"]}</p><p class="sl">Schools Analysed</p></div>', unsafe_allow_html=True)
# #     with c2:
# #         st.markdown(f'<div class="sc"><p class="sv">{len(alerts_df)}</p><p class="sl">Alerts Generated</p></div>', unsafe_allow_html=True)
# #     with c3:
# #         st.markdown(f'<div class="sc"><p class="sv">{excellent}</p><p class="sl">Excellent Schools</p></div>', unsafe_allow_html=True)

# #     st.markdown("<br>", unsafe_allow_html=True)
# #     if st.button("View Full Dashboard →", use_container_width=True, type="primary"):
# #         st.switch_page("pages/4_dashboard.py")

# """
# pages/3_processing.py — Processing Page
# Animated step-by-step AI processing. Theme-safe.
# Now includes Step 5: Save results to MySQL database.
# """
# import streamlit as st, sys, time
# from pathlib import Path

# sys.path.append(str(Path(__file__).parent.parent))
# from src.data_processor import DataProcessor
# from models.quality_rules import QualityAssessment
# from src.auth import is_logged_in, get_current_user, logout
# from src.styles import SHARED_CSS
# from src.db_saver import save_all_results   # ← NEW IMPORT

# if not is_logged_in(st.session_state):
#     st.error("🔒 Please sign in first.")
#     if st.button("Go to Login →", type="primary"):
#         st.switch_page("pages/1_login.py")
#     st.stop()

# current_user = get_current_user(st.session_state)

# st.set_page_config(page_title="Processing · School Meal Monitor", page_icon="⚙️", layout="wide")
# st.markdown(SHARED_CSS, unsafe_allow_html=True)

# # ── SIDEBAR ──
# with st.sidebar:
#     st.markdown(f'<div class="sb-user"><h4>👤 {current_user["full_name"]}</h4><p>{current_user["role"]}</p></div>', unsafe_allow_html=True)
#     if st.button("🚪 Sign Out", use_container_width=True):
#         logout(st.session_state)
#         st.switch_page("pages/1_login.py")
#     st.markdown("---")
#     st.markdown("""
#     <div class="steps">
#       <div class="st-item"><div class="st-dot done">✓</div><span class="st-lbl done">Upload</span></div>
#       <div class="st-line done"></div>
#       <div class="st-item"><div class="st-dot active">2</div><span class="st-lbl active">Process</span></div>
#       <div class="st-line"></div>
#       <div class="st-item"><div class="st-dot">3</div><span class="st-lbl">Dashboard</span></div>
#     </div>
#     """, unsafe_allow_html=True)
#     st.markdown("---")
#     if st.button("🏠 Home", use_container_width=True):
#         st.switch_page("app.py")

# # ── Guard: no data ──
# if 'data_loaded' not in st.session_state or not st.session_state['data_loaded']:
#     st.error("❌ No data found. Please upload data first.")
#     if st.button("← Go to Upload", type="primary", use_container_width=True):
#         st.switch_page("pages/2_upload_data.py")
#     st.stop()

# # ── HEADER ──
# st.markdown("""
# <div class="ph">
#   <div class="ph-badge">Step 2 of 3</div>
#   <h1>⚙️ Processing Data</h1>
#   <p>Our AI engine is scoring meal quality across all five weighted dimensions</p>
# </div>
# """, unsafe_allow_html=True)

# # ── PROCESSING ── (centered column)
# _, center, _ = st.columns([1, 3, 1])

# def step(state, icon, title, desc):
#     return f'<div class="ps {state}"><div class="pi">{icon}</div><div><p class="pt">{title}</p><p class="pd">{desc}</p></div></div>'

# with center:
#     df = st.session_state['meal_data']
#     username = st.session_state.get('username', 'admin')

#     s1 = st.empty(); s2 = st.empty(); s3 = st.empty(); s4 = st.empty(); s5 = st.empty()
#     prog   = st.progress(0)
#     status = st.empty()

#     # ── Render initial states ──
#     s1.markdown(step("running", "🔄", "Loading Data",          "Reading records from uploaded file..."),        unsafe_allow_html=True)
#     s2.markdown(step("pending", "⏳", "Calculating Metrics",   "Waiting..."),                                   unsafe_allow_html=True)
#     s3.markdown(step("pending", "⏳", "AI Quality Assessment", "Waiting..."),                                   unsafe_allow_html=True)
#     s4.markdown(step("pending", "⏳", "Generating Insights",   "Waiting..."),                                   unsafe_allow_html=True)
#     s5.markdown(step("pending", "⏳", "Saving to Database",    "Waiting..."),                                   unsafe_allow_html=True)

#     # ── Step 1: Load ──
#     status.caption(f"Loaded {len(df):,} records from {df['School_ID'].nunique()} schools")
#     time.sleep(0.8)
#     prog.progress(15)
#     s1.markdown(step("done", "✅", "Data Loaded", f"{len(df):,} records · {df['School_ID'].nunique()} schools"), unsafe_allow_html=True)

#     # ── Step 2: Metrics ──
#     s2.markdown(step("running", "🔄", "Calculating Metrics", "Computing waste %, calorie compliance, protein compliance, hygiene score..."), unsafe_allow_html=True)
#     status.caption("Computing derived metrics...")
#     time.sleep(1.1)
#     processor    = DataProcessor(df=df)
#     df_processed = processor.calculate_metrics()
#     prog.progress(40)
#     s2.markdown(step("done", "✅", "Metrics Calculated", "All performance indicators computed"), unsafe_allow_html=True)

#     # ── Step 3: AI Scoring ──
#     s3.markdown(step("running", "🔄", "AI Quality Assessment", "Scoring across Nutrition · Waste · Hygiene · Taste · Menu..."), unsafe_allow_html=True)
#     status.caption("AI scoring all 5 quality dimensions...")
#     time.sleep(1.3)
#     checker    = QualityAssessment(df_processed)
#     quality_df = checker.calculate_overall_quality()
#     alerts_df  = checker.generate_alerts(quality_df)
#     prog.progress(65)
#     s3.markdown(step("done", "✅", "Quality Assessment Complete", "Scores generated for all schools"), unsafe_allow_html=True)

#     # ── Step 4: Insights ──
#     s4.markdown(step("running", "🔄", "Generating Insights", "Building alerts and recommendations..."), unsafe_allow_html=True)
#     status.caption("Building alerts and recommendations...")
#     time.sleep(0.8)
#     stats = processor.get_summary_stats()
#     prog.progress(82)
#     s4.markdown(step("done", "✅", "Insights Ready", "All alerts and recommendations prepared"), unsafe_allow_html=True)

#     # ── Step 5: Save to MySQL ──────────────────────────────────────
#     s5.markdown(step("running", "🔄", "Saving to Database", "Writing quality scores and alerts to MySQL..."), unsafe_allow_html=True)
#     status.caption("Saving results to MySQL database...")
#     time.sleep(0.9)

#     db_result = save_all_results(quality_df, alerts_df, uploaded_by=username)

#     prog.progress(100)

#     if db_result["success"]:
#         scores_msg = db_result["scores"]["message"]
#         alerts_msg = db_result["alerts"]["message"]
#         s5.markdown(
#             step("done", "✅", "Saved to Database",
#                  f"{scores_msg} · {alerts_msg}"),
#             unsafe_allow_html=True
#         )
#     else:
#         # DB save failed — app still works, just warn the user
#         fail_msg = db_result["scores"]["message"] or db_result["alerts"]["message"]
#         s5.markdown(
#             step("done", "⚠️", "Database Save Skipped",
#                  f"Results saved in session only — {fail_msg}"),
#             unsafe_allow_html=True
#         )
#     # ──────────────────────────────────────────────────────────────

#     # Save everything to session state
#     st.session_state.update({
#         'df_processed':        df_processed,
#         'quality_df':          quality_df,
#         'alerts_df':           alerts_df,
#         'stats':               stats,
#         'processing_complete': True,
#         'db_save_result':      db_result,      # ← store so dashboard can show DB status
#     })
#     status.empty()

#     # ── SUCCESS BANNER ──
#     excellent = len(quality_df[quality_df['Overall_Quality_Score'] >= 85])
#     st.markdown("""
#     <div class="suc-banner">
#       <h2>🎉 Analysis Complete!</h2>
#       <p>Your quality assessment is ready and saved to the database. Head to the dashboard to explore the results.</p>
#     </div>
#     """, unsafe_allow_html=True)

#     # Summary chips
#     c1, c2, c3, c4 = st.columns(4)
#     with c1:
#         st.markdown(f'<div class="sc"><p class="sv">{stats["total_schools"]}</p><p class="sl">Schools Analysed</p></div>', unsafe_allow_html=True)
#     with c2:
#         st.markdown(f'<div class="sc"><p class="sv">{len(alerts_df)}</p><p class="sl">Alerts Generated</p></div>', unsafe_allow_html=True)
#     with c3:
#         st.markdown(f'<div class="sc"><p class="sv">{excellent}</p><p class="sl">Excellent Schools</p></div>', unsafe_allow_html=True)
#     with c4:
#         db_icon = "✅" if db_result["success"] else "⚠️"
#         db_label = "Saved to DB" if db_result["success"] else "Session Only"
#         st.markdown(f'<div class="sc"><p class="sv">{db_icon}</p><p class="sl">{db_label}</p></div>', unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)
#     if st.button("View Full Dashboard →", use_container_width=True, type="primary"):
#         st.switch_page("pages/4_dashboard.py")
"""
pages/3_processing.py — Processing Page
Uses background threading so the AI pipeline runs without blocking
the Streamlit server. The UI polls progress and updates live.
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
# Runs the entire AI pipeline independently of the main thread.
# Writes results into the shared `progress` dict so the UI can
# poll and update without blocking the Streamlit server.
# ══════════════════════════════════════════════════════════════

def run_ai_pipeline(df, username: str, progress: dict):
    """
    Background thread target — executes all 5 pipeline steps.

    Threading pattern:
        Main thread  → renders UI, polls `progress` every 300ms
        This thread  → does all CPU/IO work, writes results to `progress`
        Both threads → share `progress` dict as a message bus

    Args:
        df       : raw meal DataFrame
        username : logged-in user (written to DB for audit trail)
        progress : shared dict; keys written:
                   step (int), status (str), finished (bool), error (str|None)
                   + result DataFrames on completion
    """
    try:
        # ── Step 1: Load ──────────────────────────────────────
        progress.update({"step": 1, "status": "running"})
        time.sleep(0.5)                         # simulate I/O read latency
        progress.update({
            "step": 1, "status": "done",
            "records": len(df),
            "schools": df['School_ID'].nunique()
        })

        # ── Step 2: Calculate Metrics ─────────────────────────
        progress.update({"step": 2, "status": "running"})
        processor    = DataProcessor(df=df)
        df_processed = processor.calculate_metrics()   # runs in background thread
        time.sleep(0.3)
        progress.update({"step": 2, "status": "done", "df_processed": df_processed})

        # ── Step 3: AI Quality Assessment ─────────────────────
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

        # ── Step 4: Summary Stats ─────────────────────────────
        progress.update({"step": 4, "status": "running"})
        stats = processor.get_summary_stats()
        time.sleep(0.3)
        progress.update({"step": 4, "status": "done", "stats": stats})

        # ── Step 5: Save to MySQL ─────────────────────────────
        progress.update({"step": 5, "status": "running"})
        db_result = save_all_results(quality_df, alerts_df, uploaded_by=username)
        time.sleep(0.3)
        progress.update({"step": 5, "status": "done", "db_result": db_result})

        # Signal main thread that work is done
        progress["finished"] = True

    except Exception as e:
        progress["error"]    = str(e)
        progress["finished"] = True


# ══════════════════════════════════════════════════════════════
# MAIN THREAD — renders UI and polls the background thread
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

    # ── Shared dict — message bus between main and background thread ──
    progress = {
        "step": 0, "status": "pending",
        "finished": False, "error": None
    }

    # ── Launch background thread ──────────────────────────────
    # After this line the main thread is FREE.
    # Streamlit can handle other users while AI runs in background.
    thread = threading.Thread(
        target=run_ai_pipeline,
        args=(df, username, progress),
        daemon=True     # killed automatically if app restarts
    )
    thread.start()

    # ── UI placeholders (updated by poll loop below) ──────────
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

    # Initial render
    s1.markdown(step_html("running", "🔄", *STEPS[1]), unsafe_allow_html=True)
    for i in range(1, 5):
        slots[i].markdown(step_html("pending", "⏳", *STEPS[i + 1]), unsafe_allow_html=True)

    # ── Poll loop ─────────────────────────────────────────────
    # Main thread checks progress dict every 300ms and redraws
    # only the steps that changed — lightweight and non-blocking.
    while not progress.get("finished"):

        current_step   = progress.get("step", 0)
        current_status = progress.get("status", "pending")

        for i in range(5):
            step_num = i + 1
            if completed[i]:
                continue

            if step_num < current_step or (step_num == current_step and current_status == "done"):
                label, _ = STEPS[step_num]

                # Build detail string per step
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

        time.sleep(0.3)     # poll every 300ms — main thread yields here

    # ── Thread is done — join cleanly ────────────────────────
    thread.join(timeout=5)

    # ── Handle error from background thread ──────────────────
    if progress.get("error"):
        st.error(f"❌ Processing failed in background thread: {progress['error']}")
        st.stop()

    # ── Final pass — mark any remaining steps as done ─────────
    for i in range(5):
        if not completed[i]:
            label, _ = STEPS[i + 1]
            slots[i].markdown(step_html("done", "✅", label, "Complete"), unsafe_allow_html=True)

    prog.progress(100)
    msg.empty()

    # ── Pull all results out of progress dict ─────────────────
    df_processed = progress["df_processed"]
    quality_df   = progress["quality_df"]
    alerts_df    = progress["alerts_df"]
    stats        = progress["stats"]
    db_result    = progress.get("db_result", {"success": False, "scores": {}, "alerts": {}})

    # ── Persist to session state ──────────────────────────────
    st.session_state.update({
        'df_processed':        df_processed,
        'quality_df':          quality_df,
        'alerts_df':           alerts_df,
        'stats':               stats,
        'processing_complete': True,
        'db_save_result':      db_result,
    })

    # ── SUCCESS BANNER ────────────────────────────────────────
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
    if st.button("View Full Dashboard →", use_container_width=True, type="primary"):
        st.switch_page("pages/4_dashboard.py")