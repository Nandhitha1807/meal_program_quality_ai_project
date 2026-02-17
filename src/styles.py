"""
Shared CSS Design System
Deep navy · Crisp typography · Theme-safe colors
Works in both Streamlit light and dark mode
"""

GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,700;0,9..144,900;1,9..144,300&display=swap');

/* ═══════════════════════════════════════════
   DESIGN TOKENS  —  theme-safe CSS variables
═══════════════════════════════════════════ */
:root {
    /* Brand palette */
    --c-blue:      #3b82f6;
    --c-blue-dark: #1d4ed8;
    --c-blue-glow: rgba(59,130,246,0.25);
    --c-indigo:    #6366f1;
    --c-violet:    #8b5cf6;
    --c-cyan:      #06b6d4;
    --c-emerald:   #10b981;
    --c-amber:     #f59e0b;
    --c-rose:      #f43f5e;

    /* Semantic — uses opacity so they adapt */
    --success-bg:  rgba(16,185,129,0.12);
    --success-bdr: rgba(16,185,129,0.45);
    --success-txt: #10b981;

    --warn-bg:     rgba(245,158,11,0.12);
    --warn-bdr:    rgba(245,158,11,0.45);
    --warn-txt:    #f59e0b;

    --danger-bg:   rgba(244,63,94,0.12);
    --danger-bdr:  rgba(244,63,94,0.45);
    --danger-txt:  #f43f5e;

    --info-bg:     rgba(59,130,246,0.12);
    --info-bdr:    rgba(59,130,246,0.45);
    --info-txt:    #3b82f6;

    --indigo-bg:   rgba(99,102,241,0.12);
    --indigo-bdr:  rgba(99,102,241,0.45);
    --indigo-txt:  #6366f1;

    /* Surfaces — fully transparent so theme BG shows through */
    --surface-1: rgba(99,102,241,0.06);
    --surface-2: rgba(99,102,241,0.10);
    --border:    rgba(148,163,184,0.15);
    --border-focus: rgba(59,130,246,0.60);

    /* Radius */
    --r-sm: 10px;
    --r-md: 16px;
    --r-lg: 22px;
    --r-xl: 28px;

    /* Shadows */
    --shadow-sm: 0 2px 8px rgba(0,0,0,0.08);
    --shadow-md: 0 8px 24px rgba(0,0,0,0.12);
    --shadow-lg: 0 20px 48px rgba(0,0,0,0.18);

    /* Typography */
    --font-body:    'Plus Jakarta Sans', sans-serif;
    --font-display: 'Fraunces', serif;
}

/* ═══════════════════════════════════════════
   GLOBAL RESET
═══════════════════════════════════════════ */
*, *::before, *::after { box-sizing: border-box; }
* { font-family: var(--font-body) !important; }

#MainMenu, footer, header, .stDeployButton { visibility: hidden; display: none; }

/* ═══════════════════════════════════════════
   STREAMLIT OVERRIDES
═══════════════════════════════════════════ */
.main .block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 3rem !important;
}

/* ── Buttons ── */
.stButton > button,
.stFormSubmitButton > button {
    font-family: var(--font-body) !important;
    font-weight: 700 !important;
    border-radius: var(--r-sm) !important;
    transition: all 0.22s cubic-bezier(0.23,1,0.32,1) !important;
    letter-spacing: 0.01em !important;
}

.stButton > button[kind="primary"],
.stFormSubmitButton > button[kind="primary"] {
    background: linear-gradient(135deg, var(--c-blue) 0%, var(--c-blue-dark) 100%) !important;
    color: #fff !important;
    border: none !important;
    box-shadow: 0 4px 16px var(--c-blue-glow) !important;
}
.stButton > button[kind="primary"]:hover,
.stFormSubmitButton > button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px var(--c-blue-glow) !important;
}

.stButton > button[kind="secondary"] {
    background: transparent !important;
    border: 1.5px solid var(--border) !important;
}
.stButton > button[kind="secondary"]:hover {
    border-color: var(--c-blue) !important;
    color: var(--c-blue) !important;
    background: var(--info-bg) !important;
}

/* ── Download button ── */
.stDownloadButton > button {
    background: linear-gradient(135deg, var(--c-emerald) 0%, #059669 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: var(--r-sm) !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 16px rgba(16,185,129,0.25) !important;
    transition: all 0.22s ease !important;
}
.stDownloadButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 24px rgba(16,185,129,0.35) !important;
}

/* ── Inputs ── */
.stTextInput > div > div > input {
    border: 1.5px solid var(--border) !important;
    border-radius: var(--r-sm) !important;
    padding: 0.75rem 1rem !important;
    font-size: 0.95rem !important;
    background: var(--surface-1) !important;
    transition: all 0.2s ease !important;
}
.stTextInput > div > div > input:focus {
    border-color: var(--c-blue) !important;
    box-shadow: 0 0 0 3px var(--c-blue-glow) !important;
    background: var(--surface-2) !important;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    background: var(--surface-1);
    padding: 4px;
    border-radius: var(--r-sm);
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    padding: 8px 18px;
    font-weight: 600;
    font-size: 0.88rem;
    border: none !important;
    transition: all 0.2s ease;
}
.stTabs [aria-selected="true"] {
    background: var(--c-blue) !important;
    color: #fff !important;
}

/* ── Expander ── */
.streamlit-expanderHeader {
    border-radius: var(--r-sm) !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    padding: 0.85rem 1rem !important;
    border: 1.5px solid var(--border) !important;
}

/* ── Slider ── */
.stSlider > div > div > div > div {
    background: var(--c-blue) !important;
}

/* ── Multiselect ── */
.stMultiSelect > div > div {
    border-radius: var(--r-sm) !important;
    border: 1.5px solid var(--border) !important;
}

/* ── Alerts ── */
.stAlert { border-radius: var(--r-sm) !important; }

/* ═══════════════════════════════════════════
   SHARED COMPONENTS
═══════════════════════════════════════════ */

/* ── Page header banner ── */
.page-header {
    background: linear-gradient(135deg, #1e3a5f 0%, #1e40af 50%, #2563eb 100%);
    border-radius: var(--r-lg);
    padding: 2.5rem 2.5rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.page-header::after {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 200px; height: 200px;
    border-radius: 50%;
    background: rgba(255,255,255,0.06);
    pointer-events: none;
}
.page-header::before {
    content: '';
    position: absolute;
    bottom: -60px; left: 30%;
    width: 280px; height: 280px;
    border-radius: 50%;
    background: rgba(255,255,255,0.04);
    pointer-events: none;
}
.page-header h1 {
    font-family: var(--font-display) !important;
    font-size: 2.2rem;
    font-weight: 700;
    color: #fff !important;
    margin: 0 0 0.4rem;
    position: relative;
}
.page-header p {
    color: rgba(255,255,255,0.75);
    margin: 0;
    font-size: 0.95rem;
    font-weight: 400;
    position: relative;
}
.page-header .header-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.2);
    color: #fff;
    padding: 0.3rem 0.9rem;
    border-radius: 50px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 1rem;
    position: relative;
}

/* ── Sidebar user card ── */
.sidebar-user-card {
    background: linear-gradient(135deg, var(--c-blue-dark), var(--c-blue));
    border-radius: var(--r-md);
    padding: 1.3rem 1.2rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.sidebar-user-card::after {
    content: '';
    position: absolute;
    top: -20px; right: -20px;
    width: 80px; height: 80px;
    border-radius: 50%;
    background: rgba(255,255,255,0.08);
}
.sidebar-user-card h4 {
    color: #fff !important;
    font-size: 0.95rem;
    font-weight: 700;
    margin: 0 0 0.25rem;
}
.sidebar-user-card p {
    color: rgba(255,255,255,0.72) !important;
    font-size: 0.8rem;
    margin: 0;
}

/* ── Section label ── */
.section-label {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    margin: 2.2rem 0 1.2rem;
}
.section-label .line {
    flex: 1;
    height: 1px;
    background: var(--border);
}
.section-label span {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--c-blue);
    white-space: nowrap;
    padding: 0 0.5rem;
}

/* ── KPI cards ── */
.kpi-card {
    border-radius: var(--r-md);
    padding: 1.6rem 1.4rem;
    color: #fff;
    position: relative;
    overflow: hidden;
}
.kpi-card::after {
    content: '';
    position: absolute;
    bottom: -20px; right: -20px;
    width: 100px; height: 100px;
    border-radius: 50%;
    background: rgba(255,255,255,0.08);
}
.kpi-card .kpi-icon {
    font-size: 1.5rem;
    margin-bottom: 0.8rem;
    display: block;
    opacity: 0.85;
}
.kpi-card .kpi-val {
    font-family: var(--font-display) !important;
    font-size: 2.6rem;
    font-weight: 700;
    line-height: 1;
    margin: 0 0 0.4rem;
    color: #fff;
}
.kpi-card .kpi-lbl {
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    opacity: 0.78;
    margin: 0;
}
.kpi-card .kpi-sub {
    font-size: 0.78rem;
    opacity: 0.65;
    margin: 0.4rem 0 0;
}

.kpi-blue   { background: linear-gradient(135deg, #2563eb, #1d4ed8); box-shadow: 0 6px 20px rgba(37,99,235,0.30); }
.kpi-violet { background: linear-gradient(135deg, #7c3aed, #6d28d9); box-shadow: 0 6px 20px rgba(124,58,237,0.30); }
.kpi-cyan   { background: linear-gradient(135deg, #0891b2, #0e7490); box-shadow: 0 6px 20px rgba(8,145,178,0.30); }
.kpi-amber  { background: linear-gradient(135deg, #d97706, #b45309); box-shadow: 0 6px 20px rgba(217,119,6,0.30); }
.kpi-rose   { background: linear-gradient(135deg, #e11d48, #be123c); box-shadow: 0 6px 20px rgba(225,29,72,0.30); }
.kpi-emerald{ background: linear-gradient(135deg, #059669, #047857); box-shadow: 0 6px 20px rgba(5,150,105,0.30); }

/* ── Metric mini cards ── */
.metric-card {
    border-radius: var(--r-md);
    padding: 1.4rem 1.5rem;
    border-left: 4px solid;
    background: var(--surface-1);
    border-top: 1px solid var(--border);
    border-right: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
}
.metric-card.green  { border-left-color: var(--c-emerald); }
.metric-card.amber  { border-left-color: var(--c-amber);   }
.metric-card.blue   { border-left-color: var(--c-blue);    }
.metric-card.violet { border-left-color: var(--c-violet);  }
.metric-card .mc-label {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    opacity: 0.55;
    margin: 0 0 0.6rem;
}
.metric-card .mc-value {
    font-family: var(--font-display) !important;
    font-size: 2.2rem;
    font-weight: 700;
    margin: 0 0 0.35rem;
    line-height: 1;
}
.metric-card.green  .mc-value { color: var(--c-emerald); }
.metric-card.amber  .mc-value { color: var(--c-amber);   }
.metric-card.blue   .mc-value { color: var(--c-blue);    }
.metric-card.violet .mc-value { color: var(--c-violet);  }
.metric-card .mc-status {
    font-size: 0.82rem;
    font-weight: 600;
    opacity: 0.7;
    margin: 0;
}

/* ── Alert stat cards ── */
.alert-stat {
    border-radius: var(--r-md);
    padding: 1.4rem;
    border: 1px solid;
    background: var(--surface-1);
}
.alert-stat.danger  { border-color: var(--danger-bdr);  background: var(--danger-bg);  }
.alert-stat.warning { border-color: var(--warn-bdr);    background: var(--warn-bg);    }
.alert-stat.info    { border-color: var(--indigo-bdr);  background: var(--indigo-bg);  }
.alert-stat .as-icon { font-size: 1.3rem; margin-bottom: 0.5rem; display: block; }
.alert-stat .as-num {
    font-family: var(--font-display) !important;
    font-size: 2.8rem;
    font-weight: 700;
    line-height: 1;
    margin: 0 0 0.3rem;
}
.alert-stat.danger  .as-num { color: var(--danger-txt); }
.alert-stat.warning .as-num { color: var(--warn-txt);   }
.alert-stat.info    .as-num { color: var(--indigo-txt); }
.alert-stat .as-lbl {
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    opacity: 0.55;
    margin: 0 0 0.25rem;
}
.alert-stat .as-desc {
    font-size: 0.82rem;
    opacity: 0.65;
    margin: 0;
    font-weight: 500;
}

/* ── Alert detail row ── */
.alert-row {
    border-radius: var(--r-sm);
    padding: 1.1rem 1.3rem;
    margin-bottom: 0.7rem;
    border-left: 4px solid;
    border-top: 1px solid var(--border);
    border-right: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
    background: var(--surface-1);
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
}
.alert-row.danger  { border-left-color: var(--danger-bdr);  }
.alert-row.warning { border-left-color: var(--warn-bdr);    }
.alert-row .ar-title {
    font-size: 0.9rem;
    font-weight: 700;
    margin: 0;
}
.alert-row .ar-meta {
    font-size: 0.78rem;
    opacity: 0.55;
    font-weight: 500;
}

/* ── Record count pill ── */
.count-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: var(--info-bg);
    border: 1px solid var(--info-bdr);
    color: var(--info-txt);
    padding: 0.4rem 1rem;
    border-radius: 50px;
    font-size: 0.82rem;
    font-weight: 600;
    margin: 0.8rem 0 1.2rem;
}

/* ── No-alert success box ── */
.no-alerts {
    background: var(--success-bg);
    border: 1px solid var(--success-bdr);
    color: var(--success-txt);
    border-radius: var(--r-md);
    padding: 1.5rem 2rem;
    text-align: center;
    font-weight: 600;
    font-size: 1rem;
}

/* ── Step progress bar ── */
.step-bar {
    display: flex;
    align-items: center;
    gap: 0;
    margin-bottom: 2.5rem;
}
.step-item {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    flex: 1;
}
.step-dot {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.82rem;
    font-weight: 700;
    flex-shrink: 0;
    border: 2px solid var(--border);
    background: var(--surface-1);
    color: inherit;
    opacity: 0.45;
}
.step-dot.done    { background: var(--c-emerald); border-color: var(--c-emerald); color: #fff; opacity: 1; }
.step-dot.active  { background: var(--c-blue);    border-color: var(--c-blue);    color: #fff; opacity: 1; }
.step-text {
    font-size: 0.82rem;
    font-weight: 600;
    opacity: 0.45;
}
.step-text.done   { opacity: 0.7;  color: var(--c-emerald); }
.step-text.active { opacity: 1.0;  color: var(--c-blue);    }
.step-connector {
    flex: 1;
    height: 1px;
    background: var(--border);
    margin: 0 0.5rem;
}
.step-connector.done { background: var(--c-emerald); opacity: 0.5; }
</style>
"""