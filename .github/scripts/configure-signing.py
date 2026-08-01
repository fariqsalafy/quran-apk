#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Konfigurasi signing release + versionCode di build.gradle (dipanggil GitHub Actions)."""
import os, re, sys

p = 'app/build.gradle'
s = open(p, encoding='utf-8').read()

if 'signingConfigs' in s:
    print('signing sudah ada, skip')
    sys.exit(0)

inject = """
android {
    signingConfigs {
        release {
            storeFile file('../release.jks')
            storePassword System.getenv('KEYSTORE_PASS')
            keyAlias System.getenv('KEY_ALIAS')
            keyPassword System.getenv('KEY_PASS')
        }
    }
"""

# sisipkan setelah "android {" pertama
s = s.replace('android {', inject + 'android {', 1)

# arahkan buildType release ke signingConfig release
s = re.sub(
    r'release \{\s*\n\s*signingConfig signingConfigs\.debug',
    'release {\n            signingConfig signingConfigs.release',
    s, count=1)

# versionCode naik tiap build (agar Android mau update tanpa uninstall)
vc = os.getenv('VC', '100')
s = re.sub(r'versionCode \d+', 'versionCode ' + vc, s, count=1)

open(p, 'w', encoding='utf-8').write(s)
print('signing config OK, versionCode=' + vc)

# verifikasi
check = open(p, encoding='utf-8').read()
assert 'signingConfigs.release' in check, 'signingConfigs.release tidak ada!'
assert 'release.jks' in check, 'release.jks tidak ada!'
m = re.search(r'versionCode (\d+)', check)
assert m and m.group(1) == vc, 'versionCode tidak sesuai!'
print('verifikasi PASS')
