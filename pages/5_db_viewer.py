"""
pages/5_db_viewer.py — Database Verification Page
Shows exactly what is stored in MySQL — quality_scores and quality_alerts tables.
Admin only.
"""
import streamlit as st, sys, pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from src.auth import is_logged_in, get_current_user, logout
from src.styles import SHARED_CSS

import pymysql
import pymysql.cursors
from dotenv import load_dotenv
import os

load_dotenv()

# ── AUTH ──
if not is_logged_in(st.session_state):
    st.error("🔒 Please sign in first.")
    if st.button("Go to Login →", type="primary"):
        st.switch_page("pages/1_login.py")
    st.stop()

current_user = get_current_user(st.session_state)

# Admin only
if current_user.get("role") != "admin":
    st.error("⛔ This page is for admin users only.")
    st.stop()

st.set_page_config(
    page_title="DB Viewer · School Meal Monitor",
    page_icon="🗄️",
    layout="wide"
)
st.markdown(SHARED_CSS, unsafe_allow_html=True)

# ── SIDEBAR ──
with st.sidebar:
    st.markdown(f'<div class="sb-user"><h4>👤 {current_user["full_name"]}</h4><p>{current_user["role"]}</p></div>', unsafe_allow_html=True)
    if st.button("🚪 Sign Out", use_container_width=True):
        logout(st.session_state)
        st.switch_page("pages/1_login.py")
    st.markdown("---")
    if st.button("🏠 Home",            use_container_width=True): st.switch_page("app.py")
    if st.button("📤 Upload Data",     use_container_width=True): st.switch_page("pages/2_upload_data.py")
    if st.button("📊 Dashboard",       use_container_width=True): st.switch_page("pages/4_dashboard.py")

# ── HEADER ──
st.markdown("""
<div class="ph">
  <div class="ph-badge">🗄️ Admin Tool</div>
  <h1>Database Verification</h1>
  <p>Live view of what is actually stored in your MySQL database</p>
</div>
""", unsafe_allow_html=True)


# ── DB CONNECTION HELPER ──
def get_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "school_meal_db")
    )

def run_query(sql: str) -> pd.DataFrame | None:
    try:
        conn = get_connection()
        df   = pd.read_sql(sql, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"❌ Query failed: {e}")
        return None


# ══════════════════════════════════════
# STEP 1 — CONNECTION TEST
# ══════════════════════════════════════
st.markdown("### 🔌 Step 1 — Connection Test")

try:
    conn = get_connection()
    conn.close()
    st.success("✅ Connected to MySQL successfully!")

    # Show connection details (hide password)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Host",     os.getenv("DB_HOST", "localhost"))
    c2.metric("Database", os.getenv("DB_NAME", "—"))
    c3.metric("User",     os.getenv("DB_USER", "—"))
    c4.metric("Status",   "🟢 Connected")

except Exception as e:
    st.error(f"❌ Cannot connect to MySQL: {e}")
    st.info("💡 Check your .env file — DB_HOST, DB_USER, DB_PASSWORD, DB_NAME must be set correctly.")
    st.stop()

st.divider()


# ══════════════════════════════════════
# STEP 2 — TABLE EXISTENCE CHECK
# ══════════════════════════════════════
st.markdown("### 📋 Step 2 — Table Existence Check")

tables_to_check = ["meal_data", "quality_scores", "quality_alerts"]

cols = st.columns(len(tables_to_check))

for col, table in zip(cols, tables_to_check):
    try:
        conn   = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        col.markdown(f"""
        <div style="background:var(--surf);border:1px solid #059669;border-radius:12px;padding:1.2rem;text-align:center;">
          <p style="font-size:1.6rem;margin:0;">✅</p>
          <p style="font-weight:700;margin:.3rem 0 .1rem;">{table}</p>
          <p style="font-size:.82rem;opacity:.6;margin:0;">{count:,} rows</p>
        </div>
        """, unsafe_allow_html=True)
    except Exception:
        col.markdown(f"""
        <div style="background:var(--surf);border:1px solid #dc2626;border-radius:12px;padding:1.2rem;text-align:center;">
          <p style="font-size:1.6rem;margin:0;">❌</p>
          <p style="font-weight:700;margin:.3rem 0 .1rem;">{table}</p>
          <p style="font-size:.82rem;opacity:.6;margin:0;">Table not found</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.divider()


# ══════════════════════════════════════
# STEP 3 — quality_scores TABLE
# ══════════════════════════════════════
st.markdown("### 🎯 Step 3 — quality_scores Table")
st.caption("This is where AI-generated scores are saved after every processing run.")

scores_df = run_query("SELECT * FROM quality_scores ORDER BY Processed_At DESC")

if scores_df is not None and not scores_df.empty:

    # Summary row counts
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Rows",    f"{len(scores_df):,}")
    m2.metric("Schools",       scores_df["School_ID"].nunique())
    m3.metric("Avg Score",     f"{scores_df['Overall_Quality_Score'].mean():.1f}")
    m4.metric("Latest Upload", str(scores_df["Processed_At"].max())[:16])

    st.markdown("<br>", unsafe_allow_html=True)

    # Score columns for gradient
    score_cols = ["Overall_Quality_Score","Nutrition_Score","Waste_Score",
                  "Hygiene_Score","Taste_Score","Menu_Score"]

    try:
        styled = (
            scores_df.style
            .background_gradient(cmap="RdYlGn", subset=["Overall_Quality_Score"], vmin=0, vmax=100)
            .format({c: "{:.2f}" for c in score_cols if c in scores_df.columns})
        )
        st.dataframe(styled, use_container_width=True, height=400)
    except Exception:
        st.dataframe(scores_df, use_container_width=True, height=400)

    # Download button
    st.download_button(
        "📥 Download quality_scores as CSV",
        data=scores_df.to_csv(index=False).encode(),
        file_name="db_quality_scores.csv",
        mime="text/csv"
    )

elif scores_df is not None and scores_df.empty:
    st.warning("⚠️ Table exists but has 0 rows — process some data first to populate it.")
else:
    st.error("❌ Could not read quality_scores — make sure you ran create_new_tables.sql")

st.divider()


# ══════════════════════════════════════
# STEP 4 — quality_alerts TABLE
# ══════════════════════════════════════
st.markdown("### 🚨 Step 4 — quality_alerts Table")
st.caption("This is where AI-generated alerts are saved after every processing run.")

alerts_df = run_query("SELECT * FROM quality_alerts ORDER BY Created_At DESC")

if alerts_df is not None and not alerts_df.empty:

    a1, a2, a3 = st.columns(3)
    a1.metric("Total Alerts",   f"{len(alerts_df):,}")
    a2.metric("High Priority",  len(alerts_df[alerts_df["Priority"] == "High"]))
    a3.metric("Medium Priority",len(alerts_df[alerts_df["Priority"] == "Medium"]))

    st.markdown("<br>", unsafe_allow_html=True)

    def color_priority(val):
        if val == "High":   return "background-color:#fee2e2;color:#991b1b;font-weight:700"
        if val == "Medium": return "background-color:#fef9c3;color:#92400e;font-weight:700"
        return ""

    try:
        styled_alerts = alerts_df.style.applymap(color_priority, subset=["Priority"])
        st.dataframe(styled_alerts, use_container_width=True, height=350)
    except Exception:
        st.dataframe(alerts_df, use_container_width=True, height=350)

    st.download_button(
        "📥 Download quality_alerts as CSV",
        data=alerts_df.to_csv(index=False).encode(),
        file_name="db_quality_alerts.csv",
        mime="text/csv"
    )

elif alerts_df is not None and alerts_df.empty:
    st.success("✅ Table exists but has 0 alerts — all schools are performing well, or process data first.")
else:
    st.error("❌ Could not read quality_alerts — make sure you ran create_new_tables.sql")

st.divider()


# ══════════════════════════════════════
# STEP 5 — RAW SQL QUERY TOOL
# ══════════════════════════════════════
st.markdown("### 🔍 Step 5 — Run a Custom SQL Query")
st.caption("Type any SELECT query to inspect the database directly.")

default_query = "SELECT School_ID, Date, Overall_Quality_Score, Uploaded_By, Processed_At FROM quality_scores ORDER BY Overall_Quality_Score DESC LIMIT 10;"

user_query = st.text_area("SQL Query", value=default_query, height=100)

if st.button("▶️ Run Query", type="primary"):
    if not user_query.strip().upper().startswith("SELECT"):
        st.error("⛔ Only SELECT queries are allowed here.")
    else:
        result = run_query(user_query)
        if result is not None:
            if result.empty:
                st.info("Query ran successfully but returned 0 rows.")
            else:
                st.success(f"✅ {len(result):,} rows returned")
                st.dataframe(result, use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center;padding:1rem 0;opacity:.30;font-size:.78rem;letter-spacing:.05em;">
  🗄️ &nbsp; Database Verification Tool &nbsp;·&nbsp; Admin Only &nbsp;·&nbsp; School Meal Quality Monitor
</div>
""", unsafe_allow_html=True)