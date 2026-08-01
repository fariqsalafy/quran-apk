# Changelog — Al-Qur'an Digital

## v3.3.3 (Agustus 2026)

- **Desain hero jadwal shalat baru (Next Focus)**: waktu shalat berikutnya
  ditampilkan besar (nama + countdown + jam + zona WIB/WITA/WIT) di panel
  emas, 4 waktu lainnya sebagai grid kecil. Berdasarkan mockup varian C yang
  disetujui (juga jadi referensi desain widget home screen ke depan).
- **Fix bug countdown negatif** (sejak v3.3.0): logika pemilihan "waktu
  berikutnya" salah — waktu yang sudah lewat bisa terpilih (countdown minus).
  Kini hanya waktu yang belum lewat yang dipilih; malam hari otomatis
  menampilkan "Subuh Besok".

## v3.3.2 (Agustus 2026)

- **Jadwal offline = online 100% (selisih 0%)**: saat memilih kota (atau buka
  app dengan kota tersimpan), app mengunduh jadwal resmi Kemenag **12 bulan ke
  depan** dari API dan menyimpannya di localStorage. Saat offline, jadwal
  dibaca dari cache — datanya identik persis dengan online (bukan hisab
  perkiraan). Hisab lokal tetap jadi cadangan terakhir hanya jika cache kosong
  dan offline total.
- Label sumber diperjelas: "Kemenag API" (online), "Kemenag (tersimpan)"
  (offline dari cache), "Hisab Lokal" (cadangan).

## v3.3.1 (Agustus 2026)

- **Fix krusial hisab offline**: normalisasi Right Ascension (0-360°) di
  `sunPosition` — sebelumnya eqTime bisa meleset ~24 jam saat matahari di
  belahan langit selatan (Sep–Mar), membuat jadwal Des–Feb kacau. Kini akurat
  sepanjang tahun, terverifikasi 9 titik tanggal (Agustus 2026 – Maret 2028,
  termasuk tahun kabisat) vs jadwal Kemenag: selisih maks 3 menit.
- **Fix parsing tanggal API MyQuran**: format `'Sabtu, 15/08/2026'` kini
  di-parse dengan regex DD/MM/YYYY (sebelumnya `slice()` rapuh).
- **Notifikasi adzan berulang harian**: schedule pakai `on:{hour,minute}` +
  `every:'day'` (sebelumnya `at` sekali-tembak).

## v3.3.0 (Agustus 2026)

- **Fitur baru: Jadwal Shalat** di hero menu (menggantikan stats 114/6236/30/604).
  - Metode hisab **Kemenag RI** (Subuh -20°, Isya -18°, Ashar bayangan 1x,
    ihtiyat 2 menit). Hybrid: coba API MyQuran (sumber jadwal Kemenag) dulu,
    otomatis fallback ke hisab lokal jika offline/gagal.
  - Lokasi: GPS otomatis ATAU pilih kota manual (54 kota utama Indonesia,
    termasuk semua kota sekitar ABBS).
  - Menampilkan 5 waktu shalat + waktu berikutnya + countdown, kartu bisa
    diketuk untuk membuka pengaturan.
- **Fitur baru: Notifikasi Adzan** (toggle di modal Jadwal Shalat) — jadwalkan
  notifikasi tiap waktu shalat via Capacitor Local Notifications (hanya aktif
  di APK; app perlu dibuka minimal sekali setelah install).
- Dependency baru: `@capacitor/local-notifications`.

## v3.2.2 (Agustus 2026)

- **Fix: font default tidak 70.** Pinch handler lama memakai variabel
  `currentFontSize` (baseline 28, tidak pernah disinkron dari config) dan
  menyimpan 28 ke config saat sentuhan 2 jari. Handler duplikat itu dihapus;
  kini hanya ada satu mekanisme pinch yang membaca font dari CSS var.
- **Fitur baru: Kunci Ukuran Font** (`fontLock`, default ON). Saat aktif,
  pinch/gesture tidak mengubah ukuran font sama sekali; slider manual di
  Pengaturan tetap berfungsi. Toggle tersedia di Pengaturan.

## v3.2.1 (Agustus 2026)

- **Fix: tema selalu gelap/putih meski default mushaf.** Penyebab: fitur
  "Mode Malam Otomatis" (ikut prefers-color-scheme sistem) menimpa tema default
  saat aplikasi dibuka. Auto-theme dihapus total (fungsi + CSS media query +
  listener). Tema kini selalu mengikuti pilihan user / default mushaf.
- Key config dinaikkan `quranProConfig_v5` -> `v6` agar config lama yang
  terkontaminasi tema gelap tidak terbawa.

## v3.2.0 (Agustus 2026)

- **Default baru**: tema Mushaf (krem), garis mushaf NON-aktif, ukuran teks 70px.
  Key config dinaikkan `quranProConfig_v4` -> `quranProConfig_v5` agar semua
  pengguna mendapat default baru.
- **Update tanpa uninstall**: build kini memakai release keystore tetap
  (disimpan di GitHub Secrets) + `assembleRelease` + versionCode naik per build.
  Signature konsisten -> Android bisa install di atas versi lama (tidak perlu
  uninstall dulu).

## v3.1.1 (Agustus 2026)

- **Fix: fitur "Pergi ke Ayat" tidak berjalan.** Sebelumnya `goToNavTarget`
  memakai halaman awal surah (`surahPageMap`), sehingga ayat yang berada di
  halaman lain tidak pernah ditemukan & tidak di-scroll. Sekarang memakai
  `pageOfAyah(s,a)` + `scrollToAyah` (pola sama seperti bookmark presisi).

## v3.1.0 (Agustus 2026)

- Update index.html dari zip `quran-apk-github-v3.zip` — judul aplikasi
  "Al-Qur'an Pro v5".
- Bar baca: jangkar rapat di tepi layar, latar menjulur ke area gestur,
  kompensasi poni/status-bar untuk mode fullscreen APK.
- Navigasi: bookmark presisi per-ayat → halaman, buka surah tepat sasaran,
  info ayat aktif di header bar baca, pemisah "HALAMAN N".
- Pengaturan: tanda mushaf 3 mode (Otomatis/Tampil/Sembunyikan), garis mushaf,
  preview hidup di modal Pengaturan, status tombol aktif jelas (centang emas).
- Tampilan ayat: line-height 2.3, perataan dinamis, basmalah di-fit otomatis.

## v2.0.1 (Agustus 2026)

### Navigasi & Bacaan
- **Bookmark presisi**: membuka langsung halaman tempat ayat berada (peta
  ayat→halaman, mis. Ayat Kursi 2:255 → hal. 42), scroll ke tengah layar, dan
  ayat otomatis ter-highlight — sebelumnya selalu mendarat di awal surah.
- **Buka surah tepat sasaran**: memilih nama surah kini langsung menampilkan
  kotak judul surah + basmalah + ayat pertama, tanpa perlu scroll manual.
- **Info ayat aktif di bar baca**: header menampilkan `QS. [Nama] — Hal. X ·
  Ayat Y` mengikuti ayat teratas di layar; posisi "Lanjutkan Membaca" kini
  tersimpan per-ayat secara akurat saat scroll (bukan hanya saat ayat diketuk).
- **Pemisah antar halaman**: lencana "HALAMAN N" bergaris emas di tiap
  pergantian halaman.
- **Basmalah** di awal surah tampil kembali dengan megah — ukurannya di-fit
  otomatis hingga hampir selebar kolom, mengikuti ukuran huruf & rotasi layar.

### Bar Menu Baca
- Perbaikan bar **melayang di HP bergaya gesture-bar/berponi**: kompensasi
  safe-area dobel dihapus; bar bawah kini berjangkar rapat di tepi layar dengan
  latar menjulur ke area gestur.
- Bar atas diberi kompensasi poni/status-bar (siap mode fullscreen APK), dan di
  tablet/layar lebar bar kini menempel penuh tepi-ke-tepi.

### Pengaturan
- **Tanda Mushaf** (baru): tiga mode — Otomatis (deteksi per-kelompok berbasis
  pengukuran render nyata), Tampilkan, atau Sembunyikan — untuk mengatasi
  artefak lingkaran hitam pada perangkat yang memblokir font mushaf.
- **Garis mushaf**: opsi Garis Tampil / Tanpa Garis.
- **Preview hidup**: kotak pratinjau kini memperlihatkan efek semua pengaturan
  sekaligus (garis + posisinya, tanda mushaf, warna waqaf, perataan, font) dan
  digambar ulang setiap modal Pengaturan dibuka; posisi pratinjau IndoPak
  diperbaiki.
- **Status tombol aktif kini jelas** di semua grup (latar solid warna aksen +
  centang emas) — memperbaiki bug lama di mana pembersih global menghapus
  penanda "selected" grup Perataan/Garis/Tanda Mushaf.
- Blok informasi dipertegas menjadi "Sumber Data Al-Qur'an & Atribusi" dengan
  rincian data 6.236 ayat / 604 halaman.

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
