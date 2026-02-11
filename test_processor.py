# Demo script to show it works
from src.data_processor import DataProcessor

# Test with sample data
processor = DataProcessor('sample_meal_data.csv')
df = processor.load_data()
print("✅ Data loaded successfully!")
print(f"Records: {len(df)}")

# Calculate metrics
df = processor.calculate_metrics()
print("\n✅ Metrics calculated!")
print(df[['School_ID', 'Waste_Percentage', 'Calorie_Compliance']].head())

# Get summary
stats = processor.get_summary_stats()
print("\n✅ Summary Statistics:")
for key, value in stats.items():
    print(f"  {key}: {value}")