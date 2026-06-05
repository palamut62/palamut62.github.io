# Portfolio Web Sayfası — Teknik Şartname (SPEK)

> **Proje:** Umut Çelik (palamut62) — Kişisel Portfolio
> **Döküman Versiyonu:** v1.0
> **Durum:** Onaylandı / Geliştirmeye Hazır

---

## 1. Proje Genel Bakış

### 1.1 Amaç
GitHub profilini (`github.com/palamut62`) yansıtan, tek sayfalık, modern, responsive bir personal portfolio web sitesi geliştirmek. Site, potansiyel işverenlere ve işbirlikçilere Umut Çelik'in teknik yetkinliklerini ve projelerini sergileyecek.

### 1.2 Tema
**"Karanlıkta Parlayan Kod"** — Koyu arka plan, indigo/cyan vurgular, terminal esintili ama zarif bir estetik.

---

## 2. Teknoloji Stack

| Bileşen | Teknoloji | Gerekçe |
|---------|-----------|---------|
| **İşaretleme** | HTML5 (semantik) | Evrensel uyumluluk, SEO dostu |
| **Stil** | CSS3 (Custom Properties, Grid, Flexbox) | Sıfır bağımlılık, full kontrol |
| **Davranış** | Vanilla JavaScript (ES6+) | Hafif, framework gereksiz |
| **İkonlar** | SVG (inline + sprite) | Retina uyumlu, boyut bağımsız |
| **Font** | Google Fonts (Inter veya JetBrains Mono) | Modern, okunabilir tipografi |
| **Deploy** | GitHub Pages | Ücretsiz, GitHub entegrasyonu, domain bağlanabilir |

**Bağımlılıklar:** 0 (sıfır) external JS/CSS kütüphanesi. Tamamen vanilla.

---

## 3. Renk Paleti ve Tema

### 3.1 CSS Custom Properties

```css
:root {
  /* Arka planlar */
  --bg-primary:     #0a0a0f;
  --bg-secondary:   #13131a;
  --bg-card:        #1a1a24;
  --bg-hover:       #22222e;

  /* Metin renkleri */
  --text-primary:   #e4e4e7;
  --text-secondary: #a1a1aa;
  --text-muted:     #6b6b80;

  /* Vurgu renkleri */
  --accent-primary: #6366f1;   /* İndigo */
  --accent-secondary: #06b6d4; /* Cyan */
  --accent-gradient: linear-gradient(135deg, #6366f1, #06b6d4);

  /* Durum renkleri */
  --color-success:  #22c55e;
  --color-warning:  #f59e0b;
  --color-error:    #ef4444;

  /* Kenarlık ve gölge */
  --border-color:   #2a2a3a;
  --border-hover:   #3a3a5a;
  --glow-color:     rgba(99, 102, 241, 0.3);
  --shadow-card:    0 4px 20px rgba(0, 0, 0, 0.3);

  /* Tipografi */
  --font-sans:      'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono:      'JetBrains Mono', 'Fira Code', monospace;

  /* Layout */
  --max-width:      1200px;
  --section-padding: 80px 20px;
  --border-radius:  12px;
  --border-radius-sm: 8px;
}
```

### 3.2 Renk Kullanım Tablosu

| Element | Renk / Değer |
|---------|-------------|
| Sayfa arka planı | `--bg-primary` (#0a0a0f) |
| Section arka planı | `--bg-secondary` (#13131a) |
| Kart/badge arka planı | `--bg-card` (#1a1a24) |
| Ana başlıklar | `--text-primary` (#e4e4e7) |
| Alt başlıklar / açıklamalar | `--text-secondary` (#a1a1aa) |
| Linkler / vurgular | `--accent-primary` (#6366f1) |
| Hover / aktif vurgu | `--accent-secondary` (#06b6d4) |
| Başlık gradientleri | `--accent-gradient` |
| Başarı badge'leri | `--color-success` (#22c55e) |
| Kart kenarlıkları | `--border-color` (#2a2a3a) |
| Kart hover kenarlığı | `--border-hover` (#3a3a5a) |
| Glow efekti | `--glow-color` (rgba(99,102,241,0.3)) |

---

## 4. Sayfa Bölümleri — Detaylı Şartname

### 4.1 Hero Section

| Özellik | Şartname |
|---------|----------|
| **Yükseklik** | 100vh (tam ekran) |
| **Arka plan** | Gradient (#0a0a0f → #13131a) + isteğe bağlı star/particle animasyonu |
| **Avatar** | Monogram SVG veya emoji avatar (ilk etapta "UC" harfleri) |
| **Ana başlık** | "Umut Çelik" — `<h1>`, font-weight 700, 3.5rem+ |
| **Alt başlık** | "Full-stack Developer · AI Agents & Automation" — typewriter animasyonlu |
| **İkincil alt başlık** | "Kurucu @ nootle.io" — opsiyonel, `--text-secondary` |
| **CTA butonları** | 2 adet:
| | - "Projeleri Gör" (birincil, dolu buton, indigo)
| | - "İletişim" (ikincil, outline buton)
| **Sosyal linkler** | Icon row: GitHub, X/Twitter, LinkedIn, nootle.io (yeni sekme) |
| **Scroll indicator** | Aşağı ok veya "↓ Scroll" metni, sayfa altında |

**Kabul Kriterleri:**
- Sayfa yüklendiğinde typewriter otomatik başlar
- Responsive'da başlık font-size 1.5rem'a kadar küçülür
- Tüm linkler hover'da glow efekti gösterir

### 4.2 Hakkımda Section

| Özellik | Şartname |
|---------|----------|
| **Layout** | 2-column: sol biyografi, sağ stats/badge'ler |
| **Biyografi** | 2-3 cümle, samimi-profesyonel ton |
| **Konum** | "📍 Türkiye" — emoji ile |
| **GitHub Rozetleri** | Pair Extraordinaire, Pull Shark, YOLO (badge olarak) |
| **İstatistikler** | Kartçıklar: 11 takipçi, 76 takip, 6+ proje |
| **Aktif teknoloji** | "Currently diving deep into: Agentic AI, Rust, Tauri" |

**Responsive Davranış:**
- Desktop: yan yana (2-column grid)
- Mobil: üst üste (tek column)

### 4.3 Yetenekler Section

| Özellik | Şartname |
|---------|----------|
| **Layout** | 3-column grid (Frontend / Backend / Diğer) |
| **Kategori başlıkları** | Her kolon için başlık + alt çizgi |
| **Teknoloji listesi** | İkon + isim şeklinde, badge tarzı kartçıklar |
| **Frontend** | Next.js, React, TypeScript, HTML/CSS |
| **Backend** | Python, FastAPI, Node.js (ops.) |
| **Diğer** | Rust, Tauri, AI/ML, MCP |

**Kabul Kriterleri:**
- Her badge hover'da hafif yükselme + border glow
- Mobilde 2 kolona, çok darsa 1 kolona düşer

### 4.4 Projeler Section

| Özellik | Şartname |
|---------|----------|
| **Layout** | Responsive grid (desktop 3-col, tablet 2-col, mobil 1-col) |
| **Kart içeriği** | Her proje için:
| | - Proje adı (link, GitHub'a gider)
| | - Kısa açıklama (1 cümle)
| | - Teknoloji etiketleri (badge)
| | - Demo linki varsa buton |
| **Proje listesi** | |
| | **subclip** — AI-powered subtitle generator (Python, AI) |
| | **antigravity-manager** — Tauri + React + Rust desktop app |
| | **Bilirkisi-Dosya-Takip** — Dosya takip sistemi |
| | **Nakliye** — Nakliye yönetim sistemi |
| | **ai-tweet-bot** — Otomatik tweet botu (Python, AI) |
| | **borsa-mcp** — Borsa veri MCP server (Python, MCP) |

**Kabul Kriterleri:**
- Kart hover: transform: translateY(-4px) + box-shadow glow
- Etiket badge'leri kategorisine göre renklendirilmiş
- Tüm linkler `target="_blank" rel="noopener noreferrer"`

### 4.5 İletişim Section

| Özellik | Şartname |
|---------|----------|
| **E-posta** | `mailto:` link, ikonlu |
| **Sosyal linkler** | GitHub, X/Twitter, LinkedIn (ikon + kullanıcı adı) |
| **Web sitesi** | nootle.io — ikonlu link |
| **Contact form** | İsteğe bağlı (MVP'de yok, sonra eklenebilir) |

**Kabul Kriterleri:**
- Tüm linkler hover'da vurgu rengine döner
- Kopyalama butonu (e-posta için) opsiyonel

### 4.6 Footer

| Özellik | Şartname |
|---------|----------|
| **Telif** | `© 2025 Umut Çelik` |
| **Slogan** | "Built with ❤️ and ☕" |
| **Back to top** | Sabit buton, sayfa 300px scroll'da görünür |

---

## 5. Animasyonlar ve Etkileşimler

| Animasyon | Teknik | Tetikleyici |
|-----------|--------|-------------|
| **Typewriter** | JS + CSS (border-right blink) | Sayfa yüklemesi |
| **Scroll fade-in** | Intersection Observer API | Element viewport'a girdiğinde |
| **Kart hover** | CSS `transform` + `box-shadow` transition | :hover |
| **Glow efekti** | CSS box-shadow + opacity transition | :hover |
| **Smooth scroll** | CSS `scroll-behavior: smooth` | Anchor link tıklaması |
| **Star/particle** | Canvas API veya CSS animasyon (opsiyonel) | Arka plan (hero) |

### 5.1 Typewriter Detayları

```javascript
// Pseudocode
const text = "Full-stack Developer · AI Agents & Automation";
const speed = 50; // ms per karakter
const deleteSpeed = 30;
const pauseEnd = 2000;
const loop = true;
```

### 5.2 Intersection Observer Detayları

```javascript
// Pseudocode
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
```

- Scroll animasyonu: `opacity: 0 → 1`, `translateY(30px) → translateY(0)`
- Stagger: alt elemanlar 100ms gecikmeyle sırayla görünür

---

## 6. Responsive Breakpoints

| Cihaz | Breakpoint | Grid Yapısı | Font Ölçeği |
|-------|-----------|-------------|-------------|
| **Mobil** | `< 640px` | Tek kolon (1fr) | Hero başlık: 1.75rem |
| **Tablet** | `640px - 1024px` | 2 kolon grid | Hero başlık: 2.5rem |
| **Desktop** | `> 1024px` | 3 kolon grid | Hero başlık: 3.5rem+ |

**Kabul Kriterleri:**
- Mobilde menü hamburger değil, tam genişlik dikey layout
- Tüm dokunmatik hedefler min 44x44px
- Metin asla taşmaz (overflow hidden + word-break)

---

## 7. Dosya Yapısı

```
portfolio/
├── index.html           # Ana sayfa (tüm HTML)
├── css/
│   └── style.css        # Tüm stiller (CSS custom properties)
├── js/
│   └── main.js          # JS: observer, typewriter, scroll
├── assets/
│   └── icons/           # SVG ikonlar (inline kullanım)
├── ANALIZ.md            # Analiz dökümanı
├── SPEK.md              # Bu dosya (teknik şartname)
├── CONTEXT.md           # Proje bağlam dökümanı
└── README.md            # Proje tanıtımı
```

**Alternatif:** Tek dosya HTML (tüm CSS/JS inline) — deploy kolaylığı sağlar. Karar geliştirme sırasında verilecek.

---

## 8. Performans Hedefleri

| Metrik | Hedef |
|--------|-------|
| **Lighthouse Performance** | ≥ 95 |
| **Lighthouse Accessibility** | ≥ 95 |
| **Lighthouse Best Practices** | ≥ 95 |
| **Lighthouse SEO** | ≥ 95 |
| **Toplam boyut** | < 500 KB (resimsiz, fontlar dahil) |
| **First Contentful Paint (FCP)** | < 1.5s |
| **Largest Contentful Paint (LCP)** | < 2.5s |
| **Cumulative Layout Shift (CLS)** | < 0.1 |
| **External dependencies** | 0 |

---

## 9. SEO ve Meta Etiketler

```html
<title>Umut Çelik | Full-stack Developer · AI Agents & Automation</title>
<meta name="description" content="Full-stack developer, AI agents & automation. 
  Kurucu @nootle.io. Python, TypeScript, Rust, FastAPI, Next.js ile modern 
  yazılım çözümleri.">
<meta name="keywords" content="Umut Çelik, palamut62, full-stack developer, 
  AI agents, automation, nootle.io, Python, TypeScript, Rust">
<meta name="author" content="Umut Çelik">
<meta property="og:title" content="Umut Çelik | Portfolio">
<meta property="og:description" content="Full-stack developer · AI Agents & Automation">
<meta property="og:type" content="website">
<meta property="og:url" content="https://palamut62.github.io/portfolio/">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:creator" content="@palamut62">
<link rel="canonical" href="https://palamut62.github.io/portfolio/">
```

---

## 10. Deploy Konfigürasyonu

| Parametre | Değer |
|-----------|-------|
| **Platform** | GitHub Pages |
| **Branch** | `main` (veya `gh-pages`) |
| **Source** | `/` (root) veya `/docs` |
| **Custom domain** | İsteğe bağlı (nootle.io bağlanabilir) |
| **HTTPS** | Otomatik (GitHub Pages) |
| **DNS** | CNAME record → palamut62.github.io |
| **Build** | Gerekmez (static HTML) |

**Deploy adımları:**
1. Repo oluştur → `palamut62/portfolio` veya `palamut62/palamut62.github.io`
2. Dosyaları `main` branch'ine push et
3. GitHub Pages ayarlarından source'u seç
4. (Opsiyonel) Custom domain ekle

---

## 11. Timeline & İş Paketleri

| # | İş Paketi | Süre | Çıktı |
|---|-----------|------|-------|
| 1 | HTML iskelet + SEO meta tags + semantik yapı | 30 dk | `index.html` (boş section'lar) |
| 2 | CSS: değişkenler, reset, layout, dark theme | 60 dk | `style.css` (tema sistemi) |
| 3 | Hero section (typewriter, avatar, CTA) | 45 dk | Tamamlanmış Hero |
| 4 | Hakkımda + Yetenekler bölümü | 30 dk | İçerik section'ları |
| 5 | Projeler grid (6 kart) | 30 dk | Proje kartları |
| 6 | İletişim + Footer | 20 dk | Alt bölümler |
| 7 | JS: Intersection Observer, typewriter, scroll | 30 dk | `main.js` (tüm animasyonlar) |
| 8 | Responsive test + iyileştirmeler | 30 dk | Tüm breakpoint'ler test edilmiş |
| **Toplam** | | **~4 saat** | **Tamamlanmış portfolio sitesi** |

---

## 12. Kabul Kriterleri (Genel)

- [ ] Site tüm modern tarayıcılarda (Chrome, Firefox, Safari, Edge) çalışır
- [ ] Tüm breakpoint'lerde (mobil/tablet/desktop) düzgün görüntülenir
- [ ] Lighthouse tüm kategorilerde ≥ 95 puan alır
- [ ] Hiçbir external JS bağımlılığı yoktur
- [ ] Tüm linkler doğru çalışır ve yeni sekmede açar
- [ ] Typewriter animasyonu otomatik başlar ve döngüye girer
- [ ] Scroll fade-in animasyonları düzgün çalışır
- [ ] GitHub Pages'e tek push ile deploy edilebilir
- [ ] Toplam dosya boyutu 500KB'ın altındadır

---

## 13. Gelecek Geliştirmeler (Post-MVP)

- [ ] Contact form (Formspree veya Netlify Forms entegrasyonu)
- [ ] GitHub API ile canlı veri (follower sayısı, repo listesi)
- [ ] Blog bölümü
- [ ] Dark/light theme toggle
- [ ] Service Worker ile offline destek
- [ ] Particle/star background canvas animasyonu
- [ ] Proje detay modal'ları
