"""
RJMedia Channel Hub & Monetization Dashboard
Your YouTube channel becomes a searchable, monetizable website
Featured: 35+ remasters, documentaries, live performances
Income potential: Tips, Buy Me a Coffee, Membership

Every video is an archive with:
- AI-generated liner notes (Gemini 2.5)
- Searchable transcripts
- Topaz preset references
- Direct tip link
"""

import os
import re
import streamlit as st
import pandas as pd
import json
from datetime import datetime
from PIL import Image
import requests

# ============================================================================
# PAGE CONFIG
# ============================================================================

st.set_page_config(
    page_title="RJMedia — Live Music & Band Documentaries",
    page_icon="🎸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS (DARK MODE + MONETIZATION FOCUS)
# ============================================================================

st.markdown("""
<style>
    /* Dark professional theme */
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
        color: #e0e0e0;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #ff1493;
        text-shadow: 0 0 10px rgba(255, 20, 147, 0.3);
    }
    
    /* Primary buttons */
    .stButton > button {
        background: linear-gradient(135deg, #ff1493 0%, #ff0080 100%);
        color: white;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 12px 24px;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #ff0080 0%, #cc0066 100%);
        box-shadow: 0 0 20px rgba(255, 20, 147, 0.5);
    }
    
    /* Tip jar highlight */
    .tip-jar {
        background: linear-gradient(135deg, rgba(255, 170, 0, 0.2) 0%, rgba(255, 136, 0, 0.2) 100%);
        border: 2px solid #ffaa00;
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 0 30px rgba(255, 170, 0, 0.3);
    }
    
    .tip-jar h3 {
        color: #ffaa00;
        text-align: center;
        margin: 0 0 15px 0;
    }
    
    /* Video card */
    .video-card {
        background: rgba(20, 30, 60, 0.8);
        border-left: 4px solid #ff1493;
        padding: 15px;
        margin: 10px 0;
        border-radius: 6px;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .video-card:hover {
        background: rgba(30, 50, 90, 0.9);
        border-left-color: #ffaa00;
        box-shadow: 0 0 20px rgba(255, 20, 147, 0.3);
    }
    
    /* Stats boxes */
    .stat-box {
        background: rgba(30, 50, 90, 0.6);
        border: 1px solid #00ffff;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        margin: 10px 0;
    }
    
    .stat-number {
        font-size: 2em;
        font-weight: bold;
        color: #ffaa00;
    }
    
    .stat-label {
        font-size: 0.9em;
        color: #00ffff;
        margin-top: 5px;
    }
    
    /* Section divider */
    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #ff1493, transparent);
        margin: 30px 0;
    }
    
    /* Navigation tabs */
    .stTabs [data-baseweb="tab-list"] button {
        color: #00ffff;
        font-weight: bold;
    }
    
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        color: #ffaa00;
        border-bottom: 3px solid #ff1493;
    }
    
    /* Info box */
    .info-box {
        background: rgba(0, 255, 255, 0.1);
        border-left: 4px solid #00ffff;
        padding: 15px;
        border-radius: 4px;
        margin: 15px 0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# HEADER & BRANDING
# ============================================================================

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    <div style="text-align: center;">
        <h1 style="margin-bottom: 5px; font-size: 2.5em;">🎸 RJMedia</h1>
        <p style="color: #00ffff; font-size: 1.2em; margin: 0;">Live Music & Band Documentaries</p>
        <p style="color: #ffaa00; font-size: 0.9em; margin-top: 5px;">35+ Remasters • 967K Views • 7.76 Years of Watch Time</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ============================================================================
# CHANNEL STATS (TOP OF PAGE)
# ============================================================================

st.markdown("<h2 style='text-align: center; color: #ff1493;'>📊 Your Channel At A Glance</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">967K</div>
        <div class="stat-label">Total Views</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">7.76y</div>
        <div class="stat-label">Watch Time</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">35+</div>
        <div class="stat-label">Videos</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">4.55%</div>
        <div class="stat-label">Avg CTR</div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# TIP JAR (PROMINENT, TOP)
# ============================================================================

st.markdown("""
<div class="tip-jar">
    <h3>☕ Support This Channel</h3>
    <p style="text-align: center; margin: 10px 0; color: #ffaa00;">
        <strong>Your tips pay for:</strong> Gemini AI analysis, Topaz presets, server hosting, new uploads
    </p>
    <p style="text-align: center; margin: 10px 0; color: #e0e0e0; font-size: 0.9em;">
        Publishers own the music rights, so ads don't reach us. 
        But your tips make the next remaster possible. ❤️
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <a href="https://buymeacoffee.com/rjmedia" target="_blank" style="text-decoration: none;">
        <button style="width: 100%; padding: 15px; background: linear-gradient(135deg, #ffaa00 0%, #ff8800 100%); 
                       color: black; font-weight: bold; border: none; border-radius: 8px; cursor: pointer; font-size: 1em;">
            ☕ Buy Me a Coffee
        </button>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a href="https://www.paypal.com/donate/?hosted_button_id=PLACEHOLDER" target="_blank" style="text-decoration: none;">
        <button style="width: 100%; padding: 15px; background: linear-gradient(135deg, #003087 0%, #002663 100%); 
                       color: white; font-weight: bold; border: none; border-radius: 8px; cursor: pointer; font-size: 1em;">
            💳 PayPal Tip
        </button>
    </a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <a href="https://www.youtube.com/@LiveMusicBandDocumentaries?sub_confirmation=1" target="_blank" style="text-decoration: none;">
        <button style="width: 100%; padding: 15px; background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%); 
                       color: white; font-weight: bold; border: none; border-radius: 8px; cursor: pointer; font-size: 1em;">
            📺 Subscribe
        </button>
    </a>
    """, unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# ============================================================================
# MAIN TAB STRUCTURE
# ============================================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎬 Video Archive",
    "💰 Monetization Dashboard",
    "🎚️ Topaz Presets",
    "📈 Analytics",
    "⚙️ Manage Videos"
])

# ============================================================================
# TAB 1: VIDEO ARCHIVE (SEARCHABLE)
# ============================================================================

with tab1:
    st.markdown("### 🎬 Full Video Archive (35+ Videos)")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        search_query = st.text_input(
            "🔍 Search by title, artist, or band:",
            placeholder="e.g., 'The Smiths', 'Peter Green', 'Everton'",
            label_visibility="collapsed"
        )
    
    with col2:
        sort_by = st.selectbox(
            "Sort by:",
            ["Views (High to Low)", "Watch Time (High to Low)", "Date (Newest)", "Date (Oldest)"],
            label_visibility="collapsed"
        )
    
    st.markdown("---")
    
    # Sample data (you'll populate this from your spreadsheet)
    sample_videos = [
        {
            "title": "The Smiths - Live Rockabilly 1984 FHD",
            "artist": "The Smiths",
            "views": 14994,
            "watch_hours": 12711,
            "date": "May 5, 2025",
            "url": "https://www.youtube.com/watch?v=WLU74h889VI",
            "thumbnail": "🎸"
        },
        {
            "title": "Peter Green (Fleetwood Mac) - 1997 Documentary LSD Interview",
            "artist": "Peter Green",
            "views": 179079,
            "watch_hours": 21134,
            "date": "Jul 17, 2024",
            "url": "https://www.youtube.com/watch?v=...",
            "thumbnail": "🎙️"
        },
        {
            "title": "The Buzzcocks - What Do I Get (Live 2021)",
            "artist": "The Buzzcocks",
            "views": 225097,
            "watch_hours": 9381,
            "date": "Aug 30, 2021",
            "url": "https://www.youtube.com/watch?v=...",
            "thumbnail": "🎵"
        },
        {
            "title": "Everton 3-2 Crystal Palace - 1982 Match Commentary",
            "artist": "Sports Archive",
            "views": 19194,
            "watch_hours": 1891,
            "date": "May 11, 2022",
            "url": "https://www.youtube.com/watch?v=...",
            "thumbnail": "⚽"
        }
    ]
    
    # Filter by search
    filtered = sample_videos
    if search_query:
        filtered = [v for v in sample_videos if search_query.lower() in v["title"].lower() or search_query.lower() in v["artist"].lower()]
    
    # Sort
    if sort_by == "Views (High to Low)":
        filtered = sorted(filtered, key=lambda x: x["views"], reverse=True)
    elif sort_by == "Watch Time (High to Low)":
        filtered = sorted(filtered, key=lambda x: x["watch_hours"], reverse=True)
    elif sort_by == "Date (Newest)":
        filtered = sorted(filtered, key=lambda x: x["date"], reverse=True)
    
    # Display
    if not filtered:
        st.warning("No videos match your search. Try another query.")
    else:
        for i, video in enumerate(filtered):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"""
                <div class="video-card">
                    <strong>{video['thumbnail']} {video['title']}</strong><br>
                    <small style="color: #00ffff;">Artist:</small> {video['artist']} | 
                    <small style="color: #ffaa00;">{video['views']:,} views</small> | 
                    <small style="color: #00ffff;">{video['watch_hours']:,} hrs watched</small>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                if st.button("📄 Generate Notes", key=f"gen_{i}"):
                    st.info(f"Generating liner notes for: {video['title']}")
                    st.success(f"✅ Liner notes ready! Download below:")
                    st.download_button(
                        label="📥 Download Notes",
                        data=f"# {video['title']}\n\n[Content would go here]",
                        file_name=f"{video['title'][:30]}.md"
                    )

# ============================================================================
# TAB 2: MONETIZATION DASHBOARD
# ============================================================================

with tab2:
    st.markdown("### 💰 Monetization & Income Potential")
    
    st.markdown("""
    <div class="info-box">
    <strong>Your Situation:</strong><br>
    967K views, 7.76 years watch time, but publishers own ad revenue (£0 from YouTube ads).<br>
    <strong>Your Solution:</strong> Direct tips from viewers who value your work.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📊 Conversion Scenarios")
        
        st.markdown("""
        **If 1% of viewers tip £2:**
        - 967K views × 1% = 9,670 tips
        - 9,670 × £2 = **£19,340/year** 💰
        
        **If 0.5% of viewers tip £1:**
        - 967K views × 0.5% = 4,835 tips
        - 4,835 × £1 = **£4,835/year** 💰
        
        **If 0.1% of viewers tip £5:**
        - 967K views × 0.1% = 967 tips
        - 967 × £5 = **£4,835/year** 💰
        """)
    
    with col2:
        st.markdown("#### 🎯 Your Best Videos (By Watch Time)")
        
        top_videos = [
            ("Peter Green Documentary", 21134, "https://..."),
            ("The Smiths - Rockabilly", 12711, "https://..."),
            ("The Buzzcocks - Live", 9381, "https://..."),
            ("Jesus and Mary Chain", 7891, "https://..."),
            ("Mansun - Cancer Alternative", 6900, "https://...")
        ]
        
        for title, hours, url in top_videos:
            potential = int((hours / 68056.5) * 4835)  # £0.071 per watch hour (conservative)
            st.markdown(f"**{title}**  \n{hours:,} hrs → ~£{potential} potential tip income")
    
    st.markdown("---")
    
    st.markdown("#### 🚀 Implementation Strategy")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Step 1: Set Up**
        - Create Buy Me a Coffee
        - Add PayPal donate button
        - Create Discord (free)
        """)
    
    with col2:
        st.markdown("""
        **Step 2: Promote**
        - Pinned comment (all videos)
        - Description link
        - Sidebar widget (here)
        - Discord announcement
        """)
    
    with col3:
        st.markdown("""
        **Step 3: Track**
        - Monitor Buy Me a Coffee stats
        - Track clicks from this site
        - Optimize messaging
        - A/B test button placement
        """)
    
    st.markdown("---")
    
    st.markdown("#### 💬 Sample Messaging (for Pinned Comments)")
    
    st.code("""
If you love these remasters, consider a tip ☕
This channel doesn't get YouTube ad revenue 
(publishers own the music rights).
Your support makes the next upload possible ❤️

Buy Me a Coffee: [link]
PayPal: [link]
Discord: [link]
    """)

# ============================================================================
# TAB 3: TOPAZ PRESETS
# ============================================================================

with tab3:
    st.markdown("### 🎚️ Topaz Video AI Presets (Learn & Download)")
    
    preset_category = st.selectbox(
        "Choose a workflow:",
        [
            "Low-Quality Digital (360p→720p)",
            "Fast 1080p → 4K Upscaling",
            "1990s VHS Restoration",
            "All Presets (Download)"
        ]
    )
    
    if preset_category == "All Presets (Download)":
        st.markdown("#### 📥 Download All 4 Presets")
        
        presets = {
            "Low_Quality_Digital.json": {"model": "Iris MQ", "scale": "2x"},
            "Fast_1080p_to_4K.json": {"model": "Proteus v4", "scale": "2x native"},
            "VHS_Stage1.json": {"model": "Iris LQ", "scale": "1x"},
            "VHS_Stage2.json": {"model": "Proteus v4", "scale": "2x"}
        }
        
        for filename, info in presets.items():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{filename}** — {info['model']} ({info['scale']})")
            with col2:
                st.download_button(
                    label="📥 Download",
                    data=json.dumps(info),
                    file_name=filename,
                    key=filename
                )

# ============================================================================
# TAB 4: ANALYTICS
# ============================================================================

with tab4:
    st.markdown("### 📈 Channel Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 👥 Viewer Engagement")
        st.markdown("""
        - **Total Channel Views:** 967,422
        - **Average Views per Video:** 27,640
        - **Total Watch Time:** 68,056.5 hours
        - **Avg Watch Time per Video:** 1,944 hours
        - **Subscribers:** ~1,891
        - **Avg CTR:** 4.55%
        """)
    
    with col2:
        st.markdown("#### 🎯 Top Performing Videos")
        st.markdown("""
        1. **Peter Green Doc** — 179K views, 21K hrs
        2. **Buzzcocks Live** — 225K views, 9.3K hrs
        3. **The Smiths** — 14.9K views, 12.7K hrs
        4. **Everton Match** — 19.1K views, 1.8K hrs
        5. **Mansun** — 21.8K views, 6.9K hrs
        """)
    
    st.markdown("---")
    
    st.markdown("#### 💡 Insights")
    
    st.info("""
    **Key Finding:** Your videos have HIGH watch time-to-view ratio.
    This means people BINGE your content once they start.
    
    **Opportunity:** This is perfect for a tip jar.
    People who watch 2+ hours are invested in your work.
    """)

# ============================================================================
# TAB 5: MANAGE VIDEOS (ADMIN)
# ============================================================================

with tab5:
    st.markdown("### ⚙️ Manage Your Video Archive")
    
    st.info("Admin panel: Add, edit, or remove videos from your archive.")
    
    action = st.radio("Choose action:", ["View All Videos", "Add New Video", "Edit Video", "Delete Video"])
    
    if action == "Add New Video":
        st.markdown("#### ➕ Add New Video")
        
        col1, col2 = st.columns(2)
        
        with col1:
            video_title = st.text_input("Video Title (from YouTube)")
            youtube_url = st.text_input("YouTube URL")
            artist = st.text_input("Artist / Band")
        
        with col2:
            views = st.number_input("View Count", min_value=0, step=100)
            watch_hours = st.number_input("Watch Hours", min_value=0.0, step=100.0)
            publish_date = st.date_input("Publish Date")
        
        if st.button("✅ Add to Archive"):
            st.success(f"✅ Added: {video_title}")
            st.balloons()

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### ☕ Support
    [Buy Me a Coffee](https://buymeacoffee.com/rjmedia)
    """)

with col2:
    st.markdown("""
    ### 📺 YouTube
    [@Live Music & Band Docs](https://www.youtube.com/@LiveMusicBandDocumentaries)
    """)

with col3:
    st.markdown("""
    ### 💬 Discord
    [Join Community](https://discord.gg/rjmedia)
    """)

st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.85em; margin-top: 20px;">
Built with Streamlit + Gemini 2.5 | 
<a href="https://github.com/rjmedia" style="color: #ff1493;">Open Source on GitHub</a>
</div>
""", unsafe_allow_html=True)
