# 🍽️ School Meal Quality Monitor - AI-Powered Assessment System

An intelligent web application for monitoring and assessing school meal program quality using explainable rule-based AI, featuring professional UI/UX design and comprehensive analytics.

## ✨ Key Highlights

- 🤖 **100% Explainable AI** - Rule-based quality scoring system (not a black box)
- 📊 **5-Dimensional Assessment** - Nutrition, Waste, Hygiene, Taste, Menu Compliance
- 🎨 **Professional UI/UX** - Theme-adaptive design that works in both light and dark mode
- 🔐 **Secure Authentication** - SHA256 password hashing with role-based access
- 📈 **Interactive Analytics** - Real-time Plotly visualizations with downloadable reports
- ⚡ **Lightning Fast** - Process and analyze data in under 5 seconds
- 💰 **Zero Hardware Cost** - Runs on any laptop, no cloud infrastructure required

## 🎯 Core Features

### Multi-Page Architecture
- **Landing Page** - Professional hero section with feature showcase
- **Authentication System** - Secure login with session management
- **CSV Upload** - Drag-and-drop file upload with validation
- **AI Processing** - Animated 4-step quality assessment with progress tracking
- **Analytics Dashboard** - Comprehensive KPIs, charts, alerts, and data tables

### Quality Assessment Engine
- **Weighted Scoring Algorithm** - Each dimension contributes based on importance
  - Nutrition: 30% (calorie & protein compliance)
  - Waste Management: 25% (leftover percentage)
  - Hygiene: 25% (kitchen cleanliness & clean water)
  - Taste: 15% (student satisfaction rating)
  - Menu Compliance: 5% (adherence to approved menu)

### Alert System
- **High Priority** - Overall score < 70 OR Waste > 25% OR Hygiene < 75
- **Medium Priority** - Overall score < 85 OR Waste > 15% OR Taste < 3.5
- **Smart Recommendations** - Actionable suggestions for each alert

### Dashboard Visualizations
- **KPI Cards** - Total schools, meals served, average waste, taste rating
- **Compliance Metrics** - Calorie, protein, and overall compliance rates
- **Trend Charts** - Waste trends over time (line chart)
- **Quality Distribution** - Score histogram with radar chart overlay
- **School Rankings** - Horizontal bar chart sorted by performance
- **Nutrition Metrics** - Dual-line chart for calorie and protein compliance

## 🛠️ Technology Stack

**Frontend Framework:**
- Streamlit 1.28.0+ (Python web framework)
- Custom CSS with theme-adaptive design
- Lora + Outfit fonts (professional typography)

**Data Processing:**
- Python 3.10+
- Pandas (data manipulation)
- NumPy (numerical calculations)

**Visualization:**
- Plotly (interactive charts)
- Color-coded data tables with gradients

**Database Support:**
- MySQL connector (optional, code included but not required)
- CSV upload (primary data source)

**Security:**
- SHA256 password hashing
- Streamlit session state management
- Protected route authentication

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- 4GB RAM minimum
- Modern web browser (Chrome, Firefox, Edge)

### Quick Start

**Step 1: Clone Repository**
```bash
git clone <your-repo-url>
cd school-meal-monitor
```

**Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 3: Run Application**
```bash
streamlit run app.py
```

**Step 4: Open Browser**
```
http://localhost:8501
```

**Step 5: Login**
```
Username: admin
Password: admin123
```

That's it! No database setup required for basic usage.

## 📊 Data Format

### Required CSV Columns (14 total)

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| School_ID | Text | Unique school identifier | SCH001 |
| Date | Date | Meal service date (YYYY-MM-DD) | 2024-01-15 |
| Students_Present | Integer | Number of students that day | 150 |
| Meals_Served | Integer | Total meals prepared | 150 |
| Meals_Leftover | Integer | Wasted/leftover meals | 20 |
| Required_Calories | Integer | Target calories per meal | 2000 |
| Actual_Calories | Integer | Actual calories provided | 1950 |
| Required_Protein | Integer | Target protein in grams | 50 |
| Actual_Protein | Integer | Actual protein provided (g) | 48 |
| Meals_Taken | Integer | Meals consumed by students | 130 |
| Avg_Taste_Rating | Decimal | Student rating (1.0-5.0) | 4.2 |
| Kitchen_Cleaned | Boolean | Was kitchen cleaned? | True |
| Clean_Water_Available | Boolean | Was clean water available? | True |
| Menu_Followed | Boolean | Was approved menu followed? | True |

### Download Template
A CSV template with column descriptions is available within the app under the Upload page.

## 🎨 Design Features

### Theme Compatibility
- Automatically adapts to your device's light/dark theme preference
- No forced backgrounds - respects user preferences
- Semi-transparent surfaces that work on any background
- High-contrast text colors visible in both themes

### Professional Typography
- **Display Font**: Lora (serif) for headings and KPI values
- **Body Font**: Outfit (sans-serif) for content and labels
- Font weights: 300-800 for proper hierarchy

### Color System
- **Primary**: #2563eb (Blue) - Used for buttons, active states
- **Success**: #059669 (Green) - Used for compliance indicators
- **Warning**: #d97706 (Amber) - Used for medium priority alerts
- **Danger**: #dc2626 (Red) - Used for high priority alerts
- **Surfaces**: rgba(120,120,120,0.06) - Semi-transparent, theme-adaptive

### Animations
- Smooth hover effects (translateY, scale)
- Progress bar animations during processing
- Step-by-step status transitions (pending → running → done)

## 🚀 Usage Guide

### 1. Upload Data
1. Click "Get Started" or "Sign In" from landing page
2. Login with credentials (admin / admin123)
3. Navigate to Upload page
4. Drag and drop CSV file or click to browse
5. Preview data and click "Proceed to Analysis"

### 2. AI Processing
- Watch 4 animated steps:
  - Step 1: Loading data from file
  - Step 2: Calculating derived metrics (waste %, compliance %)
  - Step 3: AI quality assessment across 5 dimensions
  - Step 4: Generating alerts and recommendations
- Progress bar shows real-time status

### 3. View Dashboard
- **Top Section**: 4 KPI gradient cards
- **Nutrition**: 3 compliance metric cards
- **Alerts**: High/Medium/Total priority statistics
- **Charts**: 4 tabs with interactive visualizations
- **Data Table**: Filterable records with color gradient
- **Downloads**: Export filtered or full CSV reports

### 4. Filter and Explore
- Use score slider to filter by minimum quality score
- Multi-select schools to compare
- Click on charts to interact
- Hover over data points for details

### 5. Download Reports
- Click "Download Filtered Report" for current view
- Click "Download Full Dataset" for complete data
- Files include timestamp in filename

## 📈 Quality Grading Scale

| Grade | Score Range | Color | Meaning |
|-------|-------------|-------|---------|
| 🟢 Excellent | 85 - 100 | Green | Outstanding performance |
| 🔵 Good | 70 - 84 | Blue | Acceptable performance |
| 🟡 Fair | 50 - 69 | Amber | Needs improvement |
| 🔴 Poor | 0 - 49 | Red | Urgent attention required |

## 📁 Project Structure

```
school-meal-monitor/
│
├── app.py                          # Landing page with hero and features
│
├── pages/                          # Multi-page application
│   ├── 1_login.py                 # Authentication page
│   ├── 2_upload_data.py           # CSV upload with validation
│   ├── 3_processing.py            # Animated AI processing
│   └── 4_dashboard.py             # Analytics dashboard
│
├── src/                            # Core functionality
│   ├── auth.py                    # Authentication & session management
│   ├── data_processor.py          # Metrics calculation
│   ├── visualizations.py          # Plotly chart generation
│   ├── styles.py                  # Shared CSS design system
│   ├── db_connection.py           # MySQL connector (optional)
│   └── db_loader.py               # Database loader (optional)
│
├── models/                         # AI engine
│   └── quality_rules.py           # 5-dimension quality scoring
│
├── data/                           # User data
│   ├── users.json                 # User credentials (SHA256 hashed)
│   └── school_meal_data.xlsx      # Sample data (optional)
│
├── requirements.txt                # Python dependencies
├── .env.example                    # Database config template
├── .gitignore                      # Git exclusions
└── README.md                       # This file
```

## 🔒 Security Features

- ✅ **Password Hashing** - SHA256 encryption (no plaintext storage)
- ✅ **Session Management** - Secure Streamlit session state
- ✅ **Protected Routes** - Authentication check on every page
- ✅ **Logout Everywhere** - Sign out button accessible from all pages
- ✅ **Input Validation** - CSV column verification before processing
- ✅ **No Credential Exposure** - Demo credentials not shown in UI

### User Management
Default user is stored in `data/users.json`:
```json
{
  "admin": {
    "password_hash": "SHA256_hash_here",
    "role": "admin",
    "full_name": "Administrator"
  }
}
```

To add new users, edit this file and generate SHA256 hash of password.

## 🎓 Educational Use

This project demonstrates:
- ✅ Multi-page Streamlit application architecture
- ✅ Session state management
- ✅ Rule-based AI/ML system design
- ✅ Data validation and error handling
- ✅ Professional UI/UX design principles
- ✅ Theme-adaptive CSS techniques
- ✅ Plotly interactive visualizations
- ✅ Pandas data processing workflows
- ✅ Secure authentication implementation

## 🐛 Troubleshooting

**Issue: "Module not found" error**
```bash
pip install --upgrade -r requirements.txt
```

**Issue: Port 8501 already in use**
```bash
streamlit run app.py --server.port 8502
```

**Issue: CSV validation fails**
- Ensure all 14 columns are present
- Check date format is YYYY-MM-DD
- Verify boolean values are True/False (not 1/0)
- Download template from app for reference

**Issue: Charts not displaying**
- Check internet connection (Google Fonts load externally)
- Try different browser
- Clear browser cache

**Issue: Expander showing ".arrow_right" text**
- Ensure you've updated `src/styles.py` to latest version
- Restart Streamlit server after file changes

## 🔄 Optional: MySQL Database Setup

The app works perfectly with CSV uploads only. However, if you want to enable MySQL database loading:

### Create Database
```sql
CREATE DATABASE school_meal_db;
USE school_meal_db;

CREATE TABLE meal_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    School_ID VARCHAR(10) NOT NULL,
    Date DATE NOT NULL,
    Students_Present INT NOT NULL,
    Meals_Served INT NOT NULL,
    Meals_Leftover INT NOT NULL,
    Required_Calories INT NOT NULL,
    Actual_Calories INT NOT NULL,
    Required_Protein INT NOT NULL,
    Actual_Protein INT NOT NULL,
    Meals_Taken INT NOT NULL,
    Avg_Taste_Rating DECIMAL(2,1) NOT NULL,
    Kitchen_Cleaned BOOLEAN NOT NULL,
    Clean_Water_Available BOOLEAN NOT NULL,
    Menu_Followed BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Configure Credentials
Create `.env` file (copy from `.env.example`):
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=school_meal_db
```

### Re-enable in Upload Page
Uncomment MySQL load section in `pages/2_upload_data.py` (currently disabled by default).

## 🤝 Contributing

Contributions are welcome! Suggested enhancements:
- 📅 Date range filter for dashboard
- 🏆 School-to-school comparison feature
- 📊 PDF report export with charts
- 📈 ML-based trend prediction
- 🔍 Advanced search in data table
- 🌐 Multi-language support
- 📧 Email alert notifications

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Developed as an AI-powered school meal quality monitoring solution.

Built with ❤️ using Python, Streamlit, and Plotly.

## 🙏 Acknowledgments

- **Streamlit** - Fast web app framework for data science
- **Plotly** - Interactive visualization library
- **Pandas** - Data manipulation and analysis
- **Google Fonts** - Lora and Outfit typography
- **Anthropic Claude** - Development assistance and code review

---

### 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check troubleshooting section above
- Review the in-app help and template

### 🚀 Quick Links

- [Streamlit Documentation](https://docs.streamlit.io)
- [Plotly Python Guide](https://plotly.com/python/)
- [Pandas User Guide](https://pandas.pydata.org/docs/)

---

**Made with 🍽️ for better school meal programs**

*Last Updated: 2024 | Version 1.0*