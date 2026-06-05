# Portfolio Web Sayfası — Analiz & Plan

## 1. İstek Analizi

**Ham istek:** "Umut Çelik (palamut62) için GitHub profilini yansıtan şık bir personal portfolio web sayfası yap"

**Derinlemesine analiz:**
- **Ne isteniyor:** Kişisel portföy web sitesi (tek sayfa, modern, responsive)
- **Kimin için:** Umut Çelik — yazılım geliştirici, girişimci
- **Neden:** GitHub profilini dijital bir varlığa dönüştürmek, potansiyel işverenlere/işbirlikçilere kendini tanıtmak
- **Ton:** Profesyonel ama kişisel, teknik yetkinliği ön planda tutan

**Hedef kitle:**
| Kitle | Beklenti |
|-------|----------|
| Potansiyel işverenler | Yetkinlik kanıtı, geçmiş projeler, iletişim bilgisi |
| İşbirlikçiler (open-source) | Teknik stack, GitHub bağlantıları, sosyal bağlantılar |
| Genel ziyaretçiler | Hızlı yüklenen, mobil uyumlu, etkileyici tasarım |

---

## 2. Ana Tema

**Tema:** **"Karanlıkta Parlayan Kod"** — Koyu arka plan, neon mavi/mor vurgular, terminal esintili ama zarif

**Tema kelimeleri:** modern · minimal · karanlık · teknik · akıcı · profesyonel

**Renk paleti:**
```
Birincil arka plan: #0a0a0f (çok koyu lacivert-siyah)
İkincil arka plan: #13131a (hafif açık)
Kart arka planı:    #1a1a24
Birincil metin:     #e4e4e7 (beyazımsı gri)
İkincil metin:      #a1a1aa (soluk gri)
Vurgu (birincil):   #6366f1 (indigo/mor)
Vurgu (ikincil):    #06b6d4 (cyan/mavi)
Başarı/yeşil:       #22c55e
Gradyan:            #6366f1 → #06b6d4
```

---

## 3. Önerilen Teknoloji Stack

| Seçenek | Artıları | Karar |
|---------|----------|-------|
| **HTML/CSS/JS (vanilla)** | Hafif, sıfır bağımlılık, GitHub Pages'e tek `push` | ✅ **SEÇİLDİ** |
| Next.js | SSR, routing, zengin ekosistem | ❌ Bu proje için fazla |
| React + Vite | Modern, component tabanlı | ❌ Basit portfolio için overkill |

**Stack kararı:** Vanilla HTML/CSS/JS — hızlı, deploy'ı kolay (GitHub Pages), bakımı basit.

---

## 4. Sayfa Bölümleri (Section Planı)

### 4.1 — Hero / Üst Bölüm
- Tam ekran, arka planda gradient/particle animasyonu
- Profil fotoğrafı veya avatar (monogram)
- "Umut Çelik" — büyük başlık
- "Full-stack Developer · AI Agents & Automation" — alt başlık
  - *Alternatif:* "Full-stack developer, kurucu ortak @nootle.io"
- CTA butonları: "Projeleri Gör" + "İletişim"
- Social links (GitHub, X/Twitter, LinkedIn, nootle.io)

### 4.2 — Hakkımda
- Kısa biyografi (2-3 cümle)
- Konum: Türkiye (📍)
- GitHub rozetleri: Pair Extraordinaire, Pull Shark, YOLO
- İstatistikler: 11 takipçi, 76 takip, N proje (küçük kutucuklarda)

### 4.3 — Yetenekler (Tech Stack)
Teknoloji dilimleri halinde göster:
```
┌─────────────────────────────────────┐
│  Frontend    │  Backend    │  Diğer  │
│──────────────┼─────────────┼─────────│
│  Next.js     │  Python     │  Rust   │
│  React       │  FastAPI    │  Tauri  │
│  TypeScript  │             │  AI/ML  │
└─────────────────────────────────────┘
```
- Her teknoloji için ikon (Devicon veya basit SVG)
- Progress bar yerine "kullanım seviyesi" badges

### 4.4 — Öne Çıkan Projeler
Grid layout (2x2 veya 3 kart), her proje için:
- **Proje adı** + GitHub linki (🔗)
- **Kısa açıklama** (1 cümle)
- **Teknoloji etiketleri** (badge şeklinde)
- Demo linki varsa ayrı buton

| Proje | Açıklama | Tech |
|-------|----------|------|
| **subclip** | AI-powered subtitle generator | Python, AI |
| **antigravity-manager** | Tauri + React + Rust masaüstü uygulaması | Tauri, React, Rust |
| **Bilirkisi-Dosya-Takip** | Dosya takip sistemi | - |
| **Nakliye** | Nakliye yönetim sistemi | - |
| **ai-tweet-bot** | Otomatik tweet botu | Python, AI |
| **borsa-mcp** | Borsa veri MCP server | Python, MCP |

### 4.5 — İletişim
- E-posta (mailto link)
- Sosyal medya linkleri (GitHub, X)
- Web sitesi: nootle.io
- Basit contact form (opsiyonel — Netlify Forms veya Formspree)

### 4.6 — Footer
- © 2025 Umut Çelik
- "Built with ❤️ and ☕"
- Back to top butonu

---

## 5. Tasarım Detayları

### Animasyonlar (CSS only, JS minimal)
- [ ] Hero'da yazı yazma (typewriter) efekti
- [ ] Scroll ile fade-in kartlar (Intersection Observer ile)
- [ ] Proje kartları hover: hafif yükselme + glow efekti
- [ ] Smooth scroll (CSS scroll-behavior)
- [ ] Particle/star arka plan (canvas veya CSS)

### Responsive Breakpoints
| Cihaz | Breakpoint | Düzen |
|-------|-----------|-------|
| Mobil  | < 640px   | Tek kolon |
| Tablet | 640-1024px | 2 kolon grid |
| Desktop | > 1024px | 3 kolon grid |

### Performans Hedefleri
- Lighthouse: 95+ puan (Performance, Accessibility)
- Toplam boyut: < 500KB (resimsiz)
- Zero external JS dependencies

---

## 6. Dosya Yapısı

```
portfolio/
├── index.html          # Ana sayfa (tüm içerik tek HTML)
├── css/
│   └── style.css       # Tüm stiller (CSS custom properties ile)
├── js/
│   └── main.js         # Intersection Observer, typewriter, vs.
├── assets/
│   └── icons/          # SVG ikonlar (teknoloji logo'ları)
├── ANALIZ.md           # Bu dosya (analiz ve plan)
└── README.md           # Proje dokümantasyonu
```

**Not:** Tek dosya HTML de kullanılabilir (inline CSS/JS) — deploy kolaylığı açısından. Ancak ayrı dosyalar daha düzenli, karar geliştirme aşamasında verilecek.

---

## 7. Deploy Stratejisi

| Platform | Yöntem | Artıları |
|----------|--------|----------|
| **GitHub Pages** | `docs/` veya `gh-pages` branch | Ücretsiz, otomatik, GitHub ile entegre |
| Netlify | Drag-drop veya Git deploy | Forms desteği, ücretsiz SSL |
| Vercel | Git connect | Serverless functions (ilerisi için) |

**Öneri:** GitHub Pages — zaten GitHub profili yansıtılıyor, domain (nootle.io) bağlanabilir.

---

## 8. Timeline & İş Paketleri

| # | İş | Süre |
|---|-----|------|
| 1 | HTML iskelet + SEO meta tags | ~30dk |
| 2 | CSS: değişkenler, reset, layout, dark theme | ~1sa |
| 3 | Hero section (animasyonlu) | ~45dk |
| 4 | Hakkımda + Yetenekler bölümü | ~30dk |
| 5 | Projeler grid | ~30dk |
| 6 | İletişim + Footer | ~20dk |
| 7 | JS: scroll animasyonları, typewriter | ~30dk |
| 8 | Responsive test + iyileştirmeler | ~30dk |
| **Toplam** | | **~4 saat** |

---

## 9. Referans İlhamları

- [brittanychiang.com](https://brittanychiang.com) — minimalist portfolio
- [joshwcomeau.com](https://joshwcomeau.com) — renk kullanımı
- [rauno.me](https://rauno.me) — karanlık tema, tipografi
- GitHub Readme Stats API — dinamik GitHub istatistikleri

---

## 10. Karar Noktaları (Geliştirme Sırasında)

- [ ] Tek HTML dosyası mı, ayrı dosyalar mı?
- [ ] Particle arka plan (canvas) kullanılacak mı?
- [ ] Typewriter efekti olacak mı?
- [ ] Projeler manuel listelenecek mi (JSON'dan çekilecek mi)?
- [ ] Contact form eklenmeli mi?
- [ ] GitHub API ile canlı veri çekilmeli mi (followers, repos)?
