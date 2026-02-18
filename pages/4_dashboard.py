"""
pages/4_dashboard.py — Dashboard
Complete analytics view. Theme-safe. Perfectly aligned.
"""
import streamlit as st, pandas as pd, sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from src.visualizations import Visualizer
from src.auth import is_logged_in, get_current_user, logout
from src.styles import SHARED_CSS

# ── AUTH ──
if not is_logged_in(st.session_state):
    st.error("🔒 Please sign in first.")
    if st.button("Go to Login →", type="primary"):
        st.switch_page("pages/1_login.py")
    st.stop()

current_user = get_current_user(st.session_state)

if 'processing_complete' not in st.session_state or not st.session_state['processing_complete']:
    st.error("❌ No processed data found. Please upload and process data first.")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📤 Upload Data",  type="primary", use_container_width=True):
            st.switch_page("pages/2_upload_data.py")
    with c2:
        if st.button("⚙️ Processing", use_container_width=True):
            st.switch_page("pages/3_processing.py")
    st.stop()

df         = st.session_state['df_processed']
quality_df = st.session_state['quality_df']
alerts_df  = st.session_state['alerts_df']
stats      = st.session_state['stats']

st.set_page_config(page_title="Dashboard · School Meal Monitor", page_icon="📊",
                   layout="wide", initial_sidebar_state="expanded")
st.markdown(SHARED_CSS, unsafe_allow_html=True)

# ── SIDEBAR ──
with st.sidebar:
    st.markdown(f'<div class="sb-user"><h4>👤 {current_user["full_name"]}</h4><p>{current_user["role"]}</p></div>', unsafe_allow_html=True)

    if st.button("🚪 Sign Out", use_container_width=True):
        logout(st.session_state)
        st.switch_page("pages/1_login.py")

    st.markdown("---")
    st.markdown("""
    <div class="steps">
      <div class="st-item"><div class="st-dot done">✓</div><span class="st-lbl done">Upload</span></div>
      <div class="st-line done"></div>
      <div class="st-item"><div class="st-dot done">✓</div><span class="st-lbl done">Process</span></div>
      <div class="st-line done"></div>
      <div class="st-item"><div class="st-dot active">3</div><span class="st-lbl active">Dashboard</span></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")

    if st.button("📤 Upload New Data", use_container_width=True):
        for k in ['data_loaded','processing_complete','meal_data','df_processed','quality_df','alerts_df','stats']:
            st.session_state.pop(k, None)
        st.switch_page("pages/2_upload_data.py")

    st.markdown("---")
    # Session summary
    st.markdown(f"""
    <div style="background:var(--surf);border:1px solid var(--bdr);border-radius:var(--r1);padding:1rem;font-size:.82rem;">
      <p style="margin:0 0 .55rem;font-size:.68rem;font-weight:800;text-transform:uppercase;letter-spacing:.09em;opacity:.45;">Session</p>
      <p style="margin:.18rem 0;">Records: <strong>{len(df):,}</strong></p>
      <p style="margin:.18rem 0;">Schools: <strong>{stats['total_schools']}</strong></p>
      <p style="margin:.18rem 0;">Alerts: <strong>{len(alerts_df)}</strong></p>
      <p style="margin:0;">Source: <strong>CSV Upload</strong></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    # Grading reference
    st.markdown("""
    <div style="background:var(--surf);border:1px solid var(--bdr);border-radius:var(--r1);padding:1rem;">
      <p style="margin:0 0 .55rem;font-size:.68rem;font-weight:800;text-transform:uppercase;letter-spacing:.09em;opacity:.45;">Quality Grades</p>
      <p style="margin:.22rem 0;font-size:.8rem;">🟢 <strong>Excellent</strong> &nbsp;85 – 100</p>
      <p style="margin:.22rem 0;font-size:.8rem;">🔵 <strong>Good</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;70 – 84</p>
      <p style="margin:.22rem 0;font-size:.8rem;">🟡 <strong>Fair</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;50 – 69</p>
      <p style="margin:0;font-size:.8rem;">🔴 <strong>Poor</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 – 49</p>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════
# HEADER
# ══════════════════════════════════════
st.markdown(f"""
<div class="ph">
  <div class="ph-badge">📊 Live Results</div>
  <h1>Quality Assessment Dashboard</h1>
  <p>{len(df):,} records processed &nbsp;·&nbsp; {stats['total_schools']} schools &nbsp;·&nbsp; {len(alerts_df)} alerts generated</p>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════
# KPI CARDS
# ══════════════════════════════════════
st.markdown('<div class="sec-div"><div class="dl"></div><span>Key Performance Indicators</span><div class="dl"></div></div>', unsafe_allow_html=True)

k1, k2, k3, k4 = st.columns(4, gap="medium")

waste_cls = "kpi-r" if stats['avg_waste'] > 20 else "kpi-c"
waste_sub = "⚠️ Above 20% threshold" if stats['avg_waste'] > 20 else "✅ Within target range"

with k1:
    st.markdown(f'<div class="kpi kpi-b"><span class="ki">🏫</span><p class="kv">{stats["total_schools"]}</p><p class="kl">Total Schools</p><p class="ks">in dataset</p></div>', unsafe_allow_html=True)
with k2:
    st.markdown(f'<div class="kpi kpi-v"><span class="ki">🍽️</span><p class="kv">{stats["total_meals_served"]:,}</p><p class="kl">Meals Served</p><p class="ks">total across all schools</p></div>', unsafe_allow_html=True)
with k3:
    st.markdown(f'<div class="kpi {waste_cls}"><span class="ki">🗑️</span><p class="kv">{stats["avg_waste"]:.1f}%</p><p class="kl">Average Waste</p><p class="ks">{waste_sub}</p></div>', unsafe_allow_html=True)
with k4:
    stars = "⭐" * round(stats['avg_taste_rating'])
    st.markdown(f'<div class="kpi kpi-a"><span class="ki">⭐</span><p class="kv">{stats["avg_taste_rating"]:.1f}</p><p class="kl">Avg Taste Rating</p><p class="ks">{stars} / 5.0</p></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ══════════════════════════════════════
# NUTRITION COMPLIANCE
# ══════════════════════════════════════
st.markdown('<div class="sec-div"><div class="dl"></div><span>Nutritional Compliance</span><div class="dl"></div></div>', unsafe_allow_html=True)

excellent_n = len(quality_df[quality_df['Overall_Quality_Score'] >= 85])
ex_rate     = (excellent_n / stats['total_schools'] * 100) if stats['total_schools'] else 0
cal_ok      = stats['avg_calorie_compliance'] >= 95
prot_ok     = stats['avg_protein_compliance'] >= 95

n1, n2, n3 = st.columns(3, gap="medium")
with n1:
    st.markdown(f'<div class="mc g"><p class="ml">Calorie Compliance</p><p class="mv">{stats["avg_calorie_compliance"]:.1f}%</p><p class="ms">{"✅ On Target" if cal_ok else "⚠️ Below Target"}</p></div>', unsafe_allow_html=True)
with n2:
    st.markdown(f'<div class="mc a"><p class="ml">Protein Compliance</p><p class="mv">{stats["avg_protein_compliance"]:.1f}%</p><p class="ms">{"✅ On Target" if prot_ok else "⚠️ Below Target"}</p></div>', unsafe_allow_html=True)
with n3:
    st.markdown(f'<div class="mc v"><p class="ml">Excellent Schools</p><p class="mv">{excellent_n}</p><p class="ms">{ex_rate:.0f}% of all schools (score ≥ 85)</p></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.divider()

# ══════════════════════════════════════
# ALERTS
# ══════════════════════════════════════
st.markdown('<div class="sec-div"><div class="dl"></div><span>AI-Generated Quality Alerts</span><div class="dl"></div></div>', unsafe_allow_html=True)

if not alerts_df.empty:
    high   = len(alerts_df[alerts_df['Priority'] == 'High'])
    medium = len(alerts_df[alerts_df['Priority'] == 'Medium'])
    total  = len(alerts_df)

    a1, a2, a3 = st.columns(3, gap="medium")
    with a1:
        st.markdown(f'<div class="asc r"><span class="ai">🔴</span><p class="al">High Priority</p><p class="av">{high}</p><p class="ad">schools need urgent attention</p></div>', unsafe_allow_html=True)
    with a2:
        st.markdown(f'<div class="asc y"><span class="ai">🟡</span><p class="al">Medium Priority</p><p class="av">{medium}</p><p class="ad">schools need monitoring</p></div>', unsafe_allow_html=True)
    with a3:
        st.markdown(f'<div class="asc b"><span class="ai">📋</span><p class="al">Total Alerts</p><p class="av">{total}</p><p class="ad">quality issues detected</p></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander(f"View all {total} alert details", expanded=False):
        for _, alert in alerts_df.head(20).iterrows():
            is_high = alert['Priority'] == 'High'
            cls = 'r' if is_high else 'y'
            em  = '🔴' if is_high else '🟡'
            st.markdown(f"""
            <div class="a-row {cls}">
              <p class="ah">{em} &nbsp; School: <strong>{alert['School_ID']}</strong> &nbsp;·&nbsp; Priority: <strong>{alert['Priority']}</strong></p>
              <p class="am">📅 {alert['Date']}</p>
            </div>
            """, unsafe_allow_html=True)
            for issue in alert['Alerts']:
                st.write(f"  ⚠️ {issue}")
else:
    st.markdown('<div class="no-alert">✅ &nbsp; No Critical Alerts — All Schools Performing Well!</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.divider()

# ══════════════════════════════════════
# CHARTS
# ══════════════════════════════════════
st.markdown('<div class="sec-div"><div class="dl"></div><span>Analytics & Visualizations</span><div class="dl"></div></div>', unsafe_allow_html=True)

visualizer = Visualizer(df)
cfg = {'displayModeBar': True, 'displaylogo': False}

tab1, tab2, tab3, tab4 = st.tabs([
    "📉 Waste Trends",
    "🎯 Quality Overview",
    "🏆 School Rankings",
    "🥗 Nutrition"
])

with tab1:
    st.markdown("##### Average Food Waste Trend Over Time")
    st.plotly_chart(visualizer.plot_waste_trend(), use_container_width=True, config=cfg)
    st.info("💡 Monitor waste trends to identify patterns and implement targeted reduction measures.")

with tab2:
    st.markdown("##### Quality Score Distribution & Dimension Radar")
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        st.plotly_chart(visualizer.plot_quality_distribution(quality_df), use_container_width=True, config={'displayModeBar':False})
    with c2:
        st.plotly_chart(visualizer.plot_metrics_radar(quality_df), use_container_width=True, config={'displayModeBar':False})
    st.info("💡 The radar chart reveals performance balance across all five quality dimensions.")

with tab3:
    st.markdown("##### School-by-School Performance Comparison")
    st.plotly_chart(visualizer.plot_school_performance(quality_df), use_container_width=True, config=cfg)
    st.info("💡 Identify top performers and schools that need additional support or resources.")

with tab4:
    st.markdown("##### Calorie & Protein Compliance Over Time")
    st.plotly_chart(visualizer.plot_nutrition_compliance(), use_container_width=True, config=cfg)
    st.info("💡 Both calorie and protein compliance should ideally be at or above 100% of the required target.")

st.markdown("<br>", unsafe_allow_html=True)
st.divider()

# ══════════════════════════════════════
# DATA TABLE
# ══════════════════════════════════════
st.markdown('<div class="sec-div"><div class="dl"></div><span>Detailed Assessment Records</span><div class="dl"></div></div>', unsafe_allow_html=True)

f1, f2, f3 = st.columns([2, 3, 2], gap="medium")

with f1:
    min_score = st.slider("Minimum Quality Score", 0, 100, 0, 5)
with f2:
    selected_schools = st.multiselect(
        "Filter by School",
        options=sorted(quality_df['School_ID'].unique()),
        default=sorted(quality_df['School_ID'].unique()),
        placeholder="Select schools..."
    )
with f3:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="text-align:right;">
      <span class="c-pill">📋 &nbsp; {len(quality_df[quality_df['Overall_Quality_Score'] >= min_score]):,} records</span>
    </div>
    """, unsafe_allow_html=True)

filtered_df = quality_df[
    (quality_df['Overall_Quality_Score'] >= min_score) &
    (quality_df['School_ID'].isin(selected_schools if selected_schools else quality_df['School_ID'].unique()))
]

score_cols = [c for c in ['Overall_Quality_Score','Nutrition_Score','Waste_Score','Hygiene_Score','Taste_Score','Menu_Score'] if c in filtered_df.columns]
fmt = {c: '{:.2f}' for c in score_cols}

try:
    styled = filtered_df.style.background_gradient(cmap='RdYlGn', subset=['Overall_Quality_Score'], vmin=0, vmax=100).format(fmt)
    st.dataframe(styled, use_container_width=True, height=430)
except Exception:
    st.dataframe(filtered_df, use_container_width=True, height=430)

st.markdown("<br>", unsafe_allow_html=True)

d1, d2 = st.columns(2, gap="medium")
ts = pd.Timestamp.now().strftime('%Y%m%d_%H%M')

with d1:
    st.download_button(
        "📥 Download Filtered Report",
        data=filtered_df.to_csv(index=False).encode(),
        file_name=f"meal_quality_filtered_{ts}.csv",
        mime="text/csv", use_container_width=True
    )
with d2:
    st.download_button(
        "📥 Download Full Dataset",
        data=quality_df.to_csv(index=False).encode(),
        file_name=f"meal_quality_full_{ts}.csv",
        mime="text/csv", use_container_width=True
    )

st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.markdown("""
<div style="text-align:center;padding:1rem 0;opacity:.30;font-size:.78rem;letter-spacing:.05em;">
  🍽️ &nbsp; School Meal Quality Monitor &nbsp;·&nbsp; AI-Powered Assessment &nbsp;·&nbsp; MySQL Integrated
</div>
""", unsafe_allow_html=True)