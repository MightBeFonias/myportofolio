# My Portfolio

Portofolio pribadi berbasis Django dan Django REST Framework yang memuat profil, pengalaman, serta penghargaan dan pencapaian.

## Identitas

| | |
| --- | --- |
| Nama | Fatih Naufal Habibillah |
| Nama panggilan | Opang |
| NPM | 2506586394 |
| Kelas | PBP B |
| Program studi | Ilmu Komputer |

## Fitur

- **Profile** (`/`) memuat bio, foto, tautan sosial, dan informasi akademik.
- **Experience** (`/experience/`) menampilkan timeline dengan kategori, periode, dan status *Ongoing* atau *Finished*.
- **Awards & Achievements** (`/awards/`) menampilkan kartu dengan judul, penghargaan, deskripsi, tahun, dan gambar opsional.
- Experience dan Awards memuat data dari API DRF. Pencarian judul memakai *debounce* 300 ms dan menampilkan status memuat, hasil kosong, atau gagal memuat.
- Form tambah memakai modal. Star, unstar, dan hapus berjalan lewat AJAX. Tombol hapus meminta konfirmasi sebelum mengirim request.
- Tombol Edit membuka halaman form yang sudah ada. **Save Changes** mengirim `PATCH` melalui `fetch()` dan menampilkan hasilnya lewat toast. Setelah simpan, halaman Edit tetap terbuka.

## API

| Operasi | Metode | Experience | Awards |
| --- | --- | --- | --- |
| Daftar dan pencarian | `GET` | `/api/v1/experience/?title=kata` | `/api/v1/awards/?title=kata` |
| Tambah | `POST` | `/api/v1/experience/` | `/api/v1/awards/` |
| Detail, ubah, dan hapus | `GET`, `PUT`, `PATCH`, `DELETE` | `/api/v1/experience/<uuid>/` | `/api/v1/awards/<uuid>/` |
| Star dan unstar | `POST` | `/api/v1/experience/<uuid>/star/` | `/api/v1/awards/<uuid>/star/` |

Parameter `title` opsional. Pencarian cocok dengan sebagian judul tanpa membedakan huruf besar dan kecil. Endpoint daftar dan detail bisa dibuka lewat Browsable API.

### Izin akses

| Peran | Baca dan cari | Star | Edit | Tambah dan hapus |
| --- | --- | --- | --- | --- |
| Pengunjung | Ya | — | — | — |
| Pengguna login | Ya | Ya | — | — |
| Editor | Ya | Ya | Ya | — |
| Pemilik (superuser) | Ya | Ya | Ya | Ya |

Izin daftar dan detail diatur oleh `IsPortfolioOwnerOrEditorOrReadOnly`. Endpoint star mewajibkan login dan selalu memakai akun dari `request.user`. API memakai `SessionAuthentication`. Request yang mengubah data dari halaman menyertakan header `X-CSRFToken`.

Serializer mencantumkan field secara eksplisit dan membersihkan input teks dengan `strip_tags`. `star_count`, `is_starred`, dan `starred_by_names` bersifat *read-only*. Respons memuat username pemberi star tanpa email atau password hash. Kartu yang dirender lewat JavaScript melakukan *escaping* pada nilai teks sebelum memasukkannya ke HTML.

Respons sukses mencakup `201` untuk tambah, `200` untuk baca, edit, dan star, serta `204` untuk hapus. Input salah mendapat `400`, tindakan tanpa izin mendapat `403`, dan record yang tidak ditemukan mendapat `404`. Endpoint JSON lama `/api/experiences/` dan `/api/awards/` tetap tersedia.

## Struktur repo

```text
myportofolio/
├── manage.py
├── requirements.txt
├── main/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── api_views.py
│   ├── api_urls.py
│   ├── migrations/
│   ├── tests.py
│   └── tests_api.py
├── portofolio/
│   ├── settings.py
│   └── urls.py
├── templates/
│   ├── experience.html
│   ├── awards.html
│   ├── form_experience.html
│   ├── form_award.html
│   └── components/
└── static/
    ├── css/
    ├── docs/
    ├── img/
    └── js/
```

## Menjalankan proyek secara lokal

```bash
git clone https://github.com/MightBeFonias/myportofolio.git
cd myportofolio
```

Buat dan aktifkan virtual environment di macOS atau Linux.

```bash
python3 -m venv env
source env/bin/activate
```

Untuk Windows PowerShell, gunakan perintah berikut.

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

Install dependency, jalankan migrasi, lalu buka server lokal.

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Buka [portofolio lokal](http://127.0.0.1:8000/), [API Experience](http://127.0.0.1:8000/api/v1/experience/), atau [API Awards](http://127.0.0.1:8000/api/v1/awards/). Konfigurasi lokal memakai SQLite secara default.

Untuk mencoba operasi pemilik di database lokal, buat akun dengan `python manage.py createsuperuser`, lalu login lewat `/login/`. Untuk mencoba peran Editor, masukkan akun biasa ke grup `Editor` lewat Django Admin.

## Pengujian

Jalankan seluruh tes aplikasi atau hanya suite API.

```bash
python manage.py test main
python manage.py test main.tests_api
```

Suite aplikasi mencakup 14 tes halaman dan endpoint lama serta 26 tes API Experience dan Awards. Tes API mencakup akses publik, pencarian, validasi, operasi pemilik, penolakan perubahan oleh pengunjung dan pengguna biasa, keberhasilan `PATCH` oleh Editor, star, dan CSRF dengan autentikasi sesi.

## Deployment PWS

Situs dikonfigurasi untuk [origin HTTPS PWS](https://fatih-naufal51-myportofolio.pws.cs.ui.ac.id/). Origin tersebut tercantum di `CSRF_TRUSTED_ORIGINS`. Saat `PRODUCTION=True`, Django memakai PostgreSQL dengan pengaturan database dari environment.

Setelah deploy, cek daftar API, login, dan satu operasi tulis melalui situs. Simpan konfigurasi dan kredensial di environment deployment. Folder `env/`, database `db.sqlite3`, serta file `.env` dan `.env.prod` diabaikan Git.

### Tugas 6

1. REST (Representational State Transfer) adalah gaya arsitektur untuk merancang web API, bukan library atau format data. API yang mengembalikan JSON belum tentu RESTful. Yang menentukan adalah cara API tersebut diatur. PUT mengirim representasi pengganti, dengan seluruh field wajib. PATCH mengirim hanya field yang ingin diubah. Gunakan Patch jika ingin mengubah sebagian data saja dan gunakan PUT kalau ingin mengubah secara keseluruhan.

2. Pada GET, serializer mengubah objek model menjadi tipe data Python yang dapat dirender ke JSON (serialization). Pada POST/PATCH, serializer mengubah input menjadi data yang sudah divalidasi dan siap disimpan (deserialization). Di Tutorial 05, kita merakit bentuk yang sama secara manual. Sekarang rest_framework.serializers membantu mendefinisikan kontrak data sekaligus validasinya.

3. Autentikasi menjawab siapa kamu, sedangkan otorisasi menjawab apa yang boleh kamu lakukan. Di DRF, keduanya dipisahkan: authentication class mengisi request.user, lalu permission class memutuskan apakah request boleh diteruskan. Menyembunyikan tombol hanya mengubah tampilan. Pengguna masih bisa mengirim request langsung ke endpoint lewat Console atau klien HTTP. Permission class memeriksa setiap request di server sebelum kode view dijalankan, sehingga tindakan tanpa izin tetap ditolak dengan 403.

4. Browser dapat menyertakan cookie sesi secara otomatis. Cookie itu membantu server mengenali akun, tetapi tidak membuktikan bahwa pengguna sengaja mengirim permintaan yang mengubah data. Karena itu, POST, PUT, PATCH, dan DELETE dari pengguna yang terautentikasi lewat sesi tetap perlu token CSRF. force_authenticate() menetapkan pengguna langsung untuk menguji izin akses. Cara itu melewati alur login dan autentikasi sesi yang perlu diuji untuk membuktikan perlindungan CSRF.

## AI Disclosure

Pada Tugas 6, saya menggunakan Codex untuk melakukan beberapa automasi, automasi yang saya lakukan meliputi beberapa hal, yakni:
- Menyesuaikan unittest supaya cocok dengan codebase Tugas 6 saya sekarang.
- Memeriksa apakah codebase saya sudah memenuhi checklist pada Tugas 6.
- Memeriksa apakah ada bug pada codebase saya.
- Menyesuaikan README.md sebelum pertanyaan Reflektif supaya sesuai dengan current state dari codebase saya.

Untuk strategi prompting, saya selalu memberi constraints terhadap Codex supaya tidak mengubah file lain selain main/api_tests.py sehingga tidak terjadi perubahan yang tidak diinginkan