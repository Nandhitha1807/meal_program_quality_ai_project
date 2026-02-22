# 🍽️ AI-Based School Meal Program Quality Monitoring System

An intelligent platform for monitoring and assessing school meal program quality using rule-based AI and MySQL database integration.

## 🎯 Features

- **Multi-Dimensional Quality Assessment**: Evaluates waste, nutrition, hygiene, taste, and menu compliance
- **AI-Powered Alerts**: Automatically identifies schools requiring attention
- **Interactive Dashboard**: Real-time visualizations and analytics
- **MySQL Database**: Professional data storage and retrieval
- **Comprehensive Reporting**: Downloadable CSV reports
- **Smart Recommendations**: Actionable suggestions for improvement

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Backend**: Python, Pandas, NumPy
- **AI Engine**: Rule-based quality assessment system
- **Database**: MySQL
- **Visualization**: Plotly
- **Environment**: python-dotenv

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- MySQL Server 8.0 or higher

### Step 1: Clone Repository
```bash
git clone <your-repo-url>
cd school-meal-monitor
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure Database
1. Create `.env` file (copy from `.env.example`)
2. Update MySQL credentials:
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=school_meal_db
```

### Step 4: Create Database Table
Run this SQL in MySQL Workbench:
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

### Step 5: Load Sample Data
```bash
python load_data_to_mysql.py
```

## 🚀 Usage

### Run Application
```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

### Test Data Processing
```bash
python test_processor.py
```

## 📊 Data Format

Your meal data should include:

- `School_ID`: Unique school identifier
- `Date`: Date of meal service
- `Students_Present`: Number of students
- `Meals_Served`: Total meals prepared
- `Meals_Leftover`: Wasted meals
- `Required_Calories`: Target calories per meal
- `Actual_Calories`: Actual calories served
- `Required_Protein`: Target protein (grams)
- `Actual_Protein`: Actual protein served (grams)
- `Meals_Taken`: Meals consumed
- `Avg_Taste_Rating`: Student rating (1-5)
- `Kitchen_Cleaned`: Boolean (True/False)
- `Clean_Water_Available`: Boolean (True/False)
- `Menu_Followed`: Boolean (True/False)

## 🎯 Quality Assessment Criteria

The system evaluates meals across 5 dimensions:

- **Nutrition** (30%): Calorie and protein compliance
- **Waste Management** (25%): Food waste percentage
- **Hygiene** (25%): Kitchen cleanliness and water availability
- **Taste** (15%): Student satisfaction ratings
- **Menu Compliance** (5%): Adherence to approved menu

## 📈 Quality Grading

- **Excellent**: 85-100 points
- **Good**: 70-84 points
- **Fair**: 50-69 points
- **Poor**: 0-49 points

## 📁 Project Structure
```
school-meal-monitor/
├── data/                      # Data storage
├── src/                       # Source code
│   ├── db_connection.py      # MySQL connection
│   ├── db_loader.py          # Data loading
│   ├── data_processor.py     # Data processing
│   └── visualizations.py     # Chart generation
├── models/                    # AI models
│   └── quality_rules.py      # Quality assessment rules
├── .env                       # Database credentials (not in git)
├── .env.example              # Template for .env
├── .gitignore                # Git ignore file
├── app.py                     # Main application
├── requirements.txt           # Dependencies
├── generate_sample_data.py   # Sample data generator
├── load_data_to_mysql.py     # Load data to MySQL
├── test_processor.py         # Test script
└── README.md                  # Documentation
```

## 🔒 Security

- Never commit `.env` file to version control
- Keep MySQL credentials secure
- Use strong passwords
- Regularly update dependencies

## 👥 Contributors

- Your Name - Developer

## 📄 License

This project is licensed under the MIT License.

## 🤝 Acknowledgments

- Built with Streamlit and Plotly
- Developed for school meal quality assessment
- AI-powered rule-based system