# 🐳 Docker Deployment Guide — RJMedia Channel Hub

**Your entire Channel Hub runs in a Docker container. One command deploys everywhere.**

---

## 🚀 Quick Start (Docker)

### Option 1: Local Development (Windows/Mac/Linux)

```bash
cd C:\Dev\memoryos\rjmedia-liner-notes

# Set your Gemini API key
$env:GEMINI_API_KEY = "your-api-key-here"

# Build and run container
docker compose up -d

# Check it's running
docker ps

# View logs
docker logs rjmedia-channel-hub -f
```

**Access at:** `http://localhost:8501`

### Option 2: Stop Container

```bash
docker compose down
```

---

## 🏗️ What's in the Container

```
Python 3.11 (slim)
├── Streamlit (web framework)
├── Google Generative AI (Gemini 2.5)
├── Pandas (data processing)
├── Pillow (image handling)
└── All other dependencies

Your App:
├── app.py (main application)
├── data_manager.py (video data)
├── presets/ (Topaz presets)
└── output/ (generated files)

Storage:
├── Streamlit cache (persistent)
└── Output folder (mounted volume)
```

---

## 🌐 Deploy to Production

### Option A: Self-Hosted VPS (DigitalOcean, Linode, AWS)

#### Step 1: SSH into Server
```bash
ssh root@your-server-ip
```

#### Step 2: Install Docker
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

#### Step 3: Clone Repository
```bash
git clone https://github.com/YOUR-USERNAME/rjmedia-liner-notes.git
cd rjmedia-liner-notes
```

#### Step 4: Create .env File
```bash
cat > .env << EOF
GEMINI_API_KEY=your-api-key-here
EOF
```

#### Step 5: Start Container
```bash
docker compose up -d

# Verify
docker ps
docker logs rjmedia-channel-hub
```

#### Step 6: Access
```
http://your-server-ip:8501
```

**Cost:** $5–20/month (depending on VPS provider)

---

### Option B: Railway (Auto-Deploy from GitHub)

Railway automatically builds and deploys your Docker container.

#### Step 1: Connect GitHub
1. Go to https://railway.app
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your `rjmedia-liner-notes` fork
5. Authorize Railway

#### Step 2: Configure Environment
Railway auto-detects Dockerfile. Add secrets:
1. Click "Variables"
2. Add: `GEMINI_API_KEY=your-key`
3. Click "Deploy"

#### Step 3: Custom Domain (Optional)
1. Click "Settings"
2. "Domains" → Add custom domain
3. Point DNS to Railway

**Result:** Your app at `https://rjmedia-liner-notes.railway.app`  
**Cost:** $5/month (after free tier)

---

### Option C: Docker Hub (Pre-Built Image)

Push your container to Docker Hub so anyone can run it:

```bash
# Login to Docker Hub
docker login

# Build image
docker build -t YOUR-USERNAME/rjmedia-channel-hub:latest .

# Push to Docker Hub
docker push YOUR-USERNAME/rjmedia-channel-hub:latest

# Anyone can now run:
docker run -p 8501:8501 -e GEMINI_API_KEY="key" YOUR-USERNAME/rjmedia-channel-hub:latest
```

---

## 📊 Docker Compose Commands Reference

```bash
# Build image (first time)
docker compose build

# Start container (background)
docker compose up -d

# Stop container
docker compose down

# View logs (live)
docker compose logs -f rjmedia-channel-hub

# Restart
docker compose restart

# Rebuild and restart
docker compose up -d --build

# Remove everything (containers + volumes)
docker compose down -v

# SSH into running container
docker exec -it rjmedia-channel-hub /bin/bash

# Check container stats (CPU, memory)
docker stats rjmedia-channel-hub
```

---

## 🔐 Security Best Practices

### 1. Never Commit API Keys
```bash
# ✅ Good
echo 'GEMINI_API_KEY=...' > .env
git add .
# .gitignore includes .env

# ❌ Bad
# Never hardcode API key in app.py
```

### 2. Use Environment Variables
```bash
# Set at runtime
docker compose up -d
# Reads from .env automatically
```

### 3. Rotate Keys Regularly
```bash
# Update .env
GEMINI_API_KEY=new-key-here

# Restart container
docker compose restart
```

### 4. Limit Container Permissions
```yaml
# In docker-compose.yml
user: "1000:1000"  # Run as non-root
read_only: true    # Read-only filesystem (if possible)
```

---

## 📈 Scaling for High Traffic

### Single Container (Current)
- **Throughput:** ~100–200 concurrent users
- **CPU:** 1 vCPU sufficient
- **Memory:** 1–2 GB
- **Cost:** $5/month

### Multi-Container (Future)
If you hit traffic limits, scale to:

```yaml
version: '3.8'
services:
  rjmedia-1:
    build: .
    ports:
      - "8501:8501"
  rjmedia-2:
    build: .
    ports:
      - "8502:8501"
  nginx:
    image: nginx:latest
    ports:
      - "80:80"
    # Load balance between containers
```

---

## 🚨 Troubleshooting

### Container Won't Start
```bash
# Check logs
docker logs rjmedia-channel-hub

# Rebuild
docker compose build --no-cache
docker compose up -d
```

### API Key Not Working
```bash
# Verify env var is set
docker exec rjmedia-channel-hub echo $GEMINI_API_KEY

# Should output your key
```

### Port Already in Use
```bash
# Change port in docker-compose.yml
ports:
  - "8502:8501"  # Use 8502 instead

docker compose up -d
```

### Out of Memory
```bash
# Increase Docker memory limit
# Docker Desktop → Settings → Resources

# Or limit container memory
docker compose -f docker-compose.yml up -d -m 2g
```

### Slow Performance
```bash
# Check container stats
docker stats rjmedia-channel-hub

# If CPU high: Reduce Streamlit workers
# If memory high: Enable caching

# Restart with optimization
docker compose restart
```

---

## 📦 Docker Image Details

```
Base Image: python:3.11-slim
Size: ~400MB (compressed ~150MB)
Build Time: ~2 minutes (first build)
Runtime Memory: 300–500MB (typical)

Installed:
✅ Python 3.11
✅ Streamlit 1.28+
✅ Google Generative AI SDK
✅ Pandas, NumPy
✅ Pillow, requests
✅ curl (for health checks)
```

---

## 🔄 CI/CD Pipeline (GitHub Actions)

Auto-build and deploy on every push:

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Build Docker image
        run: docker build -t rjmedia-channel-hub:latest .
      
      - name: Push to Docker Hub
        run: |
          docker login -u ${{ secrets.DOCKER_USER }} -p ${{ secrets.DOCKER_PASS }}
          docker push rjmedia-channel-hub:latest
      
      - name: Deploy to Railway
        run: |
          # Railway deployment command
```

---

## 📊 Monitoring in Production

### Docker Stats
```bash
docker stats rjmedia-channel-hub
```

Monitor:
- **CPU %** (should be <20% at rest)
- **Memory Usage** (should be <500MB)
- **Network I/O** (incoming requests)

### Logs
```bash
# Last 100 lines
docker logs rjmedia-channel-hub --tail 100

# Follow live
docker logs rjmedia-channel-hub -f

# Export logs
docker logs rjmedia-channel-hub > logs.txt
```

### Health Check
```bash
curl http://localhost:8501/_stcore/health

# Should return 200 OK
```

---

## 🚀 One-Command Deploy

**Local:**
```bash
docker compose up -d
```

**Production (Railway auto-deploys from GitHub):**
```bash
# Just push to GitHub
git push origin main
# Railway automatically rebuilds and deploys
```

**Docker Hub:**
```bash
docker build -t username/rjmedia:latest . && docker push username/rjmedia:latest
```

---

## ✅ Production Checklist

- [ ] `.env` file created (not committed)
- [ ] API key set correctly
- [ ] Container builds without errors
- [ ] Runs locally at localhost:8501
- [ ] All buttons work
- [ ] Logs are clean (no errors)
- [ ] Health check passes
- [ ] Ready to push to GitHub
- [ ] Railway/VPS configured
- [ ] Custom domain (optional) set up
- [ ] Monitoring enabled
- [ ] Backups scheduled

---

## 💡 Pro Tips

**Tip 1: Rebuild Only Changed Layers**
```bash
docker compose build --no-cache  # Full rebuild
docker compose build              # Use cache (faster)
```

**Tip 2: Multi-Stage Build (Future)**
```dockerfile
# Reduce final image size
FROM python:3.11 AS builder
# ...
FROM python:3.11-slim
COPY --from=builder /app /app
```

**Tip 3: Persistent Data**
```yaml
volumes:
  - ./output:/app/output  # Mount folder
  - streamlit-cache:/root/.streamlit  # Named volume
```

---

## 🎯 Your Deployment Options (Ranked)

| Option | Ease | Cost | Control | Traffic |
|--------|------|------|---------|---------|
| **Railway** | ⭐⭐⭐⭐⭐ | $5/mo | Low | 1K/day |
| **Streamlit Cloud** | ⭐⭐⭐⭐⭐ | Free | None | 1K/day |
| **VPS + Docker** | ⭐⭐⭐ | $5–50/mo | High | 10K+/day |
| **Docker Hub** | ⭐⭐⭐⭐ | Free | Medium | Scale up |

**Recommendation:** Start with Railway (easy, affordable), scale to VPS as traffic grows.

---

## 🚀 Your Next Step

```bash
# Build container locally
docker compose build

# Run it
docker compose up -d

# Test at localhost:8501
# Then push to production
```

**Your entire Channel Hub now runs in one Docker container, deployable anywhere.**

Ready to go live? 🚀
