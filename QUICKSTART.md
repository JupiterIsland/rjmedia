# ⚡ Quick Start: Deploy in 5 Minutes

## Option 1: Streamlit Cloud (Recommended - Easiest)

### Step 1: GitHub Setup
```bash
cd C:\Dev\memoryos\rjmedia-liner-notes
git init
git add .
git commit -m "RJMedia Liner Notes - Initial commit"
git remote add origin https://github.com/YOUR-USERNAME/rjmedia-liner-notes.git
git push -u origin main
```

### Step 2: Get Gemini API Key
- Visit: https://aistudio.google.com/
- Click **"Get API Key"**
- Copy the key (keep this secret!)

### Step 3: Deploy on Streamlit Cloud
1. Go to https://streamlit.io/cloud
2. Click **"New app"**
3. Select your repo (`rjmedia-liner-notes`)
4. Select branch: `main`
5. File path: `app.py`
6. Click **"Deploy"**

### Step 4: Add API Key
1. Once deployed, click your app name
2. Click **Settings** (gear icon)
3. Click **Secrets**
4. Paste this:
   ```
   GEMINI_API_KEY = "your-api-key-here"
   ```
5. Click **Save**
6. App restarts automatically ✅

**Your app is live at:** `https://rjmedia-liner-notes.streamlit.app`

---

## Option 2: Local Testing (Before Deployment)

### Test Locally
```bash
cd C:\Dev\memoryos\rjmedia-liner-notes

# Install dependencies
pip install -r requirements.txt

# Set your API key
$env:GEMINI_API_KEY = "your-api-key-here"

# Run app
streamlit run app.py
```

**Opens at:** `http://localhost:8501`

**Try it:**
1. Click the **Smiths button** (your 79K-view video loads)
2. Click **"Generate Liner Notes"**
3. See it work!
4. Download outputs (Markdown, YouTube, HTML)

---

## Option 3: Docker (For Production)

### Deploy locally with Docker
```bash
cd C:\Dev\memoryos\rjmedia-liner-notes

# Set your API key in .env file
echo 'GEMINI_API_KEY=your-api-key-here' > .env

# Start container
docker compose up -d

# Check it's running
docker ps

# View logs
docker logs rjmedia-liner-notes -f
```

**Opens at:** `http://localhost:8501`

---

## 🎯 Testing Checklist

- [ ] Click **"Load: The Smiths..."** button → Balloons? ✨
- [ ] Click **"Generate Liner Notes"** → Gets full notes?
- [ ] Try **Tab 2** (Topaz Presets) → Can download JSON?
- [ ] Try **Tab 3** (Tutorial) → Topaz masterclass loads?
- [ ] Download as Markdown, YouTube Chapters, HTML → All work?

---

## 🚀 After Deployment

### Announce It
```
📢 New tool live: RJMedia Liner Notes Generator
🎸 Featured: The Smiths "How Soon Is Now?" (79K views)
🎚️ Download 4 Topaz presets + learn video restoration
📺 https://rjmedia-liner-notes.streamlit.app

#VideoRestoration #Topaz #MusicDocumentary #OpenSource
```

### Share Everywhere
- YouTube description (add link)
- Discord #announcements
- Twitter / X
- Reddit (r/VideoEditing, r/Mastering)
- GitHub discussion

### Track Success
- Streamlit Cloud dashboard: View app analytics
- YouTube: Monitor description clicks
- Discord: Watch for user remasters
- GitHub: Stars, forks, pull requests

---

## 🔑 Security Reminder

**NEVER commit your API key to GitHub!**

✅ **Safe:**
- Set as Streamlit Cloud Secret ✓
- Set as Railway/Render env var ✓
- Set locally via `export` or `.env` ✓

❌ **Unsafe:**
- Pasting into code ✗
- Committing to GitHub ✗
- Sharing in Discord ✗

---

## 🆘 Troubleshooting

### "App won't load"
```bash
# Check if service is running
docker ps

# Check logs
docker logs rjmedia-liner-notes

# Restart
docker restart rjmedia-liner-notes
```

### "API key not recognized"
```bash
# Verify it's set
echo $env:GEMINI_API_KEY

# Get a new key
# Visit: https://aistudio.google.com/
```

### "Can't connect to localhost:8501"
```bash
# Make sure Docker is running
docker ps

# If not, start Docker Desktop
```

---

## 📞 Need Help?

- **Discord**: https://discord.gg/rjmedia
- **GitHub Issues**: https://github.com/rjmedia/liner-notes/issues
- **YouTube**: @LiveMusicBandDocumentaries

---

## ✅ You're Done!

Your app is live. Your Smiths remaster is the feature.
Your Topaz presets are teaching others.
Your code is open-source.

**Now go get 100K views.** 🚀

---

**Time to completion:** 5 minutes ⏱️
**Cost:** Free (Streamlit Cloud) ✨
**Impact:** Your expertise, worldwide 🌍
