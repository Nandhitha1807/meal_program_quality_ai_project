import pandas as pd

class DataProcessor:
    def __init__(self, df=None):
        self.df = df

    def calculate_metrics(self):
        if self.df is None:
            raise ValueError("DataFrame is empty. Please load data first.")

        # Waste Percentage
        self.df['Waste_Percentage'] = (
            self.df['Meals_Leftover'] / self.df['Meals_Served']
        ) * 100

        # Calorie Compliance
        self.df['Calorie_Compliance'] = (
            self.df['Actual_Calories'] / self.df['Required_Calories']
        ) * 100

        # Protein Compliance
        self.df['Protein_Compliance'] = (
            self.df['Actual_Protein'] / self.df['Required_Protein']
        ) * 100

        # 🔥 SAFE BOOLEAN CONVERSION
        self.df['Kitchen_Cleaned'] = self.df['Kitchen_Cleaned'].apply(lambda x: 1 if x in [1, True, b'\x01'] else 0)
        self.df['Clean_Water_Available'] = self.df['Clean_Water_Available'].apply(lambda x: 1 if x in [1, True, b'\x01'] else 0)

        # Hygiene Score
        self.df['Hygiene_Score'] = (
            self.df['Kitchen_Cleaned'] * 50 +
            self.df['Clean_Water_Available'] * 50
        )

        return self.df

    def get_summary_stats(self):
        stats = {
            'total_schools': self.df['School_ID'].nunique(),
            'total_meals_served': self.df['Meals_Served'].sum(),
            'avg_waste': self.df['Waste_Percentage'].mean(),
            'avg_taste_rating': self.df['Avg_Taste_Rating'].mean(),
            'avg_calorie_compliance': self.df['Calorie_Compliance'].mean(),
            'avg_protein_compliance': self.df['Protein_Compliance'].mean()
        }
        return stats
