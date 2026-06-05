# SamsungxUASSQL

Dashboard statis ini menampilkan data Samsung dari `samsungMobilesData.csv` dengan filter, grafik, dan kartu produk.

## Akses dari HP, tablet, dan laptop tanpa Python/VScode

Cara paling mudah agar bisa dibuka dari semua perangkat adalah dengan menggunakan GitHub Pages.

### Panduan Upload ke GitHub & Buat GitHub Pages

#### Langkah 1: Siapkan Git (Jika belum)
1. Download dan install Git dari [git-scm.com](https://git-scm.com/).
2. Buka PowerShell/Command Prompt dan jalankan:
   ```powershell
   git config --global user.name "Nama Anda"
   git config --global user.email "email@anda.com"
   ```

#### Langkah 2: Inisialisasi Repository Lokal
1. Buka PowerShell di folder `C:\Users\ACER\Downloads\UAS SQL`.
2. Jalankan:
   ```powershell
   git init
   git add .
   git commit -m "Initial commit: Samsung Dashboard Project"
   ```

#### Langkah 3: Buat Repository di GitHub
1. Login ke [github.com](https://github.com).
2. Klik tombol **+** di kanan atas → **New repository**.
3. Isi nama repository: `SamsungxUASSQL` (PENTING: harus lowercase atau gunakan dash).
4. Pilih **Public** (agar bisa diakses dari mana saja).
5. Jangan centang "Initialize this repository with a README" (karena sudah punya file).
6. Klik **Create repository**.

#### Langkah 4: Connect & Push ke GitHub
1. Di halaman repository baru, copy perintah yang muncul. Contohnya:
   ```powershell
   git branch -M main
   git remote add origin https://github.com/USERNAME/SamsungxUASSQL.git
   git push -u origin main
   ```
   (Ganti `USERNAME` dengan username GitHub Anda)

2. Jalankan perintah di atas di PowerShell folder project:
   ```powershell
   git branch -M main
   git remote add origin https://github.com/USERNAME/SamsungxUASSQL.git
   git push -u origin main
   ```
   
3. Jika diminta login, masukkan username & password GitHub (atau token jika 2FA aktif).

#### Langkah 5: Aktifkan GitHub Pages
1. Buka repository di GitHub.
2. Klik **Settings** → **Pages** (di sidebar kiri).
3. Di bagian **Source**, pilih:
   - Branch: `main`
   - Folder: `/ (root)`
4. Klik **Save**.
5. Tunggu beberapa detik sampai ada notasi "Your site is live at: ...".

#### Langkah 6: Akses dari Semua Device
Setelah GitHub Pages aktif, buka link di browser HP/tablet/laptop:
```
https://USERNAME.github.io/SamsungxUASSQL/
```
(Ganti `USERNAME` dengan username GitHub Anda)

### Poin Penting
- Link GitHub Pages **hanya bisa diakses setelah GitHub Pages diaktifkan** (bukan langsung tersedia).
- Tunggu 1-2 menit setelah setup sebelum link aktif.
- Jika halaman tidak muncul, cek:
  1. Apakah branch sudah di-push: `git status`
  2. Apakah GitHub Pages sudah aktif di Settings → Pages
  3. Refresh browser atau clear cache
- Setiap perubahan file lokal perlu di-push ulang:
  ```powershell
  git add .
  git commit -m "Update dashboard"
  git push origin main
  ```

### File yang Sudah Siap
- `index.html` - halaman utama
- `styles.css` - styling
- `script.js` - logika filter dan interaksi
- `samsungMobilesData.csv` - data Samsung 407 model
- `README.md` - dokumentasi (file ini)

