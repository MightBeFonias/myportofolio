# My Portfolio

Website ini akan berisi beberapa pengalaman, background academic, dan juga beberapa informasi lain yang terkait dengan saya pribadi.

## Identitas

- **Nama:** Fatih Naufal Habibillah
- **Nama Panggilan:** Opang
- **NPM:** 2506586394
- **Kelas:** PBP B
- **Prodi:** Ilmu Komputer

## Fitur

Sejauh ini, website ini baru berisi 2 section:

- About Me
Most likely ini berisi informasi pribadi seperti nama, NPM, social links, dan juga foto saya pribadi. Not much too say di section ini

- Highlights
Section ini berisi beberapa pengalaman atau achievements yang pernah saya peroleh dalam kehidupan saya pribadi. Disini saya bagi menjadi 3 sub-section yang terdiri dari:
    - Competitive Programming
    - Research
    - Experience

Disini juga user dapat melakukan expansion untuk mendapat informasi lebih detail terkait setiap event yang saya ikuti ataupun project yang saya kerjakan.

## Repo Structure

```text
myportofolio/
├── manage.py
├── portofolio/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── asgi.py
│   └── wsgi.py
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   ├── img/
│   │   └── Opang.png
│   └── docs/
│       └── lm-kbc-paper.pdf
├── requirements.txt
├── .gitignore
└── README.md
```

## Cara Run Website

Kalau mau run local for development reason, bisa ikuti beberapa step di bawah ini

### 1. Clone Repo

```bash
git clone <https://github.com/MightBeFonias/myportofolio.git>
cd myportofolio
```

### 2. Buat dan aktifkan virtual environment

For macOS or Linux:

```bash
python3 -m venv env
source env/bin/activate
```

For Windows:

```bash
python -m venv env
env\Scripts\activate
```

### 3. Install depedencies

```bash
pip install -r requirements.txt
```

### 4. Run Django check (Opsional)

```bash
python manage.py check
```

### 5. Start the development server

```bash
python manage.py runserver
```

Kalau mau review websitenya, bisa langsung aja buka [disini](fatih-naufal51-myportofolio.pws.cs.ui.ac.id)

### Tugas 1

1.  Ya, saya menggunakan beberapa elemen semantik HTML5 seperti `<header>`, `<main>`, `<section>`, `<article>`, `<footer>`, `<ul>`, `<li>`, `<details>`, dan `<summary>`.

    Elemen `<header>` digunakan untuk nav bar, sedangkan `<main>` membungkus konten utama halaman. Saya menggunakan `<section>` untuk memisahkan bagian Profile dan Highlights. Setiap kategori pada Highlights dibungkus menggunakan `<article>`.

    Saya juga menggunakan `<ul>` dan `<li>` untuk menyusun daftar pencapaian dan pengalaman. Elemen `<details>` dan `<summary>` digunakan untuk membuat setiap item dapat diexpand ketika pengguna ingin membaca informasi yang lebih detail terkait setiap event.

    Penggunaan elemen semantik membantu saya membangun struktur halaman yang lebih terorganisasi dan mudah dipahami. Dengan struktur HTML yang jelas, CSS juga menjadi lebih mudah dikelola karena setiap bagian memiliki tujuan yang spesifik.

2. Tantangan utama yang saya temukan adalah mempertahankan keseimbangan antara teks, foto profile, nav bar, dan daftar Highlights pada ukuran layar yang berbeda. Layout yang terlihat aman di desktop tidak selalu cocok dipakai pada mobile karena lebar layar lebih terbatas.

   Pada desktop, informasi profile dan foto ditampilkan dalam layout dua kolom menggunakan CSS Grid. Pada ukuran layar yang lebih kecil, layout tersebut diubah menjadi satu kolom agar teks dan foto tidak saling bertabrakan. Saya juga mengatur ulang ukuran heading, jarak antar bagian, lebar container, serta jarak antar item menggunakan media query.

   Dalam menentukan elemen yang perlu diprioritaskan, saya memastikan terlebih dahulu bahwa informasi utama seperti nama, bio, foto, navigation, dan kategori Highlights tetap terlihat jelas. Elemen visual tambahan seperti offset shadow dan hover effect dibuat lebih sederhana agar tidak mengganggu pengguna yang menggunakan layar kecil.

   Saya mengevaluasi hasilnya dengan menguji tampilan pada ukuran desktop, tablet, dan mobile. Jika teks terlalu panjang, item terlalu sempit, atau elemen keluar dari layar, saya menyesuaikan kembali `font-size`, `gap`, `padding`, `grid-template`, dan lebar container. Saya juga menggunakan unit responsif seperti `clamp()`, `min()`, dan persentase agar ukuran elemen tidak terlalu bergantung pada satu ukuran layar.

3. Batasan utama dari static web ini adalah seluruh konten masih ditulis langsung di dalam file HTML. Jika saya ingin menambahkan, mengubah, atau menghapus pencapaian dan pengalaman, saya harus mengubah source code secara manual.

   Selain itu, interaksi yang tersedia masih terbatas pada fitur native HTML dan CSS. Contohnya, item Highlights dapat dibuka menggunakan `<details>`, tetapi belum ada sistem untuk memfilter konten, mencari item tertentu, atau mengelola konten secara dinamis.

   Pada iterasi berikutnya, saya ingin menambahkan backend Django dengan database untuk menyimpan data project, achievements, skills, dan experiences. Saya juga ingin membuat halaman admin atau dashboard agar konten portfolio dapat dikelola tanpa mengubah file HTML secara langsung.

## AI Disclosure

Saat mengerjakan project ini, saya menggunakan Hermes Agent untuk membantu saya di beberapa bagian.

Bagian yang dibantu oleh Hermes:

- Membantu saya adjust color pallete dari web saya.
- Memperbaiki semantic structure dari code HTML saya
- Membantu saya mencari logo untuk social links
- Refactor CSS supaya tidak ada code yang redundan atau useless
- Menerapkan rule of 4 pada CSS saya
- Membantu saya mencari syntax CSS yang tepat jika saya kesulitan menemukannya di internet
- Membantu saya manifest Repo Structure untuk markdown README.md

Untuk tools/skills yang agent saya gunakan sendiri ada ponytail lite supaya code saya menjadi lebih singkat dan efisien, untuk strategi prompting sendiri saya selalu meminta agent saya untuk selalu menjaga fungsionalitas code saya sebelumnya saat melakukan refactor, saya biasa menggunakan prompt ini untuk refactor "pake ponytail lite buat bantu gw refactor code ini, jangan ubah fungsi code yang sebelumnya udah gw tulis cukup hapus line yang redundan atau useless supaya code gw jadi sesingkat dan seefisien mungkin". Kalo untuk syntax sendiri saya biasanya menyampaikan ide saya dalam bentuk prompt "saya ingin implementasi blabla" atau saya menggambar dulu di tldraw lalu saya screenshot dan kirim ke hermes terkait apa yang saya inginkan, lalu nanti hermes akan manifest syntaxnya.