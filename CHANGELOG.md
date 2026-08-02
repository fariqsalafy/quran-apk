# Changelog — Al-Qur'an Digital

## v3.4.8 (Agustus 2026)

- **Fix: modal Jadwal Shalat tidak full width di layar lebar.**
  Modal ini satu-satunya yang punya `max-width:420px` inline (sisa desain
  lama) → di layar >420px muncul margin kiri-kanan, tidak sejajar dgn modal
  lain. Batas itu dihapus → ikut aturan umum: full width di HP, max-width
  560px hanya di tablet (≥768px).

## v3.4.7 (Agustus 2026)

- **Fix: kotak pemilihan lokasi tidak full width / tidak sejajar.**
  Kotak daftar hasil search (`#pm-city-list`) tidak punya `width:100%`
  eksplisit → tidak selebar input pencarian & setting-group lain. Kini
  `width:100%` + `box-sizing:border-box`. Item di dalamnya juga diubah ke
  `display:flex; align-items:center; justify-content:center` (emoji + nama
  kota benar-benar di tengah) dan item terakhir tanpa border bawah (anti
  garis dobel).

## v3.4.6 (Agustus 2026)

- **Fix: nama surat di modal Salin Ayat tidak konsisten dgn index.**
  Long-press ayat → modal menampilkan `QS. ${selectedAyah.n}` yang berasal
  dari `sNameEng` data API (ejaan Inggris: "Al-Faatiha", "Yaseen"). Kini
  memakai `SURAH_META` (ejaan Indonesia: "Al-Fatihah", "Yasin") — konsisten
  dengan daftar surat, header baca, tafsir, bookmark & teks copy.
- **Fix: search kota manual tidak menemukan kota di luar 53 daftar.**
  Database kota kini digabung: 53 lokal (dgn koordinat utk hisab) + 518
  kota/kabupaten dari API MyQuran (`/sholat/kota/semua`), di-cache di
  localStorage. Nama dinormalisasi ("KAB. WONOGIRI" → "Wonogiri"). Kota
  dari API tanpa koordinat: jadwal via API + cache 12 bln; fallback hisab
  menampilkan pesan jelas (bukan NaN) saat offline total.
- **Fix: tampilan dropdown hasil search kota** — item rata tengah, warna
  tema, hover, pemisah antar item, container berlatar, pesan "tidak
  ditemukan" di-center + saran.

## v3.4.5 (Agustus 2026)

- **Fix: ukuran teks "kembali" ke nilai lama setelah diubah.** Slider Ukuran
  Teks hanya punya `oninput` (live preview) tanpa menyimpan — nilai baru
  tersimpan hanya jika kebetulan ada aksi lain yang memicu saveData (toggle
  pengaturan, tutup reader). Kini slider punya `onchange="saveData()"`:
  begitu jari dilepas, nilai langsung tersimpan ke localStorage.

## v3.4.4 (Agustus 2026)

- **Fix: jadwal shalat hang saat offline / jaringan lambat.** `fetchMonthAPI`
  tidak punya timeout — saat offline atau jaringan lambat, fetch menunggu lama
  sebelum jatuh ke hisab lokal; prefetch 12 bulan berarti hingga 12 request
  hang paralel. Kini ada `AbortController` timeout 8 detik: request gagal
  cepat → langsung pakai cache/hisab. Ditemukan Agen-1 (workflow paralel 3
  agen, 2 Agustus 2026).

## v3.4.3 (Agustus 2026)

- **Fix: preview ukuran font tidak berubah saat slider digeser.** Cap 38px
  dari v3.4.2 membuat preview mati (default font 70px > 38px, jadi geser ke
  kanan tidak terlihat). Preview kini mengikuti slider penuh (20-120px);
  keamanan modal ditangani pengaman CSS `.font-preview` (`max-height:150px;
  overflow-y:auto`) — modal tidak akan pernah tertutup preview raksasa.
- Fix ini menggantikan pendekatan v3.4.2 (cap di JS) dengan pengaman di CSS.

## v3.4.2 (Agustus 2026)

- **Fix: preview font di Pengaturan menutupi modal.** Saat slider ukuran teks
  digeser besar (60-120px), kotak preview Arab membesar tanpa batas
  (`updateFontPreview` memakai `v` polos) dan area preview `flex-shrink:0`
  mendorong panel hingga 92vh — slider & tombol Tutup terdorong keluar layar
  (tidak bisa mengecilkan / keluar). Perbaikan:
  - `updateFontPreview` kini membatasi preview `Math.min(v, 38)` — konsisten
    dengan `applyConfig`.
  - `.font-preview` diberi `max-height: 150px; overflow-y: auto` sebagai
    pengaman.

## v3.4.1 (Agustus 2026)

- **Fix tutorial macet (stack)**: posisi ring/kartu dihitung setelah
  `scrollIntoView smooth` dengan `setTimeout 350ms` — di HP scroll smooth bisa
  >350ms sehingga koordinat elemen salah dan kartu keluar layar (tombol tak
  bisa disentuh). Kini: scroll instan (`behavior:auto`) + posisi dihitung
  setelah 2 frame (`requestAnimationFrame`) + polling elemen + clamp kartu
  selalu dalam layar.
- **Demo sample ayat**: langkah "Saat Membaca (1/2)" & "(2/2)" kini membuka
  contoh bacaan sungguhan (QS. Al-Kahf 18:60, hal. 300) dengan ayat
  ter-highlight — bukan sekadar kartu teks. Keluar dari langkah demo otomatis
  menutup reader & kembali ke menu.
- Fungsi reader (`initRead`, `closeReader`, `scrollToAyah`, `pageOfAyah`)
  diekspos ke `window` untuk keperluan tutorial.

## v3.4.0 (Agustus 2026)

- **Fitur baru: Tutorial / Tour interaktif** (vanilla JS, offline, tema app).
  - 12 langkah mencakup SEMUA fitur: jadwal shalat (lokasi + notif adzan),
    lanjutkan membaca, progres tilawah, pencarian & tab surah/juz, cara baca,
    navigasi ayat, tafsir/bookmark/salin/audio, pengaturan lengkap, tombol bantuan.
  - Muncul otomatis saat **pertama buka** dan saat **versi major naik**
    (3→4, dst — dikontrol konstanta `TUTORIAL_MAJOR`).
  - Tombol **?** di hero untuk membuka kembali kapan saja.
  - Highlight elemen dengan cincin emas + kartu penjelasan + titik progres +
    tombol Berikutnya/Lewati.

## v3.3.5 (Agustus 2026)

- **Fix hero jadwal tidak full-width**: `.hero-stats` masih `display: flex`
  (sisa desain stats bar 4 kolom) sehingga kartu menyusut ke lebar isi. Diubah
  ke `display: block; width: 100%` — kartu kini selebar hero.

## v3.3.4 (Agustus 2026)

- **Hero jadwal shalat dibersihkan**: baris lokasi/tanggal di atas dan teks
  "Metode Kemenag RI" di bawah dihapus — tampilan langsung panel jadwal
  (Berikutnya + countdown + 4 waktu lain) persis mockup varian C.

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
