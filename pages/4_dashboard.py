"""
Page 4: Dashboard - Complete Analytics View
"""

import streamlit as st
import sys
from pathlib import Path
import pandas as pd

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from src.visualizations import Visualizer
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

# Check if processing is complete
if 'processing_complete' not in st.session_state or not st.session_state['processing_complete']:
    st.error("❌ Please process data first!")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📤 Go to Upload", use_container_width=True):
            st.switch_page("pages/2_upload_data.py")
    with col2:
        if st.button("⏳ Go to Processing", use_container_width=True):
            st.switch_page("pages/3_processing.py")
    st.stop()

# Load data from session state
df = st.session_state['df_processed']
quality_df = st.session_state['quality_df']
alerts_df = st.session_state['alerts_df']
stats = st.session_state['stats']

# ========================================
# PAGE CONFIGURATION
# ========================================
st.set_page_config(
    page_title="Dashboard - School Meal Monitor",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========================================
# CUSTOM CSS
# ========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        padding: 0rem 1rem;
        background-color: #f8fafc;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
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
        st.success("Logged out!")
        st.switch_page("pages/1_login.py")
    
    st.markdown("---")
    
    st.markdown("### 📍 Current Page")
    st.success("**Dashboard**")
    
    st.markdown("### 🔄 Navigation")
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")
    if st.button("📤 Upload New Data", use_container_width=True):
        # Clear session state
        for key in ['data_loaded', 'processing_complete', 'meal_data', 'df_processed', 'quality_df', 'alerts_df', 'stats']:
            if key in st.session_state:
                del st.session_state[key]
        st.switch_page("pages/2_upload_data.py")
    
    st.markdown("---")
    
    st.markdown(f"""
        <div style='background-color: #f3f4f6; padding: 1rem; border-radius: 10px;'>
            <h3 style='margin: 0 0 0.5rem 0;'>📊 Data Summary</h3>
            <p style='margin: 0;'>Records: {len(df)}</p>
            <p style='margin: 0;'>Schools: {stats['total_schools']}</p>
            <p style='margin: 0;'>Alerts: {len(alerts_df)}</p>
            <p style='margin: 0;'>Source: {st.session_state.get('data_source', 'Unknown')}</p>
        </div>
    """, unsafe_allow_html=True)

# ========================================
# HEADER
# ========================================
st.markdown("""
    <div style='text-align: center; padding: 2rem 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 20px; margin-bottom: 2rem; box-shadow: 0 10px 25px rgba(0,0,0,0.1);'>
        <h1 style='color: white; margin: 0; font-size: 3rem;'>📊 Quality Assessment Dashboard</h1>
        <p style='color: rgba(255,255,255,0.9); font-size: 1.2rem; margin: 0.5rem 0 0 0;'>
            Real-time Analytics & Insights
        </p>
    </div>
""", unsafe_allow_html=True)

# ========================================
# KPI SECTION
# ========================================
st.markdown("## 📊 Key Performance Indicators")
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 2rem 1.5rem; border-radius: 20px; color: white; 
                    box-shadow: 0 10px 20px rgba(102,126,234,0.3);'>
            <p style='margin: 0; font-size: 0.9rem; opacity: 0.9; font-weight: 600;'>🏫 TOTAL SCHOOLS</p>
            <h1 style='margin: 0.5rem 0 0 0; color: white; font-size: 3rem;'>{stats['total_schools']}</h1>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                    padding: 2rem 1.5rem; border-radius: 20px; color: white; 
                    box-shadow: 0 10px 20px rgba(240,147,251,0.3);'>
            <p style='margin: 0; font-size: 0.9rem; opacity: 0.9; font-weight: 600;'>🍽️ MEALS SERVED</p>
            <h1 style='margin: 0.5rem 0 0 0; color: white; font-size: 3rem;'>{stats['total_meals_served']:,}</h1>
        </div>
    """, unsafe_allow_html=True)

with col3:
    waste_gradient = "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)" if stats['avg_waste'] > 20 else "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)"
    st.markdown(f"""
        <div style='background: {waste_gradient}; 
                    padding: 2rem 1.5rem; border-radius: 20px; color: white; 
                    box-shadow: 0 10px 20px rgba(79,172,254,0.3);'>
            <p style='margin: 0; font-size: 0.9rem; opacity: 0.9; font-weight: 600;'>🗑️ AVG WASTE</p>
            <h1 style='margin: 0.5rem 0 0 0; color: white; font-size: 3rem;'>{stats['avg_waste']:.1f}%</h1>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div style='background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); 
                    padding: 2rem 1.5rem; border-radius: 20px; color: white; 
                    box-shadow: 0 10px 20px rgba(250,112,154,0.3);'>
            <p style='margin: 0; font-size: 0.9rem; opacity: 0.9; font-weight: 600;'>⭐ AVG TASTE</p>
            <h1 style='margin: 0.5rem 0 0 0; color: white; font-size: 3rem;'>{stats['avg_taste_rating']:.1f}</h1>
            <p style='margin: 0; font-size: 0.8rem; opacity: 0.8;'>out of 5.0</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ========================================
# NUTRITION OVERVIEW
# ========================================
st.markdown("## 🎯 Nutritional Compliance Overview")
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    cal_status = "✅ On Target" if stats['avg_calorie_compliance'] >= 95 else "⚠️ Below Target"
    st.markdown(f"""
        <div style='background-color: #ecfdf5; padding: 2rem; 
                    border-radius: 15px; border-left: 6px solid #10b981;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.05);'>
            <h4 style='color: #065f46; margin: 0; font-size: 0.9rem; font-weight: 700;'>
                CALORIE COMPLIANCE
            </h4>
            <h1 style='color: #047857; margin: 1rem 0; font-size: 3rem;'>{stats['avg_calorie_compliance']:.1f}%</h1>
            <p style='color: #059669; margin: 0; font-weight: 600;'>{cal_status}</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    prot_status = "✅ On Target" if stats['avg_protein_compliance'] >= 95 else "⚠️ Below Target"
    st.markdown(f"""
        <div style='background-color: #fef3c7; padding: 2rem; 
                    border-radius: 15px; border-left: 6px solid #f59e0b;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.05);'>
            <h4 style='color: #92400e; margin: 0; font-size: 0.9rem; font-weight: 700;'>
                PROTEIN COMPLIANCE
            </h4>
            <h1 style='color: #d97706; margin: 1rem 0; font-size: 3rem;'>{stats['avg_protein_compliance']:.1f}%</h1>
            <p style='color: #b45309; margin: 0; font-weight: 600;'>{prot_status}</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    excellent_count = len(quality_df[quality_df['Overall_Quality_Score'] >= 85])
    excellence_rate = (excellent_count / stats['total_schools']) * 100 if stats['total_schools'] > 0 else 0
    st.markdown(f"""
        <div style='background-color: #dbeafe; padding: 2rem; 
                    border-radius: 15px; border-left: 6px solid #3b82f6;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.05);'>
            <h4 style='color: #1e3a8a; margin: 0; font-size: 0.9rem; font-weight: 700;'>
                EXCELLENT SCHOOLS
            </h4>
            <h1 style='color: #2563eb; margin: 1rem 0; font-size: 3rem;'>{excellent_count}</h1>
            <p style='color: #1d4ed8; margin: 0; font-weight: 600;'>{excellence_rate:.0f}% of total</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")

# ========================================
# ALERTS SECTION
# ========================================
st.markdown("## 🚨 AI-Generated Quality Alerts")
st.markdown("<br>", unsafe_allow_html=True)

if not alerts_df.empty:
    high_priority = len(alerts_df[alerts_df['Priority'] == 'High'])
    medium_priority = len(alerts_df[alerts_df['Priority'] == 'Medium'])
    
    col1, col2, col3 = st.columns(3)
    
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
    
    # Alert Details
    with st.expander(f"📋 View All {len(alerts_df)} Alert Details", expanded=False):
        for idx, alert in alerts_df.head(15).iterrows():
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
    st.success("✅ No Critical Alerts - All Schools Performing Well!")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")

# ========================================
# VISUALIZATIONS
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
    st.info("💡 **Insight:** Monitor waste trends to identify patterns and implement targeted interventions.")

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
# DATA TABLE
# ========================================
st.markdown("## 📋 Detailed Quality Assessment Data")
st.markdown("<br>", unsafe_allow_html=True)

# Filters
col1, col2, col3 = st.columns(3)

with col1:
    min_score = st.slider(
        "🎯 Minimum Quality Score",
        min_value=0,
        max_value=100,
        value=0,
        step=5
    )

with col2:
    selected_schools = st.multiselect(
        "🏫 Select Schools",
        options=sorted(quality_df['School_ID'].unique()),
        default=sorted(quality_df['School_ID'].unique())
    )

with col3:
    date_range = st.selectbox(
        "📅 Date Range",
        options=["All Dates", "Last 7 Days", "Last 30 Days"]
    )

# Apply filters
filtered_df = quality_df[
    (quality_df['Overall_Quality_Score'] >= min_score) &
    (quality_df['School_ID'].isin(selected_schools))
]

st.markdown(f"""
    <div style='background-color: #f3f4f6; padding: 1rem; border-radius: 10px; margin: 1rem 0;'>
        <p style='margin: 0; color: #374151; font-weight: 600;'>
            📊 Showing {len(filtered_df)} of {len(quality_df)} total records
        </p>
    </div>
""", unsafe_allow_html=True)

# Display table
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

# Download buttons
st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Data (CSV)",
        data=csv,
        file_name=f"quality_report_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv",
        use_container_width=True
    )

with col2:
    csv_full = quality_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download All Data (CSV)",
        data=csv_full,
        file_name=f"complete_report_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv",
        use_container_width=True
    )

st.markdown("<br><br>", unsafe_allow_html=True)

# Footer
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