import streamlit as st
import pandas as pd
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent))

from src.data_processor import DataProcessor
from src.visualizations import Visualizer
from models.quality_rules import QualityAssessment

# Page configuration
st.set_page_config(
    page_title="School Meal Quality Monitor",
    page_icon="🍽️",
    layout="wide"
)

# Title
st.title("🍽️ AI-Based School Meal Program Quality Monitor")
st.markdown("---")

# File uploader
uploaded_file = st.file_uploader("Upload your school meal data (CSV)", type=['csv'])

if uploaded_file is not None:
    # Process data
    with st.spinner("Processing data..."):
        # Save uploaded file temporarily
        with open("data/temp_data.csv", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Initialize processor
        processor = DataProcessor("data/temp_data.csv")
        df = processor.calculate_metrics()
        
        # Quality assessment
        quality_checker = QualityAssessment(df)
        quality_df = quality_checker.calculate_overall_quality()
        alerts_df = quality_checker.generate_alerts(quality_df)
        
        # Get summary stats
        stats = processor.get_summary_stats()
    
    # Dashboard Layout
    st.success("✅ Data processed successfully!")
    
    # Key Metrics Row
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
    
    # Quality Overview
    st.subheader("🎯 Quality Overview")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Avg Calorie Compliance", f"{stats['avg_calorie_compliance']:.1f}%")
    with col2:
        st.metric("Avg Protein Compliance", f"{stats['avg_protein_compliance']:.1f}%")
    
    st.markdown("---")
    
    # Alerts Section
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
    
    # Tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs(["Trends", "Quality Distribution", "School Performance", "Nutrition"])
    
    with tab1:
        st.plotly_chart(visualizer.plot_waste_trend(), use_container_width=True)
    
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(visualizer.plot_quality_distribution(quality_df), use_container_width=True)
        with col2:
            st.plotly_chart(visualizer.plot_metrics_radar(quality_df), use_container_width=True)
    
    with tab3:
        st.plotly_chart(visualizer.plot_school_performance(quality_df), use_container_width=True)
    
    with tab4:
        st.plotly_chart(visualizer.plot_nutrition_compliance(), use_container_width=True)
    
    st.markdown("---")
    
    # Data Tables
    st.subheader("📋 Detailed Data")
    
    tab1, tab2 = st.tabs(["Quality Scores", "Raw Data"])
    
    with tab1:
        st.dataframe(quality_df, use_container_width=True)
        
        # Download button
        csv = quality_df.to_csv(index=False)
        st.download_button(
            label="Download Quality Report",
            data=csv,
            file_name="quality_report.csv",
            mime="text/csv"
        )
    
    with tab2:
        st.dataframe(df, use_container_width=True)

else:
    st.info("👆 Please upload your school meal data CSV file to begin analysis")
    
    # Show expected format
    st.subheader("Expected Data Format")
    sample_data = pd.DataFrame({
        'School_ID': ['SCH001', 'SCH002'],
        'Date': ['2024-01-01', '2024-01-01'],
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
    st.dataframe(sample_data)

# Sidebar
with st.sidebar:
    st.header("About")
    st.write("""
    This AI-based platform monitors school meal program quality using rule-based assessment.
    
    **Features:**
    - Quality scoring across multiple dimensions
    - Real-time alerts for issues
    - Trend analysis
    - School performance comparison
    """)
    
    st.header("Quality Criteria")
    st.write("""
    **Weights:**
    - Nutrition: 30%
    - Waste: 25%
    - Hygiene: 25%
    - Taste: 15%
    - Menu Compliance: 5%
    """)