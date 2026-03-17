# 🍽️ School Meal Quality Monitor - AI-Powered Assessment System

An intelligent web application for monitoring and assessing school meal program quality using explainable rule-based AI, featuring professional UI/UX design and comprehensive analytics.

## ✨ Key Highlights

- 🤖 **100% Explainable AI** - Rule-based quality scoring system (not a black box)
- 📊 **5-Dimensional Assessment** - Nutrition, Waste, Hygiene, Taste, Menu Compliance
- 🎨 **Professional UI/UX** - Theme-adaptive design that works in both light and dark mode
- 🔐 **Secure Authentication** - SHA256 password hashing with role-based access
- 📈 **Interactive Analytics** - Real-time Plotly visualizations with downloadable reports
- ⚡ **Async Processing** - Background threading keeps server responsive during AI processing
- 🗄️ **Full MySQL Integration** - AI results saved permanently to cloud database after every run
- 🌐 **Live Deployment** - Fully deployed on Streamlit Cloud with cloud MySQL
- 💰 **Zero Hardware Cost** - Runs on any laptop, no cloud infrastructure required

## 🎯 Core Features

### Multi-Page Architecture
- **Landing Page** - Professional hero section with feature showcase
- **Authentication System** - Secure login with session management
- **CSV Upload** - Drag-and-drop file upload with 14-column validation
- **AI Processing** - Animated 5-step quality assessment with live progress tracking
- **Analytics Dashboard** - Comprehensive KPIs, charts, alerts, and data tables
- **DB Viewer** - Admin-only live database verification tool

### Quality Assessment Engine
- **Weighted Scoring Algorithm** - Each dimension contributes based on importance
  - Nutrition: 30% (calorie & protein compliance)
  - Waste Management: 25% (leftover percentage)
  - Hygiene: 25% (kitchen cleanliness & clean water)
  - Taste: 15% (student satisfaction rating)
  - Menu Compliance: 5% (adherence to approved menu)

### Async Processing Pipeline
- AI pipeline runs inside a **background thread** using Python's `threading` module
- Main Streamlit thread stays **free and responsive** during processing
- Shared `progress` dictionary acts as a **message bus** between threads
- UI polls progress every **300ms** and updates live step indicators
- Clean thread handoff using `thread.join()` after completion

### Alert System
- **High Priority** - 2 or more issues detected on the same day
- **Medium Priority** - 1 issue detected
- Issues checked: Waste > 30%, Calorie compliance < 90%, Protein compliance < 90%, Hygiene < 100, Taste < 3
- Alerts saved permanently to MySQL `quality_alerts` table

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

**Async Handling:**
- Python `threading.Thread` (background processing)
- Shared dictionary as inter-thread message bus
- 300ms polling loop for live UI updates

**Visualization:**
- Plotly (interactive charts)
- Color-coded data tables with gradients

**Database:**
- MySQL with 3 tables: `meal_data`, `quality_scores`, `quality_alerts`
- `ON DUPLICATE KEY UPDATE` prevents duplicate records on re-upload
- Results saved automatically after every AI processing run
- Admin DB Viewer page for live database verification
- Cloud MySQL hosted on Clever Cloud

**Security:**
- SHA256 password hashing
- Streamlit session state management
- Protected route authentication
- Environment variables for all credentials

**Deployment:**
- Streamlit Cloud (app hosting)
- Clever Cloud (MySQL database hosting)
- GitHub (version control and CI/CD)

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- MySQL 8.0+ (optional for local development)
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

### 2. AI Processing (5 Steps)
- **Step 1** - Loading data from uploaded file
- **Step 2** - Calculating derived metrics (waste %, compliance %)
- **Step 3** - AI quality assessment across 5 dimensions
- **Step 4** - Generating summary stats and recommendations
- **Step 5** - Saving quality scores and alerts to MySQL database
- All steps run in a background thread — UI updates live every 300ms

### 3. View Dashboard
- **Top Section**: 4 KPI gradient cards
- **Nutrition**: 3 compliance metric cards
- **Alerts**: High/Medium/Total priority statistics
- **Charts**: 4 tabs with interactive visualizations
- **Data Table**: Filterable records with color gradient
- **Downloads**: Export filtered or full CSV reports

### 4. Verify Database (Admin Only)
- Navigate to **DB Viewer** page from sidebar
- Step 1 — Connection test with live MySQL status
- Step 2 — Table existence check with row counts
- Step 3 — Browse full `quality_scores` table with color gradient
- Step 4 — Browse full `quality_alerts` table with priority colors
- Step 5 — Run custom SELECT queries directly against the database

### 5. Filter and Explore
- Use score slider to filter by minimum quality score
- Multi-select schools to compare
- Click on charts to interact
- Hover over data points for details

### 6. Download Reports
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
│   ├── 3_processing.py            # Async AI processing (background thread)
│   ├── 4_dashboard.py             # Analytics dashboard
│   └── 5_db_viewer.py             # Admin DB verification tool
│
├── src/                            # Core functionality
│   ├── auth.py                    # Authentication & session management
│   ├── data_processor.py          # Metrics calculation
│   ├── visualizations.py          # Plotly chart generation
│   ├── styles.py                  # Shared CSS design system
│   ├── db_saver.py                # Saves AI results to cloud MySQL
│   ├── db_connection.py           # MySQL connector
│   └── db_loader.py               # Database loader
│
├── models/                         # AI engine
│   └── quality_rules.py           # 5-dimension rule-based quality scoring
│
├── data/                           # User data
│   └── users.json                 # User credentials (SHA256 hashed)
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
- ✅ **Role-Based Access** - Admin sees all schools; school users see only their own data
- ✅ **DB Viewer Admin Only** - Database verification page restricted to admin role
- ✅ **Environment Variables** - All credentials stored securely, never hardcoded

### User Management
Default users are stored in `data/users.json`:
```json
{
  "admin": {
    "password_hash": "SHA256_hash_here",
    "role": "admin",
    "full_name": "Administrator"
  },
  "sch001": {
    "password_hash": "SHA256_hash_here",
    "role": "school",
    "full_name": "School 001 Manager",
    "school_id": "SCH001"
  }
}
```

## 🗄️ MySQL Database Setup

### Tables Created

```sql
-- Raw meal data from CSV uploads
CREATE TABLE IF NOT EXISTS meal_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    School_ID VARCHAR(20) NOT NULL,
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

-- AI-generated quality scores (saved automatically after processing)
CREATE TABLE IF NOT EXISTS quality_scores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    School_ID VARCHAR(20) NOT NULL,
    Date DATE NOT NULL,
    Overall_Quality_Score DECIMAL(6,4) NOT NULL,
    Nutrition_Score DECIMAL(6,4) NOT NULL,
    Waste_Score DECIMAL(6,4) NOT NULL,
    Hygiene_Score DECIMAL(6,4) NOT NULL,
    Taste_Score DECIMAL(6,4) NOT NULL,
    Menu_Score DECIMAL(6,4) NOT NULL,
    Uploaded_By VARCHAR(50) DEFAULT 'admin',
    Processed_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY uq_school_date (School_ID, Date)
);

-- AI-generated alerts (saved automatically after processing)
CREATE TABLE IF NOT EXISTS quality_alerts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    School_ID VARCHAR(20) NOT NULL,
    Date DATE NOT NULL,
    Alert_Issues TEXT NOT NULL,
    Priority VARCHAR(10) NOT NULL,
    Uploaded_By VARCHAR(50) DEFAULT 'admin',
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY uq_alert_school_date (School_ID, Date)
);
```

### Configure Credentials
Create `.env` file (copy from `.env.example`):
```env
DB_HOST=your_host
DB_PORT=3306
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=your_database
```

### Verify Data is Saved
After processing data in the app, open the **DB Viewer** page (admin login required) to confirm all 3 tables have records.

## ⚡ Async Processing — How It Works

```
Upload CSV
    ↓
Main Thread launches Background Thread
    ↓
┌─────────────────────┐     ┌──────────────────────────────┐
│    MAIN THREAD      │     │      BACKGROUND THREAD       │
│  (server stays free)│     │   (AI pipeline runs here)    │
│                     │     │                              │
│  polls progress     │◄────│  writes step status          │
│  dict every 300ms   │     │  into shared progress dict   │
│                     │     │                              │
│  updates UI live    │     │  Step 1: Load data           │
│  step 1 → done ✅   │     │  Step 2: Calculate metrics   │
│  step 2 → done ✅   │     │  Step 3: AI scoring          │
│  step 3 → running 🔄│     │  Step 4: Summary stats       │
│                     │     │  Step 5: Save to MySQL       │
└─────────────────────┘     └──────────────────────────────┘
    ↓
thread.join() — clean handoff
    ↓
Results loaded into session state
    ↓
Dashboard ready
```

## 🌐 Deployment

This app is fully deployed and live.

### Architecture
```
User Browser
     ↓
Streamlit Cloud (app hosting)
     ↓
Python Backend
  ├── Rule-based AI Engine
  ├── Background Thread (async)
  ├── SHA256 Authentication
  └── pymysql connector
           ↓
    Clever Cloud MySQL
      ├── meal_data
      ├── quality_scores
      └── quality_alerts
```

### Deployment Steps
```
1. Push code to GitHub
2. Connect GitHub repo to Streamlit Cloud
3. Add database credentials in Streamlit Cloud Secrets
4. App auto deploys on every push to main branch
```

### Streamlit Cloud Secrets
```toml
DB_HOST     = "your_cloud_host"
DB_PORT     = "3306"
DB_USER     = "your_user"
DB_PASSWORD = "your_password"
DB_NAME     = "your_database"
```

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

**Issue: DB Viewer shows "Table not found"**
- Run the full SQL from the Database Setup section above
- Check your .env file credentials are correct

**Issue: Step 5 shows "Session Only — DB unavailable"**
- Check database credentials in .env file
- App still works fully — results are in session state
- Fix credentials and re-process to save to DB

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
- **MySQL** - Database storage and retrieval
- **Clever Cloud** - Cloud database hosting
- **Google Fonts** - Lora and Outfit typography
- **Anthropic Claude** - Development assistance and code review

---

**Made with 🍽️ for better school meal programs**

*Last Updated: 2025 | Version 2.0*