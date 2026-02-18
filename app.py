# # """
# # School Meal Quality Monitor - Landing Page
# # """

# # import streamlit as st
# # from pathlib import Path
# # import sys

# # # Add src to path
# # sys.path.append(str(Path(__file__).parent))

# # from src.auth import is_logged_in, get_current_user

# # # Page config
# # st.set_page_config(
# #     page_title="School Meal Quality Monitor",
# #     page_icon="🍽️",
# #     layout="wide",
# #     initial_sidebar_state="collapsed"
# # )

# # # Custom CSS
# # st.markdown("""
# #     <style>
# #     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
    
# #     * {
# #         font-family: 'Inter', sans-serif;
# #     }
    
# #     .main {
# #         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
# #         padding: 0;
# #     }
    
# #     /* Hide Streamlit elements */
# #     #MainMenu {visibility: hidden;}
# #     footer {visibility: hidden;}
# #     header {visibility: hidden;}
    
# #     .hero-section {
# #         text-align: center;
# #         padding: 6rem 2rem 4rem 2rem;
# #         color: white;
# #     }
    
# #     .hero-title {
# #         font-size: 5rem;
# #         font-weight: 900;
# #         margin-bottom: 1rem;
# #         text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
# #         animation: fadeInDown 1s ease-in-out;
# #     }
    
# #     .hero-subtitle {
# #         font-size: 1.8rem;
# #         font-weight: 400;
# #         opacity: 0.95;
# #         margin-bottom: 3rem;
# #         animation: fadeInUp 1s ease-in-out;
# #     }
    
# #     @keyframes fadeInDown {
# #         from {
# #             opacity: 0;
# #             transform: translateY(-30px);
# #         }
# #         to {
# #             opacity: 1;
# #             transform: translateY(0);
# #         }
# #     }
    
# #     @keyframes fadeInUp {
# #         from {
# #             opacity: 0;
# #             transform: translateY(30px);
# #         }
# #         to {
# #             opacity: 1;
# #             transform: translateY(0);
# #         }
# #     }
    
# #     .feature-card {
# #         background: white;
# #         padding: 2.5rem;
# #         border-radius: 25px;
# #         box-shadow: 0 15px 35px rgba(0,0,0,0.15);
# #         margin: 1rem;
# #         transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
# #         height: 100%;
# #     }
    
# #     .feature-card:hover {
# #         transform: translateY(-15px) scale(1.02);
# #         box-shadow: 0 25px 50px rgba(0,0,0,0.25);
# #     }
    
# #     .feature-icon {
# #         font-size: 4rem;
# #         margin-bottom: 1.5rem;
# #         display: inline-block;
# #         animation: bounce 2s infinite;
# #     }
    
# #     @keyframes bounce {
# #         0%, 100% { transform: translateY(0); }
# #         50% { transform: translateY(-10px); }
# #     }
    
# #     .feature-title {
# #         font-size: 1.6rem;
# #         font-weight: 800;
# #         color: #1e293b;
# #         margin-bottom: 1rem;
# #     }
    
# #     .feature-desc {
# #         color: #64748b;
# #         line-height: 1.8;
# #         font-size: 1.05rem;
# #     }
    
# #     .stats-container {
# #         background: rgba(255, 255, 255, 0.15);
# #         backdrop-filter: blur(15px);
# #         border-radius: 25px;
# #         padding: 2.5rem;
# #         margin: 3rem 0;
# #         box-shadow: 0 10px 30px rgba(0,0,0,0.2);
# #     }
    
# #     .stat-item {
# #         text-align: center;
# #         color: white;
# #     }
    
# #     .stat-number {
# #         font-size: 4rem;
# #         font-weight: 900;
# #         text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
# #     }
    
# #     .stat-label {
# #         font-size: 1.1rem;
# #         opacity: 0.95;
# #         font-weight: 600;
# #     }
    
# #     .cta-section {
# #         background: white;
# #         padding: 4rem 2rem;
# #         border-radius: 30px 30px 0 0;
# #         margin-top: 4rem;
# #     }
    
# #     .stButton>button {
# #         background: linear-gradient(135deg, #10b981 0%, #059669 100%);
# #         color: white;
# #         border-radius: 50px;
# #         padding: 1.2rem 4rem;
# #         font-size: 1.3rem;
# #         font-weight: 800;
# #         border: none;
# #         box-shadow: 0 15px 35px rgba(16, 185, 129, 0.4);
# #         transition: all 0.3s ease;
# #         text-transform: uppercase;
# #         letter-spacing: 1px;
# #     }
    
# #     .stButton>button:hover {
# #         transform: translateY(-5px);
# #         box-shadow: 0 20px 45px rgba(16, 185, 129, 0.5);
# #     }
# #     </style>
# # """, unsafe_allow_html=True)

# # # Check if logged in
# # if is_logged_in(st.session_state):
# #     user_info = get_current_user(st.session_state)
    
# #     # Show logged in navigation in corner
# #     col1, col2 = st.columns([6, 1])
# #     with col2:
# #         if st.button("🚪 Logout", key="logout_btn"):
# #             from src.auth import logout
# #             logout(st.session_state)
# #             st.rerun()

# # # Hero Section
# # st.markdown("""
# #     <div class="hero-section">
# #         <div class="hero-title">
# #             🍽️ School Meal<br>Quality Monitor
# #         </div>
# #         <div class="hero-subtitle">
# #             AI-Powered Quality Assessment for Better Student Nutrition
# #         </div>
# #     </div>
# # """, unsafe_allow_html=True)

# # # Stats Section
# # col1, col2, col3, col4 = st.columns(4)

# # with col1:
# #     st.markdown("""
# #         <div class="stats-container">
# #             <div class="stat-item">
# #                 <div class="stat-number">5</div>
# #                 <div class="stat-label">Quality Dimensions</div>
# #             </div>
# #         </div>
# #     """, unsafe_allow_html=True)

# # with col2:
# #     st.markdown("""
# #         <div class="stats-container">
# #             <div class="stat-item">
# #                 <div class="stat-number">100%</div>
# #                 <div class="stat-label">Explainable AI</div>
# #             </div>
# #         </div>
# #     """, unsafe_allow_html=True)

# # with col3:
# #     st.markdown("""
# #         <div class="stats-container">
# #             <div class="stat-item">
# #                 <div class="stat-number">$0</div>
# #                 <div class="stat-label">Hardware Cost</div>
# #             </div>
# #         </div>
# #     """, unsafe_allow_html=True)

# # with col4:
# #     st.markdown("""
# #         <div class="stats-container">
# #             <div class="stat-item">
# #                 <div class="stat-number">5s</div>
# #                 <div class="stat-label">Analysis Time</div>
# #             </div>
# #         </div>
# #     """, unsafe_allow_html=True)

# # # White Section for Features
# # st.markdown('<div class="cta-section">', unsafe_allow_html=True)

# # # Features
# # st.markdown("""
# #     <h2 style='text-align: center; color: #1e293b; font-size: 3rem; font-weight: 900; margin-bottom: 4rem;'>
# #         ✨ Key Features
# #     </h2>
# # """, unsafe_allow_html=True)

# # col1, col2, col3 = st.columns(3)

# # with col1:
# #     st.markdown("""
# #         <div class="feature-card">
# #             <div class="feature-icon">📊</div>
# #             <div class="feature-title">Multi-Dimensional</div>
# #             <div class="feature-desc">
# #                 Evaluates nutrition, waste, hygiene, taste, and menu compliance
# #             </div>
# #         </div>
# #     """, unsafe_allow_html=True)

# # with col2:
# #     st.markdown("""
# #         <div class="feature-card">
# #             <div class="feature-icon">🤖</div>
# #             <div class="feature-title">AI-Powered</div>
# #             <div class="feature-desc">
# #                 Intelligent alerts and prioritized recommendations
# #             </div>
# #         </div>
# #     """, unsafe_allow_html=True)

# # with col3:
# #     st.markdown("""
# #         <div class="feature-card">
# #             <div class="feature-icon">📈</div>
# #             <div class="feature-title">Real-Time Analytics</div>
# #             <div class="feature-desc">
# #                 Interactive dashboards with live visualizations
# #             </div>
# #         </div>
# #     """, unsafe_allow_html=True)

# # st.markdown("<br><br>", unsafe_allow_html=True)

# # col1, col2, col3 = st.columns(3)

# # with col1:
# #     st.markdown("""
# #         <div class="feature-card">
# #             <div class="feature-icon">💡</div>
# #             <div class="feature-title">Actionable Insights</div>
# #             <div class="feature-desc">
# #                 Specific recommendations, not just data
# #             </div>
# #         </div>
# #     """, unsafe_allow_html=True)

# # with col2:
# #     st.markdown("""
# #         <div class="feature-card">
# #             <div class="feature-icon">🔒</div>
# #             <div class="feature-title">Secure</div>
# #             <div class="feature-desc">
# #                 MySQL database with encrypted storage
# #             </div>
# #         </div>
# #     """, unsafe_allow_html=True)

# # with col3:
# #     st.markdown("""
# #         <div class="feature-card">
# #             <div class="feature-icon">⚡</div>
# #             <div class="feature-title">Lightning Fast</div>
# #             <div class="feature-desc">
# #                 Process data in seconds
# #             </div>
# #         </div>
# #     """, unsafe_allow_html=True)

# # # CTA
# # st.markdown("<br><br><br>", unsafe_allow_html=True)
# # st.markdown("""
# #     <h2 style='text-align: center; color: #1e293b; font-size: 2.5rem; font-weight: 800; margin-bottom: 3rem;'>
# #         Ready to Get Started?
# #     </h2>
# # """, unsafe_allow_html=True)

# # col1, col2, col3 = st.columns([1, 1, 1])

# # with col2:
# #     if is_logged_in(st.session_state):
# #         if st.button("🚀 Go to Dashboard", use_container_width=True, type="primary"):
# #             st.switch_page("pages/2_upload_data.py")
# #     else:
# #         if st.button("🔐 Login to Start", use_container_width=True, type="primary"):
# #             st.switch_page("pages/1_login.py")

# # st.markdown('</div>', unsafe_allow_html=True)

# """
# app.py — Landing Page  
# Deep navy · Fraunces + Plus Jakarta Sans · Theme-safe
# """
# import streamlit as st
# import sys
# from pathlib import Path

# sys.path.append(str(Path(__file__).parent))
# from src.auth import is_logged_in, get_current_user
# from src.styles import GLOBAL_CSS

# st.set_page_config(
#     page_title="School Meal Quality Monitor",
#     page_icon="🍽️",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
# st.markdown("""
# <style>
# .stApp { background:#0c1526 !important; }
# .main .block-container { padding-top:0 !important; max-width:100% !important; padding-left:0 !important; padding-right:0 !important; }

# /* HERO */
# .hero { position:relative; padding:8rem 4rem 5rem; text-align:center; overflow:hidden; background:#0c1526; }
# .hero-mesh { position:absolute; inset:0; pointer-events:none;
#   background:
#     radial-gradient(ellipse 80% 55% at 15% -5%, rgba(59,130,246,0.28) 0%, transparent 65%),
#     radial-gradient(ellipse 60% 45% at 85% 5%,  rgba(139,92,246,0.22) 0%, transparent 65%),
#     radial-gradient(ellipse 50% 40% at 50% 95%, rgba(6,182,212,0.14)  0%, transparent 65%); }
# .hero-grid { position:absolute; inset:0; pointer-events:none;
#   background-image: linear-gradient(rgba(255,255,255,0.022) 1px,transparent 1px), linear-gradient(90deg,rgba(255,255,255,0.022) 1px,transparent 1px);
#   background-size:52px 52px; }
# .hero-inner { position:relative; z-index:2; max-width:800px; margin:0 auto; }
# .hero-pill { display:inline-flex; align-items:center; gap:.5rem;
#   background:rgba(59,130,246,0.12); border:1px solid rgba(59,130,246,0.32); color:#93c5fd;
#   padding:.45rem 1.2rem; border-radius:50px; font-size:.78rem; font-weight:700;
#   letter-spacing:.08em; text-transform:uppercase; margin-bottom:2rem; }
# .hero-title { font-family:'Fraunces',serif !important; font-size:clamp(3rem,7vw,5.5rem);
#   font-weight:900; color:#f0f6ff; line-height:1.05; margin:0 0 1.5rem; letter-spacing:-.02em; }
# .hero-title .accent { background:linear-gradient(135deg,#60a5fa 0%,#a78bfa 50%,#34d399 100%);
#   -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; }
# .hero-sub { font-size:1.15rem; color:#7a8fa8; max-width:520px; margin:0 auto 3.5rem; line-height:1.75; font-weight:400; }
# .stats-row { display:flex; justify-content:center; gap:1rem; flex-wrap:wrap; margin-bottom:3.5rem; }
# .stat-chip { background:rgba(255,255,255,0.045); border:1px solid rgba(255,255,255,0.09);
#   border-radius:14px; padding:1.1rem 1.8rem; min-width:130px; text-align:center; transition:all .3s ease; }
# .stat-chip:hover { background:rgba(59,130,246,0.12); border-color:rgba(59,130,246,0.3); transform:translateY(-5px); }
# .stat-chip .sn { font-family:'Fraunces',serif !important; font-size:2rem; font-weight:700; color:#e2eeff; line-height:1; margin-bottom:.3rem; }
# .stat-chip .sl { font-size:.72rem; font-weight:600; text-transform:uppercase; letter-spacing:.07em; color:#4d6480; }

# /* FEATURES */
# .features { background:#0c1526; padding:5rem 3rem; border-top:1px solid rgba(255,255,255,0.05); }
# .eyebrow { text-align:center; font-size:.72rem; font-weight:800; letter-spacing:.14em; text-transform:uppercase; color:#3b82f6; margin-bottom:.8rem; }
# .sec-title { font-family:'Fraunces',serif !important; text-align:center; font-size:clamp(1.8rem,3.5vw,2.8rem);
#   font-weight:700; color:#e8f0fe; margin:0 0 .8rem; letter-spacing:-.01em; }
# .sec-sub { text-align:center; color:#4d6480; font-size:.95rem; max-width:440px; margin:0 auto 3.5rem; line-height:1.7; }

# .feat { background:rgba(255,255,255,0.028); border:1px solid rgba(255,255,255,0.07);
#   border-radius:20px; padding:2rem 1.8rem; height:100%;
#   transition:all .35s cubic-bezier(.23,1,.32,1); position:relative; overflow:hidden; }
# .feat::before { content:''; position:absolute; top:0; left:0; right:0; height:2px; opacity:0; transition:opacity .3s ease; }
# .feat:hover { background:rgba(255,255,255,0.055); border-color:rgba(59,130,246,0.25);
#   transform:translateY(-8px); box-shadow:0 20px 48px rgba(0,0,0,0.5); }
# .feat:hover::before { opacity:1; }
# .feat.b1::before{background:linear-gradient(90deg,#3b82f6,#6366f1);}
# .feat.b2::before{background:linear-gradient(90deg,#8b5cf6,#ec4899);}
# .feat.b3::before{background:linear-gradient(90deg,#06b6d4,#3b82f6);}
# .feat.b4::before{background:linear-gradient(90deg,#10b981,#06b6d4);}
# .feat.b5::before{background:linear-gradient(90deg,#f59e0b,#f97316);}
# .feat.b6::before{background:linear-gradient(90deg,#f43f5e,#ec4899);}
# .feat-icon { width:48px; height:48px; border-radius:12px; display:flex; align-items:center; justify-content:center;
#   font-size:1.4rem; margin-bottom:1.3rem; border:1px solid rgba(255,255,255,0.1); }
# .feat-icon.i1{background:rgba(59,130,246,0.15);}
# .feat-icon.i2{background:rgba(139,92,246,0.15);}
# .feat-icon.i3{background:rgba(6,182,212,0.15);}
# .feat-icon.i4{background:rgba(16,185,129,0.15);}
# .feat-icon.i5{background:rgba(245,158,11,0.15);}
# .feat-icon.i6{background:rgba(244,63,94,0.15);}
# .feat h3 { font-size:1.05rem; font-weight:700; color:#dde8f5; margin:0 0 .55rem; }
# .feat p  { font-size:.88rem; color:#4d6480; line-height:1.65; margin:0; }

# /* HOW IT WORKS */
# .how { background:rgba(255,255,255,0.018); border-top:1px solid rgba(255,255,255,0.05);
#   border-bottom:1px solid rgba(255,255,255,0.05); padding:5rem 3rem; }
# .step-c { text-align:center; padding:1.5rem 1rem; }
# .step-num { width:52px; height:52px; border-radius:50%;
#   background:linear-gradient(135deg,#2563eb,#1d4ed8); color:#fff;
#   font-size:1.2rem; font-weight:800; display:flex; align-items:center; justify-content:center;
#   margin:0 auto 1.2rem; box-shadow:0 6px 20px rgba(37,99,235,0.38); }
# .step-ico { font-size:2rem; margin-bottom:.8rem; }
# .step-t { font-size:1rem; font-weight:700; color:#dde8f5; margin:0 0 .45rem; }
# .step-d { font-size:.86rem; color:#4d6480; line-height:1.6; margin:0; }
# .arrow-c { display:flex; align-items:flex-start; justify-content:center; padding-top:2.5rem; color:#1e3a5f; font-size:1.4rem; }

# /* CTA */
# .cta { background:#0c1526; padding:7rem 2rem; text-align:center;
#   position:relative; overflow:hidden; border-top:1px solid rgba(255,255,255,0.05); }
# .cta::before { content:''; position:absolute; inset:0;
#   background:radial-gradient(ellipse 70% 55% at 50% 100%,rgba(37,99,235,0.18) 0%,transparent 70%); pointer-events:none; }
# .cta-inner { position:relative; z-index:1; }
# .cta-t { font-family:'Fraunces',serif !important; font-size:clamp(2rem,4.5vw,3.4rem);
#   font-weight:700; color:#e8f0fe; margin:0 0 .8rem; letter-spacing:-.01em; }
# .cta-s { color:#4d6480; font-size:1rem; margin:0 0 3rem; }

# /* FOOTER */
# .footer { background:#080e1a; border-top:1px solid rgba(255,255,255,0.04);
#   padding:1.8rem 2rem; text-align:center; color:#2a3a52; font-size:.82rem; letter-spacing:.02em; }
# </style>
# """, unsafe_allow_html=True)

# # ── Logout pill if already logged in ──
# if is_logged_in(st.session_state):
#     _, btn_col = st.columns([9, 1])
#     with btn_col:
#         if st.button("Logout →"):
#             from src.auth import logout
#             logout(st.session_state)
#             st.rerun()

# # ══ HERO ══
# st.markdown("""
# <div class="hero">
#   <div class="hero-mesh"></div><div class="hero-grid"></div>
#   <div class="hero-inner">
#     <div class="hero-pill">🤖 &nbsp; Rule-Based AI Assessment Engine</div>
#     <h1 class="hero-title">School Meal<br><span class="accent">Quality Monitor</span></h1>
#     <p class="hero-sub">Ensure every student receives nutritious, hygienic, and high-quality meals — powered by intelligent, explainable AI and real-time analytics.</p>
#     <div class="stats-row">
#       <div class="stat-chip"><div class="sn">5</div><div class="sl">Quality Dimensions</div></div>
#       <div class="stat-chip"><div class="sn">100%</div><div class="sl">Explainable AI</div></div>
#       <div class="stat-chip"><div class="sn">$0</div><div class="sl">Hardware Cost</div></div>
#       <div class="stat-chip"><div class="sn">&lt;5s</div><div class="sl">Analysis Time</div></div>
#     </div>
#   </div>
# </div>
# """, unsafe_allow_html=True)

# _, mid, _ = st.columns([2.5, 1, 2.5])
# with mid:
#     lbl = "Open Dashboard →" if is_logged_in(st.session_state) else "Get Started →"
#     if st.button(lbl, use_container_width=True, type="primary", key="hero_cta"):
#         st.switch_page("pages/2_upload_data.py" if is_logged_in(st.session_state) else "pages/1_login.py")

# st.markdown("<br>", unsafe_allow_html=True)

# # ══ FEATURES ══
# st.markdown("""
# <div class="features">
#   <p class="eyebrow">What We Offer</p>
#   <h2 class="sec-title">Everything You Need to Monitor Meal Quality</h2>
#   <p class="sec-sub">A complete platform for school meal assessment with clarity and confidence.</p>
# </div>
# """, unsafe_allow_html=True)

# feats = [
#     ("b1","i1","📊","Multi-Dimensional Analysis","Simultaneously scores Nutrition, Waste, Hygiene, Taste & Menu Compliance with weighted precision."),
#     ("b2","i2","🤖","Explainable AI Engine","Rule-based expert system delivers transparent, auditable scores — no black boxes."),
#     ("b3","i3","📈","Real-Time Analytics","Interactive Plotly charts give instant visual insight into performance trends."),
#     ("b4","i4","💡","Actionable Recommendations","Converts data into prioritised, specific improvement steps — not just numbers."),
#     ("b5","i5","💾","MySQL Integration","Enterprise-grade backend for secure, structured, scalable data storage."),
#     ("b6","i6","🔒","Secure Authentication","Role-based login with hashed credentials keeps your data protected."),
# ]
# r1 = st.columns(3)
# r2 = st.columns(3)
# for col, (bc, ic, icon, title, desc) in zip(list(r1)+list(r2), feats):
#     with col:
#         st.markdown(f'<div class="feat {bc}"><div class="feat-icon {ic}">{icon}</div><h3>{title}</h3><p>{desc}</p></div>', unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)

# # ══ HOW IT WORKS ══
# st.markdown("""
# <div class="how">
#   <p class="eyebrow">Simple Workflow</p>
#   <h2 class="sec-title">Three Steps to Insights</h2>
#   <p class="sec-sub">From raw meal data to actionable quality insights in under a minute.</p>
# </div>
# """, unsafe_allow_html=True)

# s1, ar1, s2, ar2, s3 = st.columns([3,1,3,1,3])
# steps = [
#     (s1,"1","📤","Upload or Connect","Upload a CSV or connect directly to your MySQL database with one click."),
#     (s2,"2","⚙️","AI Processing","Our rule-based AI scores every record across 5 dimensions with weighted precision."),
#     (s3,"3","📊","View Insights","Explore alerts, charts, school rankings, and downloadable PDF/CSV reports."),
# ]
# for col, num, icon, title, desc in steps:
#     with col:
#         st.markdown(f'<div class="step-c"><div class="step-num">{num}</div><div class="step-ico">{icon}</div><p class="step-t">{title}</p><p class="step-d">{desc}</p></div>', unsafe_allow_html=True)
# with ar1: st.markdown('<div class="arrow-c">→</div>', unsafe_allow_html=True)
# with ar2: st.markdown('<div class="arrow-c">→</div>', unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)

# # ══ FINAL CTA ══
# st.markdown("""
# <div class="cta"><div class="cta-inner">
#   <h2 class="cta-t">Ready to Improve Meal Quality?</h2>
#   <p class="cta-s">Sign in and start monitoring in under a minute — no hardware required.</p>
# </div></div>
# """, unsafe_allow_html=True)

# _, mid2, _ = st.columns([2.5, 1, 2.5])
# with mid2:
#     lbl2 = "Open Dashboard →" if is_logged_in(st.session_state) else "Sign In →"
#     if st.button(lbl2, use_container_width=True, type="primary", key="cta2"):
#         st.switch_page("pages/2_upload_data.py" if is_logged_in(st.session_state) else "pages/1_login.py")

# st.markdown("<br>", unsafe_allow_html=True)
# st.markdown('<div class="footer">🍽️ &nbsp; School Meal Quality Monitor &nbsp;·&nbsp; AI-Powered Assessment &nbsp;·&nbsp; Built with Python &amp; Streamlit</div>', unsafe_allow_html=True)

"""
app.py — Landing Page
Follows device light/dark theme. No forced background.
Cohesive branded hero sections with transparent feature cards.
"""
import streamlit as st, sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
from src.auth import is_logged_in
from src.styles import SHARED_CSS

st.set_page_config(
    page_title="School Meal Quality Monitor",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(SHARED_CSS, unsafe_allow_html=True)

# ── Landing-only CSS ──
st.markdown("""
<style>
/* Full-width hero, override block padding */
section[data-testid="stMain"] > div:first-child { padding-top:0 !important; }
.main .block-container { padding-top:0 !important; max-width:100% !important; padding-left:0 !important; padding-right:0 !important; }

/* ── HERO — branded gradient, always readable ── */
.hero {
    padding: 6rem 2rem 4.5rem;
    text-align: center;
    background: linear-gradient(150deg, #0f2d6b 0%, #1e40af 45%, #2563eb 100%);
    position: relative; overflow: hidden;
}
.hero-glow {
    position:absolute; inset:0; pointer-events:none;
    background:
        radial-gradient(circle 600px at 10% 30%, rgba(255,255,255,0.06) 0%,transparent 60%),
        radial-gradient(circle 400px at 90% 70%, rgba(255,255,255,0.04) 0%,transparent 60%);
}
.hero-dots {
    position:absolute; inset:0; pointer-events:none;
    background-image: radial-gradient(rgba(255,255,255,0.07) 1px, transparent 1px);
    background-size: 30px 30px;
}
.hero-inner { position:relative; z-index:2; max-width:740px; margin:0 auto; }

.hero-tag {
    display:inline-flex; align-items:center; gap:.45rem;
    background:rgba(255,255,255,0.14); border:1px solid rgba(255,255,255,0.22);
    color:#fff; padding:.38rem 1.1rem; border-radius:50px;
    font-size:.72rem; font-weight:700; letter-spacing:.08em;
    text-transform:uppercase; margin-bottom:1.7rem;
}
.hero-title {
    font-family:'Lora',serif !important;
    font-size: clamp(2.6rem, 6vw, 4.8rem);
    font-weight:700; color:#fff; line-height:1.1;
    margin:0 0 1.2rem; letter-spacing:-.015em;
}
.hero-title em { font-style:italic; color:#bfdbfe; }
.hero-sub {
    font-size:1.05rem; color:rgba(255,255,255,.76);
    max-width:500px; margin:0 auto 2.8rem;
    line-height:1.75; font-weight:400;
}

/* Stats */
.stat-row {
    display:flex; justify-content:center;
    gap:.85rem; flex-wrap:wrap; margin-bottom:2.8rem;
}
.sc-chip {
    background:rgba(255,255,255,0.11); border:1px solid rgba(255,255,255,0.17);
    border-radius:12px; padding:.9rem 1.4rem; min-width:115px;
    text-align:center; transition:all .22s ease;
}
.sc-chip:hover { background:rgba(255,255,255,.18); transform:translateY(-3px); }
.sc-chip .cn {
    font-family:'Lora',serif !important;
    font-size:1.8rem; font-weight:700; color:#fff; line-height:1; margin-bottom:.2rem;
}
.sc-chip .cl {
    font-size:.68rem; font-weight:600; text-transform:uppercase;
    letter-spacing:.07em; color:rgba(255,255,255,.62);
}

/* ── INNER CONTENT wrapper — restores normal width ── */
.content-wrap { max-width:1180px; margin:0 auto; padding:0 2rem; }

/* ── FEATURES — no bg override ── */
.feat-grid { padding:4.5rem 0; }
.eyebrow {
    text-align:center; font-size:.68rem; font-weight:800;
    letter-spacing:.13em; text-transform:uppercase;
    color:#2563eb; margin-bottom:.65rem;
}
.s-title {
    font-family:'Lora',serif !important;
    text-align:center; font-size:clamp(1.6rem,3vw,2.4rem);
    font-weight:700; margin:0 0 .65rem; letter-spacing:-.01em; line-height:1.25;
}
.s-sub {
    text-align:center; opacity:.52; font-size:.92rem;
    max-width:420px; margin:0 auto 3rem; line-height:1.7;
}

.f-card {
    background:var(--surf); border:1px solid var(--bdr);
    border-radius:var(--r3); padding:1.8rem 1.6rem; height:100%;
    transition:all .28s cubic-bezier(.23,1,.32,1);
    position:relative; overflow:hidden;
}
.f-card::before {
    content:''; position:absolute; top:0;left:0;right:0;
    height:2.5px; opacity:0; transition:opacity .25s;
}
.f-card:hover { border-color:var(--b-bd); transform:translateY(-5px); box-shadow:0 12px 32px var(--b-gl); }
.f-card:hover::before { opacity:1; }
.c1::before{background:linear-gradient(90deg,#2563eb,#6366f1);}
.c2::before{background:linear-gradient(90deg,#7c3aed,#db2777);}
.c3::before{background:linear-gradient(90deg,#0891b2,#2563eb);}
.c4::before{background:linear-gradient(90deg,#059669,#0891b2);}
.c5::before{background:linear-gradient(90deg,#d97706,#ea580c);}
.c6::before{background:linear-gradient(90deg,#dc2626,#db2777);}

.f-icon {
    width:44px; height:44px; border-radius:11px;
    display:flex; align-items:center; justify-content:center;
    font-size:1.25rem; margin-bottom:1.1rem;
    background:var(--surf-2); border:1px solid var(--bdr);
}
.f-card h3 { font-size:.97rem; font-weight:700; margin:0 0 .42rem; line-height:1.3; }
.f-card p  { font-size:.83rem; opacity:.55; line-height:1.65; margin:0; }

/* ── HOW IT WORKS ── */
.how-sec { padding:4rem 0; border-top:1px solid var(--bdr); }
.step-box { text-align:center; padding:.8rem .5rem; }
.s-num {
    width:46px; height:46px; border-radius:50%;
    background:linear-gradient(135deg,#2563eb,#1d4ed8); color:#fff;
    font-size:1rem; font-weight:800;
    display:flex; align-items:center; justify-content:center;
    margin:0 auto .9rem; box-shadow:0 6px 16px rgba(37,99,235,.30);
}
.s-ico { font-size:1.7rem; margin-bottom:.65rem; }
.s-t { font-size:.95rem; font-weight:700; margin:0 0 .35rem; }
.s-d { font-size:.82rem; opacity:.52; line-height:1.6; margin:0; }
.arrow-box {
    display:flex; align-items:center; justify-content:center;
    padding-top:1.5rem; opacity:.22; font-size:1.1rem;
}

/* ── BOTTOM CTA — branded, always readable ── */
.b-cta {
    padding:5rem 2rem;
    background:linear-gradient(150deg,#0f2d6b 0%,#1e40af 50%,#2563eb 100%);
    text-align:center; position:relative; overflow:hidden;
    margin-top:1rem;
}
.b-cta::before {
    content:''; position:absolute; inset:0;
    background-image:radial-gradient(rgba(255,255,255,0.055) 1px,transparent 1px);
    background-size:28px 28px; pointer-events:none;
}
.b-cta-inner { position:relative; z-index:1; max-width:560px; margin:0 auto; }
.b-cta h2 {
    font-family:'Lora',serif !important;
    font-size:clamp(1.7rem,3.5vw,2.8rem); font-weight:700;
    color:#fff; margin:0 0 .75rem; letter-spacing:-.01em;
}
.b-cta p { color:rgba(255,255,255,.68); font-size:.95rem; margin:0 0 2.3rem; }

/* Footer */
.site-ft {
    padding:1.4rem 2rem; text-align:center;
    opacity:.38; font-size:.78rem; letter-spacing:.04em;
    border-top:1px solid var(--bdr);
}
</style>
""", unsafe_allow_html=True)

# ── Logout if already logged in ──
if is_logged_in(st.session_state):
    _, btn_col = st.columns([11, 1])
    with btn_col:
        if st.button("Logout"):
            from src.auth import logout
            logout(st.session_state)
            st.rerun()

# ════════════════════════════════════════
# HERO
# ════════════════════════════════════════
st.markdown("""
<div class="hero">
  <div class="hero-glow"></div>
  <div class="hero-dots"></div>
  <div class="hero-inner">
    <div class="hero-tag">🤖 &nbsp; AI-Powered Quality Assessment</div>
    <h1 class="hero-title">School Meal<br><em>Quality Monitor</em></h1>
    <p class="hero-sub">
      Ensure every student receives nutritious, hygienic and
      high-quality meals — powered by explainable AI and real-time analytics.
    </p>
    <div class="stat-row">
      <div class="sc-chip"><div class="cn">5</div><div class="cl">Dimensions</div></div>
      <div class="sc-chip"><div class="cn">100%</div><div class="cl">Explainable AI</div></div>
      <div class="sc-chip"><div class="cn">$0</div><div class="cl">Hardware Cost</div></div>
      <div class="sc-chip"><div class="cn">&lt;5s</div><div class="cl">Analysis Time</div></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# Hero CTA — properly centered
_, c, _ = st.columns([3, 1, 3])
with c:
    label = "Open Dashboard →" if is_logged_in(st.session_state) else "Get Started →"
    dest  = "pages/2_upload_data.py" if is_logged_in(st.session_state) else "pages/1_login.py"
    if st.button(label, use_container_width=True, type="primary", key="hero_btn"):
        st.switch_page(dest)

st.markdown("<br><br>", unsafe_allow_html=True)

# ════════════════════════════════════════
# FEATURES
# ════════════════════════════════════════
st.markdown("""
<div class="content-wrap">
<div class="feat-grid">
  <p class="eyebrow">What We Offer</p>
  <h2 class="s-title">Everything You Need to<br>Monitor Meal Quality</h2>
  <p class="s-sub">A complete AI-powered platform for school meal assessment — with clarity and confidence.</p>
</div>
</div>
""", unsafe_allow_html=True)

feats = [
    ("c1","📊","Multi-Dimensional Analysis",    "Scores 5 critical dimensions: Nutrition, Waste, Hygiene, Taste & Menu Compliance."),
    ("c2","🤖","Explainable AI Engine",          "Rule-based expert system — every score is transparent and auditable."),
    ("c3","📈","Real-Time Analytics",             "Interactive charts give instant visual insight into school performance trends."),
    ("c4","💡","Actionable Recommendations",     "Specific, prioritised improvement steps — not just numbers."),
    ("c5","💾","MySQL Database Backend",          "Enterprise-grade storage for secure and scalable data management."),
    ("c6","🔒","Secure Role-Based Login",         "Hashed credentials and session management keep your data protected."),
]

pa, pb = st.columns([1, 20]), None  # side padding via empty col trick
with st.container():
    col_pad_l, col_inner, col_pad_r = st.columns([1, 22, 1])
    with col_inner:
        r1 = st.columns(3, gap="medium")
        for col, (cls, icon, title, desc) in zip(r1, feats[:3]):
            with col:
                st.markdown(f'<div class="f-card {cls}"><div class="f-icon">{icon}</div><h3>{title}</h3><p>{desc}</p></div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        r2 = st.columns(3, gap="medium")
        for col, (cls, icon, title, desc) in zip(r2, feats[3:]):
            with col:
                st.markdown(f'<div class="f-card {cls}"><div class="f-icon">{icon}</div><h3>{title}</h3><p>{desc}</p></div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ════════════════════════════════════════
# HOW IT WORKS
# ════════════════════════════════════════
st.markdown("""
<div class="content-wrap">
<div class="how-sec">
  <p class="eyebrow">Simple Workflow</p>
  <h2 class="s-title">From Data to Insights in 3 Steps</h2>
  <p class="s-sub">Upload your meal records and get a full quality report in under a minute.</p>
</div>
</div>
""", unsafe_allow_html=True)

_, inner, _ = st.columns([1, 22, 1])
with inner:
    s1, ar1, s2, ar2, s3 = st.columns([4, 1, 4, 1, 4], gap="small")
    with s1:
        st.markdown("""<div class="step-box">
          <div class="s-num">1</div><div class="s-ico">📤</div>
          <p class="s-t">Upload CSV</p>
          <p class="s-d">Upload your school meal data as a CSV file. Download our template to get started.</p>
        </div>""", unsafe_allow_html=True)
    with ar1:
        st.markdown('<div class="arrow-box">→</div>', unsafe_allow_html=True)
    with s2:
        st.markdown("""<div class="step-box">
          <div class="s-num">2</div><div class="s-ico">⚙️</div>
          <p class="s-t">AI Processing</p>
          <p class="s-d">Our AI engine scores every record across 5 weighted quality dimensions automatically.</p>
        </div>""", unsafe_allow_html=True)
    with ar2:
        st.markdown('<div class="arrow-box">→</div>', unsafe_allow_html=True)
    with s3:
        st.markdown("""<div class="step-box">
          <div class="s-num">3</div><div class="s-ico">📊</div>
          <p class="s-t">View Insights</p>
          <p class="s-d">Explore interactive charts, school rankings, alerts and downloadable reports.</p>
        </div>""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ════════════════════════════════════════
# BOTTOM CTA
# ════════════════════════════════════════
st.markdown("""
<div class="b-cta">
  <div class="b-cta-inner">
    <h2>Ready to Improve Meal Quality?</h2>
    <p>Sign in and start monitoring in under a minute — no hardware required.</p>
  </div>
</div>
""", unsafe_allow_html=True)

_, c2, _ = st.columns([3, 1, 3])
with c2:
    label2 = "Open Dashboard →" if is_logged_in(st.session_state) else "Sign In →"
    dest2  = "pages/2_upload_data.py" if is_logged_in(st.session_state) else "pages/1_login.py"
    if st.button(label2, use_container_width=True, type="primary", key="cta_btn"):
        st.switch_page(dest2)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="site-ft">🍽️ &nbsp; School Meal Quality Monitor &nbsp;·&nbsp; AI-Powered Assessment &nbsp;·&nbsp; Built with Python & Streamlit</div>', unsafe_allow_html=True)