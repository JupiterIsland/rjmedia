def generate_buzzcocks_liner_notes(video_id="_ivgaFkD4Ac"):
    """Deep-dive liner notes for RJMedia's original front-row phone capture of The Buzzcocks at Solfest 2021 (225K+ views)"""
    return f"""# 📱🎸 The Buzzcocks — "What Do I Get" (Live at Solfest 2021 • Original RJMedia Front-Row Capture)

**Video:** [http://www.youtube.com/watch?v={video_id}](http://www.youtube.com/watch?v={video_id})  
**Filmed & Remastered By:** Richard John Murray (**RJMedia** • Live Music & Band Documentaries)  
**Camera Source:** Handheld Smartphone Capture (Front Barrier, Center-Right)  
**Performance Status:** ⭐ **225,107+ Views** • **2,265+ Likes**  
**Recorded:** August 2021 — Solfest Festival, Tarnside Farm, Cumbria, UK  
**Lineup:** Steve Diggle (Vocals / Lead Guitar), Chris Remington (Bass), Danny Farrant (Drums), Mani Perazzoli (Guitar)

---

## 1. 60-Second Archival TL;DR

Filmed personally by **RJMedia** on a smartphone right on the front barrier at Cumbrian independent festival **Solfest 2021**, this electrifying capture of the 1978 punk anthem *"What Do I Get?"* proves that great positioning and smart mastering beat multi-camera broadcast crews for raw energy. From the opening air-raid siren and Danny Farrant's pounding tom build-up to **Steve Diggle** striding out in an all-white denim suit a few feet from the lens, this recording has pulled over **225,000 views** by putting the viewer right against the stage monitors.

---

## 2. Interactive Chapters & Setlist Index

*(Copy and paste the list below directly into your YouTube description to activate chapters)*

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

## 3. Visual Gear & Stage Spotting (From the Front Barrier)

* **[0:01](https://www.youtube.com/watch?v={video_id}&t=1s) Stage Backline & Backdrop:** Colourful painted **"SOLFEST"** backdrop featuring a cosmic whale and planets; dual **Blackstar** amplifier head-and-4x12 cabinet stacks flanking the drum riser.
* **[0:26](https://www.youtube.com/watch?v={video_id}&t=26s) Drums (Danny Farrant):** Lime-green sparkle **Q Drum Co.** kit (rack tom, floor tom, deep kick drum) with Zildjian cymbals on a raised riser; bottle of bubbly resting by the kick drum.
* **[1:07](https://www.youtube.com/watch?v={video_id}&t=67s) Bass (Chris Remington):** Natural ash **Fender Jazz Bass** with tortoiseshell pickguard, maple neck, and black block inlays played with a pick for aggressive punk midrange punch.
* **[1:58](https://www.youtube.com/watch?v={video_id}&t=118s) Lead Guitar (Steve Diggle):** 3-Tone Sunburst **Fender Telecaster** with white pickguard and maple fretboard, plugged into the stage-right Blackstar stack just feet from the camera.
* **[3:23](https://www.youtube.com/watch?v={video_id}&t=203s) Rhythm/Second Guitar (Mani Perazzoli):** **Gibson Les Paul** on stage right through a twin Blackstar stack.

---

## 4. How to Remaster Smartphone Concert Footage in Topaz Video AI (The RJMedia Blueprint)

Filming on a phone at the front barrier creates four specific challenges: **Variable Frame Rate (VFR)**, **Phone ISP over-sharpening halos**, **Subwoofer OIS lens shake**, and **Blue/Magenta LED sensor clipping**. Here is the exact profile used to master phone concert footage without turning faces into plastic:

```json
{{
  "Preset": "RJMedia_Smartphone_Concert_4K",
  "Model": "Proteus v4 (prob-4)",
  "Scale": "2x (1080p Phone -> 4K UHD)",
  "Revert Compression": 42,
  "Improve Detail": 28,
  "Sharpen": 15,
  "Reduce Noise": 22,
  "Dehalo": 35,
  "Anti-Alias / Deblur": 12,
  "Recover Original Detail": 60,
  "Add Noise": 2
}}