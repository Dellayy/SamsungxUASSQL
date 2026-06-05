# SamsungxUASSQL

SamsungxUASSQL adalah dashboard statis yang dirancang untuk menampilkan kekayaan data Samsung secara visual dan interaktif. Data diambil dari `samsungMobilesData.csv` dan diolah menjadi filter modern, kartu produk, dan grafik analitis yang langsung bisa dikunjungi dari HP, tablet, atau laptop.

## Apa yang Bisa Kamu Lihat?

Dashboard ini bukan hanya daftar produk. Fitur utamanya meliputi:
- Filter interaktif untuk **RAM**, **penyimpanan**, **layar**, dan **versi Android**.
- **Kartu rekomendasi model** dengan informasi harga, prosesor, dan ulasan singkat.
- Beragam grafik yang membantu kamu menemukan pola harga, nilai, dan performa.
- **Analisis lanjutan** seperti korelasi baterai vs harga dan perbandingan rata-rata harga Android.
- **Galeri produk** dengan carousel yang responsive dan navigasi thumbnail.

## Mengapa Ini Menarik?

Dashboard ini dibuat agar kamu bisa:
- Menemukan kisaran harga Samsung paling populer dalam hitungan detik.
- Menilai apakah smartphone dengan baterai besar cenderung lebih mahal.
- Melihat versi Android mana yang menawarkan harga terbaik.
- Menemukan model best-value melalui daftar "Top N Model".

## Bagaimana Cara Menjalankannya

Sistem ini bersifat statis, jadi tidak perlu instalasi server khusus. Kamu bisa langsung buka file `index.html` di browser, atau publikasi lewat GitHub Pages agar bisa diakses dari mana saja.

## Panduan Deploy ke GitHub Pages

### 1. Siapkan Git (Jika belum)
1. Download dan install Git dari [git-scm.com](https://git-scm.com/).
2. Buka PowerShell/Command Prompt dan jalankan:
   ```powershell
   git config --global user.name "Nama Anda"
   git config --global user.email "email@anda.com"
   ```

### 2. Inisialisasi Repository Lokal
1. Buka PowerShell di folder `C:\Users\ACER\Downloads\UAS SQL`.
2. Jalankan:
   ```powershell
   git init
   git add .
   git commit -m "Initial commit: Samsung Dashboard Project"
   ```

### 3. Buat Repository GitHub
1. Login ke [github.com](https://github.com).
2. Klik **+** → **New repository**.
3. Isi nama repository: `SamsungxUASSQL`.
4. Pilih **Public**.
5. Jangan centang "Initialize this repository with a README".
6. Klik **Create repository**.

### 4. Push ke GitHub
1. Salin perintah dari halaman repository. Contoh:
   ```powershell
   git branch -M main
   git remote add origin https://github.com/USERNAME/SamsungxUASSQL.git
   git push -u origin main
   ```
   Ganti `USERNAME` dengan username GitHub kamu.

### 5. Aktifkan GitHub Pages
1. Buka repository GitHub.
2. Pergi ke **Settings** → **Pages**.
3. Pilih source:
   - Branch: `main`
   - Folder: `/ (root)`
4. Klik **Save**.
5. Setelah aktif, kamu akan melihat URL situs live.

### 6. Akses Situs
Buka link:

```text
https://USERNAME.github.io/SamsungxUASSQL/
```

## Tips Publikasi & Troubleshooting
- Tunggu 1–2 menit setelah GitHub Pages diaktifkan.
- Jika tidak muncul, refresh browser atau clear cache.
- Pastikan branch sudah di-push dengan `git status`.
- Ulangi deploy setiap kali kamu memperbarui `index.html`, `styles.css`, atau `script.js`.

## Struktur File
- `index.html` — struktur halaman dan area dashboard.
- `styles.css` — desain warna, layout, animasi, dan responsif.
- `script.js` — logika filter, grafik, carousel, dan interaksi.
- `samsungMobilesData.csv` — dataset Samsung.
- `README.md` — dokumentasi penggunaan dan fitur.

## Fitur Grafis & Analitis yang Lebih Lengkap

### 1. Analisis Harga dan Distribusi
- **Histogram Harga** (`priceHistChart`) menampilkan bagaimana harga model Samsung tersebar.
- Cocok untuk melihat apakah banyak model ada di rentang harga budget, mid-range, atau premium.

### 2. Korelasi Baterai vs Harga
- **Scatter plot** (`batteryCorrChart`) menunjukkan hubungan antara kapasitas baterai dan harga.
- Dilengkapi garis regresi dan skor korelasi untuk analisis cepat.
- Sangat berguna jika kamu ingin tahu apakah baterai besar artinya harga besar.

### 3. Perbandingan Harga Android
- **Grafik rata-rata harga per Android version** (`avgAndroidChart`).
- Menampilkan apakah versi Android terbaru cenderung muncul di segmen harga tertentu.

### 4. Rekomendasi Model Terbaik
- **Top N Model** (`topList`) memberi daftar model terbaik berdasarkan skor gabungan.
- Skor dihitung menggunakan kombinasi rating dan harga untuk menilai value terbaik.

### 5. Interaksi dan Visual Modern
- **Zoom & Pan** di grafik dengan plugin Chart.js Zoom.
- **Tooltip interaktif** menampilkan detail saat hover.
- **Carousel produk** dengan thumbnail dan navigasi keyboard.

## Saran Penggunaan
- Coba filter berdasarkan **RAM 8GB+** untuk melihat model flagship terbaik.
- Pilih **Android terbaru** untuk mengecek apakah harga cenderung naik.
- Gunakan **Top N Model** untuk rekomendasi cepat jika kamu ingin value terbaik.

## Kesan Akhir
Dashboard ini dibuat untuk membantu kamu memahami data Samsung dengan cara yang visual, langsung, dan informatif. Kalau kamu ingin menambahkan fitur lain—misalnya filter berdasarkan **kamera**, **jenis prosesor**, atau grafik per seri Galaxy—tinggal edit `script.js` dan tambahkan komponen HTML baru.
