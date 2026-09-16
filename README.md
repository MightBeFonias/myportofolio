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

### Tugas 3

1. `ModelForm` digunakan karena Django dapat membuat field form berdasarkan model secara otomatis. Dengan begitu, definisi field, tipe data, validasi dasar, dan proses penyimpanan tetap konsisten dengan model database. Pada proyek ini, `ExperienceForm` dan `AwardForm` digunakan untuk proses create dan update, sehingga saya tidak perlu menulis ulang input serta validasinya secara manual di HTML.

   `{% csrf_token %}` wajib ditambahkan pada form yang mengirim request `POST` untuk mencegah Cross-Site Request Forgery (CSRF). Token ini memastikan request perubahan data berasal dari halaman dan sesi yang valid. Pada proyek ini, token CSRF digunakan pada form create, update, dan delete.

2. JSON lebih sering dipilih dalam pengembangan web modern karena sintaksnya lebih ringkas, mudah dibaca manusia, dan mudah diproses oleh JavaScript maupun bahasa pemrograman lain. JSON juga memiliki struktur yang langsung merepresentasikan object dan array, sehingga cocok digunakan untuk pertukaran data antara server dan client.

   XML tetap berguna untuk kebutuhan tertentu, tetapi umumnya membutuhkan lebih banyak markup dan lebih verbose untuk merepresentasikan data yang sama. Karena itu, JSON digunakan pada endpoint data proyek ini, yaitu `/api/experiences/` dan `/api/awards/`.

3. Saat endpoint JSON dipanggil, view mengambil data `Experience` atau `Award` dari database dan menerapkan filter judul jika parameter `title` diberikan. Data QuerySet tersebut kemudian diubah menjadi JSON menggunakan `serializers.serialize("json", ...)` dan dikembalikan melalui `HttpResponse` dengan content type `application/json`.

   Serialization diperlukan karena object model dan QuerySet Django bukan format data yang dapat langsung dikirim sebagai response JSON. Proses ini mengubah object tersebut menjadi representasi data yang dapat dikirim melalui HTTP dan diproses oleh client. Pada halaman Experience dan Awards, response JSON tersebut juga dideserialisasi kembali menjadi object Django sebelum diberikan ke template untuk ditampilkan.

## AI Disclosure

Pada Tugas 3, saya menggunakan Hermes Agent sebagai AI assistant. Saya tetap menentukan fitur yang dibutuhkan, memilih desain dan struktur data, memberikan arahan perubahan, mereview kode, serta memutuskan perubahan yang digunakan dalam repository.

Bagian yang dibantu oleh Hermes Agent:

- Membantu saya memeriksa checklist Tugas 3 apakah sudah selesai atau belum? apakah ada yang terlewat atau tidak?.
- Menganalisis struktur proyek Django dan mencocokkannya dengan target Tugas 3.
- Membantu mengimplementasikan alur update Award dengan menduplikasi workflow yang digunakan saat implementasi update Experience
- Membantu menyusun tombol Edit serta Delete secara berdampingan dengan warna yang berbeda.
- Membantu mempertahankan confirmation modal delete dan memperbaiki styling action card agar konsisten pada halaman Experience dan Awards.
- Membantu menganalisis masalah migration production ketika kolom `Award.id` di PWS masih bertipe `bigint`, sedangkan model terbaru menggunakan UUID, lalu menyusun migration korektif `0003_award_uuid_primary_key.py`.
- Membantu menambahkan test untuk alur update dan keberadaan tombol Edit pada halaman.
- Membantu melakukan verifikasi menggunakan `manage.py check`, `manage.py test`, `makemigrations --check --dry-run`, `showmigrations`, dan `git diff --check`.
- Membantu membaca dan menelusuri hubungan antara `models.py`, `forms.py`, `views.py`, `urls.py`, template, migration, dan stylesheet sebelum perubahan dibuat.
- Membantu memastikan halaman Experience dan Awards tetap menggunakan inheritance dari `base.html` dan tidak kembali menjadi template standalone.
- Membantu memeriksa implementasi Create Form untuk Experience dan Award, termasuk field, widget tanggal, URL submit, validasi, CSRF, dan redirect setelah data tersimpan.
- Membantu memeriksa JSON endpoint Experience dan Award, termasuk response `application/json`, filtering berdasarkan parameter `title`, dan kesesuaian route yang digunakan.
- Membantu memastikan hasil deserialization dari response JSON benar-benar digunakan untuk menampilkan data pada halaman, bukan kembali mengambil QuerySet secara langsung untuk context.
- Membantu menambahkan dan memeriksa empty state ketika belum ada Experience atau Award di database.
- Membantu memperbaiki fixture test Experience agar field `started_at` yang wajib tidak menyebabkan `IntegrityError`.
- Membantu memeriksa tombol Delete, confirmation modal, form `POST`, CSRF token, endpoint delete, dan redirect setelah data dihapus.
- Membantu merapikan selector CSS yang memiliki desain sama menjadi class shared seperti `.collection-action`, `.collection-search`, dan action card bersama.
- Membantu memastikan perubahan UI tidak mengubah logic backend yang tidak berkaitan, termasuk model, endpoint JSON, dan behavior filtering.
- Membantu memeriksa responsive layout agar tombol action tetap dapat digunakan pada layar mobile.
- Membantu menganalisis masalah stylesheet yang terlihat tidak berubah, termasuk pemeriksaan URL CSS, cache-busting, server lokal, dan perbedaan antara local environment dengan PWS.
- Membantu menyusun urutan commit dan push secara terpisah berdasarkan fitur agar perubahan lebih mudah direview dan direvert.

Strategi prompting yang digunakan adalah memberikan konteks file, error, screenshot, dan target perubahan secara spesifik. Untuk perubahan UI, saya meminta agar perubahan tetap mengikuti class shared yang sudah ada, tidak mengubah logic yang tidak berkaitan, dan generalize transition `0.4s` untuk hover. Untuk debugging migration, saya memberikan pesan error production dan membandingkannya dengan model serta migration di repository.

Output AI tidak langsung digunakan tanpa pemeriksaan. Saya melakukan review manual terhadap view, URL, form, template, migration, CSS, dan test. Saya juga menjalankan test suite secara lokal dan melakukan pengecekan endpoint production. Keterbatasan AI adalah AI tidak dapat menjamin bahwa schema database production sudah sama hanya berdasarkan file migration di repository, sehingga status migration PWS tetap perlu diverifikasi langsung pada environment production.