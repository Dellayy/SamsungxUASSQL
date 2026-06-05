# SamsungxUASSQL

![Samsung Dashboard](https://img.shields.io/badge/Dashboard-Samsung-blue?style=for-the-badge&logo=android)

![Dashboard Preview](https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=1200&q=80)

SamsungxUASSQL adalah proyek dashboard visual yang menampilkan data Samsung secara modern dan interaktif. Seluruh analisis dijalankan di browser dengan HTML, CSS, dan JavaScript saja — tidak perlu backend.

---

## 🎨 Visual Highlights

- **Hero landing page** dengan judul besar dan ajakan masuk ke dashboard.
- **Panel fitur** yang menampilkan keunggulan filter, analisis, dan tampilan elegan.
- **Carousel produk** dengan thumbnail, indikator, dan animasi slide.
- **Grafik interaktif** dengan zoom, pan, dan tooltip yang jelas.
- **Top N Model** menampilkan rekomendasi terbaik berdasarkan value.

## 🌟 Ringkasan Proyek

Dashboard ini dibuat untuk membantu kamu:
- Menjelajah data Samsung secara cepat.
- Melihat pola harga, baterai, dan Android version.
- Mencari model terbaik berdasarkan value.
- Menyajikan data dalam tampilan yang responsive dan mudah dibaca.

## 📌 Apa yang Ada di Dashboard

Fitur utama yang sudah tersedia:
- Filter dinamis untuk **RAM**, **penyimpanan**, **layar**, dan **Android version**.
- **Kartu produk** dengan detail model, harga, prosesor, dan rating.
- **Carousel produk** dengan thumbnail dan kontrol keyboard.
- **Ringkasan statistik** jumlah model, rata-rata harga, dan baterai terbaik.
- Grafik interaktif:
  - Histogram harga
  - Scatter plot baterai vs harga
  - Rata-rata harga per Android version
  - Rata-rata harga per RAM
  - Top N model berdasarkan skor gabungan
- Dukungan **zoom & pan** pada grafik dengan plugin Chart.js Zoom.

## 🎯 Keunggulan yang Bikin Menarik

Dashboard ini bukan sekadar daftar. Ini membantu kamu menemukan insight seperti:
- Rentang harga Samsung yang paling sering muncul.
- Apakah smartphone dengan baterai besar biasanya lebih mahal.
- Apakah versi Android terbaru memberi nilai yang lebih baik.
- Model Samsung mana yang punya kombinasi rating dan value terbaik.

## 🚀 Cara Menjalankan Secara Lokal

### 1. Buka langsung
Cukup buka `index.html` di browser mana saja.

### 2. Jalankan server lokal (opsional)
Jika ingin demo lebih rapi, gunakan Python:

```powershell
python -m http.server 8000
```

Lalu buka:

```text
http://localhost:8000
```

> Catatan: Jika kamu memakai file `run_local_server.py`, kamu juga bisa menjalankannya langsung dari Python.

## 🌍 Publish dengan GitHub Pages

### Langkah singkat
1. `git init`
2. `git add .`
3. `git commit -m "Deploy Samsung dashboard"`
4. `git remote add origin https://github.com/USERNAME/SamsungxUASSQL.git`
5. `git push -u origin main`
6. Aktifkan GitHub Pages di Settings → Pages → Branch `main` → Folder `/ (root)`.

### Akses setelah live
```text
https://USERNAME.github.io/SamsungxUASSQL/
```

## 🧩 Struktur File

- `index.html` — halaman utama, landing, dan dashboard.
- `styles.css` — desain warna, animasi, dan layout responsif.
- `script.js` — semua logika filter, grafik, carousel, dan analisis data.
- `samsungMobilesData.csv` — dataset Samsung yang digunakan.

## 📊 Insight yang Bisa Kamu Temukan

### 1. Harga Populer
Histogram harga menunjukkan rentang harga yang paling umum dari semua model.

### 2. Baterai vs Harga
Scatter plot membantu kamu mengidentifikasi apakah model dengan baterai lebih besar juga lebih mahal.

### 3. Android Version vs Harga
Grafik rata-rata harga per Android version mengecek apakah versi terbaru naik kelas harga.

### 4. Top N Model
Daftar model terbaik didasarkan pada skor yang menyeimbangkan rating dan harga untuk value terbaik.

## 💡 Tips Eksplorasi

- Filter ke **RAM 8GB** atau lebih untuk melihat model flagship.
- Pilih **Android terbaru** untuk melihat tren harga modern.
- Gunakan **Top N Model** untuk menemukan model yang paling cocok untuk kebutuhanmu.
- Bereksperimen dengan filter kombinasi untuk menemukan smartphone ideal kamu.

## ✨ Ide Pengembangan Selanjutnya

Kalau ingin ditingkatkan lagi, kamu bisa menambahkan:
- filter berdasarkan **kamera** atau **jenis prosesor**
- grafik tren harga per seri Galaxy
- card comparison antar model
- dark/light mode toggle

## 📣 Catatan

README ini dibuat agar proyek terlihat lebih menarik dan mudah dipahami. Jika kamu ingin saya tambahkan contoh screenshot atau preview gambar dashboard, saya bisa langsung tambahkan bagian visual tersebut.
