
"""src/styles.py — Shared design tokens for all pages"""

SHARED_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Lora:ital,wght@0,600;0,700;1,500&display=swap');

/* ─── GLOBAL RESET ─── */
*, *::before, *::after { box-sizing: border-box; }

/* Apply font ONLY to safe text containers — never to SVG/icon internals */
body, 
.stMarkdown, 
.stMarkdown p, 
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3, 
.stMarkdown h4, .stMarkdown h5, .stMarkdown h6,
.stMarkdown span:not([class*="icon"]):not([class*="arrow"]),
.stButton button,
.stTextInput label,
.stTextInput input,
.stSelectbox label,
.stMultiSelect label,
[data-testid="stMarkdownContainer"],
section[data-testid="stSidebar"] {
    font-family: 'Outfit', sans-serif !important;
}

#MainMenu, footer, header, .stDeployButton { display: none !important; }

/* ─── BRAND TOKENS (work on any bg) ─── */
:root {
    /* Primary blue */
    --b:    #2563eb;
    --b-dk: #1d4ed8;
    --b-lt: #3b82f6;
    --b-gl: rgba(37,99,235,0.18);
    --b-bg: rgba(37,99,235,0.07);
    --b-bd: rgba(37,99,235,0.28);

    /* Semantic */
    --green:   #059669;
    --green-bg:rgba(5,150,105,0.08);
    --green-bd:rgba(5,150,105,0.30);

    --amber:   #d97706;
    --amber-bg:rgba(217,119,6,0.08);
    --amber-bd:rgba(217,119,6,0.30);

    --red:     #dc2626;
    --red-bg:  rgba(220,38,38,0.08);
    --red-bd:  rgba(220,38,38,0.30);

    --violet:  #7c3aed;
    --cyan:    #0891b2;

    /* Neutral surfaces — semi-transparent so theme bg shows */
    --surf:    rgba(120,120,120,0.06);
    --surf-2:  rgba(120,120,120,0.11);
    --bdr:     rgba(120,120,120,0.14);

    /* Radius */
    --r1: 8px; --r2: 14px; --r3: 20px; --r4: 28px;
}

/* ─── LAYOUT ─── */
.main .block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 3rem !important;
    max-width: 1180px;
}

/* ─── BUTTONS ─── */
.stButton > button,
.stFormSubmitButton > button {
    border-radius: var(--r1) !important;
    font-weight: 700 !important;
    font-size: 0.92rem !important;
    letter-spacing: 0.02em !important;
    transition: all 0.2s cubic-bezier(.23,1,.32,1) !important;
}
.stButton > button[kind="primary"],
.stFormSubmitButton > button[kind="primary"] {
    background: linear-gradient(135deg, var(--b) 0%, var(--b-dk) 100%) !important;
    color: #fff !important; border: none !important;
    box-shadow: 0 4px 14px var(--b-gl) !important;
}
.stButton > button[kind="primary"]:hover,
.stFormSubmitButton > button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 24px var(--b-gl) !important;
}
.stButton > button[kind="secondary"] {
    background: transparent !important;
    border: 1.5px solid var(--bdr) !important;
}
.stButton > button[kind="secondary"]:hover {
    border-color: var(--b-bd) !important;
    background: var(--b-bg) !important;
}
.stDownloadButton > button {
    background: linear-gradient(135deg, var(--green) 0%, #047857 100%) !important;
    color: #fff !important; border: none !important;
    border-radius: var(--r1) !important; font-weight: 700 !important;
    box-shadow: 0 4px 14px rgba(5,150,105,0.20) !important;
    transition: all 0.2s ease !important;
}
.stDownloadButton > button:hover { transform: translateY(-2px) !important; }

/* ─── INPUTS ─── */
.stTextInput > div > div > input {
    border: 1.5px solid var(--bdr) !important;
    border-radius: var(--r1) !important;
    padding: 0.78rem 1rem !important;
    font-size: 0.95rem !important;
    background: var(--surf) !important;
    transition: all 0.18s ease !important;
}
.stTextInput > div > div > input:focus {
    border-color: var(--b) !important;
    box-shadow: 0 0 0 3px var(--b-gl) !important;
    background: var(--b-bg) !important;
    outline: none !important;
}
.stTextInput label {
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.04em !important;
    opacity: 0.65 !important;
}

/* ─── TABS ─── */
.stTabs [data-baseweb="tab-list"] {
    gap: 3px; background: var(--surf);
    padding: 4px; border-radius: var(--r1);
}
.stTabs [data-baseweb="tab"] {
    border-radius: 6px !important; padding: 7px 16px !important;
    font-weight: 600 !important; font-size: 0.86rem !important;
    border: none !important; transition: all 0.18s ease !important;
}
.stTabs [aria-selected="true"] {
    background: var(--b) !important; color: #fff !important;
}

/* ─── EXPANDER ─── */
/* Only style container — do NOT touch .streamlit-expanderHeader internals */
[data-testid="stExpander"] {
    border: 1px solid var(--bdr) !important;
    border-radius: var(--r1) !important;
    background: var(--surf) !important;
}

/* ─── FORM ─── */
[data-testid="stForm"] {
    background: transparent !important;
    border: none !important; padding: 0 !important;
}

/* ════════════════════════════════
   SHARED COMPONENTS
════════════════════════════════ */

/* Page header banner */
.ph {
    background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 45%, #2563eb 100%);
    border-radius: var(--r3); padding: 2.2rem 2.5rem;
    margin-bottom: 2rem; color: #fff;
    position: relative; overflow: hidden;
}
.ph::after {
    content:''; position:absolute; top:-60px; right:-60px;
    width:240px; height:240px; border-radius:50%;
    background:rgba(255,255,255,0.05); pointer-events:none;
}
.ph-badge {
    display:inline-flex; align-items:center; gap:.4rem;
    background:rgba(255,255,255,0.18); border:1px solid rgba(255,255,255,0.25);
    color:#fff; padding:.28rem .85rem; border-radius:50px;
    font-size:.7rem; font-weight:700; letter-spacing:.07em;
    text-transform:uppercase; margin-bottom:.85rem;
    position:relative; z-index:1;
}
.ph h1 {
    font-family:'Lora',serif !important; font-size:1.9rem; font-weight:700;
    color:#fff !important; margin:0 0 .35rem; line-height:1.2;
    position:relative; z-index:1;
}
.ph p { color:rgba(255,255,255,.72); margin:0; font-size:.9rem; position:relative; z-index:1; }

/* Sidebar user card */
.sb-user {
    background: linear-gradient(135deg, #1d4ed8, #2563eb);
    border-radius: var(--r2); padding:1.2rem 1.25rem;
    margin-bottom:1.5rem; position:relative; overflow:hidden;
}
.sb-user::after {
    content:''; position:absolute; top:-28px; right:-28px;
    width:100px; height:100px; border-radius:50%;
    background:rgba(255,255,255,0.07);
}
.sb-user h4 { color:#fff !important; font-size:.92rem; font-weight:700; margin:0 0 .2rem; position:relative; z-index:1; }
.sb-user p  { color:rgba(255,255,255,.70) !important; font-size:.78rem; margin:0; position:relative; z-index:1; }

/* Step progress */
.steps {
    display:flex; align-items:center;
    gap:0; padding:.4rem 0; margin-bottom:.5rem;
}
.st-item { display:flex; align-items:center; gap:.45rem; }
.st-dot {
    width:26px; height:26px; border-radius:50%;
    display:flex; align-items:center; justify-content:center;
    font-size:.72rem; font-weight:700; flex-shrink:0;
    border:2px solid var(--bdr); opacity:.38;
}
.st-dot.done   { background:var(--green); border-color:var(--green); color:#fff; opacity:1; }
.st-dot.active { background:var(--b);     border-color:var(--b);     color:#fff; opacity:1; }
.st-lbl { font-size:.75rem; font-weight:600; opacity:.38; }
.st-lbl.done   { opacity:.75; color:var(--green); }
.st-lbl.active { opacity:1;   color:var(--b);     }
.st-line { flex:1; height:1px; background:var(--bdr); margin:0 .35rem; min-width:20px; }
.st-line.done { background:var(--green); opacity:.35; }

/* Section divider label */
.sec-div {
    display:flex; align-items:center; gap:.7rem;
    margin:2rem 0 1.2rem;
}
.sec-div .dl { flex:1; height:1px; background:var(--bdr); }
.sec-div span {
    font-size:.68rem; font-weight:800; letter-spacing:.1em;
    text-transform:uppercase; color:var(--b);
    padding:0 .3rem; white-space:nowrap;
}

/* KPI gradient cards — always white text, safe */
.kpi {
    border-radius:var(--r2); padding:1.5rem 1.4rem;
    color:#fff; position:relative; overflow:hidden;
    margin-bottom:.5rem;
}
.kpi::after {
    content:''; position:absolute; bottom:-24px; right:-24px;
    width:120px; height:120px; border-radius:50%;
    background:rgba(255,255,255,0.07); pointer-events:none;
}
.kpi .ki { font-size:1.3rem; display:block; margin-bottom:.65rem; opacity:.82; position:relative; z-index:1; }
.kpi .kv {
    font-family:'Lora',serif !important;
    font-size:2.4rem; font-weight:700; line-height:1;
    color:#fff; margin:0 0 .3rem; position:relative; z-index:1;
}
.kpi .kl {
    font-size:.7rem; font-weight:700; letter-spacing:.08em;
    text-transform:uppercase; opacity:.72; margin:0;
    position:relative; z-index:1;
}
.kpi .ks { font-size:.73rem; opacity:.58; margin:.28rem 0 0; position:relative; z-index:1; }

.kpi-b  { background:linear-gradient(135deg,#2563eb,#1d4ed8); box-shadow:0 6px 20px rgba(37,99,235,.28); }
.kpi-v  { background:linear-gradient(135deg,#7c3aed,#6d28d9); box-shadow:0 6px 20px rgba(124,58,237,.28); }
.kpi-c  { background:linear-gradient(135deg,#0891b2,#0e7490); box-shadow:0 6px 20px rgba(8,145,178,.28); }
.kpi-a  { background:linear-gradient(135deg,#d97706,#b45309); box-shadow:0 6px 20px rgba(217,119,6,.28); }
.kpi-r  { background:linear-gradient(135deg,#dc2626,#b91c1c); box-shadow:0 6px 20px rgba(220,38,38,.28); }
.kpi-g  { background:linear-gradient(135deg,#059669,#047857); box-shadow:0 6px 20px rgba(5,150,105,.28); }

/* Metric cards — transparent surface */
.mc {
    border-radius:var(--r2); padding:1.3rem 1.4rem;
    border-left:4px solid; background:var(--surf);
    border-top:1px solid var(--bdr); border-right:1px solid var(--bdr);
    border-bottom:1px solid var(--bdr); margin-bottom:.5rem;
}
.mc.g { border-left-color:var(--green); }
.mc.a { border-left-color:var(--amber); }
.mc.b { border-left-color:var(--b);     }
.mc.v { border-left-color:var(--violet);}
.mc .ml { font-size:.68rem; font-weight:700; letter-spacing:.09em; text-transform:uppercase; opacity:.48; margin:0 0 .5rem; }
.mc .mv {
    font-family:'Lora',serif !important;
    font-size:2rem; font-weight:700; line-height:1; margin:0 0 .3rem;
}
.mc.g .mv { color:var(--green); }
.mc.a .mv { color:var(--amber); }
.mc.b .mv { color:var(--b);     }
.mc.v .mv { color:var(--violet);}
.mc .ms { font-size:.8rem; font-weight:600; opacity:.58; margin:0; }

/* Alert stat cards */
.asc {
    border-radius:var(--r2); padding:1.3rem;
    border:1px solid; margin-bottom:.5rem;
}
.asc.r { background:var(--red-bg);   border-color:var(--red-bd);   }
.asc.y { background:var(--amber-bg); border-color:var(--amber-bd); }
.asc.b { background:var(--b-bg);     border-color:var(--b-bd);     }
.asc .ai { font-size:1.1rem; display:block; margin-bottom:.35rem; }
.asc .av {
    font-family:'Lora',serif !important;
    font-size:2.4rem; font-weight:700; line-height:1; margin:0 0 .2rem;
}
.asc.r .av { color:var(--red);   }
.asc.y .av { color:var(--amber); }
.asc.b .av { color:var(--b);     }
.asc .al { font-size:.68rem; font-weight:700; text-transform:uppercase; letter-spacing:.08em; opacity:.50; margin:0 0 .2rem; }
.asc .ad { font-size:.78rem; opacity:.58; margin:0; font-weight:500; }

/* Alert detail rows */
.a-row {
    border-radius:var(--r1); padding:.95rem 1.2rem;
    margin-bottom:.6rem; border-left:4px solid;
    border-top:1px solid var(--bdr); border-right:1px solid var(--bdr); border-bottom:1px solid var(--bdr);
    background:var(--surf);
}
.a-row.r { border-left-color:var(--red);   background:var(--red-bg);   }
.a-row.y { border-left-color:var(--amber); background:var(--amber-bg); }
.a-row .ah { font-size:.88rem; font-weight:700; margin:0 0 .22rem; }
.a-row .am { font-size:.75rem; opacity:.48; font-weight:500; }

/* Count pill */
.c-pill {
    display:inline-flex; align-items:center; gap:.35rem;
    background:var(--b-bg); border:1px solid var(--b-bd);
    color:var(--b); padding:.32rem .9rem; border-radius:50px;
    font-size:.78rem; font-weight:600; margin:.5rem 0 1.1rem;
}

/* No alerts */
.no-alert {
    background:var(--green-bg); border:1px solid var(--green-bd);
    color:var(--green); border-radius:var(--r2);
    padding:1.3rem 2rem; text-align:center;
    font-weight:700; font-size:.95rem;
}

/* Processing steps */
.ps {
    border-radius:var(--r1); padding:1rem 1.3rem;
    margin-bottom:.7rem; border-left:4px solid;
    border-top:1px solid var(--bdr); border-right:1px solid var(--bdr); border-bottom:1px solid var(--bdr);
    display:flex; align-items:flex-start; gap:.9rem;
    transition:all .3s ease;
}
.ps.pending { border-left-color:var(--bdr); background:var(--surf); opacity:.42; }
.ps.running { border-left-color:var(--b);   background:var(--b-bg); }
.ps.done    { border-left-color:var(--green); background:var(--green-bg); }
.ps .pi { font-size:1.2rem; flex-shrink:0; margin-top:.1rem; }
.ps .pt { font-size:.88rem; font-weight:700; margin:0 0 .18rem; }
.ps .pd { font-size:.78rem; opacity:.55; margin:0; }

/* Summary cards */
.sc {
    background:var(--surf); border:1px solid var(--bdr);
    border-radius:var(--r2); padding:1.3rem; text-align:center;
}
.sc .sv {
    font-family:'Lora',serif !important;
    font-size:2.2rem; font-weight:700; color:var(--b);
    margin:0 0 .25rem; line-height:1;
}
.sc .sl { font-size:.68rem; font-weight:700; text-transform:uppercase; letter-spacing:.07em; opacity:.50; margin:0; }

/* Success banner */
.suc-banner {
    background:var(--green-bg); border:1px solid var(--green-bd);
    border-radius:var(--r3); padding:1.8rem 2rem;
    text-align:center; margin:1.5rem 0;
}
.suc-banner h2 {
    font-family:'Lora',serif !important;
    font-size:1.7rem; font-weight:700;
    color:var(--green); margin:0 0 .45rem;
}
.suc-banner p { opacity:.62; font-size:.9rem; margin:0; }

/* Upload option card */
.up-card {
    background:var(--surf); border:1.5px solid var(--bdr);
    border-radius:var(--r3); padding:2rem;
    transition:all .28s cubic-bezier(.23,1,.32,1);
    height:100%;
}
.up-card:hover {
    border-color:var(--b-bd);
    box-shadow:0 8px 28px var(--b-gl);
    transform:translateY(-4px);
}
.up-card .uci { font-size:2.8rem; display:block; margin-bottom:.9rem; }
.up-card h3 {
    font-family:'Lora',serif !important;
    font-size:1.35rem; font-weight:700; margin:0 0 .45rem;
}
.up-card p { font-size:.86rem; opacity:.58; margin:0 0 1.4rem; line-height:1.6; }
</style>
"""