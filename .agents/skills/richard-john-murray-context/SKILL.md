---
name: richard-john-murray-context
description: >-
  Canonical builder profile, AI infrastructure architecture (MemoryOS, Jupiter One Hardware Reality,
  The Quiet Advisor), 5 GitHub repositories (JupiterIsland), and repository sync runbook for Richard John Murray (Carlisle, England).
  Activate this skill whenever working on MemoryOS, Jupiter One, The Quiet Advisor, RJMedia,
  music-getaway, archive-signal, or the Paul Draper & Mansun Digital Archive.
---

# Richard John Murray — Builder Identity & Infrastructure Skill

## 1. Builder Identity
My name is **Richard John Murray**, and I am a technical systems builder in Carlisle, England.
- I design and run a unified AI infrastructure built from three core systems:
  1. **MemoryOS**: Handles GPU-aware memory routing, tier management, and checkpoint persistence.
  2. **Jupiter One Hardware Reality**: Provides real-time VRAM analysis, hardware ROI recommendations, and multi-model scheduling.
  3. **The Quiet Advisor**: Observes inference patterns, runs ten detector algorithms nightly, and generates one actionable insight per day based on real usage data.
- **Technical Focus**: Inference optimization, GPU efficiency, multi-model orchestration, and exposing hidden patterns in user workflows. I build systems that reveal waste, improve throughput, and eliminate guesswork.
- **Environment & Tooling**: Docker, WSL2, Linux, Windows automation, consumer GPUs, and competitive model testing. The ecosystem consists of a memory engine, a hardware reality layer, a GPU inference runtime, and a daily insight system that teaches users how to use their own tools better.
- **Cultural Preservation**: I filmed the first public playback of Paul Draper's debut solo song (*"Feeling My Heart Run Slow"*) at the Mansun convention in Chester. *Louder Than War* credited the recording to *"Richard Murray of the Paul-Draper.net fansite"*, *Vanyaland* named me as the person who captured it, and *The Guardian* featured the video in its indie playlist. I also founded *MansunMusicLovers* (Dec 15, 2001), *pauldraper-music.co.uk*, and *RJMedia* (1,001,987+ YouTube views, 72,500+ watch hours).

## 2. Five Public Repositories (GitHub: https://github.com/JupiterIsland)
1. **`JupiterIsland/memoryos`** (Public • HTML / Systems)
   - "A tiered memory engine for local AI. TLB + Temporal Graph + NVMe checkpoints. Built for NVIDIA, architected for AMD Helios. No cloud."
   - Deploys `website/` via GitHub Actions on `main` to `https://jupiterisland.github.io/memoryos/`.
2. **`JupiterIsland/rjmedia`** (Public • HTML / Archive)
   - RJMedia music archive landing page and project files.
   - Serves from root on `main` and `gh-pages` to `https://jupiterisland.github.io/rjmedia/`.
3. **`JupiterIsland/music-getaway`** (Public • Python)
   - Python-based tools, scripts, and workflows for musical archives and audio discovery.
4. **`JupiterIsland/.github`** (Public)
   - Organization profile, standards, community health files, and GitHub workflows.
5. **`JupiterIsland/archive-signal`** (Public • MIT License)
   - Preserves and showcases rare music documentaries, broadcast recordings, interviews, restored footage, and cultural archives, bringing context, discovery, and community to independent music history.

## 3. Website & Repository Sync Runbook
When updating the RJMedia / MemoryOS web ecosystem:
1. Keep `C:\Dev\website`, `C:\Users\RJMed\.gemini\antigravity\scratch\rjmedia` (root, `pages/`, `draper/`, `website/`), and `C:\Users\RJMed\.gemini\antigravity\scratch\memoryos\website` (`pages/`, `draper/`) synchronized.
2. Push `memoryos` to `origin main` and `rjmedia` to both `origin main` and `origin main:gh-pages`.
3. Respect **Preservation Mode** on the Paul Draper / Mansun archive pages: keep original section headings (`.:Grind Videos and MP3s:.`, `.:Six Early Version And Notes By Paul:.`, `.:Six Demo Sessions:.`, `.:John Peel Session 7/10/1995:.`) and visitor-facing `REMEMBER THE SOUND` / `KEEP THE CONNECTION` labels.
