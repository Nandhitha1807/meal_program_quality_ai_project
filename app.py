import streamlit as st
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent))

from src.db_loader import load_data_from_db
from src.data_processor import DataProcessor
from src.visualizations import Visualizer
from models.quality_rules import QualityAssessment

# Page config
st.set_page_config(
    page_title="School Meal Quality Monitor",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ AI-Based School Meal Program Quality Monitor")
st.markdown("---")

# Load from MySQL
with st.spinner("Loading data from database..."):
    df = load_data_from_db()
    processor = DataProcessor(df=df)
    df = processor.calculate_metrics()

    quality_checker = QualityAssessment(df)
    quality_df = quality_checker.calculate_overall_quality()
    alerts_df = quality_checker.generate_alerts(quality_df)

    stats = processor.get_summary_stats()

st.success("✅ Data loaded and processed successfully!")

# KPI Section
st.subheader("📊 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Schools", stats['total_schools'])

with col2:
    st.metric("Total Meals Served", f"{stats['total_meals_served']:,}")

with col3:
    st.metric("Avg Waste %", f"{stats['avg_waste']:.1f}%")

with col4:
    st.metric("Avg Taste Rating", f"{stats['avg_taste_rating']:.2f}/5")

st.markdown("---")

# Nutrition Overview
st.subheader("🎯 Nutrition Overview")
col1, col2 = st.columns(2)

with col1:
    st.metric("Avg Calorie Compliance", f"{stats['avg_calorie_compliance']:.1f}%")

with col2:
    st.metric("Avg Protein Compliance", f"{stats['avg_protein_compliance']:.1f}%")

st.markdown("---")

# Alerts
if not alerts_df.empty:
    st.subheader("🚨 Active Alerts")
    st.warning(f"Found {len(alerts_df)} schools requiring attention")

    for idx, alert in alerts_df.iterrows():
        with st.expander(f"School ID: {alert['School_ID']} - Priority: {alert['Priority']}"):
            st.write(f"**Date:** {alert['Date']}")
            st.write("**Issues:**")
            for issue in alert['Alerts']:
                st.write(issue)
else:
    st.success("✅ No critical alerts - All schools performing well!")

st.markdown("---")

# Visualizations
st.subheader("📈 Analytics & Visualizations")
visualizer = Visualizer(df)

tab1, tab2, tab3, tab4 = st.tabs(
    ["Trends", "Quality Distribution", "School Performance", "Nutrition"]
)

with tab1:
    st.plotly_chart(visualizer.plot_waste_trend(), use_container_width=True)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(
            visualizer.plot_quality_distribution(quality_df),
            use_container_width=True
        )
    with col2:
        st.plotly_chart(
            visualizer.plot_metrics_radar(quality_df),
            use_container_width=True
        )

with tab3:
    st.plotly_chart(
        visualizer.plot_school_performance(quality_df),
        use_container_width=True
    )

with tab4:
    st.plotly_chart(
        visualizer.plot_nutrition_compliance(),
        use_container_width=True
    )

st.markdown("---")

# Data Table
st.subheader("📋 Detailed Data")
st.dataframe(quality_df, use_container_width=True)

# Sidebar
with st.sidebar:
    st.header("About")
    st.write("""
    This AI-based platform monitors school meal program quality using 
    rule-based assessment and MySQL database integration.
    """)

    st.header("Quality Criteria")
    st.write("""
    Nutrition: 30%  
    Waste: 25%  
    Hygiene: 25%  
    Taste: 15%  
    Menu Compliance: 5%
    """)
