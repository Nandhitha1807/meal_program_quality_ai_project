# Demo script to show it works
from src.db_loader import load_data_from_db
from src.data_processor import DataProcessor

df = load_data_from_db()
processor = DataProcessor(df=df)

df = processor.calculate_metrics()

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