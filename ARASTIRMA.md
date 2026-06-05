# Portfolio Web Sitesi Araştırma Raporu

> Proje: `~/projeler/portfolio/`
> Stack: **Vanilla HTML/CSS/JS** — sıfır harici bağımlılık
> Tema: Koyu tema, **indigo/cyan** vurgular
> Deploy: **GitHub Pages**

---

## 1. Devicon — Teknoloji İkonları

### Kaynak
- **Web sitesi:** [devicon.dev](https://devicon.dev/)
- **GitHub:** [devicons/devicon](https://github.com/devicons/devicon) — 11.7k ★, MIT lisansı
- **Toplam:** 578 ikon, 3067 varyant

### Kullanım Yöntemleri

**A) CSS class ile (Font stili)**
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css">

<i class="devicon-html5-plain colored"></i>
<i class="devicon-css3-plain colored"></i>
<i class="devicon-javascript-plain colored"></i>
<i class="devicon-python-plain colored"></i>
<i class="devicon-typescript-plain colored"></i>
<i class="devicon-rust-plain colored"></i>
<i class="devicon-fastapi-plain colored"></i>
<i class="devicon-nextjs-original colored"></i>
<i class="devicon-tauri-original colored"></i>
<i class="devicon-react-original colored"></i>
```

**B) Doğrudan SVG (önerilen — sıfır bağımlılık)**
```html
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg" height="40"/>
```
Her ikon için CDN URL formatı:
```
https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/<icon-adı>/<icon-adı>-<varyant>.svg
```

**Varyantlar:** `original`, `plain`, `line`, `original-wordmark`, `plain-wordmark`
**Renklendirme:** `.colored` class'ı eklendiğinde orijinal renkleri alır.

### Proje İçin Gereken İkonlar ve URL'leri

| İkon | CDN URL |
|------|---------|
| HTML5 | `.../html5/html5-original.svg` |
| CSS3 | `.../css3/css3-original.svg` |
| JavaScript | `.../javascript/javascript-original.svg` |
| Python | `.../python/python-original.svg` |
| TypeScript | `.../typescript/typescript-original.svg` |
| Rust | `.../rust/rust-original.svg` |
| FastAPI | `.../fastapi/fastapi-original.svg` |
| Next.js | `.../nextjs/nextjs-original.svg` |
| Tauri | `.../tauri/tauri-original.svg` |
| React | `.../react/react-original.svg` |

---

## 2. GitHub Readme Stats API

### Kaynak
- **GitHub:** [anuraghazra/github-readme-stats](https://github.com/anuraghazra/github-readme-stats) — 79.6k ★
- **Endpoint (public Vercel):** `https://github-readme-stats.vercel.app/api`

### Kart Türleri

**A) GitHub Stats Kartı**
```
https://github-readme-stats.vercel.app/api?username=umuti&show_icons=true&theme=dark
```

**B) Top Languages Kartı**
```
https://github-readme-stats.vercel.app/api/top-langs/?username=umuti&layout=compact&theme=dark
```

**C) Repo Pin Kartı**
```
https://github-readme-stats.vercel.app/api/pin/?username=umuti&repo=proje-adi&theme=dark
```

### Tema Parametreleri
- `theme=dark` — koyu arka plan, beyaz yazı
- `theme=tokyonight` — mavi/mor koyu tema (indigo/cyan ile uyumlu)
- `theme=radical` — pembe/mor
- `theme=transparent` — saydam arka plan (kendi dark tema ile kullanılabilir)

### Özel Renklendirme
```html
https://github-readme-stats.vercel.app/api?username=umuti&show_icons=true
  &title_color=6366f1    /* indigo-500 */
  &text_color=e2e8f0     /* slate-200 */
  &icon_color=06b6d4     /* cyan-500 */
  &bg_color=0f172a       /* slate-900 */
  &hide_border=true
```

### Dark/Light Duyarlı Kullanım
```html
<picture>
  <source srcset="...&theme=dark" media="(prefers-color-scheme: dark)">
  <img src="...&theme=default">
</picture>
```

### Uyarılar
- Public Vercel instance'ı rate limit'e takılabilir — en iyi çaba bazlıdır.
- Cache süreleri: stats 24s, languages 144s, pins 240s.
- Private repo istatistikleri için self-hosting gerekir.
- Top languages **skill göstergesi değildir** — byte count bazlıdır.

---

## 3. Typewriter Efekti — Saf JS

### Yaklaşım A: CSS-only (basit, tek satır)
- **Artı:** Hiç JS gerekmez.
- **Eksi:** Metin uzunluğu önceden bilinmeli (steps sayısı), tek satır, geri silme yok.

```css
.typewriter h1 {
  overflow: hidden;
  border-right: .15em solid #6366f1;
  white-space: nowrap;
  width: 0;
  animation:
    typing 3.5s steps(30, end) forwards,
    blink .75s step-end infinite;
}
@keyframes typing { from { width: 0 } to { width: 100% } }
@keyframes blink { 50% { border-color: transparent } }
```

### Yaklaşım B: Saf JS (önerilen — çok satır, silme, döngü)
```javascript
class TypeWriter {
  constructor(el, strings, period = 2000) {
    this.el = el;
    this.strings = strings;
    this.period = period;
    this.loopNum = 0;
    this.txt = '';
    this.isDeleting = false;
    this.tick();
  }
  tick() {
    const i = this.loopNum % this.strings.length;
    const fullTxt = this.strings[i];
    this.txt = this.isDeleting
      ? fullTxt.substring(0, this.txt.length - 1)
      : fullTxt.substring(0, this.txt.length + 1);

    this.el.innerHTML = `<span class="wrap">${this.txt}</span>`;

    let delta = 200 - Math.random() * 100;
    if (this.isDeleting) delta /= 2;
    if (!this.isDeleting && this.txt === fullTxt) {
      delta = this.period;
      this.isDeleting = true;
    } else if (this.isDeleting && this.txt === '') {
      this.isDeleting = false;
      this.loopNum++;
      delta = 500;
    }
    setTimeout(() => this.tick(), delta);
  }
}
// Kullanım:
// new TypeWriter(document.querySelector('.typewrite'), ['Frontend Developer', 'Rust Enthusiast', 'UI Designer']);
```

### Özellikler
- Sıfır bağımlılık, saf JS
- Yazma + silme + döngü desteği
- İmleç efekti CSS ile: `.typewrite > .wrap { border-right: 0.08em solid #6366f1; }`
- Rastgele hız varyasyonu (daha doğal)

---

## 4. Intersection Observer — Scroll Animasyonu

### Temel Kullanım
```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('fade-in-visible');
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
```

### CSS
```css
.fade-in {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease-out, transform 0.6s ease-out;
}
.fade-in-visible {
  opacity: 1;
  transform: translateY(0);
}
```

### Gelişmiş Seçenekler
```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('animate');
      observer.unobserve(entry.target); // bir kez çalıştır
    }
  });
}, {
  threshold: 0.15,       // %15 görünür olunca tetikle
  rootMargin: '0px 0px -50px 0px'  // 50px erken tetikle
});
```

### Animasyon Varyasyonları
| Efekt | CSS |
|-------|-----|
| Fade-in | `opacity: 0 → 1` |
| Slide-up | `translateY(30px) → 0` |
| Slide-left | `translateX(50px) → 0` |
| Scale-in | `scale(0.9) → scale(1)` |
| Glow-in | `box-shadow: 0 0 0 → 0 0 20px rgba(99,102,241,0.3)` |

---

## 5. CSS Custom Properties — Dark Theme

### Temel Yapı
```css
:root {
  /* Dark theme (varsayılan) */
  --bg-primary: #0f172a;       /* slate-900 */
  --bg-secondary: #1e293b;     /* slate-800 */
  --bg-card: #1e293b;
  --text-primary: #f1f5f9;     /* slate-100 */
  --text-secondary: #94a3b8;   /* slate-400 */
  --accent-indigo: #6366f1;    /* indigo-500 */
  --accent-cyan: #06b6d4;      /* cyan-500 */
  --accent-purple: #a855f7;    /* purple-500 */
  --border: #334155;           /* slate-700 */
  --shadow: rgba(0, 0, 0, 0.3);
  --glow-indigo: 0 0 20px rgba(99, 102, 241, 0.3);
  --glow-cyan: 0 0 20px rgba(6, 182, 212, 0.3);
  --gradient-hero: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
}
```

### Light Theme Desteği (opsiyonel)
```css
[data-theme="light"] {
  --bg-primary: #ffffff;
  --bg-secondary: #f8fafc;
  --bg-card: #ffffff;
  --text-primary: #0f172a;
  --text-secondary: #64748b;
  --border: #e2e8f0;
  --shadow: rgba(0, 0, 0, 0.1);
  --gradient-hero: linear-gradient(135deg, #ffffff 0%, #eef2ff 50%, #ffffff 100%);
}
```

### CSS `light-dark()` Fonksiyonu (Modern)
```css
:root {
  color-scheme: light dark;
}
body {
  background: light-dark(#ffffff, #0f172a);
  color: light-dark(#0f172a, #f1f5f9);
}
```
> Not: `light-dark()` henüz tüm tarayıcılarda tam desteklenmiyor (2025-2026 itibarıyla Chromium ve Firefox var).

### İndigo/Cyan Renk Paleti
```css
/* Vurgu renkleri */
--indigo-400: #818cf8;
--indigo-500: #6366f1;
--indigo-600: #4f46e5;
--cyan-400: #22d3ee;
--cyan-500: #06b6d4;
--cyan-600: #0891b2;

/* Hover glow */
.btn:hover {
  box-shadow: 0 0 15px var(--accent-indigo), 0 0 30px rgba(99, 102, 241, 0.2);
}
```

---

## 6. Tasarım Trendleri (2025-2026)

### Modern Developer Portfolio Özellikleri

| Trend | Açıklama |
|-------|----------|
| **Hero typewriter** | İsim + title döngüsü (Frontend Dev / Rust Enthusiast / ...) |
| **Bento grid** | Projeleri ve yetenekleri düzensiz grid kutularında gösterme |
| **Glassmorphism** | Cards: `background: rgba(30, 41, 59, 0.8); backdrop-filter: blur(10px);` |
| **Glow efekti** | İndigo/cyan neon glow hover, border glow, text glow |
| **Minimal navigasyon** | Üstte sticky navbar, yumuşak scroll, tek sayfa |
| **Smooth scroll** | `scroll-behavior: smooth;` + sekmeli bölümler |
| **Proje kartları** | Hover'da glow + scale, screenshot thumbnail, teknoloji etiketleri |
| **İlerleme çubuğu** | Scroll pozisyonu göstergesi (navbar'da) |
| **Kesintili bölümler** | `clip-path` ile diagonal geçişler veya gradient divider |
| **İstatistikler** | GitHub Readme Stats ile dinamik kartlar |

### Önerilen Bölümler (Sıralı)

1. **Hero** — İsim, typewriter title, CTA butonları, profil fotoğrafı
2. **Hakkımda** — Kısa bio, teknoloji ikonları (devicon)
3. **Yetenekler** — Kategoriye ayrılmış skill kartları (Frontend, Backend, Tools)
4. **Projeler** — GitHub pinned repo kartları veya özel proje kartları
5. **İstatistikler** — GitHub Readme Stats görselleri
6. **İletişim** — Sosyal linkler, mail formu veya direkt bağlantılar
7. **Footer** — Copyright, back-to-top butonu

### Örnek Renk Teması (İndigo/Cyan Dark)
```
Arka plan:   #0f172a (slate-900)
Kart:        #1e293b (slate-800) veya glassmorphism
Yazı:        #f1f5f9 (slate-100)
İkincil yazı:#94a3b8 (slate-400)
Vurgu:       #6366f1 (indigo-500) — butonlar, linkler, başlıklar
İkincil vurgu:#06b6d4 (cyan-500) — hover durumları, ikonlar
Başarı:      #10b981 (emerald-500)
Border:      #334155 (slate-700)
```

---

## 7. GitHub Pages Deploy Dosya Yapısı

### Seçenek A: Root'tan serve (basit)
```
portfolio/
├── index.html              # Ana sayfa
├── css/
│   └── style.css
├── js/
│   └── main.js
├── assets/
│   ├── images/             # Profil fotoğrafı, screenshotlar
│   └── icons/              # SVG ikonlar (offline yedek)
└── README.md
```
- GitHub Pages ayarı: Settings > Pages > Source: **Deploy from a branch**
- Branch: `main`, folder: `/ (root)`

### Seçenek B: `/docs` klasöründen serve (repo kökü karışmasın)
```
portfolio/
├── docs/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── assets/
│       ├── images/
│       └── icons/
├── .gitignore
└── README.md
```
- GitHub Pages ayarı: Branch: `main`, folder: `/docs`

### GitHub Pages Kurulum Adımları

1. Repo oluştur: `umuti.github.io` (kullanıcı sayfası) veya `portfolio` (proje sayfası)
2. Dosyaları push et
3. Repo > Settings > Pages > Source: **GitHub Actions** veya **Deploy from branch**
4. Branch: `main`, folder: `/` (veya `/docs`)
5. Custom domain (isteğe bağlı): DNS ayarları + CNAME dosyası

### GitHub Actions ile Deploy (opsiyonel)
```yaml
name: Deploy to Pages
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      pages: write
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v4
      - uses: actions/upload-pages-artifact@v3
        with:
          path: '.'
      - uses: actions/deploy-pages@v4
```

### Önemli Notlar
- Ana HTML dosyası **mutlaka** `index.html` olmalı
- Dosya/klasör adlarında büyük-küçük harf duyarlılığına dikkat (Linux)
- Custom domain için repo köküne `CNAME` dosyası eklenebilir
- GitHub Pages varsayılan olarak `username.github.io` adresinde yayın yapar
- Jekyll varsayılan olarak aktif — eğer static site kullanıyorsanız repo köküne `.nojekyll` dosyası ekleyin

---

## 8. Özet ve Öneriler

### Kullanılacak Teknolojiler / Araçlar

| İhtiyaç | Çözüm | Bağımlılık |
|---------|-------|------------|
| İkonlar | Devicon CDN (SVG img tag) | Sadece CDN URL |
| GitHub istatistikleri | GitHub Readme Stats API | Sadece resim URL |
| Typewriter | Saf JS class (Yaklaşım B) | Yok |
| Scroll animasyonu | Intersection Observer API | Yok |
| Dark theme | CSS custom properties | Yok |
| Tasarım | Bento grid + glassmorphism + glow | Yok |
| Deploy | GitHub Pages (root) | Yok |

### Sıfır Bağımlılık Stratejisi
Tüm harici kaynaklar **CDN URL** veya **resim URL** olarak kullanılacak:
- Devicon ikonları: `<img src="...devicon...svg">`
- GitHub Readme Stats: `<img src="...vercel.app/...">`
- Google Fonts: `<link href="https://fonts.googleapis.com/...">` (opsiyonel)
- Font Awesome yerine SVG ikonlar

Bu yaklaşımla projede **tek bir npm/yarn bağımlılığı olmayacak**, sadece HTML + CSS + JS dosyaları olacak.
