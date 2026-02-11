import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

data = []
for i in range(150):
    data.append({
        'School_ID': f'SCH{np.random.randint(1, 11):03d}',
        'Date': (datetime(2024, 1, 1) + timedelta(days=i % 30)).strftime('%Y-%m-%d'),
        'Students_Present': np.random.randint(80, 200),
        'Meals_Served': np.random.randint(80, 200),
        'Meals_Leftover': np.random.randint(5, 40),
        'Required_Calories': 2000,
        'Actual_Calories': np.random.randint(1800, 2200),
        'Required_Protein': 50,
        'Actual_Protein': np.random.randint(40, 60),
        'Meals_Taken': np.random.randint(70, 190),
        'Avg_Taste_Rating': round(np.random.uniform(2.5, 5.0), 1),
        'Kitchen_Cleaned': np.random.choice([True, False], p=[0.9, 0.1]),
        'Clean_Water_Available': np.random.choice([True, False], p=[0.95, 0.05]),
        'Menu_Followed': np.random.choice([True, False], p=[0.85, 0.15])
    })

df = pd.DataFrame(data)
df.to_csv('sample_meal_data.csv', index=False)
print(f"✅ Generated {len(df)} records")