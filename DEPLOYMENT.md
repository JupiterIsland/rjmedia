# 🚀 Deploy RJMedia Liner Notes (Free Hosting)

Choose your hosting platform. All are **completely free** for this app.

---

## Option 1: Streamlit Cloud (Easiest — 5 Minutes)

Streamlit Cloud is free, serverless, and handles everything for you.

### Steps:

1. **Fork this repo** on GitHub: [rjmedia/liner-notes](https://github.com/rjmedia/liner-notes/fork)

2. **Sign up for Streamlit Cloud**:
   - Visit: https://streamlit.io/cloud
   - Click "Sign up"
   - Authenticate with your GitHub account

3. **Create New App**:
   - Click "New app" on Streamlit Cloud dashboard
   - Select your forked repo (`rjmedia/liner-notes`)
   - Branch: `main`
   - File path: `app.py`
   - Click "Deploy"

4. **Set API Key**:
   - In Streamlit Cloud dashboard, click your app
   - Click "Manage" (gear icon)
   - Go to "Secrets"
   - Add this secret:
     ```
     GEMINI_API_KEY = "your-api-key-here"
     ```
   - Click "Save"

5. **Done!** Your app is live at: `https://rjmedia-liner-notes.streamlit.app`

**Advantages:**
- ✅ Completely free
- ✅ Automatic updates (every GitHub push deploys)
- ✅ No server to manage
- ✅ Built-in HTTPS
- ✅ Scales automatically

**Limits:**
- 1 GB RAM (plenty for this app)
- 3 concurrent users (small apps fine)
- 30-minute session timeout

---

## Option 2: Docker (Self-Hosted)

Host on your own server or local machine.

### Local Deployment:

```bash
# 1. Clone repo
git clone https://github.com/rjmedia/liner-notes.git
cd rjmedia-liner-notes

# 2. Set your API key
export GEMINI_API_KEY="your-api-key-here"

# 3. Build & run (one command)
docker compose up -d

# 4. Open in browser
# http://localhost:8501
```

### On a Linux Server (DigitalOcean, Linode, AWS):

```bash
# 1. SSH into your server
ssh root@your-server-ip

# 2. Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# 3. Clone repo
git clone https://github.com/rjmedia/liner-notes.git
cd rjmedia-liner-notes

# 4. Create .env file with your API key
echo 'GEMINI_API_KEY=your-api-key-here' > .env

# 5. Start container
docker compose up -d

# 6. Check it's running
docker logs rjmedia-liner-notes

# 7. Access via your server IP
# http://your-server-ip:8501
```

**Advantages:**
- ✅ Full control
- ✅ Unlimited users
- ✅ Custom domain possible
- ✅ No third-party rate limits

**Cost:**
- Cheapest VPS: $5–10/month (DigitalOcean, Linode)
- Or free tier (AWS, Google Cloud, Azure) with limited minutes

---

## Option 3: Railway (Docker Made Easy — $5/Month)

Railway auto-deploys from GitHub with zero configuration.

### Steps:

1. **Connect GitHub**:
   - Visit: https://railway.app
   - Sign up with GitHub
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Authorize and select your forked repo

2. **Configure Environment**:
   - Railway auto-detects `Dockerfile`
   - In Variables tab, add:
     ```
     GEMINI_API_KEY=your-api-key-here
     PORT=8501
     ```

3. **Deploy**:
   - Click "Deploy"
   - Railway builds and starts your app automatically
   - You get a public URL (e.g., `https://rjmedia-liner-notes.railway.app`)

4. **Done!**

**Advantages:**
- ✅ Automatic Docker deployment
- ✅ $5 credit per month (free)
- ✅ After free tier: $5/month is very affordable
- ✅ Easy scaling

**Cost:**
- First month: Free ($5 credit)
- After: $5–10/month depending on usage

---

## Option 4: Render (Free Tier)

Render offers 750 free compute hours per month (enough for this app).

### Steps:

1. **Visit Render**: https://render.com

2. **New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Select branch: `main`
   - Environment: `Docker`
   - Build Command: (leave default)
   - Start Command: `streamlit run app.py --server.port 10000`

3. **Environment Variables**:
   - Add: `GEMINI_API_KEY=your-api-key-here`
   - Add: `STREAMLIT_SERVER_PORT=10000`

4. **Deploy**:
   - Click "Create Web Service"
   - Render builds and deploys automatically
   - URL: `https://rjmedia-liner-notes.onrender.com`

**Advantages:**
- ✅ 750 hours/month free (always-on possible)
- ✅ Easy GitHub integration
- ✅ Auto-deploys on push
- ✅ Good uptime

**Limits:**
- Free tier: Auto-spins down after 15 minutes of inactivity (restarts on next request, ~30s cold start)
- After free tier: $7/month to stay always-on

---

## Option 5: GitHub Pages (Static Only — 100% Free)

If you want a **static read-only version** (no Gemini AI, just hosted presets):

1. **Enable GitHub Pages**:
   - Go to repo settings
   - Pages section
   - Source: "Deploy from a branch"
   - Select `main` branch, `/root` folder
   - Save

2. **Your site is live at**: `https://rjmedia.github.io/liner-notes/`

3. **Copy presets**:
   - Presets are auto-hosted at: `https://rjmedia.github.io/liner-notes/presets/`
   - Users can download directly

**Use Case:**
- Static documentation site (no API needed)
- Hosting Topaz presets as downloads
- Embed videos and static liner notes

---

## 📊 Comparison Table

| Platform | Cost | Setup Time | Maintenance | Scale | Best For |
|----------|------|-----------|-------------|-------|----------|
| **Streamlit Cloud** | Free | 5 min | None | Small | Getting started quickly |
| **Railway** | $5/mo | 5 min | Minimal | Medium | Growing projects |
| **Render** | Free* | 10 min | Minimal | Small | Always-free option |
| **Docker (Self-Hosted)** | $5–50/mo | 20 min | Manual | Large | Full control |
| **GitHub Pages** | Free | 5 min | None | N/A | Static docs only |

*Render free tier has 15-min inactivity timeout; $7/mo removes it.

---

## 🔒 Security Notes

### API Keys

**Never commit your `GEMINI_API_KEY` to GitHub.**

**Safe ways to set it:**

✅ **Streamlit Cloud**: Use "Secrets" panel (encrypted)  
✅ **Railway/Render**: Use "Environment Variables" (encrypted at rest)  
✅ **Docker/Self-Hosted**: Use `.env` file (add to `.gitignore`)

Example `.env`:
```bash
GEMINI_API_KEY="abc123..."
```

Example `.gitignore`:
```
.env
.streamlit/secrets.toml
node_modules/
__pycache__/
```

### Rotating Keys

If you accidentally expose your key:
1. Go to [aistudio.google.com](https://aistudio.google.com/)
2. Delete the exposed key
3. Generate a new one
4. Update in your hosting platform

---

## 📈 Monitoring & Logs

### Streamlit Cloud:
- Click your app → "Manage" → "Logs"

### Railway:
- Dashboard → Your app → "Logs" tab

### Render:
- Dashboard → Your app → "Logs" tab

### Docker:
```bash
docker logs rjmedia-liner-notes -f
```

---

## 🆘 Troubleshooting

### "App won't load"
- Check API key is set correctly
- View logs (see Monitoring above)
- Restart: `docker restart rjmedia-liner-notes`

### "Connection timeout"
- Cold start? Wait 30 seconds
- Check your internet connection
- Restart the service

### "API quota exceeded"
- Free Gemini API: 8 hours video/day
- Wait until next day, or upgrade to Gemini API Pro

### "Can't connect to localhost:8501"
- Docker not running? Start it: `docker compose up -d`
- Wrong port? Check: `docker ps`

---

## 📞 Need Help?

- **[Discord](https://discord.gg/rjmedia)** — Ask the community
- **[GitHub Issues](https://github.com/rjmedia/liner-notes/issues)** — Report bugs
- **[Email](mailto:rjmedia@example.com)** — Direct support

---

## ✅ Deployment Checklist

- [ ] Fork the repo
- [ ] Get Gemini API key
- [ ] Choose hosting platform
- [ ] Deploy (follow above steps)
- [ ] Test with The Smiths video
- [ ] Share link in Discord
- [ ] Star the repo ⭐

---

**Happy hosting! Your liner notes generator is live.** 🚀
