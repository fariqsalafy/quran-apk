# Changelog — Al-Qur'an ABBS

## v2.0.1 (Juli 2026)

### Perbaikan
- Fix reading bar pos-bottom melayang di atas gesture navigation — ubah `bottom: env(safe-area-inset-bottom, 0)` → `bottom: 0`
- App name konsisten "Al-Qur'an Digital" di launcher & APK filename (`AlQuran.apk`)

## v2.0.0 (Juli 2026)

### Tampilan & Pengalaman Membaca
- **Perataan teks**: default kini rata tengah ala mushaf per-baris; dapat diubah di
  Pengaturan menjadi Kanan / Rata Penuh / Kiri.
- **Garis mushaf generasi baru**: garis tipis penuh selebar kolom yang digambar
  per-baris berdasarkan pengukuran posisi teks nyata di layar (self-calibrating) —
  presisi di perangkat & ukuran huruf apa pun, kebal terhadap judul surah,
  basmalah, dan terjemahan di tengah halaman.
- Pengaturan baru: **Posisi Garis** (slider naik/turun) dan **Tanpa Garis**
  (mematikan garis sepenuhnya).
- **Ukuran huruf maksimal dinaikkan 70 → 120 px** (slider & cubit layar).
- **Highlight ayat**: ketuk ayat kini berwarna biru jelas dengan latar lembut
  di semua tema; nomor ayat berdudukan konsisten di semua perangkat.
- Responsif menyeluruh: HP kecil (<350px), HP landscape, tablet, hingga monitor
  lebar (konten & dialog terpusat otomatis).

### Rasm & Font
- **IndoPak**: teks asli Mushaf Majeed 6.236 ayat kini tertanam penuh (offline),
  dirender dengan font IndoPak Nastaleeq — bukan lagi teks Utsmani berfont Urdu.
- **Rasm Utsmani**: font resmi KFGQPC Uthmanic Hafs (Mushaf Madinah) tertanam
  base64 — tampil benar walau tanpa internet.
- Pilihan font disederhanakan: font otomatis mengikuti Standar Rasm.
- Pengaturan **Tanda Mushaf** (Otomatis / Tampilkan / Sembunyikan): tanda kecil
  mushaf (sifr, iqlab, waqaf, dll.) disembunyikan otomatis pada perangkat yang
  fontnya gagal dimuat, sehingga tidak muncul artefak lingkaran hitam; harakat
  inti selalu utuh.
- Basmalah ganda di awal surah diperbaiki; header basmalah mengikuti rasm aktif.

### Audio
- **Unduh audio 1 Al-Qur'an penuh** — Qari Misyari Rasyid Al-'Afasy, 6.236 file
  (± 500 MB), tersimpan lokal; bisa dijeda dan otomatis lanjut, ada progres MB,
  serta opsi hapus.
- Pemutar kini offline-first (cek penyimpanan lokal dulu, baru streaming) dan
  tidak lagi bergantung API perantara; perpindahan antar-surah otomatis rapi.

### Fitur Baru Lain
- **Kartu Progres Tilawah** di beranda: persentase halaman unik yang telah
  dibaca dari 604 halaman, dengan tombol reset khataman.
- **Tombol/gestur back Android**: menutup popup → keluar mode baca → baru keluar
  aplikasi (via Capacitor App plugin); di browser/PWA memakai riwayat history.
- Blok **Sumber Data Al-Qur'an & Atribusi** di halaman Informasi (Tanzil, QUL/
  QuranWBW, KFGQPC, AlQuran Cloud, Islamic Network).

### Perbaikan Bug
- Nama surah ber-apostrof (Al-An'aam, Al-A'raaf, dll.) merusak sentuhan ayat
  ("missing ) after argument list") — diperbaiki dengan escaping.
- URL font Madinah versi lama mati sehingga rasm Utsmani tampil dengan font
  sistem — kini font tertanam di dalam aplikasi.
- Posisi preview di Pengaturan tidak pas saat rasm IndoPak — kotak preview kini
  fleksibel dan terpusat.

## v1.0.0
- Rilis awal: mushaf digital 604 halaman, terjemahan Indonesia, audio streaming,
  bookmark, tafsir, pencarian, mode offline teks, tema terang/gelap/mushaf,
  pembungkus Capacitor + build APK otomatis via GitHub Actions.
