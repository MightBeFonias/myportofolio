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

### Tugas 2

1. Ketika pengguna membuka halaman Awards, browser mengirimkan request ke URL `/awards/`. Request tersebut pertama kali diterima oleh `portofolio/urls.py`, yaitu URL configuration utama proyek. URL configuration ini meneruskan request ke `main/urls.py` melalui `include()`.

   Di `main/urls.py`, pola URL `awards/` diarahkan ke view `show_awards`. View tersebut mengambil data menggunakan `Award.objects.all()` dari model `Award`, lalu memasukkan data tersebut ke dalam context dengan key `awards`. Setelah itu, view memanggil `render()` untuk menggabungkan context dengan template `templates/awards.html`.

   Template kemudian melakukan perulangan terhadap data `awards`. Setiap object Award ditampilkan sebagai card yang berisi tahun, judul, recognition, deskripsi, dan foto jika tersedia. Jika database belum memiliki data Award, template menampilkan pesan empty state. Hasil HTML yang sudah dirender kemudian dikirim kembali oleh Django sebagai response dan ditampilkan oleh browser.

2. Data untuk bagian portofolio baru sebaiknya disimpan pada model karena model memisahkan data dari tampilan. Jika data ditulis langsung di dalam template, setiap perubahan judul, deskripsi, tanggal, atau foto mengharuskan saya mengubah source code HTML secara manual.

   Dengan model `Award`, data dapat dikelola sebagai record database dan template hanya bertanggung jawab menampilkan data tersebut. Pendekatan ini membuat maintenance lebih gampang, mengurangi duplikasi, dan memungkinkan penambahan banyak award tanpa mengubah struktur template.

3. `makemigrations` membandingkan perubahan pada `models.py` dengan migration yang sudah ada, lalu membuat file migration baru yang berisi instruksi perubahan skema database. `migrate` menjalankan instruksi tersebut pada database yang digunakan oleh proyek.

   Contohnya, ketika model `Award` ditambahkan, saya perlu menjalankan `makemigrations` untuk membuat migration yang membuat tabel Award. Setelah itu, saya menjalankan `migrate` agar tabel tersebut benar-benar dibuat di database. Hal yang sama berlaku ketika field baru seperti `image` ditambahkan ke model Award.

## AI Disclosure

Pada Tugas 2, saya menggunakan Hermes Agent sebagai AI assistant untuk membantu saya. Saya tetap menentukan fitur yang dibuat, memberikan arahan terhadap perubahan, mereview ulang hasilnya, dan melakukan verifikasi terhadap hasilnya.

Bagian yang dibantu oleh Hermes Agent:

- Membantu menganalisis struktur proyek Django yang sudah ada, termasuk `models.py`, `views.py`, `urls.py`, template, stylesheet, dan test yang relevan sebelum perubahan dilakukan.
- Membantu menyusun field model Award yang diperlukan, yaitu `title`, `recognition`, `description`, `awarded_at`, dan `image`, agar informasi achievement dapat dikelola sebagai data database.
- Membantu menyusun tampilan card Awards menggunakan CSS, termasuk frame `var(--alternative)`, background `var(--paper)`, placeholder `PHOTO COMING SOON`, layout responsif, dan penyesuaian font agar konsisten dengan halaman lain.
- Membantu merapikan CSS menggunakan pendekatan Ponytail dengan menghapus deklarasi redundant, menggabungkan selector yang memiliki style sama, dan mempersingkat kode tanpa mengubah logic atau layout yang sudah disepakati.
- Membantu menyesuaikan navbar agar menggunakan native HTML `<details>` dan `<summary>` tanpa JavaScript tambahan.
- Membantu menulis dan menyesuaikan test untuk memastikan halaman Awards membaca data dari database, menampilkan placeholder foto, dan tetap menggunakan navigasi native.
- Membantu melakukan verifikasi menggunakan `manage.py check`, test Django, pengecekan `git diff --check`, pemeriksaan migration, dan pengecekan bahwa file static dapat diakses.

Strategi prompting yang digunakan adalah memberikan konteks file dan tujuan perubahan secara spesifik, lalu meminta AI untuk mempertahankan fungsionalitas yang sudah ada. Untuk refactor CSS, saya menggunakan pendekatan Ponytail dengan instruksi agar kode dipersingkat, selector redundant dihapus, dan logic atau layout tidak diubah. Semua perubahan tetap saya review dan validasi sebelum digunakan.