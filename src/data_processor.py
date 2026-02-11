# Just the core processing - no UI yet
import pandas as pd
import numpy as np

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
    
    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        return self.df
    
    def calculate_metrics(self):
        # Waste %
        self.df['Waste_Percentage'] = (self.df['Meals_Leftover'] / self.df['Meals_Served']) * 100
        
        # Calorie Compliance %
        self.df['Calorie_Compliance'] = (self.df['Actual_Calories'] / self.df['Required_Calories']) * 100
        
        # Protein Compliance %
        self.df['Protein_Compliance'] = (self.df['Actual_Protein'] / self.df['Required_Protein']) * 100
        
        # Hygiene Score
        self.df['Hygiene_Score'] = (
            self.df['Kitchen_Cleaned'].astype(int) * 50 +
            self.df['Clean_Water_Available'].astype(int) * 50
        )
        
        return self.df
    
    def get_summary_stats(self):
        stats = {
            'total_schools': self.df['School_ID'].nunique(),
            'total_meals_served': self.df['Meals_Served'].sum(),
            'avg_waste': self.df['Waste_Percentage'].mean(),
            'avg_taste_rating': self.df['Avg_Taste_Rating'].mean()
        }
        return stats