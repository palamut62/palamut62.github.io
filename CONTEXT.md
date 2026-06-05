# Proje Bağlam Dökümanı (CONTEXT)

> **Proje:** Umut Çelik (palamut62) — Kişisel Portfolio Web Sitesi
> **Amaç:** Bu döküman, projenin "neden"ini, karar gerekçelerini ve çalışma bağlamını açıklar.
> **Hedef Kitle:** Projeye sonradan dahil olan geliştiriciler, bakım yapacak kişiler, veya karar sürecini anlamak isteyenler.

---

## 1. Projenin Kökeni

### 1.1 Ne İstenmişti?
Bir kullanıcı, Umut Çelik (`palamut62`) için GitHub profilini yansıtan şık bir personal portfolio web sayfası yapılmasını talep etti.

### 1.2 Neden?
GitHub profili (`github.com/palamut62`) teknik yetkinlikleri ve projeleri gösterse de:
- **Kurumsal olmayan** bir sunum — her potansiyel işveren GitHub'ı iyi okumaz
- **Kişisel marka** eksikliği — "Umut Çelik" ismi bir web varlığına sahip değildi
- **Hikaye anlatımı** yok — GitHub sadece kod gösterir, kişiliği göstermez
- **İletişim kanalı** eksik — GitHub Issues portföy ziyaretçisi için doğru kanal değil

Portfolio sitesi bu boşlukları doldurmak için tasarlandı.

---

## 2. Temel Kararlar ve Gerekçeler

### 2.1 Neden Vanilla HTML/CSS/JS?

| Karar | Alternatif | Sebep |
|-------|-----------|-------|
| ✅ Vanilla HTML/CSS/JS | Next.js, React, Vue | Portfolio tek sayfa, kompleks state yönetimi gerekmez. Framework'ler ek bağımlılık, build süreci, bundle boyutu getirir. Vanilla daha hızlı yüklenir, GitHub Pages deploy'u tek push'tur. |

**Değerlendirilenler:**
- **Next.js** — SSR güzel, ama bu proje için ağır top. 6 section için framework gerekmez.
- **React + Vite** — Component bazlı düşünmek güzel, ama aynı işi 3 satır JS ile yapabiliyorken React yüklemek anlamsız.
- **Hugo/Jekyll** — Static site generator'lar blog için ideal, portfolio için fazla.

**Karar:** Sıfır bağımlılık, maksimum hız, minimum karmaşıklık.

### 2.2 Neden GitHub Pages?

| Platform | Artılar | Eksiler | Karar |
|----------|---------|---------|-------|
| **GitHub Pages** | Ücretsiz, GitHub ile tam entegre, SSL otomatik, custom domain desteği | Server-side işlem yok, forms desteği yok | ✅ |
| Netlify | Forms desteği, ücretsiz SSL, drag-drop deploy | Ek hesap, GitHub'dan ayrı | ❌ Bu aşamada gereksiz |
| Vercel | Serverless functions, otomatik deploy | Portfolio için overkill | ❌ |

### 2.3 Neden Tek Sayfa (SPA değil, Single Page)?

- Portfolio içeriği az (6 bölüm) — routing gerekmez
- Navigasyon anchor linklerle çözülür (`#hero`, `#projects`)
- SEO için tek URL yeterli
- Kullanıcı deneyimi: scroll ile akış doğal

### 2.4 Neden Intersection Observer (onscroll değil)?

`onscroll` event'ine kıyasla:
- **Performans:** Observer tarayıcı tarafında optimize edilir, scroll event throttling gerekmez
- **Basitlik:** `entry.isIntersecting` ile net kontrol
- **Modern:** ES6+ ile native destek, polyfill gerekmez

---

## 3. Tema Kararları

### 3.1 "Karanlıkta Parlayan Kod"

Bu temanın seçilme nedenleri:

1. **Geliştirici kimliği:** Yazılımcılar karanlık temaya alışkındır (IDE'ler, terminal, VS Code)
2. **Modern duruş:** 2024-2025 portfolio trendleri koyu temayı işaret ediyor
3. **Vurguların ön plana çıkması:** Koyu arka planda indigo/cyan renkler daha çarpıcı
4. **Enerji verimliliği:** OLED/AMOLED ekranlarda koyu tema daha az pil tüketir

### 3.2 Renk Psikolojisi

| Renk | Anlam | Kullanım |
|------|-------|----------|
| **#0a0a0f** (Koyu lacivert-siyah) | Derinlik, profesyonellik, gece | Ana arka plan |
| **#6366f1** (İndigo) | Güven, bilgelik, teknoloji | Birincil vurgu, linkler |
| **#06b6d4** (Cyan) | Yenilik, enerji, netlik | İkincil vurgu, hover state'ler |
| **#e4e4e7** (Beyazımsı gri) | Okunabilirlik, temizlik | Ana metin |

### 3.3 Tipografi Seçimi

| Font | Kullanım | Sebep |
|------|----------|-------|
| **Inter** | Ana metin, başlıklar | Mükemmel okunabilirlik, geniş karakter aralığı, Apple/Google tarafından kullanılıyor |
| **JetBrains Mono** | Kod parçacıkları, teknik etiketler | Geliştirici hissi, terminal estetiği |

---

## 4. İçerik Stratejisi

### 4.1 Dil
**Türkçe** — Proje sahibi Türkiye'de yaşıyor, birincil kitle Türkçe konuşuyor. Teknik terimler İngilizce bırakıldı ("Full-stack Developer", "AI Agents").

### 4.2 Ton
> **Profesyonel ama kişisel.** "Merhaba, ben Umut" gibi samimi bir açılış, ardından teknik yetkinliklerin net sunumu. Resmi kurumsal dilden kaçınıldı.

### 4.3 Proje Seçimi
GitHub'daki tüm repos değil, en temsil edici 6 proje seçildi:
- **subclip** — AI yetkinliğini gösterir
- **antigravity-manager** — Tauri + React + Rust full-stack
- **Bilirkisi-Dosya-Takip** — Domain-specific çözüm
- **Nakliye** — Lojistik sektör deneyimi
- **ai-tweet-bot** — Otomasyon ve AI yetkinliği
- **borsa-mcp** — MCP (Model Context Protocol) ile yenilikçi teknoloji

---

## 5. Kısıtlamalar ve Sınırlamalar

### 5.1 Teknik Kısıtlamalar
| Kısıtlama | Etkisi | Çözüm |
|-----------|--------|-------|
| 0 external JS dependency | Form işleme, analytics eklenemez | MVP'de gerekmez; ileride Formspree eklenebilir |
| GitHub Pages (static only) | Server-side işlem yok | Portfolio için yeterli |
| Vanilla HTML/CSS/JS | Component sistemi yok | Küçük proje olduğu için sorun değil; el ile DOM yönetimi |
| Tek sayfa | Routing yok | 6 section için gerekmez, anchor link yeterli |

### 5.2 İçerik Kısıtlamaları
| Kısıtlama | Sebep |
|-----------|-------|
| GitHub API kullanılmıyor (MVP) | External bağımlılık, rate limiting, offline çalışmama |
| Projeler manuel listeleniyor | JSON config gereksiz; 6 proje için HTML yeterli |
| Profil fotoğrafı yok (MVP) | İzin/ lisans sorunu; monogram avatar yeterli |

---

## 6. Bilinçli Olarak Ertelenen Özellikler

| Özellik | Neden Ertelendi | Gelecekte Nasıl Eklenir |
|---------|----------------|------------------------|
| **Contact form** | Backend/form service gerekir | Formspree (ücretsiz) entegrasyonu |
| **Particle/star background** | Canvas performansı, mobilde pil tüketimi | Canvas API ile opsiyonel toggle |
| **GitHub API entegrasyonu** | Rate limiting, offline kırılma | `fetch` ile `api.github.com/users/palamut62` |
| **Dark/Light theme toggle** | MVP'de sadece dark tema | CSS custom properties + `prefers-color-scheme` + toggle |
| **Blog bölümü** | Portfolio odağından sapma | Ayrı repo, subdomain (blog.nootle.io) |
| **Service Worker** | Static site için gereksiz | Eklenebilir (offline cache için) |

---

## 7. Proje Mimarisi (Mimari Kararlar)

### 7.1 CSS Mimarisi
- **Custom Properties** ile tema sistemi (değişkenler `:root`'ta)
- **BEM-benzeri** class isimlendirme (`.hero`, `.hero__title`, `.hero__cta`)
- **Mobile-first** medya sorguları (`min-width` bazlı)
- **CSS Grid** ana layout, **Flexbox** iç bileşenler

### 7.2 JS Mimarisi
- **Modüler fonksiyonlar** (her özellik ayrı fonksiyon)
- **DOMContentLoaded** ile başlatma
- **Intersection Observer** scroll animasyonları için
- **requestAnimationFrame** typewriter için (opsiyonel)

### 7.3 HTML Mimarisi
- **Semantik HTML5** (`<header>`, `<section>`, `<footer>`, `<nav>`)
- **Accessibility first** (aria-label, role, tabindex)
- **SEO meta** etiketleri (OG, Twitter Card)

---

## 8. Kalite Standartları

| Standart | Hedef |
|----------|-------|
| **WCAG 2.1 AA** | Tüm kontrast oranları ≥ 4.5:1 |
| **Semantic HTML** | `<div>` spam'ı yok, anlamlı elementler |
| **No console errors** | JS'de hata yok |
| **Responsive** | 320px - 2560px arası tüm ekranlar |
| **Cross-browser** | Chrome, Firefox, Safari, Edge (son 2 versiyon) |

---

## 9. İlgili Bağlantılar ve Referanslar

### 9.1 Proje Bağlantıları
| Kaynak | URL |
|--------|-----|
| GitHub Profili | https://github.com/palamut62 |
| Web Sitesi | https://nootle.io |
| GitHub Pages (canlı) | https://palamut62.github.io/portfolio/ |

### 9.2 Referans İlhamları
| Site | Neden İlham Aldık |
|------|-------------------|
| [brittanychiang.com](https://brittanychiang.com) | Minimalist, temiz portfolio yapısı |
| [joshwcomeau.com](https://joshwcomeau.com) | Renk kullanımı, gradient geçişleri |
| [rauno.me](https://rauno.me) | Koyu tema, tipografi, boşluk kullanımı |

### 9.3 Teknoloji Referansları
| Teknoloji | Dokümantasyon |
|-----------|---------------|
| Intersection Observer API | https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API |
| CSS Custom Properties | https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties |
| CSS Grid | https://css-tricks.com/snippets/css/complete-guide-grid/ |
| GitHub Pages | https://docs.github.com/en/pages |

---

## 10. Sürüm Geçmişi

| Versiyon | Tarih | Değişiklikler | Yazar |
|----------|-------|---------------|-------|
| v1.0 | Haziran 2026 | İlk sürüm — tüm kararlar, speklar, bağlam | Hermes Agent |

---

## 11. Riskler ve Mitigasyonlar

| Risk | Olasılık | Etki | Mitigasyon |
|------|----------|------|------------|
| GitHub API rate limiting | Orta | Düşük | API kullanılmıyor (manuel proje listesi) |
| Mobilde animasyon performansı | Düşük | Orta | `will-change` ile GPU hızlandırma, `@media (prefers-reduced-motion)` |
| Font yüklenmezse | Düşük | Düşük | Fallback font stack (`sans-serif`, `monospace`) |
| Tarayıcı uyumsuzluğu | Düşük | Düşük | Modern tarayıcılar (Chrome/Firefox/Safari/Edge son 2 versiyon) |
| İçerik güncellenmezse | Orta | Düşük | Manuel güncelleme; ileride JSON config eklenebilir |
