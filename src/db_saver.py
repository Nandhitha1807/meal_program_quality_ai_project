"""
src/db_saver.py — Save AI Processing Results to MySQL
Uses pymysql (works on Streamlit Cloud) instead of mysql-connector-python.
Saves quality_scores and alerts to the database after processing.
"""

import pymysql
import pymysql.cursors
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()


def get_connection():
    """
    Create and return a MySQL connection using pymysql.
    Works both locally (.env) and on Streamlit Cloud (st.secrets).
    """
    try:
        # Try Streamlit secrets first — used when deployed on Streamlit Cloud
        import streamlit as st
        config = st.secrets
        return pymysql.connect(
            host=config["DB_HOST"],
            user=config["DB_USER"],
            password=config["DB_PASSWORD"],
            database=config["DB_NAME"],
            cursorclass=pymysql.cursors.DictCursor
        )
    except Exception:
        # Fall back to .env — used in local development
        return pymysql.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "school_meal_db"),
            cursorclass=pymysql.cursors.DictCursor
        )


def save_quality_scores(quality_df: pd.DataFrame, uploaded_by: str = "admin") -> dict:
    """
    Save AI-generated quality scores to the quality_scores table.

    Args:
        quality_df : DataFrame returned by QualityAssessment.calculate_overall_quality()
        uploaded_by: username of the logged-in user who triggered processing

    Returns:
        dict with keys: success (bool), saved (int), errors (int), message (str)
    """
    result = {"success": False, "saved": 0, "errors": 0, "message": ""}

    required_cols = [
        "School_ID", "Date", "Overall_Quality_Score",
        "Nutrition_Score", "Waste_Score", "Hygiene_Score",
        "Taste_Score", "Menu_Score"
    ]
    missing = [c for c in required_cols if c not in quality_df.columns]
    if missing:
        result["message"] = f"Missing columns: {missing}"
        return result

    insert_sql = """
        INSERT INTO quality_scores
            (School_ID, Date, Overall_Quality_Score,
             Nutrition_Score, Waste_Score, Hygiene_Score,
             Taste_Score, Menu_Score, Uploaded_By)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            Overall_Quality_Score = VALUES(Overall_Quality_Score),
            Nutrition_Score       = VALUES(Nutrition_Score),
            Waste_Score           = VALUES(Waste_Score),
            Hygiene_Score         = VALUES(Hygiene_Score),
            Taste_Score           = VALUES(Taste_Score),
            Menu_Score            = VALUES(Menu_Score),
            Uploaded_By           = VALUES(Uploaded_By),
            Processed_At          = CURRENT_TIMESTAMP
    """

    try:
        conn   = get_connection()
        cursor = conn.cursor()

        for _, row in quality_df.iterrows():
            try:
                cursor.execute(insert_sql, (
                    str(row["School_ID"]),
                    str(row["Date"])[:10],
                    round(float(row["Overall_Quality_Score"]), 4),
                    round(float(row["Nutrition_Score"]), 4),
                    round(float(row["Waste_Score"]), 4),
                    round(float(row["Hygiene_Score"]), 4),
                    round(float(row["Taste_Score"]), 4),
                    round(float(row["Menu_Score"]), 4),
                    uploaded_by,
                ))
                result["saved"] += 1
            except Exception:
                result["errors"] += 1

        conn.commit()
        cursor.close()
        conn.close()

        result["success"] = True
        result["message"] = (
            f"Saved {result['saved']} quality score records"
            + (f" ({result['errors']} errors)" if result["errors"] else "")
        )

    except Exception as conn_err:
        result["message"] = f"DB connection failed: {conn_err}"

    return result


def save_alerts(alerts_df: pd.DataFrame, uploaded_by: str = "admin") -> dict:
    """
    Save AI-generated alerts to the quality_alerts table.

    Args:
        alerts_df : DataFrame returned by QualityAssessment.generate_alerts()
        uploaded_by: username of the logged-in user

    Returns:
        dict with keys: success (bool), saved (int), errors (int), message (str)
    """
    result = {"success": False, "saved": 0, "errors": 0, "message": ""}

    if alerts_df.empty:
        result["success"] = True
        result["message"] = "No alerts to save"
        return result

    insert_sql = """
        INSERT INTO quality_alerts
            (School_ID, Date, Alert_Issues, Priority, Uploaded_By)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            Alert_Issues = VALUES(Alert_Issues),
            Priority     = VALUES(Priority),
            Uploaded_By  = VALUES(Uploaded_By),
            Created_At   = CURRENT_TIMESTAMP
    """

    try:
        conn   = get_connection()
        cursor = conn.cursor()

        for _, row in alerts_df.iterrows():
            try:
                issues_str = " | ".join(row["Alerts"]) if isinstance(row["Alerts"], list) else str(row["Alerts"])
                cursor.execute(insert_sql, (
                    str(row["School_ID"]),
                    str(row["Date"])[:10],
                    issues_str,
                    str(row["Priority"]),
                    uploaded_by,
                ))
                result["saved"] += 1
            except Exception:
                result["errors"] += 1

        conn.commit()
        cursor.close()
        conn.close()

        result["success"] = True
        result["message"] = (
            f"Saved {result['saved']} alert records"
            + (f" ({result['errors']} errors)" if result["errors"] else "")
        )

    except Exception as conn_err:
        result["message"] = f"DB connection failed: {conn_err}"

    return result


def save_all_results(quality_df: pd.DataFrame, alerts_df: pd.DataFrame, uploaded_by: str = "admin") -> dict:
    """
    Convenience function — saves both quality scores and alerts in one call.

    Returns:
        dict with 'scores' and 'alerts' sub-results, and overall 'success'
    """
    scores_result = save_quality_scores(quality_df, uploaded_by)
    alerts_result = save_alerts(alerts_df, uploaded_by)

    return {
        "success": scores_result["success"] and alerts_result["success"],
        "scores":  scores_result,
        "alerts":  alerts_result,
    }