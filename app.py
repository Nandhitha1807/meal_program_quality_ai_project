

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