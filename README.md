<h1 align="center">Umut Çelik — Portfolio</h1>
<p align="center">A single-page personal portfolio with a live, switchable design system — 19 UI styles in one page.</p>

<p align="center">
  <a href="https://palamut62.github.io">Live Demo</a> ·
  <a href="https://github.com/palamut62/palamut62.github.io">Repo</a>
</p>

<p align="center">
  <img alt="Status" src="https://img.shields.io/badge/status-live-success">
  <img alt="HTML5" src="https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white">
  <img alt="Tailwind CSS" src="https://img.shields.io/badge/Tailwind_CSS-06B6D4?logo=tailwindcss&logoColor=white">
  <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black">
  <img alt="Vercel" src="https://img.shields.io/badge/Deploy-Vercel-000000?logo=vercel&logoColor=white">
</p>

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Deployment](#deployment)
- [Roadmap](#roadmap)
- [License](#license)

## Features

- **19 switchable design styles** — Glassmorphism, Neumorphism, Dark Developer, Command Palette, Card Dashboard, Fluent / Win11, Cyberpunk HUD, Neo-Brutalism, Claymorphism, Classic Windows, and more.
- **Minimal style picker** — a clean combobox in the top-right corner; pick a style and the whole page re-themes instantly.
- **Persistent selection** — your chosen style is saved in `localStorage`, so the page reopens with the last design you used.
- **Theme-aware profile photo** — the avatar adapts its frame shape, accent ring and image filter to match each style.
- **Themed content** — name, bio, project buttons and social icons all re-skin together.
- **Zero build step** — a single static `index.html` powered by the Tailwind CDN.

## Tech Stack

| Layer | Technology |
| --- | --- |
| Markup | HTML5 |
| Styling | Tailwind CSS (CDN) + custom CSS |
| Logic | Vanilla JavaScript |
| Icons | Font Awesome 6 + inline SVG |
| Fonts | Inter, Plus Jakarta Sans, Fira Code (Google Fonts) |
| Hosting | Vercel |

## Project Structure

```
portfolio/
├── index.html      # Single-page app: content, 19 themes, style picker
├── assets/
│   └── avatar.jpg  # Profile image
├── css/style.css   # Legacy minimal styles (kept for reference)
├── js/main.js      # Legacy script (kept for reference)
├── vercel.json     # Vercel routing / cache headers
└── README.md
```

## Getting Started

No build tooling required — it is a static page. Serve it locally with any static server:

```bash
# Python
python -m http.server 8000

# or Node
npx serve .
```

Then open `http://localhost:8000`.

## Usage

1. Open the page.
2. Use the **palette combobox** in the top-right to switch between the 19 design styles.
3. Click **Repo** (top-right) to view this project's source.
4. Your selected style is remembered automatically on the next visit.

## Deployment

The site is deployed on **Vercel** as a static project (`outputDirectory: "."`).

```bash
vercel --prod
```

Routing and long-term asset caching are configured in `vercel.json`.

## Roadmap

- [ ] Optional dark/light auto-detection per style
- [ ] Live GitHub repository feed
- [ ] Per-style transition animations

## License

TODO: Add a license (e.g. MIT) if you intend others to reuse this code.

## Acknowledgments

- Design styles adapted from the in-repo **UI Design Lab** playground.
- Built with [Tailwind CSS](https://tailwindcss.com) and [Font Awesome](https://fontawesome.com).
