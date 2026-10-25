"""
Generates two high-contrast, ADHD-friendly Infographic PDF Poster sheets for RJMedia:
1. RJMedia_ADHD_YouTube_Masterplan.pdf
2. RJMedia_ADHD_Topaz_Infographic.pdf

Run:
    pip install reportlab
    python generate_adhd_pdfs.py
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas


def draw_card(c, x, y, w, h, bg_hex, border_hex, title="", title_hex="#00ffff"):
    c.setFillColor(colors.HexColor(bg_hex))
    c.setStrokeColor(colors.HexColor(border_hex))
    c.setLineWidth(2)
    c.roundRect(x, y, w, h, 8, fill=1, stroke=1)
    if title:
        c.setFillColor(colors.HexColor(title_hex))
        c.setFont("Helvetica-Bold", 12)
        c.drawString(x + 12, y + h - 20, title)


def build_youtube_masterplan_pdf(filename="RJMedia_ADHD_YouTube_Masterplan.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Dark Background
    c.setFillColor(colors.HexColor("#0d1117"))
    c.rect(0, 0, width, height, fill=1, stroke=0)

    # Header Banner
    draw_card(c, 25, height - 85, width - 50, 65, "#161b22", "#ff1493")
    c.setFillColor(colors.HexColor("#ff1493"))
    c.setFont("Helvetica-Bold", 18)
    c.drawString(40, height - 48, "RJMEDIA YOUTUBE COMMAND SHEET (ADHD QUICK-ACTION)")
    c.setFillColor(colors.HexColor("#00ffff"))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(40, height - 68, "967,422 Views  |  68,056.5 Watch Hours (7.76 Years!)  |  13.55M Impressions  |  1,891 Subs")

    # Golden Rule Alert Box
    draw_card(c, 25, height - 165, width - 50, 68, "#2a1215", "#ff4444", "RULE #1: NEVER DELETE YOUR HIGH-VIEW VIDEOS!", "#ffaa00")
    c.setFillColor(colors.HexColor("#f0f6fc"))
    c.setFont("Helvetica", 9.5)
    c.drawString(37, height - 132, "• Even on your own phone recordings (Buzzcocks, Razorlight, Maximo Park), publishers claim the SONG melody.")
    c.drawString(37, height - 146, "• Deleting videos destroys your 68,056 hours of algorithmic authority. Keep every single watch hour!")
    c.drawString(37, height - 160, "• Publishers CANNOT claim your Pinned Comment or Description. Use them to funnel views to BuyMeACoffee.")

    # Mission 1 Box
    draw_card(c, 25, height - 280, width - 50, 102, "#161b22", "#00ffff", "MISSION 1 (2 MINS): FIX MAXIMO PARK TITLE (HIDDEN 2ND SONG!)", "#00ffff")
    c.setFillColor(colors.HexColor("#f0f6fc"))
    c.setFont("Helvetica", 9.5)
    c.drawString(37, height - 216, "[  ] Video ID: AIoPylSQUKw (8m 45s) actually contains TWO full songs + an NHS dedication speech!")
    c.setFillColor(colors.HexColor("#ffaa00"))
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(37, height - 232, "     New Title: Maximo Park - The National Health & Midnight On The Hill (Live Solfest 2021 Front-Row)")
    c.setFillColor(colors.HexColor("#c9d1d9"))
    c.setFont("Courier-Bold", 8.5)
    c.drawString(37, height - 248, "     Chapters: 0:00 Intro | 0:06 The National Health | 3:12 NHS Dedication | 4:25 Midnight on the Hill")
    c.drawString(37, height - 262, "     Result: Ranks in YouTube search for BOTH songs + NHS tribute.")

    # Mission 2 Box
    draw_card(c, 25, height - 405, width - 50, 112, "#161b22", "#238636", "MISSION 2 (3 MINS): LINK YOUR SOLFEST 2021 FRONT-ROW TRILOGY", "#3fb950")
    c.setFillColor(colors.HexColor("#f0f6fc"))
    c.setFont("Helvetica", 9.5)
    c.drawString(37, height - 330, "[  ] All 3 were filmed on the SAME phone from the SAME front-barrier spot at Solfest 2021:")
    c.drawString(37, height - 345, "     1. The Buzzcocks - What Do I Get (_ivgaFkD4Ac) -> 225,097 Views | 9,381 Watch Hours")
    c.drawString(37, height - 360, "     2. Razorlight - In The Morning (4vDQteeeq_8)   -> Reunited Lineup (Andy Burrows on drums)")
    c.drawString(37, height - 375, "     3. Maximo Park - National Health & Midnight on the Hill (AIoPylSQUKw)")
    c.setFillColor(colors.HexColor("#ffaa00"))
    c.drawString(37, height - 393, "[  ] ACTION: Add End Screens on Buzzcocks (last 20s) pointing directly to Razorlight & Maximo Park!")

    # Mission 3 Box: Big 5 Table
    draw_card(c, 25, height - 565, width - 50, 148, "#161b22", "#ff1493", "MISSION 3 (3 MINS): PIN YOUR COFFEE LINK ON YOUR TOP 5 GIANTS (623K VIEWS)", "#ff1493")
    c.setFillColor(colors.HexColor("#f0f6fc"))
    c.setFont("Courier-Bold", 8.8)
    y_row = height - 455
    rows = [
        "[  ] 1. _ivgaFkD4Ac | Buzzcocks - What Do I Get (Solfest 21) | 225,097 views |  9,381 hrs",
        "[  ] 2. fqVJvjKeW7s | Peter Green 1997 Documentary (LSD)     | 179,079 views | 23,134 hrs",
        "[  ] 3. ubkpJnoXVnA | Peter Green - A Hard Road              |  90,131 views | 10,007 hrs",
        "[  ] 4. WLU74h889VI | The Smiths - Rockpalast 1984 FHD (71m) |  79,529 views | 14,995 hrs",
        "[  ] 5. GjoSfR70wc0 | Peter Green 1997 Doc (FHD Remaster)    |  49,558 views |  3,428 hrs",
    ]
    for r in rows:
        c.drawString(37, y_row, r)
        y_row -= 18
    c.setFillColor(colors.HexColor("#00ffff"))
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(37, height - 552, "Proof FHD Works: Your Peter Green FHD Remaster added +49,558 EXTRA views on top of the 179K original!")

    # 5 Channel Playlists Box
    draw_card(c, 25, 30, width - 50, height - 610, "#161b22", "#e3b341", "YOUR 5 CHANNEL PLAYLIST CATEGORIES (ORGANIZE HOMEPAGE)", "#e3b341")
    c.setFillColor(colors.HexColor("#f0f6fc"))
    c.setFont("Helvetica", 9.2)
    cats = [
        "1. RJMedia Front-Row Festival & Gig Captures (Buzzcocks, Razorlight, Maximo Park, JAMC 8.33% CTR)",
        "2. Peter Green & Classic Rock Documentaries (325,000+ Views | 37,000+ Watch Hours | +953 Subs)",
        "3. FHD & 4K Concert Restorations (The Smiths Rockpalast 1984 FHD, Editors Glasto 23, 22-20s 4K)",
        "4. The Mansun & Paul Draper Vault (Channel-record 11.08% CTR @ Manchester Gorilla, Glasto 98)",
        "5. Goodison Park Historic Atmosphere (Everton 3-2 Palace: 191,582 Views & 10.0% Thumbnail CTR)"
    ]
    yc = height - 620
    for cat in cats:
        c.drawString(37, yc, cat)
        yc -= 16

    c.save()
    print(f"Saved: {filename}")


def build_topaz_infographic_pdf(filename="RJMedia_ADHD_Topaz_Infographic.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Dark Background
    c.setFillColor(colors.HexColor("#0d1117"))
    c.rect(0, 0, width, height, fill=1, stroke=0)

    # Header
    draw_card(c, 25, height - 85, width - 50, 65, "#161b22", "#00ffff")
    c.setFillColor(colors.HexColor("#00ffff"))
    c.setFont("Helvetica-Bold", 18)
    c.drawString(40, height - 48, "TOPAZ VIDEO AI: ADHD VISUAL DECISION CARD")
    c.setFillColor(colors.HexColor("#ff1493"))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(40, height - 68, "RJMedia Hardware Reality Sheet  |  Max Memory: 85%  |  Max Processes: 1  |  CPU Grain: OFF")

    # Column 1: Raw Phone
    col_w = (width - 70) / 3
    y_top = height - 460
    draw_card(c, 25, y_top, col_w, 355, "#2a1215", "#ff4444", "1. MODERN PHONE", "#ff4444")
    c.setFillColor(colors.HexColor("#ffaa00"))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(35, y_top + 315, "Solfest 2021 Captures")
    c.setFillColor(colors.HexColor("#f0f6fc"))
    c.setFont("Helvetica", 9)
    p1_lines = [
        "• Buzzcocks (225K views)",
        "• Razorlight (Solfest 21)",
        "• Maximo Park (Solfest 21)",
        "",
        "ACTION:",
        "STOP! DO NOT RUN TOPAZ!",
        "",
        "WHY:",
        "Your phone's internal ISP",
        "chip already denoised and",
        "sharpened the edges while",
        "recording.",
        "",
        "Running Proteus or Iris",
        "on clean phone footage",
        "double-sharpens halos",
        "around mic stands and",
        "turns faces into plastic.",
        "",
        "UPLOAD 100% RAW!"
    ]
    yp = y_top + 290
    for line in p1_lines:
        c.drawString(35, yp, line)
        yp -= 13

    # Column 2: 1990s VHS / PAL Broadcast
    x2 = 35 + col_w
    draw_card(c, x2, y_top, col_w, 355, "#161b22", "#ff1493", "2. 90s VHS / TV DOC", "#ff1493")
    c.setFillColor(colors.HexColor("#ffaa00"))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x2 + 10, y_top + 315, "Peter Green 97 / Mansun")
    c.setFillColor(colors.HexColor("#f0f6fc"))
    c.setFont("Helvetica", 9)
    p2_lines = [
        "STEP 0 (PRE-PROCESS):",
        "• Bob Deinterlace to 50p/60p",
        "• Crop bottom 8-14px noise",
        "",
        "STAGE 1 (CLEAN @ 1x):",
        "• Model: Iris LQ (Scale 1x)",
        "• Revert Compression: 70",
        "• Reduce Noise: 40",
        "• Dehalo: 50 (Kills ringing)",
        "• Improve Detail: 10",
        "• Sharpen: 0 (NEVER in Stg 1)",
        "• Anti-Alias/Deblur: +20",
        "• Recover Detail: 15",
        "",
        "STAGE 2 (UPSCALE @ 2x):",
        "• Model: Proteus v4 (1080p)",
        "• Revert Compression: 15",
        "• Improve Detail: 40",
        "• Sharpen: 35",
        "• Add Noise/Grain: Amt 3-4"
    ]
    yp = y_top + 290
    for line in p2_lines:
        c.drawString(x2 + 10, yp, line)
        yp -= 13

    # Column 3: Fast 1080p -> 4K
    x3 = 45 + (col_w * 2)
    draw_card(c, x3, y_top, col_w, 355, "#161b22", "#00ffff", "3. FAST 1080p -> 4K", "#00ffff")
    c.setFillColor(colors.HexColor("#ffaa00"))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x3 + 10, y_top + 315, "22-20s Jools 4K / Clean HD")
    c.setFillColor(colors.HexColor("#f0f6fc"))
    c.setFont("Helvetica", 9)
    p3_lines = [
        "HARDWARE TRAP:",
        "• NEVER use Rhea for 2x!",
        "  (Rhea is 4x only -> renders",
        "  at 8K then downscales!)",
        "",
        "FAST 4K NATIVE 2x SETTINGS:",
        "• Model: Proteus v4 (Scale 2x)",
        "• Focus Fix: OFF",
        "• Auto Parameter: OFF",
        "• Revert Compression: 25",
        "• Improve Detail: 35",
        "• Sharpen: 30",
        "• Reduce Noise: 10",
        "• Dehalo: 5",
        "• Anti-Alias/Deblur: -15",
        "• Recover Detail: 50",
        "• Add Noise (Prenoise): 2",
        "",
        "ENCODER:",
        "• HEVC NVENC Main10 (10-bit)"
    ]
    yp = y_top + 290
    for line in p3_lines:
        c.drawString(x3 + 10, yp, line)
        yp -= 13

    # Bottom CLI Cheat Box
    draw_card(c, 25, 30, width - 50, height - 510, "#12161c", "#3fb950", "GUI SLIDER TO FFMPEG CLI (tvai_up) MAPPING", "#3fb950")
    c.setFillColor(colors.HexColor("#c9d1d9"))
    c.setFont("Courier-Bold", 9)
    cli_lines = [
        "Revert Compression (60) -> compression=0.60   |   Improve Detail (30) -> details=0.30",
        "Sharpen (30)            -> blur=0.30          |   Reduce Noise (25)   -> noise=0.25",
        "Dehalo (20)             -> halo=0.20          |   Anti-Alias (-15)    -> preblur=-0.15",
        "Recover Detail (50)     -> blend=0.50         |   Add Noise (2)       -> prenoise=0.002"
    ]
    yc = height - 525
    for cl in cli_lines:
        c.drawString(37, yc, cl)
        yc -= 18

    c.save()
    print(f"Saved: {filename}")


if __name__ == "__main__":
    build_youtube_masterplan_pdf()
    build_topaz_infographic_pdf()
    print("Done! Both ADHD Infographic PDFs are ready in your folder.")
