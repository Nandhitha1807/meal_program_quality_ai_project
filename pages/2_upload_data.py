# """
# Page 2: Upload Data
# User uploads CSV or loads from MySQL database
# """

# import streamlit as st
# import pandas as pd
# import sys
# from pathlib import Path

# # Add parent directory to path
# sys.path.append(str(Path(__file__).parent.parent))

# from src.db_loader import load_data_from_db
# from src.auth import is_logged_in, get_current_user, logout
# import mysql.connector
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # ========================================
# # AUTHENTICATION CHECK
# # ========================================
# if not is_logged_in(st.session_state):
#     st.error("🔒 Please login first to access this page!")
    
#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button("🔐 Go to Login", use_container_width=True, type="primary"):
#             st.switch_page("pages/1_login.py")
#     with col2:
#         if st.button("🏠 Go to Home", use_container_width=True):
#             st.switch_page("app.py")
    
#     st.stop()

# # Get current user
# current_user = get_current_user(st.session_state)

# # ========================================
# # PAGE CONFIGURATION
# # ========================================
# st.set_page_config(
#     page_title="Upload Data - School Meal Monitor",
#     page_icon="📤",
#     layout="wide"
# )

# # ========================================
# # CUSTOM CSS
# # ========================================
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    
#     * {
#         font-family: 'Inter', sans-serif;
#     }
    
#     .upload-container {
#         background: white;
#         padding: 3rem;
#         border-radius: 20px;
#         box-shadow: 0 10px 30px rgba(0,0,0,0.1);
#         text-align: center;
#         transition: all 0.3s ease;
#     }
    
#     .upload-container:hover {
#         box-shadow: 0 15px 40px rgba(0,0,0,0.15);
#         transform: translateY(-5px);
#     }
    
#     .upload-icon {
#         font-size: 5rem;
#         margin-bottom: 1rem;
#     }
    
#     .stButton>button {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         color: white;
#         border-radius: 10px;
#         padding: 0.8rem 2rem;
#         font-weight: 700;
#         border: none;
#         font-size: 1.1rem;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # ========================================
# # SIDEBAR - USER INFO & LOGOUT
# # ========================================
# with st.sidebar:
#     st.markdown(f"""
#         <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
#                     padding: 1.5rem; border-radius: 15px; color: white; margin-bottom: 2rem;'>
#             <h3 style='margin: 0; color: white;'>👤 {current_user['full_name']}</h3>
#             <p style='margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 0.9rem;'>
#                 Role: {current_user['role']}
#             </p>
#             <p style='margin: 0.3rem 0 0 0; opacity: 0.8; font-size: 0.85rem;'>
#                 Username: {current_user['username']}
#             </p>
#         </div>
#     """, unsafe_allow_html=True)
    
#     if st.button("🚪 Logout", use_container_width=True):
#         logout(st.session_state)
#         st.success("Logged out successfully!")
#         st.switch_page("pages/1_login.py")
    
#     st.markdown("---")
    
#     st.markdown("### 📍 Current Step")
#     st.info("**Step 1:** Upload Data")
    
#     st.markdown("### 🔄 Next Steps")
#     st.write("1. ✅ Upload Data (Current)")
#     st.write("2. ⏳ Processing")
#     st.write("3. 📊 Dashboard")
    
#     st.markdown("---")
    
#     if st.button("🏠 Back to Home", use_container_width=True):
#         st.switch_page("app.py")

# # ========================================
# # HEADER
# # ========================================
# st.markdown("""
#     <div style='text-align: center; padding: 2rem 0;'>
#         <h1 style='color: #1e293b; font-size: 3rem; font-weight: 800;'>
#             📤 Upload Meal Data
#         </h1>
#         <p style='color: #64748b; font-size: 1.2rem;'>
#             Choose your data source to begin quality analysis
#         </p>
#     </div>
# """, unsafe_allow_html=True)

# st.markdown("---")

# # ========================================
# # TWO OPTIONS: CSV UPLOAD OR DATABASE LOAD
# # ========================================
# col1, col2 = st.columns(2)

# with col1:
#     st.markdown("""
#         <div class="upload-container">
#             <div class="upload-icon">📁</div>
#             <h2 style='color: #1e293b; margin-bottom: 1rem;'>Upload CSV File</h2>
#             <p style='color: #64748b; margin-bottom: 2rem;'>
#                 Upload your school meal data from a CSV file
#             </p>
#         </div>
#     """, unsafe_allow_html=True)
    
#     uploaded_file = st.file_uploader(
#         "Choose CSV file",
#         type=['csv'],
#         help="Upload CSV with meal records",
#         label_visibility="collapsed"
#     )
    
#     if uploaded_file is not None:
#         try:
#             # Read CSV
#             df = pd.read_csv(uploaded_file)
            
#             # Validate required columns
#             required_cols = [
#                 'School_ID', 'Date', 'Students_Present', 'Meals_Served',
#                 'Meals_Leftover', 'Required_Calories', 'Actual_Calories',
#                 'Required_Protein', 'Actual_Protein', 'Meals_Taken',
#                 'Avg_Taste_Rating', 'Kitchen_Cleaned', 'Clean_Water_Available',
#                 'Menu_Followed'
#             ]
            
#             missing_cols = [col for col in required_cols if col not in df.columns]
            
#             if missing_cols:
#                 st.error(f"❌ Missing columns: {', '.join(missing_cols)}")
#                 st.info("💡 Download the template below to see the correct format")
#             else:
#                 st.success(f"✅ File validated! Found {len(df)} records from {df['School_ID'].nunique()} schools")
                
#                 # Preview data
#                 with st.expander("📋 Preview Data (First 10 rows)"):
#                     st.dataframe(df.head(10), use_container_width=True)
                
#                 # Store in session state
#                 st.session_state['data_source'] = 'csv'
#                 st.session_state['meal_data'] = df
#                 st.session_state['data_loaded'] = True
                
#                 st.markdown("<br>", unsafe_allow_html=True)
                
#                 # Navigate to processing page
#                 if st.button("🚀 Proceed to Analysis", use_container_width=True, type="primary", key="csv_proceed"):
#                     st.switch_page("pages/3_processing.py")
                    
#         except Exception as e:
#             st.error(f"❌ Error reading file: {str(e)}")
#             st.info("💡 Make sure your file is a valid CSV with the correct format")

# with col2:
#     st.markdown("""
#         <div class="upload-container">
#             <div class="upload-icon">💾</div>
#             <h2 style='color: #1e293b; margin-bottom: 1rem;'>Load from Database</h2>
#             <p style='color: #64748b; margin-bottom: 2rem;'>
#                 Load meal data directly from MySQL database
#             </p>
#         </div>
#     """, unsafe_allow_html=True)
    
#     # Check database connection
#     try:
#         conn = mysql.connector.connect(
#             host=os.getenv("DB_HOST"),
#             user=os.getenv("DB_USER"),
#             password=os.getenv("DB_PASSWORD"),
#             database=os.getenv("DB_NAME")
#         )
        
#         cursor = conn.cursor()
#         cursor.execute("SELECT COUNT(*) FROM meal_data")
#         record_count = cursor.fetchone()[0]
        
#         cursor.execute("SELECT COUNT(DISTINCT School_ID) FROM meal_data")
#         school_count = cursor.fetchone()[0]
        
#         conn.close()
        
#         st.success(f"✅ Database Connected!")
#         st.info(f"📊 Found **{record_count:,}** records from **{school_count}** schools")
        
#         st.markdown("<br>", unsafe_allow_html=True)
        
#         if st.button("💾 Load from MySQL", use_container_width=True, type="primary", key="db_load"):
#             with st.spinner("🔄 Loading data from database..."):
#                 df = load_data_from_db()
                
#                 st.session_state['data_source'] = 'database'
#                 st.session_state['meal_data'] = df
#                 st.session_state['data_loaded'] = True
                
#                 st.success(f"✅ Loaded {len(df)} records!")
#                 st.balloons()
                
#                 import time
#                 time.sleep(1)
                
#                 st.switch_page("pages/3_processing.py")
                
#     except Exception as e:
#         st.error(f"❌ Database Connection Failed!")
#         st.code(str(e), language="text")
#         st.warning("💡 Make sure:")
#         st.write("- MySQL server is running")
#         st.write("- Credentials in `.env` are correct")
#         st.write("- Database `school_meal_db` exists")
#         st.write("- Table `meal_data` has data")

# # ========================================
# # DOWNLOAD TEMPLATE SECTION
# # ========================================
# st.markdown("<br><br>", unsafe_allow_html=True)
# st.markdown("---")
# st.markdown("""
#     <h2 style='text-align: center; color: #1e293b; margin: 2rem 0;'>
#         📥 Need a CSV Template?
#     </h2>
#     <p style='text-align: center; color: #64748b; font-size: 1.1rem; margin-bottom: 2rem;'>
#         Download our standard template to ensure your data is formatted correctly
#     </p>
# """, unsafe_allow_html=True)

# col1, col2, col3 = st.columns([1, 2, 1])

# with col2:
#     # Create template
#     template_df = pd.DataFrame({
#         'School_ID': ['SCH001', 'SCH002'],
#         'Date': ['2024-01-01', '2024-01-02'],
#         'Students_Present': [100, 150],
#         'Meals_Served': [100, 150],
#         'Meals_Leftover': [10, 20],
#         'Required_Calories': [2000, 2000],
#         'Actual_Calories': [1950, 2100],
#         'Required_Protein': [50, 50],
#         'Actual_Protein': [48, 52],
#         'Meals_Taken': [90, 130],
#         'Avg_Taste_Rating': [4.2, 3.8],
#         'Kitchen_Cleaned': [True, True],
#         'Clean_Water_Available': [True, False],
#         'Menu_Followed': [True, True]
#     })
    
#     csv_template = template_df.to_csv(index=False).encode('utf-8')
    
#     st.download_button(
#         label="📄 Download CSV Template",
#         data=csv_template,
#         file_name="school_meal_template.csv",
#         mime="text/csv",
#         use_container_width=True,
#         type="primary"
#     )
    
#     st.markdown("<br>", unsafe_allow_html=True)
    
#     with st.expander("📋 View Template Format & Column Descriptions"):
#         st.dataframe(template_df, use_container_width=True)
        
#         st.markdown("### 📝 Column Descriptions:")
#         st.markdown("""
#         - **School_ID**: Unique identifier for each school (e.g., SCH001)
#         - **Date**: Date of meal service (YYYY-MM-DD format)
#         - **Students_Present**: Number of students present
#         - **Meals_Served**: Total meals prepared
#         - **Meals_Leftover**: Wasted/leftover meals
#         - **Required_Calories**: Target calories per meal
#         - **Actual_Calories**: Actual calories provided
#         - **Required_Protein**: Target protein in grams
#         - **Actual_Protein**: Actual protein provided in grams
#         - **Meals_Taken**: Number of meals consumed by students
#         - **Avg_Taste_Rating**: Average student rating (1-5 scale)
#         - **Kitchen_Cleaned**: Was kitchen cleaned? (True/False)
#         - **Clean_Water_Available**: Was clean water available? (True/False)
#         - **Menu_Followed**: Was approved menu followed? (True/False)
#         """)

# st.markdown("<br><br>", unsafe_allow_html=True)
"""
pages/2_upload_data.py — Upload Page
"""
import streamlit as st
import pandas as pd, sys, os, time
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from src.db_loader import load_data_from_db
from src.auth import is_logged_in, get_current_user, logout
from src.styles import GLOBAL_CSS
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

if not is_logged_in(st.session_state):
    st.error("🔒 Please sign in first.")
    if st.button("Go to Login →", type="primary"): st.switch_page("pages/1_login.py")
    st.stop()

current_user = get_current_user(st.session_state)

st.set_page_config(page_title="Upload · School Meal Monitor", page_icon="📤", layout="wide")
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
st.markdown("""
<style>
/* Upload option cards */
.upload-opt {
    background: var(--surface-1);
    border: 1.5px solid var(--border);
    border-radius: var(--r-lg);
    padding: 2rem;
    transition: all .3s ease;
    height: 100%;
}
.upload-opt:hover { border-color: var(--c-blue); box-shadow: 0 8px 28px var(--c-blue-glow); }
.opt-icon { font-size: 3rem; margin-bottom: 1rem; display: block; }
.opt-title { font-family:'Fraunces',serif !important; font-size:1.5rem; font-weight:700; margin:0 0 .5rem; }
.opt-desc  { font-size:.88rem; opacity:.6; margin:0 0 1.5rem; line-height:1.6; }

/* Template section */
.template-box {
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: var(--r-lg);
    padding: 2rem 2.5rem;
    margin-top: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ──
with st.sidebar:
    st.markdown(f'<div class="sidebar-user-card"><h4>👤 {current_user["full_name"]}</h4><p>Role: {current_user["role"]}</p></div>', unsafe_allow_html=True)
    if st.button("🚪 Sign Out", use_container_width=True):
        logout(st.session_state)
        st.switch_page("pages/1_login.py")
    st.markdown("---")

    # Step progress
    st.markdown("""
    <div class="step-bar">
      <div class="step-item"><div class="step-dot active">1</div><span class="step-text active">Upload</span></div>
      <div class="step-connector"></div>
      <div class="step-item"><div class="step-dot">2</div><span class="step-text">Process</span></div>
      <div class="step-connector"></div>
      <div class="step-item"><div class="step-dot">3</div><span class="step-text">Dashboard</span></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")

# ── HEADER ──
st.markdown("""
<div class="page-header">
  <div class="header-badge">Step 1 of 3</div>
  <h1>📤 Upload Meal Data</h1>
  <p>Choose your data source — CSV file or live MySQL database connection</p>
</div>
""", unsafe_allow_html=True)

# ── TWO OPTIONS ──
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="upload-opt">
      <span class="opt-icon">📁</span>
      <p class="opt-title">CSV File Upload</p>
      <p class="opt-desc">Upload a CSV file exported from Excel or any data tool.</p>
    </div>
    """, unsafe_allow_html=True)

    uploaded = st.file_uploader("", type=["csv"], label_visibility="collapsed")

    if uploaded:
        try:
            df = pd.read_csv(uploaded)
            required = ['School_ID','Date','Students_Present','Meals_Served','Meals_Leftover',
                        'Required_Calories','Actual_Calories','Required_Protein','Actual_Protein',
                        'Meals_Taken','Avg_Taste_Rating','Kitchen_Cleaned','Clean_Water_Available','Menu_Followed']
            missing = [c for c in required if c not in df.columns]

            if missing:
                st.error(f"❌ Missing columns: {', '.join(missing)}")
            else:
                st.success(f"✅ {len(df):,} records · {df['School_ID'].nunique()} schools detected")
                with st.expander("Preview first 8 rows"):
                    st.dataframe(df.head(8), use_container_width=True)
                st.session_state.update({'data_source':'csv','meal_data':df,'data_loaded':True})
                if st.button("Proceed to Processing →", type="primary", use_container_width=True, key="csv_go"):
                    st.switch_page("pages/3_processing.py")
        except Exception as e:
            st.error(f"Error reading file: {e}")

with col2:
    st.markdown("""
    <div class="upload-opt">
      <span class="opt-icon">💾</span>
      <p class="opt-title">MySQL Database</p>
      <p class="opt-desc">Load data directly from your configured MySQL database.</p>
    </div>
    """, unsafe_allow_html=True)

    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"), user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"), database=os.getenv("DB_NAME")
        )
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM meal_data")
        rc = cur.fetchone()[0]
        cur.execute("SELECT COUNT(DISTINCT School_ID) FROM meal_data")
        sc = cur.fetchone()[0]
        conn.close()

        st.success("✅ Database connected")
        c1, c2 = st.columns(2)
        c1.metric("Records", f"{rc:,}")
        c2.metric("Schools", sc)
        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("Load from MySQL →", type="primary", use_container_width=True, key="db_go"):
            with st.spinner("Loading data..."):
                df = load_data_from_db()
                st.session_state.update({'data_source':'database','meal_data':df,'data_loaded':True})
                st.success(f"✅ {len(df):,} records loaded!")
                time.sleep(0.7)
                st.switch_page("pages/3_processing.py")
    except Exception as e:
        st.error("❌ Database connection failed")
        with st.expander("View error details"):
            st.code(str(e))
        st.info("Check your `.env` credentials and ensure MySQL is running.")

# ── TEMPLATE DOWNLOAD ──
st.markdown("""
<div class="section-label">
  <div class="line"></div><span>CSV Template</span><div class="line"></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="template-box">', unsafe_allow_html=True)
tc1, tc2 = st.columns([2, 1])
with tc1:
    st.markdown("**Need a template?** Download the CSV template to ensure your data is formatted correctly before uploading.")
    tdf = pd.DataFrame({
        'School_ID':['SCH001','SCH002'],'Date':['2024-01-01','2024-01-02'],
        'Students_Present':[100,150],'Meals_Served':[100,150],'Meals_Leftover':[10,20],
        'Required_Calories':[2000,2000],'Actual_Calories':[1950,2100],
        'Required_Protein':[50,50],'Actual_Protein':[48,52],
        'Meals_Taken':[90,130],'Avg_Taste_Rating':[4.2,3.8],
        'Kitchen_Cleaned':[True,True],'Clean_Water_Available':[True,False],'Menu_Followed':[True,True]
    })
    with st.expander("View column descriptions"):
        cols_desc = {
            "School_ID":"Unique school identifier (e.g. SCH001)",
            "Date":"Date of meal service — YYYY-MM-DD",
            "Students_Present":"Number of students that day",
            "Meals_Served":"Total meals prepared",
            "Meals_Leftover":"Leftover / wasted meals",
            "Required_Calories":"Target calories per meal",
            "Actual_Calories":"Calories actually served",
            "Required_Protein":"Target protein in grams",
            "Actual_Protein":"Protein actually served",
            "Meals_Taken":"Meals consumed by students",
            "Avg_Taste_Rating":"Student rating 1–5",
            "Kitchen_Cleaned":"Was kitchen cleaned? True/False",
            "Clean_Water_Available":"Was clean water available? True/False",
            "Menu_Followed":"Was the approved menu followed? True/False",
        }
        for col, desc in cols_desc.items():
            st.markdown(f"**`{col}`** — {desc}")
with tc2:
    st.download_button(
        "📄 Download Template",
        data=tdf.to_csv(index=False).encode(),
        file_name="school_meal_template.csv",
        mime="text/csv",
        use_container_width=True,
        type="primary"
    )
st.markdown("</div>", unsafe_allow_html=True)