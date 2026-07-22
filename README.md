# Al-Qur'an ABBS — Build APK Otomatis

**Versi 2.0.0** — riwayat perubahan lengkap ada di [CHANGELOG.md](CHANGELOG.md).

Aplikasi Al-Qur'an digital (IndoPak & Rasm Utsmani Madinah, offline penuh) yang
di-build menjadi APK Android secara otomatis oleh GitHub Actions. Tidak perlu
menginstal Android Studio.

## Cara pakai (sekali saja)

1. **Buat repository baru** di GitHub (misal `quran-apk`). Boleh Private.
2. **Upload seluruh isi folder ini** ke repo tersebut:
   - Lewat web: tombol *uploading an existing file* → tarik semua file & folder.
     Pastikan folder `.github/workflows/build-apk.yml` ikut terunggah
     (kalau lewat web, upload folder `.github` bisa dengan drag seluruh folder).
   - Atau lewat git:
     ```bash
     git init
     git add .
     git commit -m "Al-Quran ABBS v1"
     git branch -M main
     git remote add origin https://github.com/USERNAME/quran-apk.git
     git push -u origin main
     ```
3. Buka tab **Actions** di repo → workflow "Build APK" berjalan otomatis (± 5–10 menit).
4. Setelah hijau ✅, buka tab **Releases** → unduh `AlQuran-ABBS.apk`.
5. Kirim APK ke HP (WA/Drive), instal. Izinkan "instal dari sumber tidak dikenal".

Setiap kali file `www/index.html` diperbarui lalu di-push, APK baru otomatis
muncul di Releases.

## Kustomisasi

| Yang diubah | Di mana |
|---|---|
| Nama aplikasi di launcher | `appName` di `capacitor.config.json` |
| Package ID | `appId` di `capacitor.config.json` (ubah SEBELUM build pertama) |
| Ikon & splash | ganti `resources/icon.png` (1024×1024) & `resources/splash.png` (2732×2732) |
| Isi aplikasi | `www/index.html` |

## Catatan

- APK ini **debug/self-signed**: langsung bisa diinstal manual di HP mana pun,
  tapi belum bisa diunggah ke Play Store. Untuk Play Store perlu keystore +
  build AAB release (bisa ditambahkan ke workflow ini nanti).
- Semua data Al-Qur'an (teks Utsmani + IndoPak + font mushaf) sudah tertanam
  di `www/index.html`, jadi aplikasi berfungsi 100% tanpa internet.
  Internet hanya dipakai untuk fitur audio murottal.
