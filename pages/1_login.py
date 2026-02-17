# """
# Page 1: Login Page
# Clean professional login - no demo credentials shown
# """

# import streamlit as st
# import sys
# from pathlib import Path

# sys.path.append(str(Path(__file__).parent.parent))
# from src.auth import authenticate, is_logged_in

# st.set_page_config(
#     page_title="Login - School Meal Monitor",
#     page_icon="🍽️",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=DM+Serif+Display&display=swap');

#     /* ── THEME-SAFE TOKENS ── */
#     :root {
#         --brand-primary:   #2563eb;
#         --brand-secondary: #1d4ed8;
#         --brand-accent:    #3b82f6;
#         --success:         #16a34a;
#         --error:           #dc2626;
#         --warning:         #d97706;

#         /* surfaces adapt to light/dark */
#         --surface:         rgba(255,255,255,0.07);
#         --surface-border:  rgba(100,116,139,0.25);
#         --text-primary:    inherit;
#         --text-muted:      #64748b;
#         --input-bg:        rgba(100,116,139,0.08);
#         --input-border:    rgba(100,116,139,0.3);
#         --input-focus:     #2563eb;
#         --card-shadow:     0 20px 60px rgba(0,0,0,0.12);
#     }

#     * { font-family: 'DM Sans', sans-serif; box-sizing: border-box; }

#     /* Hide Streamlit chrome */
#     #MainMenu, footer, header { visibility: hidden; }
#     .stDeployButton { display: none; }

#     /* Full-page gradient background */
#     .stApp {
#         background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 40%, #2563eb 70%, #3b82f6 100%);
#         min-height: 100vh;
#     }

#     .main .block-container {
#         padding-top: 5vh;
#         padding-bottom: 2rem;
#         max-width: 440px !important;
#         margin: 0 auto;
#     }

#     /* ── CARD ── */
#     .login-card {
#         background: #ffffff;
#         border-radius: 24px;
#         padding: 3rem 2.5rem 2.5rem;
#         box-shadow: var(--card-shadow);
#         margin-bottom: 1.5rem;
#         position: relative;
#         overflow: hidden;
#     }

#     .login-card::before {
#         content: '';
#         position: absolute;
#         top: 0; left: 0; right: 0;
#         height: 4px;
#         background: linear-gradient(90deg, #2563eb, #3b82f6, #60a5fa);
#     }

#     /* ── LOGO AREA ── */
#     .logo-ring {
#         width: 72px;
#         height: 72px;
#         background: linear-gradient(135deg, #2563eb, #3b82f6);
#         border-radius: 20px;
#         display: flex;
#         align-items: center;
#         justify-content: center;
#         font-size: 2rem;
#         margin: 0 auto 1.5rem;
#         box-shadow: 0 8px 24px rgba(37,99,235,0.35);
#     }

#     .login-title {
#         font-family: 'DM Serif Display', serif;
#         font-size: 2rem;
#         font-weight: 400;
#         color: #0f172a;
#         text-align: center;
#         margin: 0 0 0.4rem;
#         line-height: 1.2;
#     }

#     .login-subtitle {
#         color: #64748b;
#         font-size: 0.95rem;
#         text-align: center;
#         margin: 0 0 2.5rem;
#         font-weight: 400;
#     }

#     /* ── INPUT LABELS ── */
#     .stTextInput label {
#         color: #374151 !important;
#         font-size: 0.875rem !important;
#         font-weight: 600 !important;
#         letter-spacing: 0.02em;
#         margin-bottom: 0.4rem;
#     }

#     /* ── INPUT FIELDS ── */
#     .stTextInput > div > div > input {
#         background: #f8fafc !important;
#         border: 1.5px solid #e2e8f0 !important;
#         border-radius: 12px !important;
#         padding: 0.85rem 1.1rem !important;
#         font-size: 1rem !important;
#         color: #0f172a !important;
#         transition: all 0.2s ease;
#     }

#     .stTextInput > div > div > input:focus {
#         border-color: #2563eb !important;
#         background: #fff !important;
#         box-shadow: 0 0 0 4px rgba(37,99,235,0.12) !important;
#     }

#     .stTextInput > div > div > input::placeholder {
#         color: #94a3b8 !important;
#     }

#     /* ── PRIMARY BUTTON ── */
#     .stButton > button[kind="primary"],
#     .stFormSubmitButton > button[kind="primary"] {
#         background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%) !important;
#         color: #ffffff !important;
#         border: none !important;
#         border-radius: 12px !important;
#         padding: 0.9rem 2rem !important;
#         font-size: 1rem !important;
#         font-weight: 700 !important;
#         letter-spacing: 0.03em !important;
#         width: 100%;
#         transition: all 0.25s ease;
#         box-shadow: 0 4px 16px rgba(37,99,235,0.35) !important;
#     }

#     .stButton > button[kind="primary"]:hover,
#     .stFormSubmitButton > button[kind="primary"]:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 8px 24px rgba(37,99,235,0.45) !important;
#     }

#     /* ── SECONDARY BUTTON ── */
#     .stButton > button[kind="secondary"] {
#         background: transparent !important;
#         color: #2563eb !important;
#         border: 1.5px solid #2563eb !important;
#         border-radius: 12px !important;
#         padding: 0.7rem 1.5rem !important;
#         font-weight: 600 !important;
#         width: 100%;
#         transition: all 0.2s ease;
#     }

#     .stButton > button[kind="secondary"]:hover {
#         background: rgba(37,99,235,0.06) !important;
#     }

#     /* ── DIVIDER ── */
#     .divider {
#         display: flex;
#         align-items: center;
#         gap: 1rem;
#         margin: 1.5rem 0;
#         color: #94a3b8;
#         font-size: 0.85rem;
#     }
#     .divider::before,
#     .divider::after {
#         content: '';
#         flex: 1;
#         height: 1px;
#         background: #e2e8f0;
#     }

#     /* ── ALERT MESSAGES ── */
#     .stAlert {
#         border-radius: 12px !important;
#         border: none !important;
#     }

#     /* ── FOOTER TEXT ── */
#     .footer-text {
#         text-align: center;
#         color: rgba(255,255,255,0.7);
#         font-size: 0.85rem;
#         margin-top: 2rem;
#         padding-bottom: 2rem;
#     }

#     /* ── SPINNER ── */
#     .stSpinner > div {
#         border-top-color: #2563eb !important;
#     }

#     /* ── FORM ── */
#     [data-testid="stForm"] {
#         background: transparent !important;
#         border: none !important;
#         padding: 0 !important;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Already logged in check
# if is_logged_in(st.session_state):
#     st.success("✅ You are already logged in!")
#     if st.button("Go to Upload →", type="primary", use_container_width=True):
#         st.switch_page("pages/2_upload_data.py")
#     st.stop()

# # ── CARD ──
# st.markdown("""
#     <div class="login-card">
#         <div class="logo-ring">🍽️</div>
#         <h1 class="login-title">Welcome back</h1>
#         <p class="login-subtitle">Sign in to School Meal Quality Monitor</p>
#     </div>
# """, unsafe_allow_html=True)

# # ── LOGIN FORM ──
# with st.form("login_form", clear_on_submit=False):
#     username = st.text_input(
#         "Username",
#         placeholder="Enter your username",
#     )

#     password = st.text_input(
#         "Password",
#         type="password",
#         placeholder="Enter your password",
#     )

#     st.markdown("<br>", unsafe_allow_html=True)

#     submit = st.form_submit_button(
#         "Sign In →",
#         use_container_width=True,
#         type="primary"
#     )

#     if submit:
#         if not username.strip() or not password.strip():
#             st.error("⚠️  Please enter both username and password.")
#         else:
#             with st.spinner("Verifying credentials..."):
#                 import time
#                 success, result = authenticate(username.strip(), password)

#                 if success:
#                     st.session_state['logged_in'] = True
#                     st.session_state['user_info'] = result
#                     st.session_state['username'] = username.strip()

#                     st.success(f"Welcome, {result['full_name']}! Redirecting...")
#                     time.sleep(0.8)
#                     st.switch_page("pages/2_upload_data.py")
#                 else:
#                     st.error("❌  Invalid username or password. Please try again.")

# # ── DIVIDER ──
# st.markdown('<div class="divider">or</div>', unsafe_allow_html=True)

# # ── BACK TO HOME ──
# if st.button("← Back to Home", use_container_width=True):
#     st.switch_page("app.py")

# # ── FOOTER ──
# st.markdown("""
#     <div class="footer-text">
#         🍽️ School Meal Quality Monitor &nbsp;·&nbsp; AI-Powered Assessment
#     </div>
# """, unsafe_allow_html=True)

"""
pages/1_login.py — Login Page
Clean card design, no demo credentials shown
"""
import streamlit as st
import sys, time
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from src.auth import authenticate, is_logged_in
from src.styles import GLOBAL_CSS

st.set_page_config(
    page_title="Sign In · School Meal Monitor",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
st.markdown("""
<style>
/* Force dark background on login page */
.stApp { background: #0c1526 !important; }
.main .block-container { padding-top: 5vh !important; max-width: 480px !important; }

/* ── LOGIN CARD ── */
.login-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.09);
    border-radius: 24px;
    padding: 3rem 2.5rem 2.5rem;
    position: relative;
    overflow: hidden;
    margin-bottom: 1.5rem;
}
.login-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #3b82f6, #6366f1, #8b5cf6);
}
.login-card::after {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 180px; height: 180px;
    border-radius: 50%;
    background: rgba(59,130,246,0.06);
    pointer-events: none;
}

/* ── LOGO ── */
.login-logo {
    width: 68px; height: 68px;
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    border-radius: 18px;
    display: flex; align-items: center; justify-content: center;
    font-size: 2rem;
    margin: 0 auto 1.5rem;
    box-shadow: 0 8px 24px rgba(37,99,235,0.40);
    position: relative; z-index: 1;
}
.login-title {
    font-family: 'Fraunces', serif !important;
    font-size: 2.2rem;
    font-weight: 700;
    color: #e8f0fe;
    text-align: center;
    margin: 0 0 0.35rem;
    letter-spacing: -.01em;
    position: relative; z-index: 1;
}
.login-sub {
    color: #4d6480;
    font-size: 0.92rem;
    text-align: center;
    margin: 0 0 2.5rem;
    font-weight: 400;
    position: relative; z-index: 1;
}

/* ── LABEL OVERRIDE ── */
.stTextInput label {
    color: #7a8fa8 !important;
    font-size: 0.8rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.06em !important;
    text-transform: uppercase !important;
    margin-bottom: 0.4rem !important;
}

/* ── INPUT FIELDS for dark bg ── */
.stTextInput > div > div > input {
    background: rgba(255,255,255,0.05) !important;
    border: 1.5px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    color: #e2eeff !important;
    padding: 0.85rem 1.1rem !important;
    font-size: 1rem !important;
}
.stTextInput > div > div > input::placeholder { color: #2a3a52 !important; }
.stTextInput > div > div > input:focus {
    border-color: #3b82f6 !important;
    background: rgba(59,130,246,0.08) !important;
    box-shadow: 0 0 0 3px rgba(59,130,246,0.18) !important;
}

/* ── SUBMIT BUTTON ── */
.stFormSubmitButton > button {
    width: 100% !important;
    padding: 1rem !important;
    font-size: 1rem !important;
    margin-top: 0.5rem !important;
}

/* ── BACK BUTTON ── */
.stButton > button {
    width: 100% !important;
    background: transparent !important;
    border: 1.5px solid rgba(255,255,255,0.1) !important;
    color: #4d6480 !important;
    border-radius: 12px !important;
    padding: 0.75rem !important;
    font-weight: 600 !important;
    transition: all .2s ease !important;
}
.stButton > button:hover {
    border-color: rgba(59,130,246,0.4) !important;
    color: #93c5fd !important;
    background: rgba(59,130,246,0.06) !important;
}

/* ── FORM container ── */
[data-testid="stForm"] {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
}

/* ── BRAND FOOTER ── */
.login-footer {
    text-align: center;
    color: #1e3a5f;
    font-size: 0.8rem;
    padding: 2rem 0;
    letter-spacing: .03em;
}

/* ── DIVIDER ── */
.or-divider {
    display: flex; align-items: center; gap: 1rem;
    color: #1e3a5f; font-size: 0.8rem;
    margin: 1.2rem 0;
}
.or-divider::before, .or-divider::after {
    content: ''; flex: 1; height: 1px;
    background: rgba(255,255,255,0.07);
}
</style>
""", unsafe_allow_html=True)

# Already logged in
if is_logged_in(st.session_state):
    st.markdown('<div class="login-card"><p style="text-align:center;color:#10b981;font-weight:600;">✅ You are already signed in.</p></div>', unsafe_allow_html=True)
    if st.button("Continue to Upload →", type="primary", use_container_width=True):
        st.switch_page("pages/2_upload_data.py")
    st.stop()

# ══ CARD ══
st.markdown("""
<div class="login-card">
  <div class="login-logo">🍽️</div>
  <h1 class="login-title">Welcome back</h1>
  <p class="login-sub">Sign in to School Meal Quality Monitor</p>
</div>
""", unsafe_allow_html=True)

# ══ FORM ══
with st.form("login_form"):
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    st.markdown("<br>", unsafe_allow_html=True)
    submit = st.form_submit_button("Sign In →", use_container_width=True, type="primary")

    if submit:
        if not username.strip() or not password.strip():
            st.error("⚠️ Please enter both username and password.")
        else:
            with st.spinner("Verifying credentials..."):
                success, result = authenticate(username.strip(), password)
                if success:
                    st.session_state['logged_in'] = True
                    st.session_state['user_info'] = result
                    st.session_state['username'] = username.strip()
                    st.success(f"Welcome, {result['full_name']}!")
                    time.sleep(0.8)
                    st.switch_page("pages/2_upload_data.py")
                else:
                    st.error("❌ Invalid username or password. Please try again.")

st.markdown('<div class="or-divider">or</div>', unsafe_allow_html=True)

if st.button("← Back to Home", use_container_width=True):
    st.switch_page("app.py")

st.markdown('<div class="login-footer">🍽️ &nbsp; School Meal Quality Monitor &nbsp;·&nbsp; AI-Powered</div>', unsafe_allow_html=True)