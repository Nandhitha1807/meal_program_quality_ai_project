# 🍽️ AI-Based School Meal Program Quality Monitor

An intelligent platform for monitoring and assessing school meal program quality using rule-based AI.

## Features
- 📊 Real-time quality assessment
- 🚨 Automated alerts for quality issues
- 📈 Trend analysis and visualizations
- 🏫 School-wise performance tracking
- 📋 Comprehensive reporting

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
streamlit run app.py
```

## Data Format
Your CSV should contain these columns:
- School_ID, Date, Students_Present, Meals_Served, Meals_Leftover
- Required_Calories, Actual_Calories, Required_Protein, Actual_Protein
- Meals_Taken, Avg_Taste_Rating, Kitchen_Cleaned, Clean_Water_Available, Menu_Followed

## Quality Assessment
The system evaluates:
- Waste Management (25%)
- Nutritional Compliance (30%)
- Hygiene Standards (25%)
- Taste Quality (15%)
- Menu Compliance (5%)