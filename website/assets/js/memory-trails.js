/**
 * RJMedia Historical Intelligence Platform v1
 * JSON-Driven Memory Trails™, Memory Constellations™, Echoes™,
 * Legacy Engine™, and Preservation Risk Engine™
 */

const FALLBACK_TRAILS_DATA = {
  trails: [
    {
      id: "mansun-story",
      title: "The Mansun Story",
      description: "A journey through performances, recordings and archive moments.",
      items: [
        { year: "1995", title: "John Peel Session", objectId: "mansun-1995-peel", url: "./pages/mansun-mp3-vault.html" },
        { year: "1997", title: "Early Interview", objectId: "mansun-1997-001", url: "./pages/mansun-albums.html" },
        { year: "1998", title: "Festival Appearance", objectId: "mansun-1998-001", url: "./pages/draper-articles.html" },
        { year: "1999", title: "Television Performance", objectId: "mansun-1999-001", url: "./youtube.html" },
        { year: "2003", title: "Solo Direction", objectId: "pd-2003-solo", url: "./pages/draper-news.html" }
      ]
    },
    {
      id: "britpop-trail",
      title: "Britpop Timeline",
      description: "Key moments across the Britpop era.",
      items: [
        { year: "1994", title: "Emerging Scene", objectId: "britpop-1994-001", url: "./pages/mansun-singles.html" },
        { year: "1995", title: "Festival Growth", objectId: "britpop-1995-001", url: "./pages/mansun-mp3-vault.html" },
        { year: "1997", title: "Peak Era", objectId: "britpop-1997-001", url: "./pages/mansun-albums.html" },
        { year: "1998", title: "Six & Art Rock Shift", objectId: "britpop-1998-001", url: "./pages/press-layout.html" }
      ]
    },
    {
      id: "paul-draper-solo",
      title: "Paul Draper Solo Trajectory",
      description: "From Draposound studio logs and the 2014 Chester world premiere to Kscope solo LPs and 2027 live dates.",
      items: [
        { year: "2006", title: "38 Forum Q&As", objectId: "pd-2006-qa", url: "./pages/draper-qa.html" },
        { year: "2014", title: "Chester World Premiere", objectId: "pd-2014-chester", url: "./pages/draper-news.html" },
        { year: "2017", title: "Spooky Action (#19)", objectId: "pd-2017-spooky", url: "./pages/mansun-albums.html" },
        { year: "2022", title: "Cult Leader Tactics", objectId: "pd-2022-clt", url: "./pages/mansun-albums.html" },
        { year: "2027", title: "Indie By The Sea", objectId: "pd-2027-blackpool", url: "./pages/draper-news.html" }
      ]
    }
  ]
};

const FALLBACK_CONSTELLATION_DATA = {
  constellation: "Britpop & Mansun Historical Network",
  centreNode: "mansun",
  nodes: [
    {
      id: "mansun",
      label: "Mansun",
      type: "band",
      x: 440,
      y: 260,
      xPct: 48,
      yPct: 46,
      url: "./pages/index.html",
      summary: "Chester art-rock quartet (1995–2003) • #1 LP Attack of the Grey Lantern & Six"
    },
    {
      id: "paul",
      label: "Paul Draper",
      type: "person",
      x: 210,
      y: 140,
      xPct: 22,
      yPct: 22,
      url: "./pages/mansun-albums.html",
      summary: "Songwriter, producer & solo artist (Spooky Action, Cult Leader Tactics, Mansun Retold)"
    },
    {
      id: "bbc",
      label: "BBC Sessions",
      type: "organisation",
      x: 670,
      y: 150,
      xPct: 75,
      yPct: 24,
      url: "./pages/mansun-mp3-vault.html",
      summary: "1995 John Peel Session (Grey Lantern, Flourella, Skin Up Pin Up, Take It Easy Chicken)"
    },
    {
      id: "nme",
      label: "NME & Melody Maker",
      type: "publication",
      x: 640,
      y: 390,
      xPct: 74,
      yPct: 68,
      url: "./pages/press-layout.html",
      summary: "1996–2000 Magazine Features, Student Guide '98 & Psychobabble Scans"
    },
    {
      id: "six-tour",
      label: "1998 Six Tour",
      type: "tour",
      x: 450,
      y: 90,
      xPct: 50,
      yPct: 14,
      url: "./youtube.html",
      summary: "Brixton Academy '98 Broadcast & Soundmasters Reference CD"
    },
    {
      id: "chester",
      label: "2014 Chester Premiere",
      type: "venue",
      x: 150,
      y: 340,
      xPct: 18,
      yPct: 56,
      url: "./pages/draper-news.html",
      summary: "World premiere of 'Feeling My Heart Run Slow' filmed by Richard Murray"
    },
    {
      id: "blackpool",
      label: "Blackpool May 2027",
      type: "venue",
      x: 280,
      y: 440,
      xPct: 33,
      yPct: 78,
      url: "./pages/draper-news.html",
      summary: "Indie By The Sea Festival at Winter Gardens Blackpool (Saturday 1 May 2027)"
    },
    {
      id: "community",
      label: "MML & 2006 Q&A",
      type: "community",
      x: 480,
      y: 450,
      xPct: 56,
      yPct: 78,
      url: "./pages/draper-qa.html",
      summary: "25-Year Community Archive (Dec 2001–2026) & 38 Forum Q&As"
    }
  ],
  edges: [
    { from: "mansun", to: "paul", relationship: "founder_and_frontman" },
    { from: "mansun", to: "bbc", relationship: "recorded_sessions" },
    { from: "mansun", to: "nme", relationship: "featured_in" },
    { from: "mansun", to: "six-tour", relationship: "headlined" },
    { from: "paul", to: "chester", relationship: "premiered_solo_debut" },
    { from: "paul", to: "blackpool", relationship: "scheduled_2027_performance" },
    { from: "mansun", to: "community", relationship: "preserved_by" },
    { from: "paul", to: "six-tour", relationship: "wrote_and_produced" },
    { from: "chester", to: "blackpool", relationship: "solo_era_continuity" }
  ]
};

const TRAIL_BUILDER_CATALOG = {
  "paul draper": {
    query: "Paul Draper",
    subtitle: "Songwriter, Producer & Solo Artist Trajectory (1995–2027)",
    steps: [
      { year: "1995", title: "Mansun Formation & John Peel Session", meta: "Grey Lantern · Take It Easy Chicken", url: "./pages/mansun-mp3-vault.html" },
      { year: "1997", title: "Attack Of The Grey Lantern (#1 UK LP)", meta: "Parlophone · Produced by Paul Draper", url: "./pages/mansun-albums.html" },
      { year: "1998", title: "Six & Soundmasters Reference Notes", meta: "Handwritten Lyric & Studio Scans", url: "./pages/mansun-mp3-vault.html" },
      { year: "2003", title: "Solo Material & Grind Sessions", meta: "The Diary · Slide · Precious Internal", url: "./pages/mansun-mp3-vault.html" },
      { year: "2014", title: "Chester Convention Solo World Premiere", meta: "Feeling My Heart Run Slow · Filmed by Richard Murray", url: "./pages/draper-news.html" },
      { year: "2017–2022", title: "Spooky Action (#19) & Cult Leader Tactics (#22)", meta: "Kscope Solo Studio Albums & Mansun Retold", url: "./pages/mansun-albums.html" },
      { year: "2027", title: "Indie By The Sea — Blackpool Winter Gardens", meta: "Saturday 1 May 2027 · Live Festival Performance", url: "./pages/draper-news.html" }
    ]
  },
  "mansun": {
    query: "Mansun",
    subtitle: "Complete Band Evolution, Broadcasts & Boxsets (1995–2004)",
    steps: [
      { year: "1995", title: "Take It Easy Chicken & Peel Session", meta: "7 Oct 1995 Broadcast Vault", url: "./pages/mansun-mp3-vault.html" },
      { year: "1996", title: "Stripper Vicar & Numbered EP Run", meta: "One EP through Five EP · UK Chart Run", url: "./pages/mansun-singles.html" },
      { year: "1997", title: "Attack Of The Grey Lantern (UK #1)", meta: "Wide Open Space · Taxlo$$", url: "./pages/mansun-albums.html" },
      { year: "1998", title: "Six & Brixton Academy Live Broadcast", meta: "Peak Art-Rock Era · 13-Track Masterpiece", url: "./youtube.html" },
      { year: "2000", title: "Little Kix & Anton Corbijn Portraits", meta: "I Can Only Disappoint U (UK #8)", url: "./pages/draper-gallery.html" },
      { year: "2004", title: "Kleptomania 3-CD Boxset Release", meta: "Exclusive News Broken on pauldraper.tk", url: "./pages/draper-news.html" }
    ]
  },
  "britpop": {
    query: "Britpop",
    subtitle: "90s Independent & Broadcast History Trail (1994–1999)",
    steps: [
      { year: "1994", title: "Emerging UK Indie Scene", meta: "Early Singles & Regional Press", url: "./pages/mansun-singles.html" },
      { year: "1995", title: "BBC Radio 1 Peel Sessions & Festival Growth", meta: "Broadcast Preservation", url: "./pages/mansun-mp3-vault.html" },
      { year: "1996", title: "Melody Maker & NME Cover Features", meta: "Tom Sheehan Photography", url: "./pages/press-layout.html" },
      { year: "1997", title: "Peak Era: Attack Of The Grey Lantern Hits #1", meta: "February 1997 Official Chart", url: "./pages/mansun-albums.html" },
      { year: "1998", title: "Post-Britpop Progressive Shift: Six", meta: "NME Student Guide '98 & Uncut", url: "./pages/draper-articles.html" }
    ]
  },
  "six": {
    query: "Six (1998)",
    subtitle: "From Early Demo Sessions & Handwritten Notes to Full Tour Broadcasts",
    steps: [
      { year: "Early 1998", title: ".:Six Demo Sessions:.", meta: "Six Monitor Mix · Dr Funkoffski · Gods Are Not Us", url: "./pages/mansun-mp3-vault.html" },
      { year: "20 Jun 1998", title: "The Soundmasters Reference CD Inlay", meta: "Unmastered Reference Tracklist Scan", url: "./pages/mansun-albums.html" },
      { year: "Sept 1998", title: ".:Six Early Version And Notes By Paul:.", meta: "13 Tracks + Handwritten Track-by-Track Commentary", url: "./pages/mansun-mp3-vault.html" },
      { year: "Oct 1998", title: "Brixton Academy Live Television Broadcast", meta: "She Makes My Wheels Turn · Live Vault", url: "./youtube.html" }
    ]
  }
};

/**
 * 1. Load Memory Trails directly from JSON (with fallback for local file:// viewing)
 */
async function loadMemoryTrails() {
  const container = document.getElementById("memoryTrailContainer");
  if (!container) return;

  try {
    const response = await fetch("./assets/data/memory-trails.json");
    if (!response.ok) throw new Error("HTTP " + response.status);
    const data = await response.json();
    renderTrails(data.trails);
  } catch (error) {
    console.warn("Memory Trails using embedded JSON dataset:", error.message);
    renderTrails(FALLBACK_TRAILS_DATA.trails);
  }
}

function renderTrails(trails) {
  const container = document.getElementById("memoryTrailContainer");
  if (!container) return;

  container.innerHTML = "";

  trails.forEach(trail => {
    const card = document.createElement("div");
    card.className = "trail-card";

    card.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:0.5rem; margin-bottom:0.25rem;">
        <h3>${trail.title}</h3>
        <span style="font-family:'JetBrains Mono',monospace; font-size:0.7rem; font-weight:800; text-transform:uppercase; letter-spacing:0.1em; background:rgba(0,0,0,0.06); padding:0.25rem 0.65rem; border-radius:999px;">
          TRAIL ID: ${trail.id}
        </span>
      </div>
      <p>${trail.description}</p>
      <div class="trail-line">
        ${trail.items.map(item => `
          <a href="${item.url}" class="trail-item">
            <div class="trail-year">${item.year}</div>
            <div class="trail-dot"></div>
            <div class="trail-title">${item.title}</div>
          </a>
        `).join("")}
      </div>
    `;

    container.appendChild(card);
  });
}

/**
 * 2. Memory Constellations™ Prototype Renderer
 */
async function loadMemoryConstellations() {
  const canvas = document.getElementById("constellationCanvas");
  if (!canvas) return;

  let data = FALLBACK_CONSTELLATION_DATA;
  try {
    const response = await fetch("./assets/data/constellation.json");
    if (response.ok) {
      data = await response.json();
    }
  } catch (err) {
    // Use fallback constellation data
  }

  renderConstellation(canvas, data);
}

function renderConstellation(canvas, data) {
  // Clear existing star nodes
  canvas.querySelectorAll(".star-node").forEach(el => el.remove());

  let svg = document.getElementById("constellationSvg");
  if (!svg) {
    svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.id = "constellationSvg";
    canvas.prepend(svg);
  }
  svg.innerHTML = "";

  const nodeMap = {};
  data.nodes.forEach(n => {
    nodeMap[n.id] = n;
  });

  // Draw SVG connecting lines using percentage coordinates for responsive layout
  data.edges.forEach(edge => {
    const fromNode = nodeMap[edge.from];
    const toNode = nodeMap[edge.to];
    if (!fromNode || !toNode) return;

    const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
    line.setAttribute("x1", (fromNode.xPct || 50) + "%");
    line.setAttribute("y1", (fromNode.yPct || 50) + "%");
    line.setAttribute("x2", (toNode.xPct || 50) + "%");
    line.setAttribute("y2", (toNode.yPct || 50) + "%");
    line.setAttribute("class", "constellation-edge");
    line.dataset.from = edge.from;
    line.dataset.to = edge.to;
    svg.appendChild(line);
  });

  // Create star nodes
  data.nodes.forEach(node => {
    const element = document.createElement("a");
    element.href = node.url || "#";
    element.className = "star-node" + (node.id === data.centreNode ? " centre-star" : "");
    element.style.left = (node.xPct ? node.xPct + "%" : node.x + "px");
    element.style.top = (node.yPct ? node.yPct + "%" : node.y + "px");
    element.dataset.nodeId = node.id;

    element.innerHTML = `
      <span>${node.label}</span>
      <span class="star-node-badge">${node.type || "node"}</span>
    `;

    element.addEventListener("mouseenter", () => {
      highlightConstellationNode(node, data.edges);
    });

    canvas.appendChild(element);
  });
}

function highlightConstellationNode(node, edges) {
  const inspectorTitle = document.getElementById("constellationInspectorTitle");
  const inspectorDesc = document.getElementById("constellationInspectorDesc");
  const inspectorLink = document.getElementById("constellationInspectorLink");

  if (inspectorTitle) inspectorTitle.textContent = node.label + " (" + (node.type || "Archive Node").toUpperCase() + ")";
  if (inspectorDesc) inspectorDesc.textContent = node.summary || "Click node to explore connected archive items.";
  if (inspectorLink && node.url) inspectorLink.href = node.url;

  document.querySelectorAll(".constellation-edge").forEach(line => {
    if (line.dataset.from === node.id || line.dataset.to === node.id) {
      line.classList.add("highlighted");
    } else {
      line.classList.remove("highlighted");
    }
  });
}

/**
 * 3. Trail Builder AI — Interactive Search-to-Journey Generator
 */
function generateTrailFromQuery(rawQuery) {
  const output = document.getElementById("trailBuilderOutput");
  if (!output) return;

  const q = (rawQuery || "Paul Draper").trim().toLowerCase();
  let matched = TRAIL_BUILDER_CATALOG["paul draper"];

  if (q.includes("mansun")) {
    matched = TRAIL_BUILDER_CATALOG["mansun"];
  } else if (q.includes("britpop") || q.includes("90s")) {
    matched = TRAIL_BUILDER_CATALOG["britpop"];
  } else if (q.includes("six") || q.includes("1998")) {
    matched = TRAIL_BUILDER_CATALOG["six"];
  } else if (q.includes("paul") || q.includes("draper") || q.includes("solo") || q.includes("spooky") || q.includes("cult")) {
    matched = TRAIL_BUILDER_CATALOG["paul draper"];
  }

  output.innerHTML = `
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:1rem;">
      <div>
        <span style="font-family:'JetBrains Mono',monospace; font-size:0.72rem; font-weight:800; letter-spacing:0.14em; text-transform:uppercase; color:#000000; background:rgba(0,0,0,0.08); padding:0.25rem 0.65rem; border-radius:999px;">
          MEMORY TRAIL GENERATED • ${matched.steps.length} CONNECTED MOMENTS
        </span>
        <h4 style="font-size:1.35rem; font-weight:900; margin:0.5rem 0 0.15rem; text-transform:uppercase;">
          Journey: ${matched.query}
        </h4>
        <div style="font-size:0.88rem; color:#525252;">${matched.subtitle}</div>
      </div>
    </div>
    <div class="generated-trail-vertical">
      ${matched.steps.map((step, idx) => `
        <a href="${step.url}" class="gen-step-card">
          <div style="display:flex; align-items:center; gap:1rem;">
            <span class="trail-year" style="min-width:95px; text-align:center;">${step.year}</span>
            <div>
              <div style="font-weight:900; font-size:0.98rem;">${step.title}</div>
              <div style="font-family:'JetBrains Mono',monospace; font-size:0.74rem; color:#525252;">${step.meta}</div>
            </div>
          </div>
          <span style="font-family:'JetBrains Mono',monospace; font-size:0.75rem; font-weight:800; text-transform:uppercase;">Open Node →</span>
        </a>
        ${idx < matched.steps.length - 1 ? `<div class="gen-arrow">↓</div>` : ``}
      `).join("")}
    </div>
  `;

  // Update active preset pill state
  document.querySelectorAll(".trail-preset-btn").forEach(btn => {
    if (btn.dataset.query && btn.dataset.query.toLowerCase() === matched.query.toLowerCase()) {
      btn.classList.add("active");
    } else {
      btn.classList.remove("active");
    }
  });
}

function initTrailBuilder() {
  const input = document.getElementById("trailSearchInput");
  const btn = document.getElementById("trailSearchBtn");

  if (btn && input) {
    btn.addEventListener("click", () => generateTrailFromQuery(input.value));
    input.addEventListener("keydown", e => {
      if (e.key === "Enter") {
        e.preventDefault();
        generateTrailFromQuery(input.value);
      }
    });
  }

  document.querySelectorAll(".trail-preset-btn").forEach(preset => {
    preset.addEventListener("click", () => {
      const q = preset.dataset.query || "Paul Draper";
      if (input) input.value = q;
      generateTrailFromQuery(q);
    });
  });

  if (document.getElementById("trailBuilderOutput")) {
    generateTrailFromQuery("Paul Draper");
  }
}

document.addEventListener("DOMContentLoaded", () => {
  loadMemoryTrails();
  loadMemoryConstellations();
  initTrailBuilder();
});
