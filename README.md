# 🎸 RJMedia Digital Liner Notes Generator

[![YouTube](https://img.shields.io/badge/YouTube-Live_Music_%26_Band_Docs-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@LiveMusicBandDocumentaries)
[![Buy Me a Coffee](https://img.shields.io/badge/Support-Buy_Me_a_Coffee-yellow?style=for-the-badge&logo=buy-me-a-coffee)](https://buymeacoffee.com/rjmedia)
[![GitHub](https://img.shields.io/badge/GitHub-Open_Source-blue?style=for-the-badge&logo=github)](https://github.com/rjmedia)
[![Discord](https://img.shields.io/badge/Discord-Join_Community-7289da?style=for-the-badge&logo=discord)](https://discord.gg/rjmedia)

---

## 🎬 What Is This?

**RJMedia Digital Liner Notes Generator** turns your long YouTube music videos into interactive, searchable companion guides using **Google Gemini 2.5 Multimodal AI**.

Instead of viewers scrubbing through 90 minutes of footage looking for a specific song or moment, they get:

✅ **Auto-Generated Chapter Index** — Every song/segment with clickable timestamps  
✅ **Setlist & Track Listing** — Copy straight to YouTube description (auto-activates chapter scrubber)  
✅ **Gear & Visual Details** — Instruments, amplifiers, stage setup spotted via AI  
✅ **Key Quotes & Trivia** — Best stories, interviews, historical context  
✅ **Restoration Notes** — What audio/video work was done, why it matters  

**The Result:** Fans read a 2-minute guide, click to scenes they care about, then watch the full video. Engagement skyrockets.

---

## 🌟 Proof: The Smiths Remaster

**[The Smiths — "How Soon Is Now?" (RJMedia Remaster)](https://youtu.be/WLU74h889VI?si=yg-SakWqJW7S7kd6)**

📊 **79K views in 1 year** from a channel of dedicated music lovers who care about **quality**, not just quantity.

This app generated the liner notes you see in that video description. Now it's open-source so you can generate them for your own content.

---

## 🚀 Quick Start (5 Minutes)

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get a Free Gemini API Key

```bash
# Visit: https://aistudio.google.com/
# Click "Get API Key" → Copy your key
export GEMINI_API_KEY="your-key-here"
```

### 3. Run the App

```bash
streamlit run app.py
```

The app opens in your browser at `http://localhost:8501`

### 4. Try It

- **Option A:** Click the **Featured Smiths Remaster** button to see a real example
- **Option B:** Paste any YouTube URL and generate liner notes

### 5. Download Output

Choose your format:
- 📥 **Markdown** — For GitHub & local editing
- 📥 **YouTube Chapters** — Copy/paste into your video description
- 📥 **GitHub Pages HTML** — Auto-hostable webpage

---

## 🎚️ Bonus: Expert Topaz Presets

This app includes **4 production-ready Topaz Video AI presets** for teaching video restoration:

| Preset | Use Case | Output | Speed |
|--------|----------|--------|-------|
| **Low-Quality Digital** | 360p→720p web rips, compression artifacts | 720p–1080p | ~6 hrs (RTX 4070) |
| **Fast 1080p→4K** | Native 2x scaling, maximum FPS | 4K @ 60fps | ~4 hrs (RTX 4080) |
| **VHS Stage 1** | Artifact stripping, 1x native (cleanup only) | 480p stabilized | ~2 hrs |
| **VHS Stage 2** | VHS upscaling + film grain, 2x scale | 1440x1080 | ~3 hrs |

**Why include these?**

1. **Teaching Tool** — Every parameter has a reason. Viewers learn HOW Topaz actually works.
2. **Discussion Driver** — Fans download presets, tweak them, post results in Discord. Community grows.
3. **Transparency** — You show exactly HOW you restored their favorite videos.

---

## 📖 How It Works (Under the Hood)

### The Pipeline

```
YouTube URL
    ↓
Google Gemini 2.5 (samples 1 frame/sec + audio)
    ↓
Auto-generates:
    - Chapter timestamps
    - Setlist index
    - Gear identification
    - Quotes & trivia
    - Restoration notes
    ↓
Markdown output (with clickable MM:SS links)
    ↓
You download & use:
    - YouTube description (chapters)
    - GitHub Pages (webpage)
    - Social media (snippets)
```

### Gemini 2.5 Capabilities

- **Video Understanding**: Watches 1 frame per second for visual context
- **Audio Analysis**: Understands speech, music, instruments
- **Timestamp Accuracy**: Knows exactly when each moment occurs
- **Up to 2 Hours**: Can process full YouTube videos in a single API call
- **Free Tier**: 8 hours of YouTube processing per day (no charge)

---

## 💾 Repository Structure

```
rjmedia-liner-notes/
├── app.py                          # Main Streamlit app
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── presets/
│   ├── Low_Quality_Digital.json    # 360p→720p restoration
│   ├── Fast_1080p_to_4K.json       # 1080p→4K upscaling
│   ├── VHS_Restoration_Stage1.json # VHS cleanup (1x)
│   └── VHS_Restoration_Stage2.json # VHS upscaling (2x)
│
└── examples/
    ├── Smiths_Liner_Notes.md       # Generated example
    ├── Smiths_YouTube_Chapters.txt # Copy-paste ready
    └── index.html                  # GitHub Pages version
```

---

## 🎯 Use Cases

### For Your Channel
- **Generate liner notes** for every new upload in 5 minutes
- **Educate viewers** on your restoration process via Topaz presets
- **Drive engagement** with interactive timestamps and gear spotting
- **Build community** via shareable presets and Discord discussion

### For Restoration Hobbyists
- **Learn Topaz settings** from battle-tested presets
- **Understand WHY** each parameter matters
- **Tweak and experiment** with your own footage
- **Share results** with the RJMedia community

### For Music Archivists
- **Create searchable indexes** of rare footage
- **Preserve context** (gear, quotes, historical facts) alongside the video
- **Make rare performances accessible** to modern audiences
- **Drive discoverability** via YouTube chapters and metadata

---

## 🔧 Advanced: Running Locally Without Streamlit

If you want to integrate this into your own workflow:

```python
from app import generate_liner_notes

youtube_url = "https://youtu.be/WLU74h889VI"
liner_notes = generate_liner_notes(youtube_url)

# Save to file
with open("output.md", "w") as f:
    f.write(liner_notes)
```

Or via CLI:

```bash
python app.py --url "https://youtu.be/WLU74h889VI" --output "my_notes.md"
```

---

## 🤝 Contributing

Have a better Topaz preset? Found a bug? Want to add a feature?

**We'd love your help!**

1. **Fork** this repository
2. **Create a branch** (`git checkout -b feature/my-preset`)
3. **Commit** your changes (`git commit -m "Add XYZ preset"`)
4. **Push** (`git push origin feature/my-preset`)
5. **Open a Pull Request**

All contributors get credited on the app homepage + mentioned in the Discord.

---

## 📺 Watch It In Action

See this exact app generate liner notes for real videos on the **RJMedia YouTube channel**:

**[Live Music & Band Documentaries](https://www.youtube.com/@LiveMusicBandDocumentaries)**

- The Smiths — "How Soon Is Now?" (79K views, 1 year)
- The Verve — "Bitter Sweet Symphony" (Remaster)
- Mansun — "Wide Open Space" (Remaster)
- Kasabian — "L.S.F." (Documentary)
- 22-20s — "Broken Man" (Archive Restoration)

---

## ☕ Support This Project

This app is **100% free and open-source**. No ads, no paywalls, no tracking.

If it helps your workflow:

| Support Level | How |
|---------------|-----|
| **Free** | ⭐ Star this repo, fork it, share with friends |
| **Coffee** | ☕ [Buy Me a Coffee](https://buymeacoffee.com/rjmedia) — Even $1 helps |
| **Member** | 💬 [Join Discord](https://discord.gg/rjmedia) — Post your work, get feedback |
| **Subscribe** | 📺 [YouTube](https://www.youtube.com/@LiveMusicBandDocumentaries) — New remasters weekly |

---

## 🛠️ Topaz Settings Reference

### GUI-to-FFmpeg Parameter Mapping

| GUI Parameter | tvai_up Key | GUI Range | CLI Range | Example |
|---------------|-------------|-----------|-----------|---------|
| Revert Compression | `compression` | -100 to 100 | -1.0 to 1.0 | GUI 60 = CLI 0.60 |
| Improve Detail | `details` | -100 to 100 | -1.0 to 1.0 | GUI 30 = CLI 0.30 |
| Sharpen | `blur` | -100 to 100 | -1.0 to 1.0 | GUI 30 = CLI 0.30 |
| Reduce Noise | `noise` | -100 to 100 | -1.0 to 1.0 | GUI 25 = CLI 0.25 |
| Dehalo | `halo` | -100 to 100 | -1.0 to 1.0 | GUI 20 = CLI 0.20 |
| Anti-Alias / Deblur | `preblur` | -100 to 100 | -1.0 to 1.0 | GUI -15 = CLI -0.15 |
| Recover Original Detail | `blend` | 0 to 100 | 0.0 to 1.0 | GUI 40 = CLI 0.40 |

### FFmpeg CLI Example (Fast 1080p→4K)

```bash
ffmpeg -hide_banner -i "input_1080p.mp4" \
-sws_flags spline+accurate_rnd+full_chroma_int \
-filter_complex "tvai_up=model=prob-4:scale=2:preblur=-0.15:noise=0.10:details=0.35:halo=0.05:blur=0.30:compression=0.25:prenoise=0.002:blend=0.50:device=0:vram=0.85:instances=1" \
-c:v hevc_nvenc -profile:v main10 -pix_fmt p010le -rc constqp -qp 16 -preset p6 \
-c:a copy "output_4k_fast.mp4"
```

---

## 📚 Learn More

- **[Topaz Video AI Docs](https://www.topazlabs.com/)**
- **[Google Gemini API](https://ai.google.dev/)**
- **[Streamlit Docs](https://docs.streamlit.io/)**
- **[RJMedia Discord](https://discord.gg/rjmedia)** — Ask questions, share results

---

## 📄 License

This project is open-source under the **MIT License**. You're free to use, modify, and distribute.

See [LICENSE](LICENSE) for details.

---

## 🙏 Credits

**Built with ❤️ by:**
- **RJMedia** — Video restoration & music archiving
- **Google Gemini 2.5** — AI video analysis
- **Topaz Labs** — Video AI technology
- **Streamlit** — Web app framework

---

## 📞 Get Help

**Having issues?**

1. Check the [Troubleshooting](#troubleshooting) section below
2. **[Open an Issue](https://github.com/rjmedia/liner-notes/issues)** on GitHub
3. **[Join the Discord](https://discord.gg/rjmedia)** — Ask the community
4. **[Email Support](mailto:rjmedia@example.com)**

---

## ❓ Troubleshooting

### "GEMINI_API_KEY not set"
```bash
# Set your API key
export GEMINI_API_KEY="your-key-here"
streamlit run app.py
```

### "No matching distribution found for google-genai"
```bash
pip install --upgrade pip
pip install google-genai==0.3.0
```

### "Streamlit app crashes on load"
```bash
# Clear cache and restart
rm -rf ~/.streamlit
streamlit run app.py --logger.level=debug
```

### "Video too long / API timeout"
The Gemini API processes up to 2 hours of video per call. For longer videos:
1. Split into chapters in YouTube
2. Generate liner notes for each chapter separately
3. Combine manually

---

## 🎬 What's Next?

**Planned Features:**

- [ ] Auto-upload to GitHub Pages with custom domain
- [ ] Integration with YouTube API (auto-post chapters)
- [ ] Batch processing (generate liner notes for entire channel)
- [ ] Discord bot (generate on-demand via bot commands)
- [ ] Stable Diffusion album artwork generation
- [ ] IPFS archival (decentralized backup)

**Want to help?** See [Contributing](#-contributing) above.

---

## 📊 Stats

| Metric | Value |
|--------|-------|
| Lines of Code | ~1,200 |
| Topaz Presets Included | 4 |
| Supported Video Formats | All YouTube URLs |
| Max Video Length (Free Tier) | 2 hours |
| Processing Speed | Real-time (API) |
| Storage Required | ~50 MB |
| Monthly API Cost | $0 (free tier) |

---

**⭐ If this project helps your workflow, please star this repo!**

---

**Last Updated:** January 2025  
**Status:** Active Development  
**License:** MIT  
**Author:** RJMedia

---

*"Music deserves to be heard in the best way possible. That's what RJMedia is about."*
