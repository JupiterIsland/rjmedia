import streamlit as st

st.set_page_config(
    page_title="RJMedia // Technical Archive",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject CSS for the stark black-and-white wireframe aesthetic
st.markdown("""
    <style>
    /* Force White Background and Black Text */
    .stApp { 
        background-color: #FFFFFF; 
        color: #000000; 
        font-family: 'Courier New', Courier, monospace; 
    }
    
    /* Container Borders */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border: 2px solid #000000 !important;
        border-radius: 0px !important;
        padding: 15px !important;
        background-color: #FFFFFF !important;
        margin-bottom: 10px;
    }

    /* Buttons */
    .stButton>button {
        background-color: #FFFFFF;
        color: #000000;
        border: 1px solid #000000;
        border-radius: 0px;
        text-transform: uppercase;
        font-size: 0.75rem;
        font-weight: bold;
        width: 100%;
        padding: 0.5rem;
    }
    .stButton>button:hover {
        background-color: #000000;
        color: #FFFFFF;
        border-color: #000000;
    }

    /* Override Button Text for Select Video Active State */
    .stButton>button p {
        font-size: 0.75rem;
        margin: 0;
    }

    /* Metrics */
    div[data-testid="stMetricValue"] {
        color: #000000 !important;
        font-weight: bold;
        font-size: 1.8rem;
    }
    div[data-testid="stMetricLabel"] {
        color: #000000 !important;
        text-transform: uppercase;
        font-size: 0.75rem;
        font-weight: bold;
    }
    div[data-testid="stMetricDelta"] {
        color: #666666 !important;
        font-size: 0.7rem;
    }

    /* Typography */
    h1, h2, h3, h4, h5, h6, p, li {
        color: #000000 !important;
    }
    h2, h3, h4, h5 {
        text-transform: uppercase;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    /* Dividers */
    hr { 
        border-top: 2px solid #000000; 
        margin: 1em 0; 
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 1. HEADER BOX
# ---------------------------------------------------------
with st.container(border=True):
    st.markdown("**RJMEDIA // TECHNICAL ARCHIVE & REMASTER LAB**")
    
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.button("▶ YOUTUBE CHANNEL")
    c2.button("☕ BUY ME A COFFEE")
    c3.button("⌘ GITHUB REPOS")
    c4.button("◐ INVERT MONOCHROME")
    c5.button("🖨 PRINT SHEET")
    
    st.markdown("## LIVE MUSIC & BAND DOCUMENTARIES")
    st.caption("Front-Barrier Raw Captures (Solfest / Manchester / Leeds) • 1990s Broadcast Documentaries • Topaz Video AI Tensor Pipelines")

# ---------------------------------------------------------
# 2. METRICS BOX
# ---------------------------------------------------------
with st.container(border=True):
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("01 // VERIFIED VIEWS", "967,422", "32,578 TO 1,000,000", delta_color="off")
    m2.metric("02 // WATCH TIME", "68,056.5 H", "7.76 YEARS CONTINUOUS", delta_color="off")
    m3.metric("03 // IMPRESSIONS", "13,550,376", "4.55% AVG CTR (11.88% PEAK)", delta_color="off")
    m4.metric("04 // YOUTUBE ADSENSE", "£0.00", "100% CLAIMED BY PUBLISHERS", delta_color="off")

# ---------------------------------------------------------
# 3. HARDWARE REALITY BOX
# ---------------------------------------------------------
with st.container(border=True):
    h1, h2, h3 = st.columns([2, 1, 1])
    with h1:
        st.markdown("**PENNY-PER-WATCH HARDWARE REALITY** &nbsp;&nbsp;&nbsp;&nbsp; **100% INDEPENDENT**")
        st.write("Record labels claim 100% of YouTube ad revenue on live music & documentaries—even on footage filmed personally on my phone at the barrier. If every viewer contributed **1p per watch**, here is what this archive generates to cover GPU power & storage:")
        st.markdown("**VIEWS: 967,422 ⸻⸻⸻⸻⸻ = £9,674.22 (@ 1p)**")
    with h2:
        st.button("☕ £3 // GPU POWER COFFEE")
        st.button("📋 COPY SOLFEST PINNED COMMENT")
    with h3:
        st.button("📼 £5 // SPONSOR A VHS TAPE")
        st.button("📋 COPY DOCS PINNED COMMENT")

# ---------------------------------------------------------
# 4. MAIN ARCHIVE & VIDEO SPLIT
# ---------------------------------------------------------
col1, col2 = st.columns([1.2, 2.5])

with col1:
    with st.container(border=True):
        st.markdown("**CHANNEL ARCHIVE PILLARS    5 CATEGORIES**")
        st.button("01 // FRONT-ROW RAW CAPTURES")
        st.button("02 // PETER GREEN & ROCK DOCS")
        st.button("03 // FHD & 4K REMASTERS")
        st.button("04 // MANSUN & PAUL DRAPER VAULT")
        st.button("05 // GOODISON PARK ATMOSPHERE")
        
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("**SELECT VIDEO** &nbsp;&nbsp; 245K+ VIEWS • 100% RAW PHONE")
        
        # Simulated active state button
        st.button("**The Buzzcocks — What Do I Get (Live Solfest 2021)**\n\n225,097 VIEWS • 9,381 HRS • +276 SUBS")
        st.button("Razorlight — In The Morning (Live Solfest 2021)\n\n779 VIEWS • REUNITED CLASSIC LINEUP")
        st.button("Maximo Park — The National Health & Midnight On The Hill (Solfest 21)\n\n8M 45S • 2 FULL SONGS • NHS DEDICATION")

with col2:
    with st.container(border=True):
        st.markdown("**THE BUZZCOCKS — WHAT DO I GET (LIVE SOLFEST 2021)** &nbsp; 225,097 VIEWS • 9,381 HRS • +276 SUBS")
        
        # Video Player Embed with black background wrapper matching Error 153 layout
        st.components.v1.html(
            f'''
            <div style="background-color: #111; border: 1px solid black; padding: 2px;">
                <iframe width="100%" height="400" 
                src="https://www.youtube.com/embed/_ivgaFkD4Ac" 
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen></iframe>
            </div>
            ''',
            height=410
        )
        
        v1, v2, v3 = st.columns([2, 1, 1])
        with v1:
            st.caption("Filmed personally by RJMedia on the front barrier at Solfest 2021 in Cumbria. Zero Topaz processing—pure front-row punk energy.")
        with v2:
            st.button("📋 COPY YOUTUBE CHAPTERS")
        with v3:
            st.button("↗ OPEN ON YOUTUBE")
        
        # Bottom Split Detail Boxes
        b1, b2 = st.columns(2)
        with b1:
            with st.container(border=True):
                st.markdown("**INTERACTIVE TIMESTAMPS &nbsp;&nbsp; CLICK TO SEEK**")
                st.markdown("""
                * **0:00** - Front-Barrier View & Air-Raid Siren Walk-On
                * **0:20** - Danny Farrant Walks Out to Green Sparkle Kit
                * **0:47** - Pounding Tom Intro & Crowd Chant
                * **1:05** - Chris Remington Bass Entrance (Fender Jazz Bass)
                * **1:46** - Steve Diggle Walks Out (All-White Denim Suit)
                """)
        with b2:
            with st.container(border=True):
                st.markdown("**STAGE GEAR & HARDWARE REALITY &nbsp;&nbsp; 100% RAW PHONE**")
                st.markdown("""
                * **Backdrop:** Painted 'SOLFEST' cosmic whale mural + dual Blackstar 4x12 stacks.
                * **Drums (Danny Farrant):** Lime-green sparkle Q Drum Co. kit.
                * **Bass (Chris Remington):** Natural ash Fender Jazz Bass (black block inlays).
                * **Lead Guitar (Steve Diggle):** Sunburst Fender Telecaster.
                * **Hardware Reality:** Left 100% untouched—phone ISP already sharpened edges.
                """)
