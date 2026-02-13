"""
Page 1: Upload Data
"""

import streamlit as st
import pandas as pd
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from src.db_loader import load_data_from_db
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# Page config
st.set_page_config(
    page_title="Upload Data - School Meal Monitor",
    page_icon="📤",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .upload-container {
        background: white;
        padding: 3rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    .upload-icon {
        font-size: 5rem;
        margin-bottom: 1rem;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        padding: 0.8rem 2rem;
        font-weight: 700;
        border: none;
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div style='text-align: center; padding: 2rem 0;'>
        <h1 style='color: #1e293b; font-size: 3rem; font-weight: 800;'>
            📤 Upload Meal Data
        </h1>
        <p style='color: #64748b; font-size: 1.2rem;'>
            Choose your data source to begin quality analysis
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Two options: CSV Upload or Database Load
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="upload-container">
            <div class="upload-icon">📁</div>
            <h2 style='color: #1e293b; margin-bottom: 1rem;'>Upload CSV File</h2>
            <p style='color: #64748b; margin-bottom: 2rem;'>
                Upload your school meal data from a CSV file
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Choose CSV file",
        type=['csv'],
        help="Upload CSV with meal records",
        label_visibility="collapsed"
    )
    
    if uploaded_file is not None:
        try:
            # Read CSV
            df = pd.read_csv(uploaded_file)
            
            # Validate required columns
            required_cols = [
                'School_ID', 'Date', 'Students_Present', 'Meals_Served',
                'Meals_Leftover', 'Required_Calories', 'Actual_Calories',
                'Required_Protein', 'Actual_Protein', 'Meals_Taken',
                'Avg_Taste_Rating', 'Kitchen_Cleaned', 'Clean_Water_Available',
                'Menu_Followed'
            ]
            
            missing_cols = [col for col in required_cols if col not in df.columns]
            
            if missing_cols:
                st.error(f"❌ Missing columns: {', '.join(missing_cols)}")
            else:
                st.success(f"✅ File validated! Found {len(df)} records from {df['School_ID'].nunique()} schools")
                
                # Preview data
                with st.expander("📋 Preview Data"):
                    st.dataframe(df.head(10), use_container_width=True)
                
                # Store in session state
                st.session_state['data_source'] = 'csv'
                st.session_state['meal_data'] = df
                st.session_state['data_loaded'] = True
                
                # Navigate to processing page
                if st.button("🚀 Proceed to Analysis", use_container_width=True, type="primary"):
                    st.switch_page("pages/processing.py")
                    
        except Exception as e:
            st.error(f"❌ Error reading file: {str(e)}")

with col2:
    st.markdown("""
        <div class="upload-container">
            <div class="upload-icon">💾</div>
            <h2 style='color: #1e293b; margin-bottom: 1rem;'>Load from Database</h2>
            <p style='color: #64748b; margin-bottom: 2rem;'>
                Load meal data directly from MySQL database
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Check database connection
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM meal_data")
        record_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(DISTINCT School_ID) FROM meal_data")
        school_count = cursor.fetchone()[0]
        
        conn.close()
        
        st.success(f"✅ Database Connected!")
        st.info(f"📊 Found {record_count:,} records from {school_count} schools")
        
        if st.button("💾 Load from MySQL", use_container_width=True, type="primary"):
            with st.spinner("Loading data from database..."):
                df = load_data_from_db()
                
                st.session_state['data_source'] = 'database'
                st.session_state['meal_data'] = df
                st.session_state['data_loaded'] = True
                
                st.success(f"✅ Loaded {len(df)} records!")
                st.switch_page("pages/processing.py")
                
    except Exception as e:
        st.error(f"❌ Database Connection Failed!")
        st.code(str(e))
        st.info("💡 Make sure MySQL is running and credentials in .env are correct")

# Download Template Option
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
    <h2 style='text-align: center; color: #1e293b; margin: 2rem 0;'>
        📥 Need a Template?
    </h2>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    template_df = pd.DataFrame({
        'School_ID': ['SCH001', 'SCH002'],
        'Date': ['2024-01-01', '2024-01-02'],
        'Students_Present': [100, 150],
        'Meals_Served': [100, 150],
        'Meals_Leftover': [10, 20],
        'Required_Calories': [2000, 2000],
        'Actual_Calories': [1950, 2100],
        'Required_Protein': [50, 50],
        'Actual_Protein': [48, 52],
        'Meals_Taken': [90, 130],
        'Avg_Taste_Rating': [4.2, 3.8],
        'Kitchen_Cleaned': [True, True],
        'Clean_Water_Available': [True, False],
        'Menu_Followed': [True, True]
    })
    
    csv_template = template_df.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="📄 Download CSV Template",
        data=csv_template,
        file_name="school_meal_template.csv",
        mime="text/csv",
        use_container_width=True
    )
    
    with st.expander("📋 View Template Format"):
        st.dataframe(template_df, use_container_width=True)

# Sidebar
with st.sidebar:
    st.markdown("### 📍 Current Step")
    st.info("**Step 1:** Upload Data")
    
    st.markdown("### 🔄 Next Steps")
    st.write("1. ✅ Upload Data (Current)")
    st.write("2. ⏳ Processing")
    st.write("3. 📊 Dashboard")
    
    st.markdown("---")
    
    if st.button("🏠 Back to Home"):
        st.switch_page("app.py")