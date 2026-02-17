# """
# Page 4: Dashboard - Complete Analytics View
# Theme-compatible (light + dark mode)
# """

# import streamlit as st
# import sys
# from pathlib import Path
# import pandas as pd

# sys.path.append(str(Path(__file__).parent.parent))

# from src.visualizations import Visualizer
# from src.auth import is_logged_in, get_current_user, logout

# # ── AUTH CHECK ──
# if not is_logged_in(st.session_state):
#     st.error("🔒 Please login first!")
#     if st.button("🔐 Go to Login", type="primary"):
#         st.switch_page("pages/1_login.py")
#     st.stop()

# current_user = get_current_user(st.session_state)

# if 'processing_complete' not in st.session_state or not st.session_state['processing_complete']:
#     st.error("❌ No processed data found. Please upload and process data first.")
#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button("📤 Upload Data", use_container_width=True, type="primary"):
#             st.switch_page("pages/2_upload_data.py")
#     with col2:
#         if st.button("⏳ Processing", use_container_width=True):
#             st.switch_page("pages/3_processing.py")
#     st.stop()

# # Load from session
# df         = st.session_state['df_processed']
# quality_df = st.session_state['quality_df']
# alerts_df  = st.session_state['alerts_df']
# stats      = st.session_state['stats']

# st.set_page_config(
#     page_title="Dashboard - School Meal Monitor",
#     page_icon="📊",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # ── THEME-COMPATIBLE CSS ──
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=DM+Serif+Display&display=swap');

# * { font-family: 'DM Sans', sans-serif; }

# /* ── HIDE CHROME ── */
# #MainMenu, footer { visibility: hidden; }

# /* ─────────────────────────────────────────
#    THEME-SAFE CSS VARIABLES
#    Works in both light mode and dark mode
# ───────────────────────────────────────── */
# :root {
#     --blue-start:   #2563eb;
#     --blue-end:     #1d4ed8;
#     --purple-start: #7c3aed;
#     --purple-end:   #6d28d9;
#     --pink-start:   #db2777;
#     --pink-end:     #be185d;
#     --teal-start:   #0891b2;
#     --teal-end:     #0e7490;

#     --green-bg:   rgba(22,163,74,0.12);
#     --green-bdr:  #16a34a;
#     --green-text: #16a34a;

#     --amber-bg:   rgba(217,119,6,0.12);
#     --amber-bdr:  #d97706;
#     --amber-text: #d97706;

#     --red-bg:     rgba(220,38,38,0.12);
#     --red-bdr:    #dc2626;
#     --red-text:   #dc2626;

#     --indigo-bg:  rgba(99,102,241,0.12);
#     --indigo-bdr: #6366f1;
#     --indigo-text:#6366f1;

#     --blue-bg:    rgba(37,99,235,0.10);
#     --blue-bdr:   #2563eb;
#     --blue-text:  #2563eb;

#     --card-radius: 16px;
#     --card-shadow: 0 4px 20px rgba(0,0,0,0.08);
# }

# /* ── KPI METRIC CARDS ── */
# .kpi-card {
#     padding: 1.8rem 1.5rem;
#     border-radius: var(--card-radius);
#     color: #ffffff;
#     box-shadow: var(--card-shadow);
#     margin-bottom: 0.5rem;
# }
# .kpi-label {
#     font-size: 0.78rem;
#     font-weight: 700;
#     letter-spacing: 0.08em;
#     opacity: 0.88;
#     margin: 0 0 0.6rem;
#     text-transform: uppercase;
# }
# .kpi-value {
#     font-size: 2.8rem;
#     font-weight: 800;
#     line-height: 1;
#     margin: 0;
#     color: #ffffff;
# }
# .kpi-sub {
#     font-size: 0.8rem;
#     opacity: 0.75;
#     margin: 0.4rem 0 0;
# }

# .kpi-blue   { background: linear-gradient(135deg, #2563eb, #1d4ed8); box-shadow: 0 8px 24px rgba(37,99,235,0.30); }
# .kpi-pink   { background: linear-gradient(135deg, #db2777, #be185d); box-shadow: 0 8px 24px rgba(219,39,119,0.30); }
# .kpi-teal   { background: linear-gradient(135deg, #0891b2, #0e7490); box-shadow: 0 8px 24px rgba(8,145,178,0.30); }
# .kpi-amber  { background: linear-gradient(135deg, #d97706, #b45309); box-shadow: 0 8px 24px rgba(217,119,6,0.30); }
# .kpi-red    { background: linear-gradient(135deg, #dc2626, #b91c1c); box-shadow: 0 8px 24px rgba(220,38,38,0.30); }

# /* ── COMPLIANCE CARDS ── */
# .compliance-card {
#     padding: 1.8rem;
#     border-radius: var(--card-radius);
#     border-left: 5px solid;
#     box-shadow: var(--card-shadow);
#     margin-bottom: 0.5rem;
#     /* no background set = inherits theme bg */
# }
# .compliance-card.green  { border-color: var(--green-bdr);  background: var(--green-bg);  }
# .compliance-card.amber  { border-color: var(--amber-bdr);  background: var(--amber-bg);  }
# .compliance-card.blue   { border-color: var(--blue-bdr);   background: var(--blue-bg);   }

# .compliance-label {
#     font-size: 0.75rem;
#     font-weight: 700;
#     letter-spacing: 0.08em;
#     text-transform: uppercase;
#     opacity: 0.7;
#     margin: 0 0 0.5rem;
# }
# .compliance-value {
#     font-size: 2.5rem;
#     font-weight: 800;
#     margin: 0 0 0.4rem;
#     line-height: 1;
# }
# .compliance-card.green  .compliance-value { color: var(--green-text); }
# .compliance-card.amber  .compliance-value { color: var(--amber-text); }
# .compliance-card.blue   .compliance-value { color: var(--blue-text);  }
# .compliance-status { font-size: 0.85rem; font-weight: 600; opacity: 0.8; margin: 0; }

# /* ── ALERT CARDS ── */
# .alert-stat-card {
#     padding: 1.5rem;
#     border-radius: var(--card-radius);
#     border-left: 5px solid;
#     box-shadow: var(--card-shadow);
#     margin-bottom: 0.5rem;
# }
# .alert-stat-card.red    { background: var(--red-bg);    border-color: var(--red-bdr);    }
# .alert-stat-card.amber  { background: var(--amber-bg);  border-color: var(--amber-bdr);  }
# .alert-stat-card.indigo { background: var(--indigo-bg); border-color: var(--indigo-bdr); }

# .alert-stat-label {
#     font-size: 0.75rem;
#     font-weight: 700;
#     letter-spacing: 0.06em;
#     text-transform: uppercase;
#     opacity: 0.7;
#     margin: 0 0 0.4rem;
# }
# .alert-stat-value {
#     font-size: 2.8rem;
#     font-weight: 800;
#     margin: 0 0 0.3rem;
#     line-height: 1;
# }
# .alert-stat-card.red    .alert-stat-value { color: var(--red-text);    }
# .alert-stat-card.amber  .alert-stat-value { color: var(--amber-text);  }
# .alert-stat-card.indigo .alert-stat-value { color: var(--indigo-text); }
# .alert-stat-desc { font-size: 0.85rem; opacity: 0.7; margin: 0; font-weight: 500; }

# /* ── ALERT DETAIL CARDS ── */
# .alert-detail {
#     padding: 1.2rem 1.5rem;
#     border-radius: 12px;
#     border-left: 4px solid;
#     margin-bottom: 0.8rem;
#     box-shadow: 0 2px 8px rgba(0,0,0,0.05);
# }
# .alert-detail.red   { background: var(--red-bg);   border-color: var(--red-bdr);   }
# .alert-detail.amber { background: var(--amber-bg); border-color: var(--amber-bdr); }
# .alert-school { font-size: 0.95rem; font-weight: 700; margin: 0 0 0.5rem; }

# /* ── SECTION HEADER ── */
# .section-header {
#     font-family: 'DM Serif Display', serif;
#     font-size: 1.6rem;
#     font-weight: 400;
#     margin: 2rem 0 1rem;
#     padding-left: 1rem;
#     border-left: 4px solid #2563eb;
# }

# /* ── DASHBOARD HERO ── */
# .dash-hero {
#     background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 60%, #3b82f6 100%);
#     border-radius: 20px;
#     padding: 2.5rem;
#     margin-bottom: 2rem;
#     color: white;
#     box-shadow: 0 12px 40px rgba(37,99,235,0.3);
# }
# .dash-hero h1 {
#     font-family: 'DM Serif Display', serif;
#     font-size: 2.2rem;
#     font-weight: 400;
#     color: white;
#     margin: 0 0 0.4rem;
# }
# .dash-hero p {
#     opacity: 0.85;
#     margin: 0;
#     font-size: 1rem;
# }

# /* ── RECORD COUNT BADGE ── */
# .record-badge {
#     display: inline-block;
#     padding: 0.5rem 1rem;
#     border-radius: 50px;
#     font-size: 0.85rem;
#     font-weight: 600;
#     background: rgba(37,99,235,0.12);
#     color: #2563eb;
#     margin: 0.8rem 0 0;
#     border: 1px solid rgba(37,99,235,0.2);
# }

# /* ── BUTTONS ── */
# .stButton > button {
#     border-radius: 10px !important;
#     font-weight: 600 !important;
#     transition: all 0.2s ease !important;
# }
# .stDownloadButton > button {
#     border-radius: 10px !important;
#     font-weight: 600 !important;
# }

# /* ── TABS ── */
# .stTabs [data-baseweb="tab-list"] {
#     gap: 6px;
#     background: transparent;
# }
# .stTabs [data-baseweb="tab"] {
#     border-radius: 10px 10px 0 0;
#     padding: 10px 20px;
#     font-weight: 600;
#     font-size: 0.9rem;
# }
# .stTabs [aria-selected="true"] {
#     background: #2563eb !important;
#     color: white !important;
# }

# /* ── SIDEBAR USER CARD ── */
# .sidebar-user {
#     background: linear-gradient(135deg, #2563eb, #1d4ed8);
#     padding: 1.3rem;
#     border-radius: 14px;
#     color: white;
#     margin-bottom: 1.5rem;
# }
# .sidebar-user h4 { color: white; margin: 0 0 0.3rem; font-size: 1rem; }
# .sidebar-user p  { color: rgba(255,255,255,0.8); margin: 0; font-size: 0.82rem; }

# /* ── EXPANDER ── */
# .streamlit-expanderHeader {
#     border-radius: 10px !important;
#     font-weight: 600 !important;
# }

# /* ── SUCCESS TOAST ── */
# .no-alert-box {
#     background: var(--green-bg);
#     border: 1px solid var(--green-bdr);
#     border-radius: 14px;
#     padding: 1.5rem 2rem;
#     text-align: center;
#     color: var(--green-text);
#     font-weight: 600;
#     font-size: 1.05rem;
# }
# </style>
# """, unsafe_allow_html=True)

# # ── SIDEBAR ──
# with st.sidebar:
#     st.markdown(f"""
#         <div class="sidebar-user">
#             <h4>👤 {current_user['full_name']}</h4>
#             <p>Role: {current_user['role']}</p>
#         </div>
#     """, unsafe_allow_html=True)

#     if st.button("🚪 Logout", use_container_width=True):
#         logout(st.session_state)
#         st.switch_page("pages/1_login.py")

#     st.markdown("---")
#     st.markdown("**📍 Current Page**")
#     st.success("Dashboard ✅")

#     st.markdown("**🔄 Navigation**")
#     if st.button("🏠 Home", use_container_width=True):
#         st.switch_page("app.py")
#     if st.button("📤 Upload New Data", use_container_width=True):
#         for key in ['data_loaded','processing_complete','meal_data','df_processed','quality_df','alerts_df','stats']:
#             st.session_state.pop(key, None)
#         st.switch_page("pages/2_upload_data.py")

#     st.markdown("---")
#     st.markdown(f"""
#         **📊 Session Summary**
#         - Records: **{len(df)}**
#         - Schools: **{stats['total_schools']}**
#         - Alerts: **{len(alerts_df)}**
#         - Source: **{st.session_state.get('data_source','Unknown').upper()}**
#     """)

# # ── HERO HEADER ──
# st.markdown(f"""
#     <div class="dash-hero">
#         <h1>📊 Quality Assessment Dashboard</h1>
#         <p>AI-powered insights · Real-time analytics · MySQL integrated</p>
#         <span class="record-badge">
#             {len(df)} records · {stats['total_schools']} schools · {len(alerts_df)} alerts
#         </span>
#     </div>
# """, unsafe_allow_html=True)

# # ── KPI CARDS ──
# st.markdown('<p class="section-header">Key Performance Indicators</p>', unsafe_allow_html=True)

# k1, k2, k3, k4 = st.columns(4)

# with k1:
#     st.markdown(f"""
#         <div class="kpi-card kpi-blue">
#             <p class="kpi-label">🏫 Total Schools</p>
#             <p class="kpi-value">{stats['total_schools']}</p>
#             <p class="kpi-sub">in dataset</p>
#         </div>
#     """, unsafe_allow_html=True)

# with k2:
#     st.markdown(f"""
#         <div class="kpi-card kpi-pink">
#             <p class="kpi-label">🍽️ Meals Served</p>
#             <p class="kpi-value">{stats['total_meals_served']:,}</p>
#             <p class="kpi-sub">total across all schools</p>
#         </div>
#     """, unsafe_allow_html=True)

# with k3:
#     waste_cls = "kpi-red" if stats['avg_waste'] > 20 else "kpi-teal"
#     waste_sub = "⚠️ Above threshold" if stats['avg_waste'] > 20 else "✅ Within range"
#     st.markdown(f"""
#         <div class="kpi-card {waste_cls}">
#             <p class="kpi-label">🗑️ Avg Waste</p>
#             <p class="kpi-value">{stats['avg_waste']:.1f}%</p>
#             <p class="kpi-sub">{waste_sub}</p>
#         </div>
#     """, unsafe_allow_html=True)

# with k4:
#     taste_sub = "⭐" * round(stats['avg_taste_rating'])
#     st.markdown(f"""
#         <div class="kpi-card kpi-amber">
#             <p class="kpi-label">⭐ Avg Taste</p>
#             <p class="kpi-value">{stats['avg_taste_rating']:.1f}</p>
#             <p class="kpi-sub">{taste_sub} out of 5</p>
#         </div>
#     """, unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)

# # ── NUTRITION COMPLIANCE ──
# st.markdown('<p class="section-header">Nutritional Compliance</p>', unsafe_allow_html=True)

# n1, n2, n3 = st.columns(3)

# with n1:
#     cal_ok = stats['avg_calorie_compliance'] >= 95
#     st.markdown(f"""
#         <div class="compliance-card green">
#             <p class="compliance-label">Calorie Compliance</p>
#             <p class="compliance-value">{stats['avg_calorie_compliance']:.1f}%</p>
#             <p class="compliance-status">{'✅ On Target' if cal_ok else '⚠️ Below Target'}</p>
#         </div>
#     """, unsafe_allow_html=True)

# with n2:
#     prot_ok = stats['avg_protein_compliance'] >= 95
#     st.markdown(f"""
#         <div class="compliance-card amber">
#             <p class="compliance-label">Protein Compliance</p>
#             <p class="compliance-value">{stats['avg_protein_compliance']:.1f}%</p>
#             <p class="compliance-status">{'✅ On Target' if prot_ok else '⚠️ Below Target'}</p>
#         </div>
#     """, unsafe_allow_html=True)

# with n3:
#     excellent_count = len(quality_df[quality_df['Overall_Quality_Score'] >= 85])
#     ex_rate = (excellent_count / stats['total_schools'] * 100) if stats['total_schools'] else 0
#     st.markdown(f"""
#         <div class="compliance-card blue">
#             <p class="compliance-label">Excellent Schools</p>
#             <p class="compliance-value">{excellent_count}</p>
#             <p class="compliance-status">{ex_rate:.0f}% of all schools</p>
#         </div>
#     """, unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)
# st.divider()

# # ── ALERTS ──
# st.markdown('<p class="section-header">AI-Generated Quality Alerts</p>', unsafe_allow_html=True)

# if not alerts_df.empty:
#     high   = len(alerts_df[alerts_df['Priority'] == 'High'])
#     medium = len(alerts_df[alerts_df['Priority'] == 'Medium'])
#     total  = len(alerts_df)

#     a1, a2, a3 = st.columns(3)
#     with a1:
#         st.markdown(f"""
#             <div class="alert-stat-card red">
#                 <p class="alert-stat-label">🔴 High Priority</p>
#                 <p class="alert-stat-value">{high}</p>
#                 <p class="alert-stat-desc">schools need urgent attention</p>
#             </div>
#         """, unsafe_allow_html=True)
#     with a2:
#         st.markdown(f"""
#             <div class="alert-stat-card amber">
#                 <p class="alert-stat-label">🟡 Medium Priority</p>
#                 <p class="alert-stat-value">{medium}</p>
#                 <p class="alert-stat-desc">schools need monitoring</p>
#             </div>
#         """, unsafe_allow_html=True)
#     with a3:
#         st.markdown(f"""
#             <div class="alert-stat-card indigo">
#                 <p class="alert-stat-label">📊 Total Alerts</p>
#                 <p class="alert-stat-value">{total}</p>
#                 <p class="alert-stat-desc">issues detected</p>
#             </div>
#         """, unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)

#     with st.expander(f"📋 View All {total} Alert Details", expanded=False):
#         for _, alert in alerts_df.head(20).iterrows():
#             is_high   = alert['Priority'] == 'High'
#             card_cls  = 'red' if is_high else 'amber'
#             emoji     = '🔴' if is_high else '🟡'
#             st.markdown(f"""
#                 <div class="alert-detail {card_cls}">
#                     <p class="alert-school">
#                         {emoji} School: <strong>{alert['School_ID']}</strong>
#                         &nbsp;·&nbsp; Date: {alert['Date']}
#                         &nbsp;·&nbsp; Priority: <strong>{alert['Priority']}</strong>
#                     </p>
#             """, unsafe_allow_html=True)
#             for issue in alert['Alerts']:
#                 st.write(f"  ⚠️ {issue}")
#             st.markdown("</div>", unsafe_allow_html=True)
# else:
#     st.markdown("""
#         <div class="no-alert-box">
#             ✅ &nbsp; No Critical Alerts — All Schools Performing Well!
#         </div>
#     """, unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)
# st.divider()

# # ── VISUALIZATIONS ──
# st.markdown('<p class="section-header">Analytics & Visualizations</p>', unsafe_allow_html=True)

# visualizer = Visualizer(df)

# tab1, tab2, tab3, tab4 = st.tabs([
#     "📉 Waste Trends",
#     "🎯 Quality Overview",
#     "🏆 School Rankings",
#     "🥗 Nutrition"
# ])

# with tab1:
#     st.markdown("##### Food Waste Trend Over Time")
#     st.plotly_chart(
#         visualizer.plot_waste_trend(),
#         use_container_width=True,
#         config={'displayModeBar': True, 'displaylogo': False}
#     )
#     st.info("💡 Monitor trends to identify patterns and implement targeted interventions.")

# with tab2:
#     st.markdown("##### Quality Distribution & Radar")
#     c1, c2 = st.columns(2)
#     with c1:
#         st.plotly_chart(
#             visualizer.plot_quality_distribution(quality_df),
#             use_container_width=True,
#             config={'displayModeBar': False}
#         )
#     with c2:
#         st.plotly_chart(
#             visualizer.plot_metrics_radar(quality_df),
#             use_container_width=True,
#             config={'displayModeBar': False}
#         )
#     st.info("💡 The radar chart shows performance balance across all five quality dimensions.")

# with tab3:
#     st.markdown("##### School Performance Comparison")
#     st.plotly_chart(
#         visualizer.plot_school_performance(quality_df),
#         use_container_width=True,
#         config={'displayModeBar': True, 'displaylogo': False}
#     )
#     st.info("💡 Identify top performers and schools needing additional support.")

# with tab4:
#     st.markdown("##### Nutritional Compliance Analysis")
#     st.plotly_chart(
#         visualizer.plot_nutrition_compliance(),
#         use_container_width=True,
#         config={'displayModeBar': True, 'displaylogo': False}
#     )
#     st.info("💡 Both calorie and protein compliance should ideally be at or above 100%.")

# st.markdown("<br>", unsafe_allow_html=True)
# st.divider()

# # ── DATA TABLE ──
# st.markdown('<p class="section-header">Detailed Assessment Records</p>', unsafe_allow_html=True)

# f1, f2, f3 = st.columns(3)
# with f1:
#     min_score = st.slider("🎯 Min Quality Score", 0, 100, 0, 5)
# with f2:
#     selected_schools = st.multiselect(
#         "🏫 Filter Schools",
#         options=sorted(quality_df['School_ID'].unique()),
#         default=sorted(quality_df['School_ID'].unique())
#     )
# with f3:
#     date_range = st.selectbox("📅 Date Range", ["All Dates", "Last 7 Days", "Last 30 Days"])

# filtered_df = quality_df[
#     (quality_df['Overall_Quality_Score'] >= min_score) &
#     (quality_df['School_ID'].isin(selected_schools))
# ]

# st.markdown(f"""
#     <div class="record-badge">
#         Showing {len(filtered_df)} of {len(quality_df)} records
#     </div>
#     <br>
# """, unsafe_allow_html=True)

# # Format columns that exist
# fmt_cols = {c: '{:.2f}' for c in ['Overall_Quality_Score','Nutrition_Score','Waste_Score','Hygiene_Score','Taste_Score','Menu_Score'] if c in filtered_df.columns}

# try:
#     styled = filtered_df.style.background_gradient(
#         cmap='RdYlGn', subset=['Overall_Quality_Score'], vmin=0, vmax=100
#     ).format(fmt_cols)
#     st.dataframe(styled, use_container_width=True, height=440)
# except Exception:
#     st.dataframe(filtered_df, use_container_width=True, height=440)

# st.markdown("<br>", unsafe_allow_html=True)

# d1, d2 = st.columns(2)
# with d1:
#     st.download_button(
#         "📥 Download Filtered Data",
#         data=filtered_df.to_csv(index=False).encode('utf-8'),
#         file_name=f"quality_filtered_{pd.Timestamp.now().strftime('%Y%m%d_%H%M')}.csv",
#         mime="text/csv",
#         use_container_width=True
#     )
# with d2:
#     st.download_button(
#         "📥 Download All Data",
#         data=quality_df.to_csv(index=False).encode('utf-8'),
#         file_name=f"quality_all_{pd.Timestamp.now().strftime('%Y%m%d_%H%M')}.csv",
#         mime="text/csv",
#         use_container_width=True
#     )

# st.markdown("<br><br>", unsafe_allow_html=True)
# st.divider()
# st.markdown("""
#     <div style='text-align:center; padding: 1rem 0; opacity: 0.55; font-size: 0.85rem;'>
#         🍽️ School Meal Quality Monitor &nbsp;·&nbsp; AI-Powered &nbsp;·&nbsp; MySQL Integrated
#     </div>
# """, unsafe_allow_html=True)
"""
pages/4_dashboard.py — Dashboard
Fully theme-safe. Works in Streamlit light + dark mode.
"""
import streamlit as st
import pandas as pd, sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from src.visualizations import Visualizer
from src.auth import is_logged_in, get_current_user, logout
from src.styles import GLOBAL_CSS

# ── AUTH ──
if not is_logged_in(st.session_state):
    st.error("🔒 Please sign in first.")
    if st.button("Go to Login →", type="primary"): st.switch_page("pages/1_login.py")
    st.stop()

current_user = get_current_user(st.session_state)

if 'processing_complete' not in st.session_state or not st.session_state['processing_complete']:
    st.error("❌ No processed data. Please upload and process data first.")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📤 Upload Data", type="primary", use_container_width=True): st.switch_page("pages/2_upload_data.py")
    with c2:
        if st.button("⚙️ Processing", use_container_width=True): st.switch_page("pages/3_processing.py")
    st.stop()

df         = st.session_state['df_processed']
quality_df = st.session_state['quality_df']
alerts_df  = st.session_state['alerts_df']
stats      = st.session_state['stats']

st.set_page_config(page_title="Dashboard · School Meal Monitor", page_icon="📊", layout="wide", initial_sidebar_state="expanded")
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# ── SIDEBAR ──
with st.sidebar:
    st.markdown(f'<div class="sidebar-user-card"><h4>👤 {current_user["full_name"]}</h4><p>Role: {current_user["role"]}</p></div>', unsafe_allow_html=True)

    if st.button("🚪 Sign Out", use_container_width=True):
        logout(st.session_state)
        st.switch_page("pages/1_login.py")

    st.markdown("---")
    st.markdown("""
    <div class="step-bar">
      <div class="step-item"><div class="step-dot done">✓</div><span class="step-text done">Upload</span></div>
      <div class="step-connector done"></div>
      <div class="step-item"><div class="step-dot done">✓</div><span class="step-text done">Process</span></div>
      <div class="step-connector done"></div>
      <div class="step-item"><div class="step-dot active">3</div><span class="step-text active">Dashboard</span></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    if st.button("🏠 Home", use_container_width=True): st.switch_page("app.py")
    if st.button("📤 Upload New Data", use_container_width=True):
        for k in ['data_loaded','processing_complete','meal_data','df_processed','quality_df','alerts_df','stats']:
            st.session_state.pop(k, None)
        st.switch_page("pages/2_upload_data.py")

    st.markdown("---")
    st.markdown(f"""
    <div style="background:var(--surface-1);border:1px solid var(--border);border-radius:var(--r-sm);padding:1rem;font-size:.82rem;">
      <p style="margin:0 0 .35rem;font-weight:700;opacity:.55;font-size:.72rem;text-transform:uppercase;letter-spacing:.07em;">Session</p>
      <p style="margin:.2rem 0;">Records: <strong>{len(df):,}</strong></p>
      <p style="margin:.2rem 0;">Schools: <strong>{stats['total_schools']}</strong></p>
      <p style="margin:.2rem 0;">Alerts: <strong>{len(alerts_df)}</strong></p>
      <p style="margin:0;">Source: <strong>{st.session_state.get('data_source','—').upper()}</strong></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style="background:var(--surface-1);border:1px solid var(--border);border-radius:var(--r-sm);padding:1rem;">
      <p style="margin:0 0 .6rem;font-weight:700;opacity:.55;font-size:.72rem;text-transform:uppercase;letter-spacing:.07em;">Quality Grading</p>
      <p style="margin:.25rem 0;font-size:.82rem;">🟢 <strong>Excellent</strong> — 85–100</p>
      <p style="margin:.25rem 0;font-size:.82rem;">🔵 <strong>Good</strong> — 70–84</p>
      <p style="margin:.25rem 0;font-size:.82rem;">🟡 <strong>Fair</strong> — 50–69</p>
      <p style="margin:0;font-size:.82rem;">🔴 <strong>Poor</strong> — 0–49</p>
    </div>
    """, unsafe_allow_html=True)

# ══ HEADER ══
st.markdown(f"""
<div class="page-header">
  <div class="header-badge">📊 Live Dashboard</div>
  <h1>Quality Assessment Dashboard</h1>
  <p>{len(df):,} records processed · {stats['total_schools']} schools · {len(alerts_df)} active alerts</p>
</div>
""", unsafe_allow_html=True)

# ══ KPI CARDS ══
st.markdown('<div class="section-label"><div class="line"></div><span>Key Performance Indicators</span><div class="line"></div></div>', unsafe_allow_html=True)

k1, k2, k3, k4 = st.columns(4)
waste_cls = "kpi-rose" if stats['avg_waste'] > 20 else "kpi-cyan"
waste_sub = "⚠️ Above threshold" if stats['avg_waste'] > 20 else "✅ Within range"

with k1:
    st.markdown(f'<div class="kpi-card kpi-blue"><span class="kpi-icon">🏫</span><p class="kpi-val">{stats["total_schools"]}</p><p class="kpi-lbl">Total Schools</p><p class="kpi-sub">in dataset</p></div>', unsafe_allow_html=True)
with k2:
    st.markdown(f'<div class="kpi-card kpi-violet"><span class="kpi-icon">🍽️</span><p class="kpi-val">{stats["total_meals_served"]:,}</p><p class="kpi-lbl">Meals Served</p><p class="kpi-sub">total</p></div>', unsafe_allow_html=True)
with k3:
    st.markdown(f'<div class="kpi-card {waste_cls}"><span class="kpi-icon">🗑️</span><p class="kpi-val">{stats["avg_waste"]:.1f}%</p><p class="kpi-lbl">Avg Waste</p><p class="kpi-sub">{waste_sub}</p></div>', unsafe_allow_html=True)
with k4:
    stars = "⭐" * round(stats['avg_taste_rating'])
    st.markdown(f'<div class="kpi-card kpi-amber"><span class="kpi-icon">⭐</span><p class="kpi-val">{stats["avg_taste_rating"]:.1f}</p><p class="kpi-lbl">Avg Taste</p><p class="kpi-sub">{stars} / 5</p></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ══ NUTRITION COMPLIANCE ══
st.markdown('<div class="section-label"><div class="line"></div><span>Nutritional Compliance</span><div class="line"></div></div>', unsafe_allow_html=True)

excellent_count = len(quality_df[quality_df['Overall_Quality_Score'] >= 85])
ex_rate = (excellent_count / stats['total_schools'] * 100) if stats['total_schools'] else 0
cal_ok  = stats['avg_calorie_compliance'] >= 95
prot_ok = stats['avg_protein_compliance'] >= 95

n1, n2, n3 = st.columns(3)
with n1:
    st.markdown(f'<div class="metric-card green"><p class="mc-label">Calorie Compliance</p><p class="mc-value">{stats["avg_calorie_compliance"]:.1f}%</p><p class="mc-status">{"✅ On Target" if cal_ok else "⚠️ Below Target"}</p></div>', unsafe_allow_html=True)
with n2:
    st.markdown(f'<div class="metric-card amber"><p class="mc-label">Protein Compliance</p><p class="mc-value">{stats["avg_protein_compliance"]:.1f}%</p><p class="mc-status">{"✅ On Target" if prot_ok else "⚠️ Below Target"}</p></div>', unsafe_allow_html=True)
with n3:
    st.markdown(f'<div class="metric-card violet"><p class="mc-label">Excellent Schools</p><p class="mc-value">{excellent_count}</p><p class="mc-status">{ex_rate:.0f}% of all schools</p></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.divider()

# ══ ALERTS ══
st.markdown('<div class="section-label"><div class="line"></div><span>AI-Generated Quality Alerts</span><div class="line"></div></div>', unsafe_allow_html=True)

if not alerts_df.empty:
    high   = len(alerts_df[alerts_df['Priority'] == 'High'])
    medium = len(alerts_df[alerts_df['Priority'] == 'Medium'])
    total  = len(alerts_df)

    a1, a2, a3 = st.columns(3)
    with a1:
        st.markdown(f'<div class="alert-stat danger"><span class="as-icon">🔴</span><p class="as-lbl">High Priority</p><p class="as-num">{high}</p><p class="as-desc">schools need urgent attention</p></div>', unsafe_allow_html=True)
    with a2:
        st.markdown(f'<div class="alert-stat warning"><span class="as-icon">🟡</span><p class="as-lbl">Medium Priority</p><p class="as-num">{medium}</p><p class="as-desc">schools need monitoring</p></div>', unsafe_allow_html=True)
    with a3:
        st.markdown(f'<div class="alert-stat info"><span class="as-icon">📊</span><p class="as-lbl">Total Alerts</p><p class="as-num">{total}</p><p class="as-desc">issues detected</p></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander(f"View all {total} alert details", expanded=False):
        for _, alert in alerts_df.head(20).iterrows():
            is_high  = alert['Priority'] == 'High'
            cls      = 'danger' if is_high else 'warning'
            emoji    = '🔴' if is_high else '🟡'
            st.markdown(f"""
            <div class="alert-row {cls}">
              <p class="ar-title">{emoji} &nbsp; School: <strong>{alert['School_ID']}</strong> &nbsp;·&nbsp; Priority: <strong>{alert['Priority']}</strong></p>
              <p class="ar-meta">📅 {alert['Date']}</p>
            </div>
            """, unsafe_allow_html=True)
            for issue in alert['Alerts']:
                st.write(f"  ⚠️ {issue}")
else:
    st.markdown('<div class="no-alerts">✅ &nbsp; No Critical Alerts — All Schools Performing Well!</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.divider()

# ══ CHARTS ══
st.markdown('<div class="section-label"><div class="line"></div><span>Analytics & Visualizations</span><div class="line"></div></div>', unsafe_allow_html=True)

visualizer = Visualizer(df)

tab1, tab2, tab3, tab4 = st.tabs(["📉 Waste Trends", "🎯 Quality Overview", "🏆 School Rankings", "🥗 Nutrition"])

cfg = {'displayModeBar': True, 'displaylogo': False}

with tab1:
    st.markdown("##### Average Food Waste Over Time")
    st.plotly_chart(visualizer.plot_waste_trend(), use_container_width=True, config=cfg)
    st.info("💡 Monitor waste trends to identify patterns and implement targeted interventions across schools.")

with tab2:
    st.markdown("##### Quality Distribution & Dimension Radar")
    c1, c2 = st.columns(2)
    with c1:
        st.plotly_chart(visualizer.plot_quality_distribution(quality_df), use_container_width=True, config={'displayModeBar':False})
    with c2:
        st.plotly_chart(visualizer.plot_metrics_radar(quality_df), use_container_width=True, config={'displayModeBar':False})
    st.info("💡 The radar chart shows performance balance across all five quality dimensions.")

with tab3:
    st.markdown("##### School-by-School Performance Comparison")
    st.plotly_chart(visualizer.plot_school_performance(quality_df), use_container_width=True, config=cfg)
    st.info("💡 Identify top performers and schools needing additional support and resources.")

with tab4:
    st.markdown("##### Calorie & Protein Compliance")
    st.plotly_chart(visualizer.plot_nutrition_compliance(), use_container_width=True, config=cfg)
    st.info("💡 Both calorie and protein compliance should ideally be at or above 100% of the required target.")

st.markdown("<br>", unsafe_allow_html=True)
st.divider()

# ══ DATA TABLE ══
st.markdown('<div class="section-label"><div class="line"></div><span>Detailed Assessment Records</span><div class="line"></div></div>', unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)
with f1:
    min_score = st.slider("Min Quality Score", 0, 100, 0, 5)
with f2:
    selected_schools = st.multiselect(
        "Filter Schools",
        options=sorted(quality_df['School_ID'].unique()),
        default=sorted(quality_df['School_ID'].unique())
    )
with f3:
    date_range = st.selectbox("Date Range", ["All Dates", "Last 7 Days", "Last 30 Days"])

filtered_df = quality_df[
    (quality_df['Overall_Quality_Score'] >= min_score) &
    (quality_df['School_ID'].isin(selected_schools))
]

st.markdown(f'<div class="count-pill">📋 &nbsp; Showing {len(filtered_df):,} of {len(quality_df):,} records</div>', unsafe_allow_html=True)

score_cols = [c for c in ['Overall_Quality_Score','Nutrition_Score','Waste_Score','Hygiene_Score','Taste_Score','Menu_Score'] if c in filtered_df.columns]
fmt = {c: '{:.2f}' for c in score_cols}

try:
    styled = filtered_df.style.background_gradient(cmap='RdYlGn', subset=['Overall_Quality_Score'], vmin=0, vmax=100).format(fmt)
    st.dataframe(styled, use_container_width=True, height=440)
except Exception:
    st.dataframe(filtered_df, use_container_width=True, height=440)

st.markdown("<br>", unsafe_allow_html=True)
d1, d2 = st.columns(2)
with d1:
    st.download_button(
        "📥 Download Filtered Report",
        data=filtered_df.to_csv(index=False).encode(),
        file_name=f"quality_filtered_{pd.Timestamp.now().strftime('%Y%m%d_%H%M')}.csv",
        mime="text/csv", use_container_width=True
    )
with d2:
    st.download_button(
        "📥 Download Full Dataset",
        data=quality_df.to_csv(index=False).encode(),
        file_name=f"quality_full_{pd.Timestamp.now().strftime('%Y%m%d_%H%M')}.csv",
        mime="text/csv", use_container_width=True
    )

st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.markdown("""
<div style="text-align:center;padding:1.2rem 0;opacity:.35;font-size:.82rem;letter-spacing:.04em;">
  🍽️ &nbsp; School Meal Quality Monitor &nbsp;·&nbsp; AI-Powered Assessment &nbsp;·&nbsp; MySQL Integrated
</div>
""", unsafe_allow_html=True)