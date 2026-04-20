# """
# pages/2_upload_data.py — Upload Page
# CSV upload ONLY. No MySQL load option. Clean, aligned layout.
# """
# import streamlit as st, pandas as pd, sys, time
# from pathlib import Path

# sys.path.append(str(Path(__file__).parent.parent))
# from src.auth import is_logged_in, get_current_user, logout
# from src.styles import SHARED_CSS

# if not is_logged_in(st.session_state):
#     st.error("🔒 Please sign in first.")
#     if st.button("Go to Login →", type="primary"):
#         st.switch_page("pages/1_login.py")
#     st.stop()

# current_user = get_current_user(st.session_state)

# st.set_page_config(page_title="Upload · School Meal Monitor", page_icon="📤", layout="wide")
# st.markdown(SHARED_CSS, unsafe_allow_html=True)

# # ── Page-specific CSS for upload ──
# st.markdown("""
# <style>
# /* Fix file uploader spacing to prevent tooltip overlap */
# [data-testid="stFileUploader"] {
#     margin-bottom: 2rem !important;
# }

# /* Ensure file uploader section has enough bottom padding */
# [data-testid="stFileUploader"] > div {
#     padding-bottom: 1rem !important;
# }

# /* Upload card hover state should not overlap */
# .up-card {
#     z-index: 1;
#     position: relative;
# }
# </style>
# """, unsafe_allow_html=True)

# # ── SIDEBAR ──
# with st.sidebar:
#     st.markdown(f'<div class="sb-user"><h4>👤 {current_user["full_name"]}</h4><p>{current_user["role"]}</p></div>', unsafe_allow_html=True)
#     if st.button("🚪 Sign Out", use_container_width=True):
#         logout(st.session_state)
#         st.switch_page("pages/1_login.py")
#     st.markdown("---")
#     st.markdown("""
#     <div class="steps">
#       <div class="st-item"><div class="st-dot active">1</div><span class="st-lbl active">Upload</span></div>
#       <div class="st-line"></div>
#       <div class="st-item"><div class="st-dot">2</div><span class="st-lbl">Process</span></div>
#       <div class="st-line"></div>
#       <div class="st-item"><div class="st-dot">3</div><span class="st-lbl">Dashboard</span></div>
#     </div>
#     """, unsafe_allow_html=True)
#     st.markdown("---")
#     if st.button("🏠 Home", use_container_width=True):
#         st.switch_page("app.py")

# # ── HEADER ──
# st.markdown("""
# <div class="ph">
#   <div class="ph-badge">Step 1 of 3</div>
#   <h1>📤 Upload Meal Data</h1>
#   <p>Upload your CSV file to begin AI quality assessment</p>
# </div>
# """, unsafe_allow_html=True)

# # ── SHOW INFO FOR SCHOOL USERS ──
# if current_user.get('role') == 'school':
#     school_id = current_user.get('school_id')
#     st.info(f"""
# 📍 **You are logged in as: {current_user['full_name']}**

# You can upload a CSV file with data from your school, the dashboard will show data for **{school_id}**.

# """)
#     st.markdown("<br>", unsafe_allow_html=True)

# # ── MAIN LAYOUT: upload left, info right ──
# left, right = st.columns([3, 2], gap="large")

# REQUIRED_COLS = [
#     'School_ID','Date','Students_Present','Meals_Served','Meals_Leftover',
#     'Required_Calories','Actual_Calories','Required_Protein','Actual_Protein',
#     'Meals_Taken','Avg_Taste_Rating','Kitchen_Cleaned','Clean_Water_Available','Menu_Followed'
# ]

# with left:
#     st.markdown("""
#     <div class="up-card">
#       <span class="uci">📁</span>
#       <h3>Upload CSV File</h3>
#       <p>Select your school meal data CSV file. All 14 required columns must be present.</p>
#     </div>
#     """, unsafe_allow_html=True)
#     st.markdown("<br>", unsafe_allow_html=True)

#     uploaded = st.file_uploader(
#         "Choose your CSV file",
#         type=["csv"],
#         help="Must contain all 14 required columns"
#     )
    
#     # Add spacing to prevent tooltip overlap
#     st.markdown("<div style='margin-bottom:1.5rem;'></div>", unsafe_allow_html=True)

#     if uploaded:
#         try:
#             df = pd.read_csv(uploaded)
#             missing = [c for c in REQUIRED_COLS if c not in df.columns]

#             if missing:
#                 st.error(f"❌ Missing {len(missing)} column(s): `{'`, `'.join(missing)}`")
#                 st.info("📥 Download the template below to see the correct format.")
#             else:
#                 # School user validation and filtering
#                 if current_user.get('role') == 'school':
#                     user_school_id = current_user.get('school_id')
#                     schools_in_csv = df['School_ID'].unique().tolist()
                    
#                     # Check if user's school is in the CSV
#                     if user_school_id not in schools_in_csv:
#                         st.error(f"""
# ❌ **Invalid CSV for your account**

# This CSV does not contain any data for **{user_school_id}**.

# **Schools found in CSV:** {', '.join(schools_in_csv)}

# **Your school:** {user_school_id}

# Please upload a CSV file that contains data for **{user_school_id}**.
# """)
#                         st.stop()  # Stop processing
                    
#                     # Warn if CSV has OTHER schools too
#                     other_schools = [s for s in schools_in_csv if s != user_school_id]
#                     if other_schools:
#                         st.warning(f"""
# ⚠️ **Multiple schools detected in CSV**

# This CSV contains data for multiple schools:
# - **Your school:** {user_school_id} ✅
# - **Other schools:** {', '.join(other_schools)} 

# Only **{user_school_id}** data will be processed and visible.
# Other schools' data will be filtered out automatically.
# """)
                    
#                     # Filter to only user's school IMMEDIATELY
#                     df = df[df['School_ID'] == user_school_id].copy()
#                     st.success(f"✅ Found **{len(df):,} records** for **{user_school_id}**")
#                 else:
#                     # Admin sees all schools
#                     st.success(f"✅ Valid! Found **{len(df):,} records** from **{df['School_ID'].nunique()} schools**")

#                 with st.expander("Preview — first 8 rows"):
#                     st.dataframe(df.head(8), use_container_width=True)

#                 st.session_state.update({
#                     'data_source': 'csv',
#                     'meal_data':   df,
#                     'data_loaded': True
#                 })
#                 st.markdown("<br>", unsafe_allow_html=True)
#                 if st.button("Proceed to Analysis →", type="primary", use_container_width=True):
#                     st.switch_page("pages/3_processing.py")

#         except Exception as e:
#             st.error(f"❌ Could not read file: {e}")

# with right:
#     # What we check
#     st.markdown("""
#     <div style="background:var(--surf);border:1px solid var(--bdr);border-radius:var(--r2);padding:1.6rem 1.8rem;margin-bottom:1.2rem;">
#       <p style="font-size:.7rem;font-weight:800;letter-spacing:.09em;text-transform:uppercase;opacity:.45;margin:0 0 1rem;">What We Analyse</p>
#     """, unsafe_allow_html=True)

#     checks = [
#         ("📊","Nutrition","Calorie & protein compliance against targets"),
#         ("🗑️","Waste","Meal leftover percentage per serving"),
#         ("🧼","Hygiene","Kitchen cleanliness & clean water checks"),
#         ("⭐","Taste","Average student rating across meals"),
#         ("📋","Menu","Whether approved menu was followed"),
#     ]
#     for icon, label, desc in checks:
#         st.markdown(f"""
#         <div style="display:flex;align-items:flex-start;gap:.8rem;margin-bottom:.9rem;">
#           <span style="font-size:1.1rem;margin-top:.05rem;">{icon}</span>
#           <div>
#             <p style="font-size:.85rem;font-weight:700;margin:0 0 .1rem;">{label}</p>
#             <p style="font-size:.78rem;opacity:.52;margin:0;">{desc}</p>
#           </div>
#         </div>
#         """, unsafe_allow_html=True)

#     st.markdown("</div>", unsafe_allow_html=True)

#     # Weights reference
#     st.markdown("""
#     <div style="background:var(--b-bg);border:1px solid var(--b-bd);border-radius:var(--r2);padding:1.2rem 1.5rem;">
#       <p style="font-size:.7rem;font-weight:800;letter-spacing:.09em;text-transform:uppercase;color:var(--b);margin:0 0 .8rem;">Score Weights</p>
#       <div style="display:flex;flex-direction:column;gap:.4rem;">
#         <div style="display:flex;justify-content:space-between;font-size:.82rem;"><span>🥗 Nutrition</span><strong>30%</strong></div>
#         <div style="display:flex;justify-content:space-between;font-size:.82rem;"><span>🗑️ Waste</span><strong>25%</strong></div>
#         <div style="display:flex;justify-content:space-between;font-size:.82rem;"><span>🧼 Hygiene</span><strong>25%</strong></div>
#         <div style="display:flex;justify-content:space-between;font-size:.82rem;"><span>⭐ Taste</span><strong>15%</strong></div>
#         <div style="display:flex;justify-content:space-between;font-size:.82rem;"><span>📋 Menu</span><strong>5%</strong></div>
#       </div>
#     </div>
#     """, unsafe_allow_html=True)

# # ── TEMPLATE SECTION ──
# st.markdown('<div class="sec-div"><div class="dl"></div><span>CSV Template</span><div class="dl"></div></div>', unsafe_allow_html=True)

# tl, tr = st.columns([3, 1], gap="large")

# TEMPLATE_DF = pd.DataFrame({
#     'School_ID':['SCH001','SCH002'],'Date':['2024-01-01','2024-01-02'],
#     'Students_Present':[100,150],'Meals_Served':[100,150],'Meals_Leftover':[10,20],
#     'Required_Calories':[2000,2000],'Actual_Calories':[1950,2100],
#     'Required_Protein':[50,50],'Actual_Protein':[48,52],
#     'Meals_Taken':[90,130],'Avg_Taste_Rating':[4.2,3.8],
#     'Kitchen_Cleaned':[True,True],'Clean_Water_Available':[True,False],'Menu_Followed':[True,True]
# })

# with tl:
#     st.markdown("**Download the template** to ensure your data is formatted correctly before uploading.")
#     with st.expander("View all 14 column descriptions"):
#         col_desc = {
#             "School_ID":               "Unique school identifier e.g. SCH001",
#             "Date":                    "Date of meal service — YYYY-MM-DD format",
#             "Students_Present":        "Number of students present that day",
#             "Meals_Served":            "Total number of meals prepared",
#             "Meals_Leftover":          "Number of leftover / wasted meals",
#             "Required_Calories":       "Target calories per meal",
#             "Actual_Calories":         "Calories actually provided in the meal",
#             "Required_Protein":        "Target protein per meal in grams",
#             "Actual_Protein":          "Actual protein provided in grams",
#             "Meals_Taken":             "Number of meals consumed by students",
#             "Avg_Taste_Rating":        "Average student taste rating (1–5 scale)",
#             "Kitchen_Cleaned":         "Was the kitchen cleaned? True / False",
#             "Clean_Water_Available":   "Was clean water available? True / False",
#             "Menu_Followed":           "Was the approved menu followed? True / False",
#         }
#         for col, desc in col_desc.items():
#             st.markdown(f"**`{col}`** — {desc}")

# with tr:
#     st.markdown("<br>", unsafe_allow_html=True)
#     st.download_button(
#         "📄 Download Template",
#         data=TEMPLATE_DF.to_csv(index=False).encode(),
#         file_name="school_meal_template.csv",
#         mime="text/csv",
#         use_container_width=True,
#     )
#     st.caption("2-row example with all 14 columns")

"""
pages/2_upload_data.py — Upload Page
Two input methods:
  Tab 1 — Manual Form  : single day entry via web form
  Tab 2 — CSV Upload   : bulk upload via CSV file
Both methods feed into the same AI processing pipeline.
"""
import streamlit as st, pandas as pd, sys
from pathlib import Path
from datetime import date

sys.path.append(str(Path(__file__).parent.parent))
from src.auth import is_logged_in, get_current_user, logout
from src.styles import SHARED_CSS

# ── AUTH ──
if not is_logged_in(st.session_state):
    st.error("🔒 Please sign in first.")
    if st.button("Go to Login →", type="primary"):
        st.switch_page("pages/1_login.py")
    st.stop()

current_user = get_current_user(st.session_state)

st.set_page_config(
    page_title="Upload · School Meal Monitor",
    page_icon="📤",
    layout="wide"
)
st.markdown(SHARED_CSS, unsafe_allow_html=True)

# ── Page CSS ──
st.markdown("""
<style>
[data-testid="stFileUploader"] { margin-bottom: 2rem !important; }
[data-testid="stFileUploader"] > div { padding-bottom: 1rem !important; }
.up-card { z-index: 1; position: relative; }

/* Tab styling */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    border-bottom: 2px solid var(--bdr);
    margin-bottom: 1.5rem;
}
.stTabs [data-baseweb="tab"] {
    font-size: .88rem !important;
    font-weight: 700 !important;
    padding: .6rem 1.4rem !important;
    border-radius: 8px 8px 0 0 !important;
}

/* Form field labels */
.stNumberInput label, .stSelectbox label,
.stSlider label, .stDateInput label {
    font-size: .78rem !important;
    font-weight: 700 !important;
    letter-spacing: .05em !important;
    text-transform: uppercase !important;
    opacity: .55 !important;
}

/* Form section divider */
.form-section {
    background: var(--surf);
    border: 1px solid var(--bdr);
    border-radius: var(--r2);
    padding: 1.2rem 1.4rem;
    margin-bottom: 1rem;
}
.form-section-title {
    font-size: .7rem;
    font-weight: 800;
    letter-spacing: .09em;
    text-transform: uppercase;
    opacity: .45;
    margin: 0 0 1rem;
}
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ──
with st.sidebar:
    st.markdown(
        f'<div class="sb-user"><h4>👤 {current_user["full_name"]}</h4>'
        f'<p>{current_user["role"]}</p></div>',
        unsafe_allow_html=True
    )
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
  <p>Enter data manually using the form or upload a CSV file for bulk records</p>
</div>
""", unsafe_allow_html=True)

# ── SCHOOL USER INFO ──
if current_user.get('role') == 'school':
    school_id = current_user.get('school_id')
    st.info(
        f"📍 **You are logged in as: {current_user['full_name']}**\n\n"
        f"The dashboard will show data for **{school_id}** only."
    )
    st.markdown("<br>", unsafe_allow_html=True)

# ── REQUIRED COLUMNS ──
REQUIRED_COLS = [
    'School_ID', 'Date', 'Students_Present', 'Meals_Served', 'Meals_Leftover',
    'Required_Calories', 'Actual_Calories', 'Required_Protein', 'Actual_Protein',
    'Meals_Taken', 'Avg_Taste_Rating', 'Kitchen_Cleaned',
    'Clean_Water_Available', 'Menu_Followed'
]

# ── RIGHT PANEL — always visible ──
main_col, right_col = st.columns([3, 2], gap="large")

with right_col:
    st.markdown("""
    <div style="background:var(--surf);border:1px solid var(--bdr);
         border-radius:var(--r2);padding:1.6rem 1.8rem;margin-bottom:1.2rem;">
      <p style="font-size:.7rem;font-weight:800;letter-spacing:.09em;
         text-transform:uppercase;opacity:.45;margin:0 0 1rem;">What We Analyse</p>
    """, unsafe_allow_html=True)

    checks = [
        ("📊", "Nutrition",  "Calorie & protein compliance against targets"),
        ("🗑️", "Waste",      "Meal leftover percentage per serving"),
        ("🧼", "Hygiene",    "Kitchen cleanliness & clean water checks"),
        ("⭐", "Taste",      "Average student rating across meals"),
        ("📋", "Menu",       "Whether approved menu was followed"),
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

    st.markdown("""
    <div style="background:var(--b-bg);border:1px solid var(--b-bd);
         border-radius:var(--r2);padding:1.2rem 1.5rem;">
      <p style="font-size:.7rem;font-weight:800;letter-spacing:.09em;
         text-transform:uppercase;color:var(--b);margin:0 0 .8rem;">Score Weights</p>
      <div style="display:flex;flex-direction:column;gap:.4rem;">
        <div style="display:flex;justify-content:space-between;font-size:.82rem;"><span>🥗 Nutrition</span><strong>30%</strong></div>
        <div style="display:flex;justify-content:space-between;font-size:.82rem;"><span>🗑️ Waste</span><strong>25%</strong></div>
        <div style="display:flex;justify-content:space-between;font-size:.82rem;"><span>🧼 Hygiene</span><strong>25%</strong></div>
        <div style="display:flex;justify-content:space-between;font-size:.82rem;"><span>⭐ Taste</span><strong>15%</strong></div>
        <div style="display:flex;justify-content:space-between;font-size:.82rem;"><span>📋 Menu</span><strong>5%</strong></div>
      </div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# MAIN COLUMN — TWO TABS
# ══════════════════════════════════════════════════════════════
with main_col:

    tab_form, tab_csv = st.tabs([
        "📝  Enter Manually",
        "📁  Upload CSV File"
    ])

    # ════════════════════════════════════
    # TAB 1 — MANUAL FORM
    # ════════════════════════════════════
    with tab_form:

        st.markdown("""
        <div class="up-card">
          <span class="uci">📝</span>
          <h3>Enter Daily Meal Data</h3>
          <p>Fill in today's meal details directly. No file needed — just enter the values and submit.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        # Determine school options based on role
        if current_user.get('role') == 'school':
            school_options = [current_user.get('school_id', 'SCH001')]
        else:
            school_options = [
                'SCH001', 'SCH002', 'SCH003', 'SCH004', 'SCH005',
                'SCH006', 'SCH007', 'SCH008', 'SCH009', 'SCH010'
            ]

        with st.form("meal_entry_form", clear_on_submit=False):

            # ── Section 1: Basic Info ──
            st.markdown('<p class="form-section-title">📍 Basic Information</p>', unsafe_allow_html=True)
            fi1, fi2 = st.columns(2)
            with fi1:
                school_id_form = st.selectbox(
                    "School ID",
                    options=school_options,
                    help="Select the school for this entry"
                )
            with fi2:
                meal_date = st.date_input(
                    "Date of Meal Service",
                    value=date.today(),
                    help="Date when meals were served"
                )

            st.markdown("<br>", unsafe_allow_html=True)

            # ── Section 2: Meal Counts ──
            st.markdown('<p class="form-section-title">🍽️ Meal Count Details</p>', unsafe_allow_html=True)
            mc1, mc2, mc3 = st.columns(3)
            with mc1:
                students_present = st.number_input(
                    "Students Present",
                    min_value=1, max_value=1000, value=150,
                    help="Total students who came to school"
                )
            with mc2:
                meals_served = st.number_input(
                    "Meals Served",
                    min_value=1, max_value=1000, value=150,
                    help="Total meals prepared and served"
                )
            with mc3:
                meals_leftover = st.number_input(
                    "Meals Leftover",
                    min_value=0, max_value=500, value=10,
                    help="Meals that were wasted or not consumed"
                )
            meals_taken = st.number_input(
                "Meals Taken by Students",
                min_value=0, max_value=1000, value=140,
                help="Actual number of meals consumed by students"
            )

            st.markdown("<br>", unsafe_allow_html=True)

            # ── Section 3: Nutrition ──
            st.markdown('<p class="form-section-title">🥗 Nutrition Details</p>', unsafe_allow_html=True)
            n1, n2 = st.columns(2)
            with n1:
                req_cal = st.number_input(
                    "Required Calories (target)",
                    min_value=500, max_value=5000, value=2000,
                    help="Target calorie count per meal"
                )
                req_prot = st.number_input(
                    "Required Protein in grams (target)",
                    min_value=10, max_value=200, value=50,
                    help="Target protein per meal in grams"
                )
            with n2:
                act_cal = st.number_input(
                    "Actual Calories (provided)",
                    min_value=500, max_value=5000, value=1950,
                    help="Actual calorie count in today's meal"
                )
                act_prot = st.number_input(
                    "Actual Protein in grams (provided)",
                    min_value=10, max_value=200, value=48,
                    help="Actual protein in today's meal in grams"
                )

            st.markdown("<br>", unsafe_allow_html=True)

            # ── Section 4: Quality Checks ──
            st.markdown('<p class="form-section-title">🧼 Quality & Hygiene Checks</p>', unsafe_allow_html=True)
            qc1, qc2, qc3 = st.columns(3)
            with qc1:
                kitchen_cleaned = st.selectbox(
                    "Kitchen Cleaned Today?",
                    options=["Yes", "No"],
                    help="Was the kitchen properly cleaned before cooking?"
                )
            with qc2:
                clean_water = st.selectbox(
                    "Clean Water Available?",
                    options=["Yes", "No"],
                    help="Was clean drinking water available for students?"
                )
            with qc3:
                menu_followed = st.selectbox(
                    "Approved Menu Followed?",
                    options=["Yes", "No"],
                    help="Was the pre-approved meal menu followed today?"
                )

            st.markdown("<br>", unsafe_allow_html=True)

            # ── Section 5: Taste Rating ──
            st.markdown('<p class="form-section-title">⭐ Student Feedback</p>', unsafe_allow_html=True)
            avg_taste = st.slider(
                "Average Taste Rating (1.0 = Very Poor  →  5.0 = Excellent)",
                min_value=1.0, max_value=5.0,
                value=4.0, step=0.1,
                help="Average rating collected from student feedback forms"
            )

            # Rating label
            if avg_taste >= 4.5:
                taste_label = "⭐⭐⭐⭐⭐ Excellent"
            elif avg_taste >= 3.5:
                taste_label = "⭐⭐⭐⭐ Good"
            elif avg_taste >= 2.5:
                taste_label = "⭐⭐⭐ Fair"
            elif avg_taste >= 1.5:
                taste_label = "⭐⭐ Poor"
            else:
                taste_label = "⭐ Very Poor"
            st.caption(f"Selected: {avg_taste} — {taste_label}")

            st.markdown("<br>", unsafe_allow_html=True)

            # ── SUBMIT ──
            submitted = st.form_submit_button(
                "✅ Submit & Analyse →",
                type="primary",
                use_container_width=True
            )

            if submitted:
                # Validate meal counts
                if meals_leftover > meals_served:
                    st.error("❌ Meals Leftover cannot be greater than Meals Served.")
                elif meals_taken > meals_served:
                    st.error("❌ Meals Taken cannot be greater than Meals Served.")
                else:
                    # Build DataFrame from form inputs
                    df_form = pd.DataFrame([{
                        'School_ID':             school_id_form,
                        'Date':                  str(meal_date),
                        'Students_Present':      int(students_present),
                        'Meals_Served':          int(meals_served),
                        'Meals_Leftover':        int(meals_leftover),
                        'Required_Calories':     int(req_cal),
                        'Actual_Calories':       int(act_cal),
                        'Required_Protein':      int(req_prot),
                        'Actual_Protein':        int(act_prot),
                        'Meals_Taken':           int(meals_taken),
                        'Avg_Taste_Rating':      float(avg_taste),
                        'Kitchen_Cleaned':       kitchen_cleaned == "Yes",
                        'Clean_Water_Available': clean_water     == "Yes",
                        'Menu_Followed':         menu_followed   == "Yes",
                    }])

                    # Save to session state
                    st.session_state.update({
                        'data_source': 'form',
                        'meal_data':   df_form,
                        'data_loaded': True
                    })

                    st.success(
                        f"✅ Data entered for **{school_id_form}** on **{meal_date}** — "
                        f"proceeding to AI analysis!"
                    )

                    st.switch_page("pages/3_processing.py")

    # ════════════════════════════════════
    # TAB 2 — CSV UPLOAD
    # ════════════════════════════════════
    with tab_csv:

        st.markdown("""
        <div class="up-card">
          <span class="uci">📁</span>
          <h3>Upload CSV File</h3>
          <p>Upload a CSV with multiple records for bulk analysis. All 14 required columns must be present.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        uploaded = st.file_uploader(
            "Choose your CSV file",
            type=["csv"],
            help="Must contain all 14 required columns"
        )

        st.markdown("<div style='margin-bottom:1.5rem;'></div>", unsafe_allow_html=True)

        if uploaded:
            try:
                df_csv = pd.read_csv(uploaded)
                missing = [c for c in REQUIRED_COLS if c not in df_csv.columns]

                if missing:
                    st.error(
                        f"❌ Missing {len(missing)} column(s): "
                        f"`{'`, `'.join(missing)}`"
                    )
                    st.info("📥 Download the template below to see the correct format.")
                else:
                    # School user validation
                    if current_user.get('role') == 'school':
                        user_school_id = current_user.get('school_id')
                        schools_in_csv = df_csv['School_ID'].unique().tolist()

                        if user_school_id not in schools_in_csv:
                            st.error(f"""
❌ **Invalid CSV for your account**

This CSV does not contain data for **{user_school_id}**.

**Schools found in CSV:** {', '.join(schools_in_csv)}

Please upload a CSV that contains data for **{user_school_id}**.
""")
                            st.stop()

                        other_schools = [s for s in schools_in_csv if s != user_school_id]
                        if other_schools:
                            st.warning(f"""
⚠️ **Multiple schools detected**

Only **{user_school_id}** data will be processed.
Other schools ({', '.join(other_schools)}) will be filtered out automatically.
""")

                        df_csv = df_csv[df_csv['School_ID'] == user_school_id].copy()
                        st.success(
                            f"✅ Found **{len(df_csv):,} records** for **{user_school_id}**"
                        )
                    else:
                        st.success(
                            f"✅ Valid! Found **{len(df_csv):,} records** "
                            f"from **{df_csv['School_ID'].nunique()} schools**"
                        )

                    with st.expander("Preview — first 8 rows"):
                        st.dataframe(df_csv.head(8), use_container_width=True)

                    st.session_state.update({
                        'data_source': 'csv',
                        'meal_data':   df_csv,
                        'data_loaded': True
                    })

                    st.markdown("<br>", unsafe_allow_html=True)
                    if st.button(
                        "Proceed to Analysis →",
                        type="primary",
                        use_container_width=True,
                        key="csv_proceed_btn"
                    ):
                        st.switch_page("pages/3_processing.py")

            except Exception as e:
                st.error(f"❌ Could not read file: {e}")

        # ── TEMPLATE SECTION ──
        st.markdown(
            '<div class="sec-div"><div class="dl"></div>'
            '<span>CSV Template</span><div class="dl"></div></div>',
            unsafe_allow_html=True
        )

        TEMPLATE_DF = pd.DataFrame({
            'School_ID':              ['SCH001', 'SCH002'],
            'Date':                   ['2024-01-01', '2024-01-02'],
            'Students_Present':       [100, 150],
            'Meals_Served':           [100, 150],
            'Meals_Leftover':         [10, 20],
            'Required_Calories':      [2000, 2000],
            'Actual_Calories':        [1950, 2100],
            'Required_Protein':       [50, 50],
            'Actual_Protein':         [48, 52],
            'Meals_Taken':            [90, 130],
            'Avg_Taste_Rating':       [4.2, 3.8],
            'Kitchen_Cleaned':        [True, True],
            'Clean_Water_Available':  [True, False],
            'Menu_Followed':          [True, True],
        })

        tl, tr = st.columns([3, 1], gap="large")

        with tl:
            st.markdown(
                "**Download the template** to ensure your data is "
                "formatted correctly before uploading."
            )
            with st.expander("View all 14 column descriptions"):
                col_desc = {
                    "School_ID":             "Unique school identifier e.g. SCH001",
                    "Date":                  "Date of meal service — YYYY-MM-DD format",
                    "Students_Present":      "Number of students present that day",
                    "Meals_Served":          "Total number of meals prepared",
                    "Meals_Leftover":        "Number of leftover / wasted meals",
                    "Required_Calories":     "Target calories per meal",
                    "Actual_Calories":       "Calories actually provided in the meal",
                    "Required_Protein":      "Target protein per meal in grams",
                    "Actual_Protein":        "Actual protein provided in grams",
                    "Meals_Taken":           "Number of meals consumed by students",
                    "Avg_Taste_Rating":      "Average student taste rating (1–5 scale)",
                    "Kitchen_Cleaned":       "Was the kitchen cleaned? True / False",
                    "Clean_Water_Available": "Was clean water available? True / False",
                    "Menu_Followed":         "Was the approved menu followed? True / False",
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