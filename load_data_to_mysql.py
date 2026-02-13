"""
Load sample data from CSV into MySQL database
Run this ONCE after creating the table in MySQL Workbench
"""

import mysql.connector
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

print("🔄 Starting data load process...")

# Step 1: Generate sample data if doesn't exist
if not os.path.exists('sample_meal_data.csv'):
    print("📊 Generating sample data...")
    import generate_sample_data
    print("✅ Sample data generated!")

# Step 2: Load CSV
print("📖 Reading CSV file...")
df = pd.read_csv('sample_meal_data.csv')
print(f"✅ Loaded {len(df)} records from CSV")

# Step 3: Connect to MySQL
print("🔌 Connecting to MySQL...")
try:
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = conn.cursor()
    print("✅ Connected to MySQL!")
except Exception as e:
    print(f"❌ Connection failed: {e}")
    exit()

# Step 4: Clear existing data (optional - remove if you want to keep old data)
print("🗑️ Clearing existing data...")
cursor.execute("DELETE FROM meal_data")
conn.commit()
print("✅ Existing data cleared!")

# Step 5: Insert data
print("💾 Inserting data into MySQL...")

insert_query = """
INSERT INTO meal_data 
(School_ID, Date, Students_Present, Meals_Served, Meals_Leftover, 
 Required_Calories, Actual_Calories, Required_Protein, Actual_Protein, 
 Meals_Taken, Avg_Taste_Rating, Kitchen_Cleaned, Clean_Water_Available, 
 Menu_Followed)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

success_count = 0
error_count = 0

for index, row in df.iterrows():
    try:
        values = (
            row['School_ID'],
            row['Date'],
            int(row['Students_Present']),
            int(row['Meals_Served']),
            int(row['Meals_Leftover']),
            int(row['Required_Calories']),
            int(row['Actual_Calories']),
            int(row['Required_Protein']),
            int(row['Actual_Protein']),
            int(row['Meals_Taken']),
            float(row['Avg_Taste_Rating']),
            bool(row['Kitchen_Cleaned']),
            bool(row['Clean_Water_Available']),
            bool(row['Menu_Followed'])
        )
        
        cursor.execute(insert_query, values)
        success_count += 1
        
        # Show progress every 50 records
        if (index + 1) % 50 == 0:
            print(f"   Processed {index + 1}/{len(df)} records...")
            
    except Exception as e:
        error_count += 1
        print(f"❌ Error on row {index + 1}: {e}")

# Step 6: Commit changes
conn.commit()
print(f"\n✅ Successfully inserted {success_count} records!")

if error_count > 0:
    print(f"⚠️ Failed to insert {error_count} records")

# Step 7: Verify data
cursor.execute("SELECT COUNT(*) FROM meal_data")
total_records = cursor.fetchone()[0]
print(f"📊 Total records in database: {total_records}")

# Step 8: Show sample data
print("\n📋 Sample data from database:")
cursor.execute("SELECT * FROM meal_data LIMIT 5")
sample_records = cursor.fetchall()

for record in sample_records:
    print(f"   {record[1]} | {record[2]} | Waste: {record[5]} meals")

# Close connection
cursor.close()
conn.close()

print("\n🎉 Data load complete! You can now run: streamlit run app.py")