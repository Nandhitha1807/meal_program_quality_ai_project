class QualityAssessment:
    def __init__(self, df):
        self.df = df

    # 🎯 Calculate Individual Scores
    def calculate_overall_quality(self):
        df = self.df.copy()

        # Nutrition Score (average of calorie & protein)
        df['Nutrition_Score'] = (
            (df['Calorie_Compliance'] + df['Protein_Compliance']) / 2
        )

        # Waste Score (lower waste = higher score)
        df['Waste_Score'] = 100 - df['Waste_Percentage']

        # Hygiene Score already calculated (0–100)
        df['Hygiene_Score'] = df['Hygiene_Score']

        # Taste Score (scale to 100)
        df['Taste_Score'] = df['Avg_Taste_Rating'] * 20

        # Menu Score
        df['Menu_Score'] = df['Menu_Followed'].apply(
            lambda x: 100 if x in [1, True, b'\x01'] else 0
        )

        # 🎯 Weighted Overall Score
        df['Overall_Quality_Score'] = (
            df['Nutrition_Score'] * 0.30 +
            df['Waste_Score'] * 0.25 +
            df['Hygiene_Score'] * 0.25 +
            df['Taste_Score'] * 0.15 +
            df['Menu_Score'] * 0.05
        )

        return df

    # 🚨 Generate Alerts
    def generate_alerts(self, df):
        alerts = []

        for _, row in df.iterrows():
            issues = []

            if row['Waste_Percentage'] > 30:
                issues.append("High food waste")

            if row['Calorie_Compliance'] < 90:
                issues.append("Low calorie compliance")

            if row['Protein_Compliance'] < 90:
                issues.append("Low protein compliance")

            if row['Hygiene_Score'] < 100:
                issues.append("Hygiene issue detected")

            if row['Avg_Taste_Rating'] < 3:
                issues.append("Low taste rating")

            if issues:
                alerts.append({
                    "School_ID": row["School_ID"],
                    "Date": row["Date"],
                    "Alerts": issues,
                    "Priority": "High" if len(issues) >= 2 else "Medium"
                })

        return df.__class__(alerts)
