# Aplikasi Manajemen Data Mahasiswa

## Deskripsi Proyek
Aplikasi manajemen data mahasiswa adalah program Python sederhana yang memungkinkan pengguna untuk melakukan operasi dasar pada data mahasiswa, seperti menambah, menampilkan, menghapus, dan mengubah data.

## Fitur Utama
- Tambah data mahasiswa baru
- Tampilkan seluruh data mahasiswa
- Hapus data mahasiswa
- Ubah data mahasiswa (nama dan nilai)

## Algoritma Program

### Struktur Data
Program menggunakan struktur data `list` untuk menyimpan data mahasiswa, dimana setiap mahasiswa direpresentasikan sebagai `dictionary` dengan dua kunci:
- `'nama'`: Menyimpan nama mahasiswa
- `'nilai'`: Menyimpan nilai mahasiswa

### Alur Algoritma Utama
1. **Inisialisasi**
   - Membuat list kosong `mahasiswa` untuk menyimpan data

2. **Fungsi Tambah Data**
   - Menerima input nama dan nilai
   - Membuat dictionary baru dengan data mahasiswa
   - Menambahkan dictionary ke list `mahasiswa`

3. **Fungsi Tampilkan Data**
   - Memeriksa apakah list `mahasiswa` kosong
   - Jika tidak kosong, iterasi dan tampilkan setiap data mahasiswa
   - Jika kosong, tampilkan pesan "Tidak ada data mahasiswa"

4. **Fungsi Hapus Data**
   - Menerima nama mahasiswa yang akan dihapus
   - Gunakan list comprehension untuk membuat list baru tanpa mahasiswa tersebut
   - Update list `mahasiswa`

5. **Fungsi Ubah Data**
   - Menerima nama lama, nama baru, dan nilai baru
   - Cari mahasiswa berdasarkan nama lama
   - Ubah nama dan nilai mahasiswa yang sesuai

6. **Menu Utama**
   - Tampilkan pilihan menu
   - Terima input pengguna
   - Jalankan fungsi sesuai pilihan
   - Lakukan perulangan sampai pengguna memilih keluar

## Struktur Kode

### Variabel Global
```python
mahasiswa = []  # List untuk menyimpan data mahasiswa
```

### Fungsi-Fungsi Utama

#### `tambah(nama, nilai)`
- Parameter: nama mahasiswa dan nilai
- Menambahkan dictionary mahasiswa ke list
- Contoh: `tambah("Budi", 85)`

#### `tampilkan()`
- Menampilkan seluruh data mahasiswa
- Menangani kasus list kosong
- Mencetak nama dan nilai setiap mahasiswa

#### `hapus(nama)`
- Parameter: nama mahasiswa yang akan dihapus
- Menggunakan list comprehension untuk menyaring data
- Membuat list baru tanpa mahasiswa yang dimaksud

#### `ubah(nama_lama, nama_baru, nilai_baru)`
- Parameter: nama lama, nama baru, dan nilai baru
- Mencari mahasiswa dengan nama lama
- Memperbarui nama dan nilai mahasiswa

#### `menu()`
- Fungsi utama untuk menjalankan program
- Loop tak terbatas menampilkan pilihan menu
- Menerima dan memproses input pengguna
- Memanggil fungsi sesuai pilihan

## Contoh Penggunaan

```python
# Menambah data mahasiswa
tambah("Budi", 85)
tambah("Ani", 90)

# Tampilkan data
tampilkan()  # Akan menampilkan data Budi dan Ani

# Hapus data
hapus("Budi")

# Ubah data
ubah("Ani", "Ani Susanti", 95)
```

## Kompleksitas Algoritma

1. **Tambah Data**: O(1)
   - Operasi konstan, menambah elemen di akhir list

2. **Tampilkan Data**: O(n)
   - Iterasi seluruh list mahasiswa

3. **Hapus Data**: O(n)
   - Membuat list baru dengan filtering

4. **Ubah Data**: O(n)
   - Mencari mahasiswa dengan iterasi list

## Batasan dan Catatan
- Data disimpan hanya selama program berjalan
- Tidak ada validasi input yang kompleks
- Nama mahasiswa bersifat unik untuk operasi

## Pengembangan Lanjutan
- Validasi input
- Penyimpanan data ke file
- Fitur sorting dan filtering
- Antarmuka grafis (GUI)

## Persyaratan
- Python 3.x

## Cara Menjalankan
```bash
python manajemen_mahasiswa.py
```

**Arfianda F. Satritama**