#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ganti domain situs Desa Gondosuli di SELURUH file sekaligus.

Dipakai nanti saat pindah dari Vercel ke domain berbayar.
Yang ikut diganti: sitemap.xml, robots.txt, dan semua tag
canonical / og:url / og:image di 12 halaman HTML.

CARA PAKAI (buka Terminal di folder project ini):

    python ganti-domain.py https://desagondosuli.com

Tanpa argumen = mode pratinjau, cuma menampilkan apa yang akan berubah:

    python ganti-domain.py
"""

import sys
import re
import glob
import datetime

DOMAIN_LAMA = "https://gondosulifix.vercel.app"

TARGET = ["sitemap.xml", "robots.txt", "index.html"] + sorted(glob.glob("pages/*.html"))


def main():
    if len(sys.argv) < 2:
        print(f"Mode pratinjau — domain sekarang: {DOMAIN_LAMA}\n")
        total = 0
        for f in TARGET:
            try:
                n = open(f, encoding="utf-8").read().count(DOMAIN_LAMA)
            except FileNotFoundError:
                continue
            if n:
                print(f"  {f:34} {n} tautan")
                total += n
        print(f"\n  Total {total} tautan akan diganti.")
        print("  Jalankan lagi dengan domain baru, contoh:")
        print("      python ganti-domain.py https://desagondosuli.com")
        return

    baru = sys.argv[1].rstrip("/")
    if not baru.startswith("https://"):
        print("Domain harus diawali https:// — contoh: https://desagondosuli.com")
        sys.exit(1)

    total, diubah = 0, 0
    for f in TARGET:
        try:
            t = open(f, encoding="utf-8").read()
        except FileNotFoundError:
            continue
        n = t.count(DOMAIN_LAMA)
        if not n:
            continue
        open(f, "w", encoding="utf-8").write(t.replace(DOMAIN_LAMA, baru))
        print(f"  {f:34} {n} tautan diganti")
        total += n
        diubah += 1

    # tanggal <lastmod> di sitemap disegarkan sekalian
    try:
        s = open("sitemap.xml", encoding="utf-8").read()
        hari_ini = datetime.date.today().isoformat()
        s = re.sub(r"<lastmod>[^<]*</lastmod>", f"<lastmod>{hari_ini}</lastmod>", s)
        open("sitemap.xml", "w", encoding="utf-8").write(s)
        print(f"  sitemap.xml                        tanggal lastmod -> {hari_ini}")
    except FileNotFoundError:
        pass

    print(f"\nSelesai: {total} tautan di {diubah} file diganti ke {baru}")
    print("\nLangkah berikutnya:")
    print("  1. Upload semua file ke hosting baru")
    print(f"  2. Daftarkan {baru} di Google Search Console")
    print(f"  3. Kirim sitemap: {baru}/sitemap.xml")
    print("  4. Kalau domain Vercel lama masih aktif, arahkan (redirect 301) ke domain baru")
    print("\nJANGAN LUPA: ganti juga DOMAIN_LAMA di baris atas file ini,")
    print(f'             jadi DOMAIN_LAMA = "{baru}"')


if __name__ == "__main__":
    main()
