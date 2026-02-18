"""
pages/1_login.py — Login Page
Follows device light/dark theme. Clean card, no demo credentials shown.
"""
import streamlit as st, sys, time
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from src.auth import authenticate, is_logged_in
from src.styles import SHARED_CSS

st.set_page_config(
    page_title="Sign In · School Meal Monitor",
    page_icon="🍽️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown(SHARED_CSS, unsafe_allow_html=True)

# ── Login-only CSS: no forced bg — adapts to device theme ──
st.markdown("""
<style>
/* Center layout, appropriate top padding */
.main .block-container {
    max-width: 440px !important;
    padding-top: 4vh !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
}

/* ── LOGO MARK ── */
.logo-mark {
    width: 66px; height: 66px;
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    border-radius: 18px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.9rem;
    margin: 0 auto 1.4rem;
    box-shadow: 0 8px 24px rgba(37,99,235,0.30);
}

/* ── HEADING ── */
.login-head {
    text-align: center;
    margin-bottom: 2.2rem;
}
.login-head h1 {
    font-family: 'Lora', serif !important;
    font-size: 1.9rem; font-weight: 700;
    margin: 0 0 .3rem; letter-spacing: -.01em;
}
.login-head p {
    font-size: .88rem; opacity: .52;
    margin: 0; font-weight: 400;
}

/* ── TOP ACCENT LINE on form area ── */
.form-card {
    border-radius: var(--r3);
    border: 1px solid var(--bdr);
    background: var(--surf);
    padding: 2.2rem 2rem 1.8rem;
    position: relative; overflow: hidden;
    margin-bottom: 1.2rem;
}
.form-card::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, #2563eb, #6366f1, #7c3aed);
}

/* ── INPUT LABELS ── */
.stTextInput label {
    font-size: .78rem !important;
    font-weight: 700 !important;
    letter-spacing: .05em !important;
    text-transform: uppercase !important;
    opacity: .55 !important;
}

/* ── FORM SUBMIT BUTTON ── */
.stFormSubmitButton > button {
    width: 100% !important;
    padding: .9rem !important;
    font-size: .95rem !important;
    margin-top: .3rem !important;
    border-radius: var(--r1) !important;
}

/* ── BACK BUTTON ── */
.stButton > button {
    width: 100% !important;
    border-radius: var(--r1) !important;
    font-size: .88rem !important;
    padding: .7rem !important;
    background: transparent !important;
    border: 1.5px solid var(--bdr) !important;
    font-weight: 600 !important;
    opacity: .7;
}
.stButton > button:hover {
    border-color: var(--b-bd) !important;
    background: var(--b-bg) !important;
    opacity: 1 !important;
    color: var(--b) !important;
}

/* ── DIVIDER ── */
.or-div {
    display:flex; align-items:center; gap:.8rem;
    opacity:.38; font-size:.78rem;
    margin:.9rem 0;
}
.or-div::before, .or-div::after {
    content:''; flex:1; height:1px; background:var(--bdr);
}

/* ── FOOTER ── */
.login-ft {
    text-align:center; opacity:.30;
    font-size:.75rem; margin-top:2rem;
    letter-spacing:.03em;
}
</style>
""", unsafe_allow_html=True)

# Already logged in
if is_logged_in(st.session_state):
    st.success("✅ You are already signed in.")
    if st.button("Continue →", type="primary", use_container_width=True):
        st.switch_page("pages/2_upload_data.py")
    st.stop()

# ── HEADER ──
st.markdown("""
<div class="login-head">
  <div class="logo-mark">🍽️</div>
  <h1>Welcome back</h1>
  <p>Sign in to School Meal Quality Monitor</p>
</div>
""", unsafe_allow_html=True)

# ── FORM CARD ──
st.markdown('<div class="form-card">', unsafe_allow_html=True)

with st.form("login_form", clear_on_submit=False):
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    st.markdown("<br>", unsafe_allow_html=True)
    submit = st.form_submit_button("Sign In →", use_container_width=True, type="primary")

    if submit:
        if not username.strip() or not password.strip():
            st.error("⚠️ Please enter both username and password.")
        else:
            with st.spinner("Verifying..."):
                ok, result = authenticate(username.strip(), password)
            if ok:
                st.session_state['logged_in']  = True
                st.session_state['user_info']  = result
                st.session_state['username']   = username.strip()
                st.success(f"✅ Welcome, {result['full_name']}!")
                time.sleep(0.7)
                st.switch_page("pages/2_upload_data.py")
            else:
                st.error("❌ Invalid username or password. Please try again.")

st.markdown('</div>', unsafe_allow_html=True)

# ── BACK LINK ──
st.markdown('<div class="or-div">or</div>', unsafe_allow_html=True)
if st.button("← Back to Home", use_container_width=True):
    st.switch_page("app.py")

st.markdown('<div class="login-ft">🍽️ School Meal Quality Monitor · AI-Powered</div>', unsafe_allow_html=True)