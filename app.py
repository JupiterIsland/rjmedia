"""
RJMedia Digital Liner Notes Generator & Channel Category Suite
Powered by Google Gemini 2.5 Multimodal + Streamlit
Organizes Live Music & Band Documentaries into 4 clear categories,
generates timestamped companion guides, and provides Topaz Video AI presets.
"""

import os
import re
import json
from datetime import datetime
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

try:
    from google import genai
    from google.genai import types
except ImportError:
    genai = None
    types = None

# ============================================================================
# PAGE CONFIGURATION & SESSION STATE
# ============================================================================

st.set_page_config(
    page_title="RJMedia Archive Vault & Liner Notes",
    page_icon="🎸",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "youtube_url_input" not in st.session_state:
    st.session_state.youtube_url_input = "https://youtu.be/4vDQteeeq_8?si=BQS5dUCLN_faDMcs"
if "generated_notes" not in st.session_state:
    st.session_state.generated_notes = ""
if "selected_category" not in st.session_state:
    st.session_state.selected_category = "📱 Category 1: Front-Row Festival Captures (Filmed by RJMedia)"

# ============================================================================
# CHANNEL CATEGORIES & CATALOG STRUCTURE
# ============================================================================

CHANNEL_CATEGORIES = {
    "📱 Category 1: Front-Row Festival Captures (Filmed by RJMedia)": {
        "description": "100% raw, untouched front-barrier smartphone captures filmed personally by RJMedia at Solfest 2021 in Cumbria.",
        "monetization_note": "Audio claimed by music publishers; monetize via Pinned Comment Tip Jar + End-Screen Cross-Linking.",
        "videos": {
            "Razorlight — 'In The Morning' (Live Solfest 2021 • Front-Row Capture)": "http://www.youtube.com/watch?v=4vDQteeeq_8",
            "The Buzzcocks — 'What Do I Get' (Live Solfest 2021 • 225K+ Views)": "http://www.youtube.com/watch?v=_ivgaFkD4Ac"
        }
    },
    "🎬 Category 2: Deep Band Documentaries & Biographies": {
        "description": "Long-form television documentaries, rare interviews, and deep musical history.",
        "monetization_note": "High watch-time authority drivers (179K+ views). Ideal for driving traffic to companion guides & tip jar.",
        "videos": {
            "Peter Green (Fleetwood Mac) — 1997 Documentary: LSD & Giving Money Away (179K Views)": "http://www.youtube.com/watch?v=fqVJvjKeW7s",
            "Leaves — We Are Shadows (Full 56-Minute Band Documentary)": "http://www.youtube.com/watch?v=GVne5G6uyt0"
        }
    },
    "✨ Category 3: 4K & HD Remastered Classics": {
        "description": "Archival live performances and broadcasts restored using precision Topaz Video AI & audio mastering pipelines.",
        "monetization_note": "Showcases RJMedia's technical restoration skills; links directly to downloadable Topaz JSON presets.",
        "videos": {
            "The Smiths — 'How Soon Is Now?' (RJMedia Remaster • 79K Views)": "https://youtu.be/WLU74h889VI?si=yg-SakWqJW7S7kd6",
            "22-20s — 'Such A Fool' (Live on Jools Holland 4K Remaster)": "http://www.youtube.com/watch?v=0ZQu8Fj1d8o",
            "The Verve — Live in London, 1993 (Restored & Remastered)": "http://www.youtube.com/watch?v=s5gKHgB63Lo",
            "Kasabian — T In The Park 2004 (Kinross, Scotland)": "http://www.youtube.com/watch?v=j1kZAP87n08"
        }
    },
    "📼 Category 4: 1990s Indie Gig & Radio Session Vault": {
        "description": "Rare 1990s club gigs, VHS bootlegs, and BBC radio sessions preserved for dedicated fans.",
        "monetization_note": "Cult fanbase magnet; high repeat viewership and community discussion.",
        "videos": {
            "Mansun — Manchester Roadhouse 21/09/1996 (Full 40m Set)": "http://www.youtube.com/watch?v=SHyclRafWnw",
            "The Verve — 'The Rolling People' Live at Haigh Hall (24/05/1998)": "http://www.youtube.com/watch?v=dSf8-EqTlUU",
            "Mansun — Live in Margate (24/01/1999 • Full 80m Concert)": "http://www.youtube.com/watch?v=YdZBmYkY-oQ",
            "Mansun — John Peel Session (24/03/1996)": "http://www.youtube.com/watch?v=xD9Vq0k5i3U"
        }
    }
}

# ============================================================================
# TOPAZ PRESETS
# ============================================================================

PRESET_LOW_QUALITY = {
    "Model": "Iris MQ (iris-2)",
    "Scale Factor": "2x (Stop at 720p/1080p)",
    "Revert Compression": 70,
    "Improve Detail": 20,
    "Sharpen": 10,
    "Reduce Noise": 25,
    "Dehalo": 20,
    "Anti-Alias / Deblur": -15,
    "Recover Original Detail": 40,
    "Focus Fix": "Off"
}

PRESET_FAST_4K = {
    "Model": "Proteus v4 (prob-4)",
    "Scale Factor": "2x (1080p → 4K native)",
    "Revert Compression": 25,
    "Improve Detail": 35,
    "Sharpen": 30,
    "Reduce Noise": 10,
    "Dehalo": 5,
    "Anti-Alias / Deblur": -15,
    "Recover Original Detail": 50,
    "Add Noise (Amount)": 2,
    "Add Noise (Size)": 1
}

PRESET_VHS_STAGE1 = {
    "Model": "Iris LQ (iris-3) — Stage 1: Cleaning",
    "Scale Factor": "1x (Native 480p/576p resolution)",
    "Revert Compression": 70,
    "Improve Detail": 10,
    "Sharpen": 0,
    "Reduce Noise": 40,
    "Dehalo": 50,
    "Anti-Alias / Deblur": 20,
    "Recover Original Detail": 15,
    "Purpose": "Strip VHS & broadcast ringing before upscaling"
}

PRESET_VHS_STAGE2 = {
    "Model": "Proteus v4 (prob-4) — Stage 2: Upscaling",
    "Scale Factor": "2x (→ 1440x1080 4:3 Pillarbox)",
    "Revert Compression": 15,
    "Improve Detail": 40,
    "Sharpen": 35,
    "Reduce Noise": 5,
    "Dehalo": 15,
    "Anti-Alias / Deblur": -10,
    "Recover Original Detail": 30,
    "Add Noise (Amount)": 4,
    "Add Noise (Size)": 2,
    "Purpose": "Upscale + inject fine grain to mask AI smoothness"
}

# ============================================================================
# DEEP LINER NOTES GENERATORS FOR RJMEDIA CATALOG
# ============================================================================

def generate_razorlight_liner_notes(video_id="4vDQteeeq_8"):
    """Deep-dive liner notes for Razorlight - In The Morning (Live Solfest 2021) filmed by RJMedia."""
    return f"""# 📱🎸 Razorlight — "In The Morning" (Live at Solfest 2021 • Original RJMedia Front-Row Capture)

**Video:** [http://www.youtube.com/watch?v={video_id}](http://www.youtube.com/watch?v={video_id})  
**Filmed By:** Richard John Murray (**RJMedia** • Live Music & Band Documentaries)  
**Source Reality:** **100% Untouched Smartphone Capture** (Filmed on the exact same phone & front barrier spot as the 225K-view Buzzcocks Solfest video)  
**Recorded:** August 2021 — Solfest Festival, Tarnside Farm, Cumbria, UK  
**Classic Reunited Lineup:** Johnny Borrell (Vocals / Guitar), Björn Ågren (Guitar), Carl Dalemo (Bass), Andy Burrows (Drums), plus touring keys

---

## 1. 60-Second Archival TL;DR

Filmed personally by **RJMedia** right against the front barrier at Cumbrian festival **Solfest 2021** (right behind a fan holding up the iconic round yellow *"solfest"* sign), this raw, untouched capture documents the classic reunited **Razorlight** lineup tearing through their 2006 indie-rock anthem *"In The Morning"*. Featuring **Andy Burrows** back behind the drum kit, **Björn Ågren** locking in the jagged opening riff on his natural semi-hollow guitar through dual red Blackstar amps, **Carl Dalemo** on his white Fender bass, and **Johnny Borrell** delivering a blistering center-stage vocal and guitar solo, the clip ends with a celebratory pan across the lit-up Solfest fairground at night.

---

## 2. Interactive Chapters & Timeline

*(Copy and paste the list below directly into your YouTube description to activate chapters)*

- [0:00](https://www.youtube.com/watch?v={video_id}&t=0s) **Opening Guitar Riff (Björn Ågren & Johnny Borrell) & Driving Drum Beat**
- [0:17](https://www.youtube.com/watch?v={video_id}&t=17s) **First Verse ("I don't know what I'm going to do / Maybe I've been here too long...")**
- [0:35](https://www.youtube.com/watch?v={video_id}&t=35s) **First Chorus ("In the morning, you know we won't remember a thing...")**
- [0:52](https://www.youtube.com/watch?v={video_id}&t=52s) **Second Verse ("Wake up, vomit up, hung around the stage...")**
- [1:09](https://www.youtube.com/watch?v={video_id}&t=69s) **Second Chorus & Front-Row Hands-In-The-Air Singalong**
- [1:41](https://www.youtube.com/watch?v={video_id}&t=101s) **Johnny Borrell & Björn Ågren Interlocking Guitar Solo Breakdown**
- [2:02](https://www.youtube.com/watch?v={video_id}&t=122s) **Post-Solo Chorus Drop & Crowd Jump**
- [2:49](https://www.youtube.com/watch?v={video_id}&t=169s) **Bridge Build-Up ("I didn't know who to trust...")**
- [3:21](https://www.youtube.com/watch?v={video_id}&t=201s) **Final Chorus Climax ("All night long... In the morning!")**
- [3:38](https://www.youtube.com/watch?v={video_id}&t=218s) **Big Finish, "Thank You!" & Night-Time Pan Across Solfest Fairground Ride**

---

## 3. Visual Gear & Stage Spotting (From the Front Barrier)

* **[0:01](https://www.youtube.com/watch?v={video_id}&t=1s) Stage Left Guitar Rig (Björn Ågren):** Natural maple finish **Gibson ES-335 / Epiphone Casino style semi-hollow electric guitar** with f-holes, played through **dual red Blackstar amplifier heads/combos** sitting on a flight case behind a full floor pedalboard; red **Nord Electro/Stage** keyboard positioned behind him.
* **[0:28](https://www.youtube.com/watch?v={video_id}&t=28s) Center Drum Riser (Andy Burrows):** White/silver sparkle drum kit on a rolling riser featuring the custom bass drum head emblazoned with **"THE RAZORLIGHT ARMS — LONDON • STOCKHOLM"**.
* **[0:32](https://www.youtube.com/watch?v={video_id}&t=32s) Center Vocals & Guitar (Johnny Borrell):** Sunburst **Fender Telecaster/Stratocaster** played low while singing into the center microphone.
* **[0:41](https://www.youtube.com/watch?v={video_id}&t=41s) Stage Right Bass Rig (Carl Dalemo):** Olympic White **Fender Precision Bass** with dark pickguard, framed by vertical cyan LED stage light tubes.
* **[3:42](https://www.youtube.com/watch?v={video_id}&t=222s) Solfest Night Atmosphere:** Camera pans right across the festival crowd to reveal strings of coloured festoon lights and the glowing Solfest fairground tower ride against the Cumbrian night sky before returning to the red-lit stage.

---

## 4. Channel Strategy Note: Connecting Your Solfest 2021 Series

Because this video was filmed from the **exact same front-barrier spot on the same phone** as your **225,107-view Buzzcocks Solfest video**, linking the two together via a dedicated **"Solfest 2021 Front-Row Vault"** playlist and an End Screen on the Buzzcocks video lets your 225K viewers discover this reunited Razorlight performance automatically.
"""


def generate_buzzcocks_liner_notes(video_id="_ivgaFkD4Ac"):
    """Deep-dive liner notes for RJMedia's 100% raw front-row phone capture of The Buzzcocks at Solfest 2021 (225K+ views)."""
    return f"""# 📱🎸 The Buzzcocks — "What Do I Get" (Live at Solfest 2021 • 100% Raw Front-Row Phone Capture)

**Video:** [http://www.youtube.com/watch?v={video_id}](http://www.youtube.com/watch?v={video_id})  
**Filmed By:** Richard John Murray (**RJMedia** • Live Music & Band Documentaries)  
**Source Reality:** **100% Untouched Smartphone Capture** (Zero AI / Zero Post-Processing — Companion to the Razorlight Solfest 2021 Capture)  
**Performance Status:** ⭐ **225,107+ Views** • **2,265+ Likes**  
**Recorded:** August 2021 — Solfest Festival, Tarnside Farm, Cumbria, UK  
**Lineup:** Steve Diggle (Vocals / Lead Guitar), Chris Remington (Bass), Danny Farrant (Drums), Mani Perazzoli (Guitar)

---

## 1. 60-Second Archival TL;DR

Filmed personally by **RJMedia** on a handheld phone right on the front barrier at Cumbrian festival **Solfest 2021**—with **zero remastering or post-processing**—this capture of the 1978 punk classic *"What Do I Get?"* has racked up over **225,000 views** on pure atmosphere alone. From the opening air-raid siren and Danny Farrant's tom build-up to **Steve Diggle** walking out in an all-white denim suit just feet from the lens, it proves that front-barrier positioning and a solid phone mic/camera beat over-processed studio edits every time.

---

## 2. Interactive Chapters & Setlist Index

- [0:00](https://www.youtube.com/watch?v={video_id}&t=0s) **Front-Barrier View & Air-Raid Siren Walk-On Tape**
- [0:20](https://www.youtube.com/watch?v={video_id}&t=20s) **Danny Farrant Walks Out to the Green Sparkle Drum Kit**
- [0:47](https://www.youtube.com/watch?v={video_id}&t=47s) **Pounding Drum Intro & Cumbrian Crowd Chant**
- [1:05](https://www.youtube.com/watch?v={video_id}&t=65s) **Chris Remington Bass Entrance & Driving Punk Groove**
- [1:46](https://www.youtube.com/watch?v={video_id}&t=106s) **Steve Diggle Stage Entrance (All-White Denim Suit)**
- [2:06](https://www.youtube.com/watch?v={video_id}&t=126s) **Main Guitar Riff Explodes ("What Do I Get?" Intro)**
- [2:40](https://www.youtube.com/watch?v={video_id}&t=160s) **First Verse ("I just want a lover like any other...")**
- [3:00](https://www.youtube.com/watch?v={video_id}&t=180s) **Chorus & Front-Row "Oh-Oh-Oh" Singalong**
- [3:43](https://www.youtube.com/watch?v={video_id}&t=223s) **Steve Diggle Center-Stage Guitar Solo**
- [4:26](https://www.youtube.com/watch?v={video_id}&t=266s) **Final Verse & High-Energy Breakdown**
- [5:11](https://www.youtube.com/watch?v={video_id}&t=311s) **Climax, Windmill Chords & Big Finish**

---

## 3. Visual Gear & Stage Spotting

* **[0:01](https://www.youtube.com/watch?v={video_id}&t=1s) Stage Backline & Backdrop:** Colourful painted **"SOLFEST"** backdrop featuring a cosmic whale and planets; dual **Blackstar** amplifier head-and-4x12 cabinet stacks flanking the drum riser.
* **[0:26](https://www.youtube.com/watch?v={video_id}&t=26s) Drums (Danny Farrant):** Lime-green sparkle **Q Drum Co.** kit with Zildjian cymbals on a raised riser.
* **[1:07](https://www.youtube.com/watch?v={video_id}&t=67s) Bass (Chris Remington):** Natural ash **Fender Jazz Bass** with tortoiseshell pickguard and black block inlays.
* **[1:58](https://www.youtube.com/watch?v={video_id}&t=118s) Lead Guitar (Steve Diggle):** 3-Tone Sunburst **Fender Telecaster** with white pickguard and maple fretboard.
* **[3:23](https://www.youtube.com/watch?v={video_id}&t=203s) Rhythm/Second Guitar (Mani Perazzoli):** **Gibson Les Paul** on stage right through a twin Blackstar stack.
"""


def generate_peter_green_liner_notes(video_id="fqVJvjKeW7s"):
    """Deep-dive liner notes for Peter Green (Fleetwood Mac) 1997 Documentary - 179K+ views."""
    return f"""# 🎸 Peter Green (Fleetwood Mac) — 1997 Documentary: LSD, Giving Money Away & The Road Back

**Video:** [http://www.youtube.com/watch?v={video_id}](http://www.youtube.com/watch?v={video_id})  
**Channel:** Live Music & Band Documentaries (RJMedia)  
**Archival Status:** ⭐ **179,152+ Views** • **2,941+ Likes**  
**Original Broadcast:** 1997 UK Television Documentary (24 mins 56 secs)  
**Featured Artists:** Peter Green, Len Green (Brother), Nigel Watson, Cozy Powell, Spike Edney (Peter Green Splinter Group)

---

## 1. 60-Second Archival TL;DR

For two decades, the fate of Fleetwood Mac founder **Peter Green**—the working-class East End guitar prodigy behind *"Albatross"*, *"Black Magic Woman"*, and *"Man of the World"*—was shrouded in myth. This rare 1997 documentary steps inside the family home where Green lived quietly for years, hears directly from Peter and his brother Len about the 1960s American LSD trip, psychiatric hospitalization, and electroconvulsive therapy (ECT) that derailed his career, and follows his fragile, deeply moving return to the stage with the **Peter Green Splinter Group** in 1997.

---

## 2. Interactive Chapters & Documentary Timeline

- [0:10](https://www.youtube.com/watch?v={video_id}&t=10s) **Introduction: Two Decades of Silence & The Legend of Peter Green**
- [1:23](https://www.youtube.com/watch?v={video_id}&t=83s) **1969 Archival Performance: Fleetwood Mac — "Oh Well (Part 1)"**
- [1:58](https://www.youtube.com/watch?v={video_id}&t=118s) **Brother Len Green on the 1960s US Tour, LSD & Santana's Visit**
- [2:49](https://www.youtube.com/watch?v={video_id}&t=169s) **Schizophrenia Diagnosis & The Reclusive Years in Richmond**
- [3:38](https://www.youtube.com/watch?v={video_id}&t=218s) **Peter Green Speaks Candidly About LSD, ECT & Heavy Tranquilizers**
- [4:15](https://www.youtube.com/watch?v={video_id}&t=255s) **Inside Peter's Bedroom: Gold Discs for "Albatross" & "Black Magic Woman"**
- [6:01](https://www.youtube.com/watch?v={video_id}&t=361s) **Reunion in Southend, Stopping the Heavy Tablets & Coming Back to Life**
- [7:16](https://www.youtube.com/watch?v={video_id}&t=436s) **Cutting His Long Fingernails & Picking Up the Guitar Again**
- [8:46](https://www.youtube.com/watch?v={video_id}&t=526s) **Peter Reacts to B.B. King's Famous Quote ("Shiver Down My Back")**
- [9:13](https://www.youtube.com/watch?v={video_id}&t=553s) **Peter Watches 1969 Footage of Himself Playing "Oh Well"**
- [10:31](https://www.youtube.com/watch?v={video_id}&t=631s) **The Truth Behind the "Pop Star Gives Money Away" Headlines**
- [11:38](https://www.youtube.com/watch?v={video_id}&t=698s) **On Tour in 1997 with the Peter Green Splinter Group (Ipswich Corn Exchange)**
- [15:55](https://www.youtube.com/watch?v={video_id}&t=955s) **"I Used to Put On a Sadness... I'm Not Sad Anymore"**
- [16:34](https://www.youtube.com/watch?v={video_id}&t=994s) **Backstage Radio Interview: "Clapton and Hendrix Go First... I Might Be the Third Thief"**
- [18:57](https://www.youtube.com/watch?v={video_id}&t=1137s) **Stage Walk-On & Live Performance: "Travelling Riverside Blues"**
- [20:57](https://www.youtube.com/watch?v={video_id}&t=1257s) **Peter on Fame: "Watch Out for People Who Pay False Compliments"**
- [21:30](https://www.youtube.com/watch?v={video_id}&t=1290s) **Live Performance: "Black Magic Woman" (Splinter Group)**
- [23:06](https://www.youtube.com/watch?v={video_id}&t=1386s) **"It's Not a Comeback, It's Starting Again" & Finale: "Man of the World"**
"""


def generate_smiths_liner_notes(video_id="WLU74h889VI"):
    """Liner notes for The Smiths - How Soon Is Now? (79K views)."""
    return f"""# 🎸 The Smiths — "How Soon Is Now?" (RJMedia Remaster • 79K Views)

**Video:** [https://youtu.be/{video_id}](https://youtu.be/{video_id})  
**Status:** ⭐ 79K views in 1 year  

---

## Interactive Chapters
- [0:00](https://www.youtube.com/watch?v={video_id}&t=0s) **Opening & Intro**
- [0:15](https://www.youtube.com/watch?v={video_id}&t=15s) **Signature Tremolo Guitar Riff (Johnny Marr)**
- [1:05](https://www.youtube.com/watch?v={video_id}&t=65s) **Vocal Entry (Morrissey)**
- [2:30](https://www.youtube.com/watch?v={video_id}&t=150s) **First Chorus**
- [3:45](https://www.youtube.com/watch?v={video_id}&t=225s) **Middle 8 / Bridge**
- [5:20](https://www.youtube.com/watch?v={video_id}&t=320s) **Final Chorus & Outro**
"""


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_api_key():
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        try:
            key = st.secrets.get("GEMINI_API_KEY")
        except Exception:
            key = None
    return key


def extract_video_id(url):
    match = re.search(r"(?:v=|youtu\.be\/|embed\/|shorts\/)([0-9A-Za-z_-]{11})", url)
    return match.group(1) if match else "4vDQteeeq_8"


def extract_chapters(liner_notes):
    chapters = []
    for line in liner_notes.splitlines():
        match = re.search(r"\[(\d{1,2}:\d{2}(?::\d{2})?)\]\([^)]+\)\s*(?:—|-)?\s*\**([^*(\n]+)\**", line)
        if match:
            chapters.append(f"{match.group(1).strip()} {match.group(2).strip()}")
    if not chapters:
        return "0:00 Intro"
    if not chapters[0].startswith(("0:00", "00:00")):
        chapters.insert(0, "0:00 Intro")
    return "\n".join(chapters)


def markdown_to_html(markdown_text):
    html_body = markdown_text
    html_body = re.sub(r"^### (.*)$", r"<h3>\1</h3>", html_body, flags=re.MULTILINE)
    html_body = re.sub(r"^## (.*)$", r"<h2>\1</h2>", html_body, flags=re.MULTILINE)
    html_body = re.sub(r"^# (.*)$", r"<h1>\1</h1>", html_body, flags=re.MULTILINE)
    html_body = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank">\1</a>', html_body)
    html_body = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", html_body)
    html_body = re.sub(r"^[*-] (.*)$", r"<li>\1</li>", html_body, flags=re.MULTILINE)
    html_body = html_body.replace("\n\n", "<br><br>")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>RJMedia Official Digital Liner Notes</title>
    <style>
        body {{ font-family: sans-serif; max-width: 860px; margin: 0 auto; padding: 28px; background: #0d1117; color: #c9d1d9; line-height: 1.65; }}
        h1, h2, h3 {{ color: #ff1493; }}
        a {{ color: #00ffff; text-decoration: none; font-weight: 600; }}
        .container {{ background: #161b22; padding: 32px; border-radius: 10px; border-left: 5px solid #ff1493; }}
    </style>
</head>
<body><div class="container">{html_body}</div></body>
</html>"""


def display_preset_ui(name, preset, key_prefix=""):
    st.markdown(f"### {name}", unsafe_allow_html=True)
    cols = st.columns(2)
    for i, (param, value) in enumerate(preset.items()):
        with cols[i % 2]:
            st.metric(label=param, value=str(value))
    json_data = json.dumps(preset, indent=2)
    st.download_button(
        label=f"📥 Download {name} as JSON",
        data=json_data,
        file_name=f"{name.replace(' ', '_').replace(':', '')}.json",
        mime="application/json",
        key=f"dl_{key_prefix}_{name}"
    )


def generate_liner_notes(youtube_url):
    video_id = extract_video_id(youtube_url)
    if video_id == "4vDQteeeq_8":
        return generate_razorlight_liner_notes(video_id)
    if video_id == "_ivgaFkD4Ac":
        return generate_buzzcocks_liner_notes(video_id)
    if video_id == "fqVJvjKeW7s":
        return generate_peter_green_liner_notes(video_id)
    if video_id == "WLU74h889VI":
        return generate_smiths_liner_notes(video_id)

    api_key = get_api_key()
    if not api_key or genai is None or types is None:
        return f"""# 🎸 RJMedia Archive Entry ({video_id})
**Video:** [http://www.youtube.com/watch?v={video_id}](http://www.youtube.com/watch?v={video_id})

- [0:00](https://www.youtube.com/watch?v={video_id}&t=0s) **Opening & Stage Intro**
- [1:30](https://www.youtube.com/watch?v={video_id}&t=90s) **Main Performance Highlight**
- [3:00](https://www.youtube.com/watch?v={video_id}&t=180s) **Finale & Crowd Reaction**

*(Add your `GEMINI_API_KEY` in the left sidebar to run full 1-FPS frame + audio analysis on any custom video!)*"""

    try:
        client = genai.Client(api_key=api_key)
        prompt = f"""
        You are an expert music archivist creating 'Digital Liner Notes' for RJMedia.
        Analyze this YouTube video and generate:
        1. **60-Second TL;DR**
        2. **Interactive Setlist & Chapters** formatted as: - [MM:SS](https://www.youtube.com/watch?v={video_id}&t=XXs) **Title**
        3. **Gear & Stage Spotting**
        4. **Key Quotes & Trivia**
        """
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[types.Part.from_uri(file_uri=youtube_url, mime_type="video/*"), prompt]
        )
        return response.text
    except Exception as e:
        return f"Gemini Error: {str(e)}"


# ============================================================================
# HEADER & BRANDING
# ============================================================================

st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0f0f0f 0%, #1a1a1a 100%); color: #00ffff; }
    .header-main { font-size: 2.4em; font-weight: bold; color: #ff1493; text-align: center; margin: 12px 0 4px 0; }
    .section-title { font-size: 1.5em; color: #00ffff; border-bottom: 3px solid #ff1493; padding-bottom: 8px; margin: 16px 0 12px 0; font-weight: 700; }
    .cat-box { background: #141c24; border: 1px solid #30363d; border-left: 4px solid #ff1493; padding: 14px; border-radius: 6px; margin-bottom: 14px; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header-main">🎸 RJMedia Channel Vault, Categories & Liner Notes Suite 🎸</div>
<div style="text-align: center; color: #00ffff; margin-bottom: 20px;">
    <strong>Live Music & Band Documentaries</strong> — Categorized Concert Vault, Front-Row Captures & Topaz AI Blueprints<br>
    <a href="https://www.youtube.com/@LiveMusicBandDocumentaries" target="_blank" style="color: #ff1493;">📺 Subscribe on YouTube</a> | 
    <a href="https://buymeacoffee.com/rjmedia" target="_blank" style="color: #ffaa00;">☕ Support via Penny-Per-Watch Tip Jar</a>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs([
    "🗂️ Categorized Channel Vault & Liner Notes",
    "🎚️ Topaz Presets Library",
    "📚 Topaz Masterclass (Raw Phone vs. VHS)",
    "💰 Channel Monetization & Cross-Link Strategy"
])

# ============================================================================
# TAB 1: CATEGORIZED CHANNEL VAULT & LINER NOTES
# ============================================================================

with tab1:
    st.markdown('<div class="section-title">Step 1: Browse Your Channel by Category (Showcasing Full Depth)</div>', unsafe_allow_html=True)

    selected_cat = st.radio(
        "Select a Channel Category:",
        list(CHANNEL_CATEGORIES.keys()),
        index=0,
        horizontal=True
    )
    cat_data = CHANNEL_CATEGORIES[selected_cat]

    st.markdown(f"""
    <div class="cat-box">
        <strong style="color:#ff1493;">{selected_cat}</strong><br>
        <span style="color:#e6edf3;">{cat_data['description']}</span><br>
        <small style="color:#ffaa00;">💡 <strong>Revenue Strategy:</strong> {cat_data['monetization_note']}</small>
    </div>
    """, unsafe_allow_html=True)

    col_left, col_right = st.columns([1.05, 0.95])

    with col_left:
        st.markdown("#### 📺 Videos in This Category")
        for v_title, v_url in cat_data["videos"].items():
            if st.button(f"▶️ Load: {v_title}", use_container_width=True, key=v_url):
                st.session_state.youtube_url_input = v_url
                st.session_state.generated_notes = generate_liner_notes(v_url)

    with col_right:
        youtube_url = st.text_input(
            "Active YouTube URL (or paste any video link):",
            key="youtube_url_input"
        )
        if youtube_url:
            st.video(youtube_url)
        if st.button("🚀 Generate / Refresh Liner Notes", type="primary", use_container_width=True):
            st.session_state.generated_notes = generate_liner_notes(youtube_url)

    if not st.session_state.generated_notes:
        st.session_state.generated_notes = generate_razorlight_liner_notes("4vDQteeeq_8")

    st.markdown("---")
    st.markdown(st.session_state.generated_notes)

    dl1, dl2, dl3 = st.columns(3)
    with dl1:
        st.download_button(
            "📥 Download Markdown (.md)",
            data=st.session_state.generated_notes,
            file_name=f"liner_notes_{extract_video_id(youtube_url)}.md",
            mime="text/markdown",
            use_container_width=True
        )
    with dl2:
        st.download_button(
            "📥 Copy YouTube Chapters (.txt)",
            data=extract_chapters(st.session_state.generated_notes),
            file_name=f"chapters_{extract_video_id(youtube_url)}.txt",
            mime="text/plain",
            use_container_width=True
        )
    with dl3:
        st.download_button(
            "📥 GitHub Pages HTML (.html)",
            data=markdown_to_html(st.session_state.generated_notes),
            file_name=f"index_{extract_video_id(youtube_url)}.html",
            mime="text/html",
            use_container_width=True
        )

# ============================================================================
# TAB 2: TOPAZ PRESETS
# ============================================================================

with tab2:
    st.markdown('<div class="section-title">🎚️ Expert Topaz Video AI Presets</div>', unsafe_allow_html=True)
    preset_choice = st.selectbox(
        "Choose a workflow:",
        [
            "1990s Broadcast Documentary & VHS (2-Stage Profile)",
            "Low-Quality Digital (360p-480p Web Rips)",
            "Fast 1080p → 4K Upscaling (Native 2x Speed Profile)"
        ]
    )
    if preset_choice == "1990s Broadcast Documentary & VHS (2-Stage Profile)":
        c1, c2 = st.columns(2)
        with c1:
            display_preset_ui("VHS Stage 1 - Iris", PRESET_VHS_STAGE1, "v1")
        with c2:
            display_preset_ui("VHS Stage 2 - Proteus", PRESET_VHS_STAGE2, "v2")
    elif preset_choice == "Low-Quality Digital (360p-480p Web Rips)":
        display_preset_ui("Low Quality Digital", PRESET_LOW_QUALITY, "lq")
    else:
        display_preset_ui("Fast 1080p to 4K", PRESET_FAST_4K, "4k")

# ============================================================================
# TAB 3: TOPAZ MASTERCLASS
# ============================================================================

with tab3:
    st.markdown('<div class="section-title">📚 Rule #0 of Remastering: Raw Phone Captures vs. Archival VHS</div>', unsafe_allow_html=True)
    st.markdown("""
    ### Why Your Solfest 2021 Videos (The Buzzcocks & Razorlight) Were Left 100% Untouched
    - **The Buzzcocks (`225,107+ views`)** and **Razorlight (`In The Morning`)** at Solfest 2021 were both filmed by RJMedia right on the front barrier using the exact same smartphone—with **zero Topaz AI processing**.
    - **Why?** Modern smartphones already run an internal Image Signal Processor (ISP) that denoises and sharpens edges in real time. Running heavy Topaz sharpening on top of clean front-row phone footage creates glowing halos around microphone stands and ruins natural stage lighting.
    - **Reserve Topaz Video AI for Damaged/Legacy Sources:** Use the 2-Stage Iris + Proteus pipeline on 1990s interlaced PAL documentaries (*Peter Green 1997*), 1990s VHS club bootlegs (*Mansun 1996*, *The Verve 1993*), and starved early-2000s broadcast captures.
    """)

# ============================================================================
# TAB 4: MONETIZATION & CHANNEL STRATEGY
# ============================================================================

with tab4:
    st.markdown('<div class="section-title">💰 How to Turn Views Into Income (Without Deleting Your Hits!)</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 1. Why You Must NOT Delete Your 225K Buzzcocks or 179K Peter Green Videos
    Even when you film a concert yourself on your own phone (like **The Buzzcocks** and **Razorlight** at Solfest 2021), YouTube's automated **Content ID** detects the underlying song composition owned by music publishers and claims the AdSense. Deleting those videos won't make music uploads monetizable—it only destroys your channel's 480,000+ views of algorithmic authority!

    ### 2. Funnel Your 225,000 Buzzcocks Viewers Straight Into Razorlight
    Put this **Pinned Comment** on your 225K-view Buzzcocks video right now so viewers discover your Razorlight capture filmed on the exact same phone at Solfest:
    """)
    st.code("""📌 Filmed by RJMedia right on the front barrier at Solfest 2021 on my phone (100% raw & untouched!).
👉 Watch RAZORLIGHT ('In The Morning') filmed from this exact same barrier spot at Solfest 2021: https://youtu.be/4vDQteeeq_8
🎬 Watch our 179K-view Peter Green (Fleetwood Mac) 1997 Documentary: https://youtu.be/fqVJvjKeW7s
☕ Music uploads earn £0.00 in YouTube AdSense due to song copyright claims—if you enjoyed this front-row capture, toss a penny/coffee in the tip jar: https://buymeacoffee.com/rjmedia""", language="text")

    st.markdown("""
    ### 3. What to Put on a Second, 100% AdSense-Monetizable Channel (`RJMedia Tech & Remaster Lab`)
    Keep **Live Music & Band Documentaries** intact as your massive music archive + tip-jar funnel, and launch a linked second channel containing **zero copyrighted song audio**:
    1. **Voiceover / Silent Topaz Video AI Before-and-After Breakdowns** (100% AdSense safe).
    2. **GPU & Hardware Benchmarks** (VRAM scaling, `MemoryOS`, and `Jupiter One` hardware reality tests).
    3. **Concert Gear & Behind-the-Barrier Stories** using your own voiceover and still frames from Solfest.
    """)