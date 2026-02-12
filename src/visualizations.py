import plotly.express as px
import plotly.graph_objects as go

class Visualizer:
    def __init__(self, df):
        self.df = df

    # 📈 Waste Trend Over Time
    def plot_waste_trend(self):
        trend_df = self.df.groupby("Date")["Waste_Percentage"].mean().reset_index()

        fig = px.line(
            trend_df,
            x="Date",
            y="Waste_Percentage",
            title="Average Waste Percentage Over Time",
            markers=True
        )

        return fig

    # 🎯 Quality Distribution
    def plot_quality_distribution(self, quality_df):
        fig = px.histogram(
            quality_df,
            x="Overall_Quality_Score",
            nbins=20,
            title="Distribution of Overall Quality Scores"
        )

        return fig

    # 🏫 School Performance Comparison
    def plot_school_performance(self, quality_df):
        school_avg = quality_df.groupby("School_ID")[
            "Overall_Quality_Score"
        ].mean().reset_index()

        fig = px.bar(
            school_avg,
            x="School_ID",
            y="Overall_Quality_Score",
            title="Average Quality Score by School"
        )

        return fig

    # 🥗 Nutrition Compliance Chart
    def plot_nutrition_compliance(self):
        avg_calorie = self.df["Calorie_Compliance"].mean()
        avg_protein = self.df["Protein_Compliance"].mean()

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=["Calorie Compliance", "Protein Compliance"],
            y=[avg_calorie, avg_protein]
        ))

        fig.update_layout(
            title="Average Nutrition Compliance"
        )

        return fig

    # 📊 Radar Chart for Metrics
    def plot_metrics_radar(self, quality_df):
        avg_values = quality_df[[
            "Nutrition_Score",
            "Waste_Score",
            "Hygiene_Score",
            "Taste_Score",
            "Menu_Score"
        ]].mean()

        categories = list(avg_values.index)

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=avg_values.values,
            theta=categories,
            fill='toself'
        ))

        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            title="Average Quality Metrics Radar"
        )

        return fig
