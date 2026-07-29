# Website Desa Gondosuli

Situs profil Desa Gondosuli, Kecamatan Pakuniran, Kabupaten Probolinggo, Jawa Timur.

Dibuat sebagai bagian dari kegiatan KKN. Situs ini berstatus **fondasi awal** — sudah siap dipakai
dan berisi data lapangan yang lengkap, tetapi belum memiliki panel admin. Penambahan konten baru
masih dilakukan dengan menyunting berkas HTML secara langsung.

Dokumen ini ditujukan untuk dua pembaca:

- **Bagian 1–3** untuk perangkat desa — apa yang dimiliki dan apa yang harus dijaga.
- **Bagian 4–8** untuk pengembang (programmer) yang nanti melanjutkan.

---

## 1. Apa saja isi situs ini

| Halaman | Berkas | Isi |
|---|---|---|
| Beranda | `index.html` | Profil desa, 6 kartu dusun, cuplikan informasi, peta, galeri, kontak |
| Profil Dusun | `pages/dusun.html` | Daftar 6 dusun |
| Detail dusun | `pages/dusun-*.html` | 6 halaman: Kletek, Pakes, Karangduwek, Durin, Ranon, Krajan |
| Informasi | `pages/informasi.html` | Daftar 34 artikel, dikelompokkan per kategori |
| Detail artikel | `pages/informasi-detail.html` | Isi lengkap artikel, dipanggil lewat `?id=` |
| Peta | `pages/peta.html` | Peta interaktif, 82 titik lokasi |
| Berita | `pages/berita.html` | **Belum jadi** — lihat Bagian 7 |

**34 artikel informasi**: Pertanian 6, Pendidikan 9, UMKM 8, Keagamaan 2, Kesehatan 3, Lainnya 6.

**82 titik peta**: UMKM 33, Pertanian 25, Pendidikan 12, Keagamaan 8, Kesehatan 3, Pemerintahan 1.

Seluruh teks artikel dan profil dusun disalin **verbatim** dari dokumen hasil pendataan lapangan.
Jangan diringkas atau diubah gaya bahasanya tanpa persetujuan penyusun aslinya.

---

## 2. Akun dan kepemilikan

Bagian ini yang paling penting saat serah terima. Isi tabel di bawah ini dan simpan di tempat aman.

| Layanan | Untuk apa | Didaftarkan atas email | Catatan |
|---|---|---|---|
| Domain | Alamat situs | _(isi)_ | Wajib diperpanjang tiap tahun |
| Hosting | Tempat situs disimpan | _(isi)_ | Wajib diperpanjang tiap tahun |
| GitHub | Penyimpan kode | _(isi)_ | `github.com/strawberaraa/websitegondosulifix` |
| Email desa | Kontak di situs | `desagondosuliprobolinggo@gmail.com` | Dipakai juga untuk pendaftaran layanan di atas |

**Tiga hal yang wajib dijaga perangkat desa:**

1. **Perpanjang domain dan hosting sebelum jatuh tempo.** Kalau domain telat diperpanjang, alamat
   situs bisa diambil orang lain dan sangat sulit diambil kembali.
2. **Simpan akses email desa.** Semua pemberitahuan tagihan dan perubahan akun masuk ke sana.
   Kalau email ini hilang aksesnya, domain dan hosting ikut sulit diurus.
3. **Akun harus atas nama desa**, bukan atas nama pribadi mahasiswa atau pihak ketiga.

Bila ke depan ingin memakai domain resmi `.desa.id` (gratis tahun pertama, lalu sekitar
Rp 55.000/tahun), pendaftarannya melalui perangkat desa dengan SK Kepala Desa dan surat permohonan,
diajukan di layanan Kementerian Komunikasi dan Digital.

---

## 3. Mengubah isi tanpa bantuan programmer

Tiga hal berikut relatif aman dikerjakan sendiri. Selalu **salin dulu berkasnya** sebagai cadangan
sebelum menyunting.

### Mengganti nomor telepon atau email kontak

Ada di **12 berkas** (`index.html` dan seluruh isi `pages/`). Cari tulisan `kontak-item`,
lalu ubah nomor atau emailnya. Harus diubah di semua berkas supaya seragam.

### Mengganti foto

Timpa berkas lama di folder `images/` dengan **nama berkas yang persis sama**.
Perhatikan huruf besar-kecil: di server, `Foto.jpg` dan `foto.jpg` dianggap dua berkas berbeda.

Ukuran foto sebaiknya maksimal 1600 piksel dan di bawah 700 KB. Foto langsung dari kamera
biasanya 5–7 MB dan akan membuat situs sangat lambat dibuka.

### Menambah artikel informasi

Ikuti panduan yang sudah ditulis sebagai komentar di bagian atas data artikel, di dalam
`pages/informasi-detail.html`. **Penting:** artikel harus ditambahkan di **dua berkas** sekaligus,
yaitu `pages/informasi.html` dan `pages/informasi-detail.html` (lihat Bagian 6).

---

## 4. Struktur berkas

```
.
├── index.html              Beranda (1.601 baris)
├── pages/                  11 halaman
├── css/
│   ├── style.css           Tata letak umum, navbar, beranda (1.300 baris)
│   ├── pages.css           Halaman dusun, kartu berita/artikel (760 baris)
│   └── artsy.css           Animasi daun, partikel, dekorasi (1.379 baris)
├── js/main.js              Navbar, menu HP, animasi muncul (146 baris)
├── images/                 106 berkas, ±31 MB (sudah dikompres)
├── images-asli/            Cadangan foto asli sebelum dikompres, ±183 MB
├── sitemap.xml             44 URL, untuk mesin pencari
├── robots.txt
├── ganti-domain.py         Alat bantu ganti domain (lihat Bagian 5)
└── websitegondosuli/       Salinan repo Git yang terhubung ke GitHub → Vercel
```

**Tanpa proses build.** HTML, CSS, dan JavaScript biasa. Tidak ada Node, npm, bundler, atau
basis data. Cukup unggah seluruh berkas ke `public_html`, situs langsung jalan.

Pustaka eksternal dimuat lewat CDN, hanya pada halaman peta:

- Leaflet 1.9.4 — peta 2D
- Leaflet.markercluster 1.5.3 — pengelompokan penanda
- MapLibre GL 5.24.0 — tampilan peta 3D

**Dua folder yang tidak perlu diunggah ke hosting:** `images-asli/` dan `websitegondosuli/`.

---

## 5. Deployment

Saat ini situs dideploy otomatis oleh **Vercel** dari repositori GitHub
`github.com/strawberaraa/websitegondosulifix` (branch `main`).

Repo tersebut berada di dalam subfolder `websitegondosuli/`, **terpisah dari folder kerja**.
Karena itu setiap selesai menyunting, isinya harus disalin dulu:

```bash
# dari folder utama
cp index.html sitemap.xml robots.txt websitegondosuli/
cp -r css js pages images websitegondosuli/

cd websitegondosuli
git add -A
git commit -m "keterangan perubahan"
git push
```

Kalau tidak disalin, perubahan tidak akan muncul di situs meskipun sudah di-push.
Susunan dua folder ini sebaiknya disederhanakan (lihat Bagian 7).

### Pindah ke hosting berbayar

Situs statis, jadi cukup diunggah ke `public_html` lewat cPanel. Aktifkan SSL agar alamatnya
menjadi `https://`.

Ada **79 alamat lengkap** yang tertulis langsung di dalam kode (tag canonical, `og:url`,
`sitemap.xml`, `robots.txt`). Jalankan skrip berikut **sebelum** mengunggah:

```bash
python ganti-domain.py                              # lihat dulu apa yang akan berubah
python ganti-domain.py https://desagondosuli.com    # jalankan penggantian
```

Setelah domain aktif: daftarkan di Google Search Console dan kirim `sitemap.xml`.

---

## 6. Cara kerja data

Tidak ada basis data. Semua konten disimpan sebagai array JavaScript di dalam berkas HTML.

### Artikel informasi — `CURATED_DATA`

Array berisi 34 artikel, dikelompokkan per kategori dengan pembatas komentar.
Bentuk satu artikel:

```js
{ id: 'kategori-nama-dusun', nama: 'Judul Artikel', cat: 'pertanian',
  dusun: 'Krajan', foto: 'images/NamaFoto.jpg',
  ringkas: 'Satu kalimat untuk kartu.',
  paragraf: [
    { img: 'images/Foto1.jpg', caption: 'Keterangan foto' },   // blok foto
    "Paragraf pertama...",                                      // blok teks
  ] }
```

`paragraf` boleh mencampur teks dan foto; urutannya persis seperti yang akan tampil, sehingga
tata letaknya bisa dibuat mengikuti dokumen aslinya. Bila blok foto pertama sama dengan `foto:`
utama, foto itu tidak ditampilkan dua kali — keterangannya dipindah ke bawah foto header.

> **Perhatian:** array ini **digandakan di dua berkas**, `pages/informasi.html` dan
> `pages/informasi-detail.html`, dan keduanya harus identik. Ini utang teknis yang paling
> mendesak dibereskan (lihat Bagian 7).

### Titik peta

Array 82 objek `{ nama, cat, dusun, lat, lng, elev, foto, deskripsi, telepon }`.
**Juga digandakan** di `index.html` dan `pages/peta.html`.

### Cuplikan di beranda

`index.html` punya array `ITEMS` tersendiri berisi ringkasan artikel untuk widget
"Informasi Seputar Desa" dan "Info Lainnya". Ini **salinan ketiga** dari sebagian data artikel.

---

## 7. Utang teknis dan batasan

Daftar ini sengaja ditulis apa adanya agar pengembang berikutnya tahu kondisi sebenarnya.

### Prioritas tinggi

**Data digandakan di beberapa berkas.** Artikel ada di 2 berkas, titik peta di 2 berkas, ringkasan
artikel di 1 berkas lagi. Setiap perubahan harus dilakukan di semua tempat, dan gampang jadi tidak
sinkron. Solusinya: pindahkan ke berkas `.json` terpisah lalu muat dengan `fetch()`, atau langsung
gunakan CMS.

**Belum ada panel admin.** Menambah konten berarti menyunting HTML. Ini penghalang terbesar bagi
perangkat desa. Pilihan yang masuk akal: CMS berbasis berkas seperti Decap CMS (dulu Netlify CMS)
yang bisa langsung menyunting isi repo GitHub, atau pindah ke WordPress bila ingin sepenuhnya
dikelola sendiri oleh desa.

**Susunan dua folder.** Folder kerja dan repo Git terpisah, sehingga perubahan pernah tidak
ikut ter-deploy. Sebaiknya folder utama itu sendiri yang dijadikan repo Git.

### Prioritas sedang

**Halaman berita belum jadi.** `pages/berita.html` masih berisi 5 berita contoh dengan foto dari
Unsplash, dan seluruh tautan "Baca Selengkapnya" mengarah ke berkas yang tidak ada
(`berita-tembakau-pakes.html` dan empat lainnya). Halaman ini juga tidak tertaut dari menu mana pun
dan sengaja tidak dimasukkan ke `sitemap.xml`. Pilihannya: diselesaikan, atau dihapus.

**Pratinjau tautan artikel di media sosial belum jalan.** Tag `og:` pada halaman artikel diisi
lewat JavaScript, sedangkan WhatsApp dan Facebook tidak menjalankan JavaScript. Akibatnya semua
artikel memakai pratinjau yang sama. Perbaikannya: buat berkas HTML terpisah per artikel, atau
gunakan server yang bisa merender di sisi server.

**`sitemap.xml` dibuat manual.** Setiap ada artikel baru, URL-nya harus ditambahkan sendiri.

### Prioritas rendah

- Nama berkas gambar memakai spasi dan tanda kurung. Tidak menimbulkan masalah saat ini, tetapi
  sebaiknya diseragamkan (huruf kecil, tanpa spasi) bila ada penataan ulang.
- 6 berkas gambar di folder `images/` tidak dipakai di halaman mana pun: `Bu Bidan.jpg`,
  `Kelompok Bermain Miftahul Hasanah.jpeg`, `LOGO DESA DONDOSULI (R).png`,
  `Perkebunan Tembakau (1).jpg`, `UMKM toko kelontong .jpg`, `lahantembakau.jpg`.
- Belum ada favicon lengkap untuk perangkat Apple dan belum ada `manifest.json`.

---

## 8. Hal yang perlu diketahui sebelum menyunting

**Huruf besar-kecil nama berkas.** Server hosting memakai Linux yang membedakan `Foto.jpg` dan
`foto.jpg`, sedangkan Windows tidak. Gambar bisa tampil normal di komputer tetapi kosong saat
online. Seluruh rujukan gambar saat ini sudah diperiksa dan cocok.

**Jangan pasang `overflow` pada `.nav-links` di tampilan desktop.** Menu dropdown memakai
`position: absolute`, sehingga akan ikut terpotong dan menu tidak bisa dibuka. Pembatasan ukuran
hanya boleh di dalam media query untuk tampilan HP, karena di sana dropdown-nya `position: static`.
Catatan ini juga ditulis langsung di `css/style.css`.

**Ukuran foto.** Sebelum dikompres, beranda memuat 50,8 MB sekali buka — sekitar dua menit pada
jaringan 3 Mbps. Setelah dikompres menjadi 3,5 MB. Jaga agar setiap foto tetap di bawah 700 KB.

**Teks konten bersifat verbatim.** Isi artikel dan profil dusun disalin apa adanya dari dokumen
pendataan lapangan, termasuk penulisan yang terlihat seperti salah ketik. Jangan diperbaiki
sepihak tanpa mengecek dokumen aslinya.
