
"""pages/2_upload_data.py — Upload Page
CSV upload ONLY. No MySQL load option. Clean, aligned layout.
"""
import streamlit as st, pandas as pd, sys, time
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from src.auth import is_logged_in, get_current_user, logout
from src.styles import SHARED_CSS

if not is_logged_in(st.session_state):
    st.error("🔒 Please sign in first.")
    if st.button("Go to Login →", type="primary"):
        st.switch_page("pages/1_login.py")
    st.stop()

current_user = get_current_user(st.session_state)

st.set_page_config(page_title="Upload · School Meal Monitor", page_icon="📤", layout="wide")
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
      <div class="st-item"><div class="st-dot active">1</div><span class="st-lbl active">Upload</span></div>
      <div class="st-line"></div>
      <div class="st-item"><div class="st-dot">2</div><span class="st-lbl">Process</span></div>
      <div class="st-line"></div>
      <div class="st-item"><div class="st-dot">3</div><span class="st-lbl">Dashboard</span></div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")

# ── HEADER ──
st.markdown("""
<div class="ph">
  <div class="ph-badge">Step 1 of 3</div>
  <h1>📤 Upload Meal Data</h1>
  <p>Upload your CSV file to begin AI quality assessment</p>
</div>
""", unsafe_allow_html=True)

# ── MAIN LAYOUT: upload left, info right ──
left, right = st.columns([3, 2], gap="large")

REQUIRED_COLS = [
    'School_ID','Date','Students_Present','Meals_Served','Meals_Leftover',
    'Required_Calories','Actual_Calories','Required_Protein','Actual_Protein',
    'Meals_Taken','Avg_Taste_Rating','Kitchen_Cleaned','Clean_Water_Available','Menu_Followed'
]

with left:
    st.markdown("""
    <div class="up-card">
      <span class="uci">📁</span>
      <h3>Upload CSV File</h3>
      <p>Select your school meal data CSV file. All 14 required columns must be present.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    uploaded = st.file_uploader(
        "Choose your CSV file",
        type=["csv"],
        help="Must contain all 14 required columns"
    )

    if uploaded:
        try:
            df = pd.read_csv(uploaded)
            missing = [c for c in REQUIRED_COLS if c not in df.columns]

            if missing:
                st.error(f"❌ Missing {len(missing)} column(s): `{'`, `'.join(missing)}`")
                st.info("📥 Download the template below to see the correct format.")
            else:
                st.success(f"✅ Valid! Found **{len(df):,} records** from **{df['School_ID'].nunique()} schools**")

                with st.expander("Preview — first 8 rows"):
                    st.dataframe(df.head(8), use_container_width=True)

                st.session_state.update({
                    'data_source': 'csv',
                    'meal_data':   df,
                    'data_loaded': True
                })
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("Proceed to Analysis →", type="primary", use_container_width=True):
                    st.switch_page("pages/3_processing.py")

        except Exception as e:
            st.error(f"❌ Could not read file: {e}")

with right:
    # What we check
    st.markdown("""
    <div style="background:var(--surf);border:1px solid var(--bdr);border-radius:var(--r2);padding:1.6rem 1.8rem;margin-bottom:1.2rem;">
      <p style="font-size:.7rem;font-weight:800;letter-spacing:.09em;text-transform:uppercase;opacity:.45;margin:0 0 1rem;">What We Analyse</p>
    """, unsafe_allow_html=True)

    checks = [
        ("📊","Nutrition","Calorie & protein compliance against targets"),
        ("🗑️","Waste","Meal leftover percentage per serving"),
        ("🧼","Hygiene","Kitchen cleanliness & clean water checks"),
        ("⭐","Taste","Average student rating across meals"),
        ("📋","Menu","Whether approved menu was followed"),
    ]
    for icon, label, desc in checks:
        st.markdown(f"""
        <div style="display:flex;align-items:flex-start;gap:.8rem;margin-bottom:.9rem;">
          <span style="font-size:1.1rem;margin-top:.05rem;">{icon}</span>
          <div>
            <p style="font-size:.85rem;font-weight:700;margin:0 0 .1rem;">{label}</p>
            <p style="font-size:.78rem;opacity:.52;margin:0;">{desc}</p>
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Weights reference
    st.markdown("""
    <div style="background:var(--b-bg);border:1px solid var(--b-bd);border-radius:var(--r2);padding:1.2rem 1.5rem;">
      <p style="font-size:.7rem;font-weight:800;letter-spacing:.09em;text-transform:uppercase;color:var(--b);margin:0 0 .8rem;">Score Weights</p>
      <div style="display:flex;flex-direction:column;gap:.4rem;">
        <div style="display:flex;justify-content:space-between;font-size:.82rem;"><span>🥗 Nutrition</span><strong>30%</strong></div>
        <div style="display:flex;justify-content:space-between;font-size:.82rem;"><span>🗑️ Waste</span><strong>25%</strong></div>
        <div style="display:flex;justify-content:space-between;font-size:.82rem;"><span>🧼 Hygiene</span><strong>25%</strong></div>
        <div style="display:flex;justify-content:space-between;font-size:.82rem;"><span>⭐ Taste</span><strong>15%</strong></div>
        <div style="display:flex;justify-content:space-between;font-size:.82rem;"><span>📋 Menu</span><strong>5%</strong></div>
      </div>
    </div>
    """, unsafe_allow_html=True)


st.markdown('<div class="sec-div"><div class="dl"></div><span>CSV Template</span><div class="dl"></div></div>', unsafe_allow_html=True)

tl, tr = st.columns([3, 1], gap="large")

TEMPLATE_DF = pd.DataFrame({
    'School_ID':['SCH001','SCH002'],'Date':['2024-01-01','2024-01-02'],
    'Students_Present':[100,150],'Meals_Served':[100,150],'Meals_Leftover':[10,20],
    'Required_Calories':[2000,2000],'Actual_Calories':[1950,2100],
    'Required_Protein':[50,50],'Actual_Protein':[48,52],
    'Meals_Taken':[90,130],'Avg_Taste_Rating':[4.2,3.8],
    'Kitchen_Cleaned':[True,True],'Clean_Water_Available':[True,False],'Menu_Followed':[True,True]
})

with tl:
    st.markdown("**Download the template** to ensure your data is formatted correctly before uploading.")
    with st.expander("View all 14 column descriptions"):
        col_desc = {
            "School_ID":               "Unique school identifier e.g. SCH001",
            "Date":                    "Date of meal service — YYYY-MM-DD format",
            "Students_Present":        "Number of students present that day",
            "Meals_Served":            "Total number of meals prepared",
            "Meals_Leftover":          "Number of leftover / wasted meals",
            "Required_Calories":       "Target calories per meal",
            "Actual_Calories":         "Calories actually provided in the meal",
            "Required_Protein":        "Target protein per meal in grams",
            "Actual_Protein":          "Actual protein provided in grams",
            "Meals_Taken":             "Number of meals consumed by students",
            "Avg_Taste_Rating":        "Average student taste rating (1–5 scale)",
            "Kitchen_Cleaned":         "Was the kitchen cleaned? True / False",
            "Clean_Water_Available":   "Was clean water available? True / False",
            "Menu_Followed":           "Was the approved menu followed? True / False",
        }
        for col, desc in col_desc.items():
            st.markdown(f"**`{col}`** — {desc}")

with tr:
    st.markdown("<br>", unsafe_allow_html=True)
    st.download_button(
        "📄 Download Template",
        data=TEMPLATE_DF.to_csv(index=False).encode(),
        file_name="school_meal_template.csv",
        mime="text/csv",
        use_container_width=True,
    )
    st.caption("2-row example with all 14 columns")