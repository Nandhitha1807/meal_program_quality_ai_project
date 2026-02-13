"""
School Meal Quality Monitoring System
Main Streamlit Application with MySQL Integration
"""

import streamlit as st
import sys
from pathlib import Path
import pandas as pd

# Add src to path
sys.path.append(str(Path(__file__).parent))

from src.db_loader import load_data_from_db
from src.data_processor import DataProcessor
from src.visualizations import Visualizer
from models.quality_rules import QualityAssessment

# ========================================
# PAGE CONFIGURATION
# ========================================
st.set_page_config(
    page_title="School Meal Quality Monitor",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========================================
# CUSTOM CSS FOR BEAUTIFUL DESIGN
# ========================================
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main container */
    .main {
        padding: 0rem 1rem;
        background-color: #f8fafc;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Headers */
    h1 {
        color: #1e293b;
        font-weight: 800;
        text-align: center;
        padding: 1rem 0;
        font-size: 2.5rem;
    }
    
    h2 {
        color: #334155;
        font-weight: 700;
        border-left: 5px solid #3b82f6;
        padding-left: 1rem;
        margin-top: 2rem;
        font-size: 1.8rem;
    }
    
    h3 {
        color: #475569;
        font-weight: 600;
    }
    
    /* Metric Cards - Custom styling */
    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    div[data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2);
    }
    
    div[data-testid="metric-container"] > div {
        color: white !important;
    }
    
    div[data-testid="metric-container"] label {
        color: rgba(255, 255, 255, 0.9) !important;
        font-weight: 600 !important;
    }
    
    /* Success/Warning/Error boxes */
    .stSuccess {
        background-color: #d1fae5;
        border-left: 5px solid #10b981;
        padding: 1rem;
        border-radius: 10px;
        color: #065f46;
    }
    
    .stWarning {
        background-color: #fef3c7;
        border-left: 5px solid #f59e0b;
        padding: 1rem;
        border-radius: 10px;
        color: #92400e;
    }
    
    .stError {
        background-color: #fee2e2;
        border-left: 5px solid #ef4444;
        padding: 1rem;
        border-radius: 10px;
        color: #991b1b;
    }
    
    /* Dataframe styling */
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    section[data-testid="stSidebar"] .css-1d391kg {
        color: white;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #f3f4f6;
        border-radius: 10px;
        font-weight: 600;
        padding: 1rem;
        border: 1px solid #e5e7eb;
    }
    
    .streamlit-expanderHeader:hover {
        background-color: #e5e7eb;
        border-color: #3b82f6;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px 10px 0px 0px;
        padding: 12px 24px;
        background-color: #f1f5f9;
        color: #64748b;
        font-weight: 600;
        border: none;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        padding: 0.6rem 2rem;
        font-weight: 700;
        border: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* Download button */
    .stDownloadButton>button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        border-radius: 10px;
        padding: 0.6rem 2rem;
        font-weight: 700;
        border: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .stDownloadButton>button:hover {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #3b82f6 !important;
    }
    
    /* Slider */
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Multiselect */
    .stMultiSelect > div > div {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# ========================================
# HEADER SECTION
# ========================================
st.markdown("""
    <div style='text-align: center; padding: 2rem 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 20px; margin-bottom: 2rem; box-shadow: 0 10px 25px rgba(0,0,0,0.1);'>
        <h1 style='color: white; margin: 0; font-size: 3rem;'>🍽️ School Meal Quality Monitor</h1>
        <p style='color: rgba(255,255,255,0.9); font-size: 1.3rem; margin: 0.5rem 0 0 0; font-weight: 500;'>
            AI-Powered Quality Assessment System
        </p>
        <p style='color: rgba(255,255,255,0.8); font-size: 1rem; margin: 0.3rem 0 0 0;'>
            Ensuring Quality Nutrition for Every Student
        </p>
    </div>
    """, unsafe_allow_html=True)

# ========================================
# LOAD DATA FROM MYSQL DATABASE
# ========================================
@st.cache_data(ttl=300)  # Cache for 5 minutes
def load_and_process_data():
    """Load data from MySQL and process it"""
    try:
        df = load_data_from_db()
        
        if df.empty:
            raise ValueError("No data found in database")
        
        processor = DataProcessor(df=df)
        df = processor.calculate_metrics()
        
        quality_checker = QualityAssessment(df)
        quality_df = quality_checker.calculate_overall_quality()
        alerts_df = quality_checker.generate_alerts(quality_df)
        
        stats = processor.get_summary_stats()
        
        return df, quality_df, alerts_df, stats
        
    except Exception as e:
        raise Exception(f"Data loading error: {str(e)}")

# Load data
with st.spinner("🔄 Loading data from MySQL database..."):
    try:
        df, quality_df, alerts_df, stats = load_and_process_data()
        st.success("✅ Data loaded and processed successfully from MySQL!")
    except Exception as e:
        st.error(f"❌ Database Error: {str(e)}")
        st.info("💡 Make sure MySQL is running and data is loaded. Run: `python load_data_to_mysql.py`")
        st.stop()

# ========================================
# KPI SECTION - BEAUTIFUL GRADIENT CARDS
# ========================================
st.markdown("## 📊 Key Performance Indicators")
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 2rem 1.5rem; border-radius: 20px; color: white; 
                    box-shadow: 0 10px 20px rgba(102,126,234,0.3);
                    transition: transform 0.3s ease;'>
            <p style='margin: 0; font-size: 0.9rem; opacity: 0.9; font-weight: 600;'>🏫 TOTAL SCHOOLS</p>
            <h1 style='margin: 0.5rem 0 0 0; color: white; font-size: 3rem;'>{}</h1>
        </div>
    """.format(stats['total_schools']), unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                    padding: 2rem 1.5rem; border-radius: 20px; color: white; 
                    box-shadow: 0 10px 20px rgba(240,147,251,0.3);'>
            <p style='margin: 0; font-size: 0.9rem; opacity: 0.9; font-weight: 600;'>🍽️ MEALS SERVED</p>
            <h1 style='margin: 0.5rem 0 0 0; color: white; font-size: 3rem;'>{:,}</h1>
        </div>
    """.format(stats['total_meals_served']), unsafe_allow_html=True)

with col3:
    waste_gradient = "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)" if stats['avg_waste'] > 20 else "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)"
    st.markdown("""
        <div style='background: {}; 
                    padding: 2rem 1.5rem; border-radius: 20px; color: white; 
                    box-shadow: 0 10px 20px rgba(79,172,254,0.3);'>
            <p style='margin: 0; font-size: 0.9rem; opacity: 0.9; font-weight: 600;'>🗑️ AVG WASTE</p>
            <h1 style='margin: 0.5rem 0 0 0; color: white; font-size: 3rem;'>{:.1f}%</h1>
        </div>
    """.format(waste_gradient, stats['avg_waste']), unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div style='background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); 
                    padding: 2rem 1.5rem; border-radius: 20px; color: white; 
                    box-shadow: 0 10px 20px rgba(250,112,154,0.3);'>
            <p style='margin: 0; font-size: 0.9rem; opacity: 0.9; font-weight: 600;'>⭐ AVG TASTE</p>
            <h1 style='margin: 0.5rem 0 0 0; color: white; font-size: 3rem;'>{:.1f}</h1>
            <p style='margin: 0; font-size: 0.8rem; opacity: 0.8;'>out of 5.0</p>
        </div>
    """.format(stats['avg_taste_rating']), unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ========================================
# NUTRITION COMPLIANCE OVERVIEW
# ========================================
st.markdown("## 🎯 Nutritional Compliance Overview")
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    cal_status = "✅ On Target" if stats['avg_calorie_compliance'] >= 95 else "⚠️ Below Target"
    st.markdown("""
        <div style='background-color: #ecfdf5; padding: 2rem; 
                    border-radius: 15px; border-left: 6px solid #10b981;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.05);'>
            <h4 style='color: #065f46; margin: 0; font-size: 0.9rem; font-weight: 700;'>
                CALORIE COMPLIANCE
            </h4>
            <h1 style='color: #047857; margin: 1rem 0; font-size: 3rem;'>{:.1f}%</h1>
            <p style='color: #059669; margin: 0; font-weight: 600;'>{}</p>
        </div>
    """.format(stats['avg_calorie_compliance'], cal_status), unsafe_allow_html=True)

with col2:
    prot_status = "✅ On Target" if stats['avg_protein_compliance'] >= 95 else "⚠️ Below Target"
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 2rem; 
                    border-radius: 15px; border-left: 6px solid #f59e0b;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.05);'>
            <h4 style='color: #92400e; margin: 0; font-size: 0.9rem; font-weight: 700;'>
                PROTEIN COMPLIANCE
            </h4>
            <h1 style='color: #d97706; margin: 1rem 0; font-size: 3rem;'>{:.1f}%</h1>
            <p style='color: #b45309; margin: 0; font-weight: 600;'>{}</p>
        </div>
    """.format(stats['avg_protein_compliance'], prot_status), unsafe_allow_html=True)

with col3:
    excellent_count = len(quality_df[quality_df['Overall_Quality_Score'] >= 85])
    excellence_rate = (excellent_count / stats['total_schools']) * 100 if stats['total_schools'] > 0 else 0
    st.markdown("""
        <div style='background-color: #dbeafe; padding: 2rem; 
                    border-radius: 15px; border-left: 6px solid #3b82f6;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.05);'>
            <h4 style='color: #1e3a8a; margin: 0; font-size: 0.9rem; font-weight: 700;'>
                EXCELLENT SCHOOLS
            </h4>
            <h1 style='color: #2563eb; margin: 1rem 0; font-size: 3rem;'>{}</h1>
            <p style='color: #1d4ed8; margin: 0; font-weight: 600;'>{:.0f}% of total</p>
        </div>
    """.format(excellent_count, excellence_rate), unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")

# ========================================
# ALERTS SECTION - ENHANCED DESIGN
# ========================================
st.markdown("## 🚨 AI-Generated Quality Alerts")
st.markdown("<br>", unsafe_allow_html=True)

if not alerts_df.empty:
    high_priority = len(alerts_df[alerts_df['Priority'] == 'High'])
    medium_priority = len(alerts_df[alerts_df['Priority'] == 'Medium'])
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown(f"""
            <div style='background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%); 
                        padding: 1.5rem; border-radius: 15px; 
                        border-left: 6px solid #dc2626;
                        box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
                <h3 style='color: #991b1b; margin: 0; font-size: 1rem; font-weight: 700;'>
                    🔴 HIGH PRIORITY
                </h3>
                <p style='font-size: 3rem; font-weight: 800; color: #dc2626; margin: 0.5rem 0 0 0;'>
                    {high_priority}
                </p>
                <p style='color: #b91c1c; margin: 0; font-weight: 600;'>schools need urgent attention</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div style='background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); 
                        padding: 1.5rem; border-radius: 15px; 
                        border-left: 6px solid #f59e0b;
                        box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
                <h3 style='color: #92400e; margin: 0; font-size: 1rem; font-weight: 700;'>
                    🟡 MEDIUM PRIORITY
                </h3>
                <p style='font-size: 3rem; font-weight: 800; color: #f59e0b; margin: 0.5rem 0 0 0;'>
                    {medium_priority}
                </p>
                <p style='color: #b45309; margin: 0; font-weight: 600;'>schools need monitoring</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        total_alerts = len(alerts_df)
        st.markdown(f"""
            <div style='background: linear-gradient(135deg, #e0e7ff 0%, #c7d2fe 100%); 
                        padding: 1.5rem; border-radius: 15px; 
                        border-left: 6px solid #6366f1;
                        box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
                <h3 style='color: #3730a3; margin: 0; font-size: 1rem; font-weight: 700;'>
                    📊 TOTAL ALERTS
                </h3>
                <p style='font-size: 3rem; font-weight: 800; color: #6366f1; margin: 0.5rem 0 0 0;'>
                    {total_alerts}
                </p>
                <p style='color: #4f46e5; margin: 0; font-weight: 600;'>issues detected</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Alert Details in Expandable Cards
    with st.expander(f"📋 View All {len(alerts_df)} Alert Details", expanded=False):
        for idx, alert in alerts_df.head(15).iterrows():  # Show first 15
            priority_color = "#dc2626" if alert['Priority'] == 'High' else "#f59e0b"
            priority_bg = "#fee2e2" if alert['Priority'] == 'High' else "#fef3c7"
            priority_emoji = "🔴" if alert['Priority'] == 'High' else "🟡"
            
            st.markdown(f"""
                <div style='background-color: {priority_bg}; padding: 1.5rem; 
                            margin-bottom: 1rem; border-radius: 12px;
                            border-left: 5px solid {priority_color};
                            box-shadow: 0 2px 4px rgba(0,0,0,0.05);'>
                    <h4 style='margin: 0 0 0.5rem 0; color: #374151; font-weight: 700;'>
                        {priority_emoji} School: <span style='color: {priority_color};'>{alert['School_ID']}</span> 
                        | Date: {alert['Date']} | Priority: <span style='color: {priority_color};'>{alert['Priority']}</span>
                    </h4>
            """, unsafe_allow_html=True)
            
            st.markdown("**Issues Detected:**")
            for issue in alert['Alerts']:
                st.write(f"  ⚠️ {issue}")
            
            st.markdown("</div>", unsafe_allow_html=True)
else:
    st.markdown("""
        <div style='background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%); 
                    padding: 2rem; border-radius: 15px; text-align: center;
                    border-left: 6px solid #10b981;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.05);'>
            <h2 style='color: #065f46; margin: 0;'>✅ Excellent Performance!</h2>
            <p style='color: #047857; margin: 0.5rem 0 0 0; font-size: 1.2rem; font-weight: 600;'>
                No critical alerts - All schools are performing well
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")

# ========================================
# VISUALIZATIONS - INTERACTIVE CHARTS
# ========================================
st.markdown("## 📈 Analytics Dashboard")
st.markdown("<br>", unsafe_allow_html=True)

visualizer = Visualizer(df)

tab1, tab2, tab3, tab4 = st.tabs([
    "📉 Waste Trends",
    "🎯 Quality Overview",
    "🏆 School Rankings",
    "🥗 Nutrition Metrics"
])

with tab1:
    st.markdown("### Food Waste Analysis Over Time")
    st.plotly_chart(
        visualizer.plot_waste_trend(),
        use_container_width=True,
        config={'displayModeBar': True, 'displaylogo': False}
    )
    
    st.info("💡 **Insight:** Monitor the waste trend to identify patterns and implement targeted interventions.")

with tab2:
    st.markdown("### Quality Distribution & Performance Metrics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(
            visualizer.plot_quality_distribution(quality_df),
            use_container_width=True,
            config={'displayModeBar': False}
        )
    
    with col2:
        st.plotly_chart(
            visualizer.plot_metrics_radar(quality_df),
            use_container_width=True,
            config={'displayModeBar': False}
        )
    
    st.info("💡 **Insight:** The radar chart shows balanced performance across all quality dimensions.")

with tab3:
    st.markdown("### School Performance Comparison")
    st.plotly_chart(
        visualizer.plot_school_performance(quality_df),
        use_container_width=True,
        config={'displayModeBar': True, 'displaylogo': False}
    )
    
    st.info("💡 **Insight:** Identify top performers and schools needing additional support.")

with tab4:
    st.markdown("### Nutritional Compliance Analysis")
    st.plotly_chart(
        visualizer.plot_nutrition_compliance(),
        use_container_width=True,
        config={'displayModeBar': True, 'displaylogo': False}
    )
    
    st.info("💡 **Insight:** Both calorie and protein compliance should ideally be at or above 100%.")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")

# ========================================
# DATA TABLE WITH FILTERS
# ========================================
st.markdown("## 📋 Detailed Quality Assessment Data")
st.markdown("<br>", unsafe_allow_html=True)

# Add filters
col1, col2, col3 = st.columns(3)

with col1:
    min_score = st.slider(
        "🎯 Minimum Quality Score",
        min_value=0,
        max_value=100,
        value=0,
        step=5,
        help="Filter schools by minimum quality score"
    )

with col2:
    selected_schools = st.multiselect(
        "🏫 Select Schools",
        options=sorted(quality_df['School_ID'].unique()),
        default=sorted(quality_df['School_ID'].unique()),
        help="Filter by specific schools"
    )

with col3:
    date_range = st.selectbox(
        "📅 Date Range",
        options=["All Dates", "Last 7 Days", "Last 30 Days"],
        help="Filter by date range"
    )

# Apply filters
filtered_df = quality_df[
    (quality_df['Overall_Quality_Score'] >= min_score) &
    (quality_df['School_ID'].isin(selected_schools))
]

# Display filtered count
st.markdown(f"""
    <div style='background-color: #f3f4f6; padding: 1rem; border-radius: 10px; margin: 1rem 0;'>
        <p style='margin: 0; color: #374151; font-weight: 600;'>
            📊 Showing {len(filtered_df)} of {len(quality_df)} total records
        </p>
    </div>
""", unsafe_allow_html=True)

# Display table with styling
st.dataframe(
    filtered_df.style.background_gradient(
        cmap='RdYlGn',
        subset=['Overall_Quality_Score'],
        vmin=0,
        vmax=100
    ).format({
        'Overall_Quality_Score': '{:.2f}',
        'Nutrition_Score': '{:.2f}',
        'Waste_Score': '{:.2f}',
        'Hygiene_Score': '{:.2f}',
        'Taste_Score': '{:.2f}',
        'Menu_Score': '{:.2f}'
    }),
    use_container_width=True,
    height=450
)

# Download options
st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Data (CSV)",
        data=csv,
        file_name=f"quality_assessment_report_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv",
        use_container_width=True
    )

with col2:
    # Download full data
    csv_full = quality_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download All Data (CSV)",
        data=csv_full,
        file_name=f"complete_quality_report_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv",
        use_container_width=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ========================================
# SIDEBAR - ENHANCED
# ========================================
with st.sidebar:
    st.markdown("""
        <div style='text-align: center; padding: 1.5rem 0;'>
            <img src='https://img.icons8.com/fluency/96/000000/school.png' width='100'>
            <h2 style='color: white; margin: 1rem 0; font-weight: 700;'>About This System</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style='background-color: rgba(255,255,255,0.15); 
                    padding: 1.5rem; border-radius: 15px; color: white;
                    backdrop-filter: blur(10px);'>
            <p style='line-height: 1.8; font-size: 0.95rem;'>
                This AI-powered platform monitors school meal program quality using 
                intelligent rule-based assessment and real-time MySQL database integration 
                to ensure every student receives quality nutrition.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style='background-color: rgba(255,255,255,0.15); 
                    padding: 1.5rem; border-radius: 15px; color: white;
                    backdrop-filter: blur(10px);'>
            <h3 style='color: white; margin: 0 0 1rem 0; font-weight: 700;'>🎯 Quality Criteria</h3>
            <div style='background-color: rgba(255,255,255,0.1); padding: 0.8rem; border-radius: 8px; margin-bottom: 0.5rem;'>
                <strong>🥗 Nutrition:</strong> 30%
            </div>
            <div style='background-color: rgba(255,255,255,0.1); padding: 0.8rem; border-radius: 8px; margin-bottom: 0.5rem;'>
                <strong>🗑️ Waste Management:</strong> 25%
            </div>
            <div style='background-color: rgba(255,255,255,0.1); padding: 0.8rem; border-radius: 8px; margin-bottom: 0.5rem;'>
                <strong>🧼 Hygiene Standards:</strong> 25%
            </div>
            <div style='background-color: rgba(255,255,255,0.1); padding: 0.8rem; border-radius: 8px; margin-bottom: 0.5rem;'>
                <strong>😋 Taste Quality:</strong> 15%
            </div>
            <div style='background-color: rgba(255,255,255,0.1); padding: 0.8rem; border-radius: 8px;'>
                <strong>📋 Menu Compliance:</strong> 5%
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style='background-color: rgba(255,255,255,0.15); 
                    padding: 1.5rem; border-radius: 15px; color: white;
                    backdrop-filter: blur(10px);'>
            <h3 style='color: white; margin: 0 0 1rem 0; font-weight: 700;'>📊 Grading Scale</h3>
            <div style='background: linear-gradient(135deg, #10b981 0%, #059669 100%); 
                        padding: 1rem; border-radius: 10px; margin-bottom: 0.7rem;'>
                <strong>✅ Excellent</strong><br>
                <span style='font-size: 1.2rem;'>85 - 100 points</span>
            </div>
            <div style='background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); 
                        padding: 1rem; border-radius: 10px; margin-bottom: 0.7rem;'>
                <strong>✅ Good</strong><br>
                <span style='font-size: 1.2rem;'>70 - 84 points</span>
            </div>
            <div style='background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); 
                        padding: 1rem; border-radius: 10px; margin-bottom: 0.7rem;'>
                <strong>⚠️ Fair</strong><br>
                <span style='font-size: 1.2rem;'>50 - 69 points</span>
            </div>
            <div style='background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); 
                        padding: 1rem; border-radius: 10px;'>
                <strong>❌ Poor</strong><br>
                <span style='font-size: 1.2rem;'>0 - 49 points</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Refresh button
    if st.button("🔄 Refresh Data from Database", use_container_width=True):
        st.cache_data.clear()
        st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style='text-align: center; padding: 1rem; 
                    background-color: rgba(255,255,255,0.1); 
                    border-radius: 10px;'>
            <p style='color: rgba(255,255,255,0.8); margin: 0; font-size: 0.85rem;'>
                💾 Data Source: MySQL Database<br>
                🔄 Auto-refresh: Every 5 minutes<br>
                📊 Records: {}<br>
                🏫 Schools: {}
            </p>
        </div>
    """.format(len(df), stats['total_schools']), unsafe_allow_html=True)

# ========================================
# FOOTER
# ========================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
    <div style='text-align: center; padding: 2rem 0; color: #64748b;'>
        <p style='margin: 0; font-size: 0.9rem;'>
            🍽️ School Meal Quality Monitor | Powered by AI & MySQL
        </p>
        <p style='margin: 0.5rem 0 0 0; font-size: 0.85rem;'>
            Ensuring Quality Nutrition for Every Student
        </p>
    </div>
""", unsafe_allow_html=True)