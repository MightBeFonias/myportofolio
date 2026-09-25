# My Portfolio

Website ini akan berisi beberapa pengalaman, background academic, dan juga beberapa informasi lain yang terkait dengan saya pribadi.

## Identitas

- **Nama:** Fatih Naufal Habibillah
- **Nama Panggilan:** Opang
- **NPM:** 2506586394
- **Kelas:** PBP B
- **Prodi:** Ilmu Komputer

## Fitur

Website ini merupakan portofolio pribadi yang terdiri dari beberapa bagian dan fitur berikut:

- **About Me**
  Menampilkan informasi pribadi saya seperti nama, NPM, program studi, bio, social links, dan juga foto saya pribadi.

- **Experience**
  Menampilkan pengalaman saya beserta timeline dari experience terkait, bagian ini juga dilengkapi dengan deskripsi, kategori, periode waktu, dan status ongoing atau finished.

- **Awards & Achievements**
  Menampilkan pencapaian dalam bentuk card yang berisi tahun, nama event, result, deskripsi, dan gambar kalo misal ada foto pas event berlangsung.

- **Create Form**
  Pemilik Porto(Fatih) dapat menambahkan data Experience dan Award melalui form berbasis `ModelForm`.

- **Update Form**
  Data Experience dan Award yang sudah tersimpan dapat diubah oleh Editor atau Pemilik Porto(Fatih) melalui tombol Edit pada masing-masing card, jadi ga perlu delete terus create lagi dari 0 kalo mau update

- **Delete dengan Confirmation Modal**
  Pemilik Porto(Fatih) dapat menghapus data melalui tombol Delete, tapi ada double confirmation untuk mencegah deletion yang ga disengaja oleh Pemilik Porto(Fatih).

- **Search**
  Halaman Experience dan Awards menyediakan pencarian berdasarkan judul dari card terkait.

- **JSON Data Delivery**
  Data tersedia melalui endpoint berikut:
  - `/api/experiences/`
  - `/api/awards/`

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

### Tugas 4

1. ...

2. ...

3. ...

## AI Disclosure

Pada Tugas 4, saya tidak menggunakan AI sama sekali dalam seluruh tahapan pengerjaan saya, informasi yang saya dapatkan hanya berasal dari internet seperti stackoverflow, django docs, dll. Saya juga tak menggunakan AI Overview untuk mengerjakan Tugas 4.