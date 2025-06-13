# Tugas Besar PASD - Kelompok Lima Watt
Repository Tugas Besar Mata Kuliah PASD - Kelompok Lima Watt

## Deskripsi
KasirKita merupakan aplikasi kasir digital yang dibangun menggunakan Python dan Streamlit. Aplikasi ini tidak hanya menangani proses transaksi penjualan di restoran, tetapi juga mengelola stok barang, mencatat laporan, dan bahkan menganalisis perilaku pelanggan dengan bantuan model machine learning. Proyek ini menggabungkan paradigma Object-Oriented Programming (OOP) dan Functional Programming (FP), serta menggunakan algoritma Random Forest untuk prediksi pelanggan churn.

## Dataset
1. Cleaned_200_Price_Data_Final.csv:
   Dataset ini merupakan data dummy yang akan dijadikan data test, dengan informasi:
   1. Item: Nama menu
   2. Category: Kategori menu (Makananan/Minuman)
   3. Price: Harga menu
   4. 
3. Clean_Data_Restaurant_Final.csv:

## Functional Program
FP adalah paradigma pemrograman yang berfokus pada penggunaan fungsi-fungsi murni (pure functions), di mana data bersifat immutable (tidak diubah setelah dibuat) dan tidak ada efek samping (side effect).

Prinsip FP:
1.  Pure Function (Fungsi Murni) adalah fungsi yang selalu memberikan output yang sama untuk input yang sama dan tidak menghasilkan efek samping (side effect) seperti mengubah data di luar dirinya.
2.  Immutability (Data Tidak Bisa Diubah) adalah prinsip di mana data tidak diubah setelah dibuat. Jika kamu ingin mengubah data, maka kamu harus membuat salinan/modifikasi baru, bukan mengubah nilai aslinya.
3.  Higher-Order Function (Fungsi Tingkat Tinggi) function adalah fungsi yang menerima fungsi lain sebagai argumen, atau mengembalikan fungsi sebagai hasil. Ini memungkinkan kita untuk membuat logika yang lebih fleksibel dan reusable.
   

Fungsi yang dipakai:
1. hitung_total_pemesanan(daftar_item):
   Menghitung total harga semua item dalam pemesanan.
2. analisis_tren_item(data_penjualan):
   Menentukan item yang paling banyak terjual dari data penjualan.

## Object-Oriented Program
OOP adalah pemrograman yang berfokus pada penggunaan objek—struktur yang menggabungkan data dan fungsi yang berkaitan—untuk membangun program yang modular, terorganisir, dan mudah dipelihara.

Prinsip OOP:
1. Encapsulation (Enkapsulasi) adalah proses menyatukan data (atribut) dan perilaku (fungsi/metode) ke dalam satu kesatuan objek, serta menyembunyikan data agar tidak bisa diakses langsung dari luar. Tujuannya
   adalah untuk menjaga keamanan data dan membatasi akses langsung ke atribut.

2. Inheritance (Pewarisan) adalah prinsip OOP yang memungkinkan sebuah class (anak/turunan) mewarisi atribut dan metode dari class lain (induk).
3. Polymorphism (Polimorfisme) adalah prinsip OOP yang memungkinkan satu nama metode digunakan oleh banyak class, tapi perilakunya bisa berbeda tergantung objeknya.
4. Abstraction (Abstraksi) adalah prinsip OOP yang menyembunyikan detail teknis dari suatu objek dan hanya menampilkan bagian penting yang perlu diketahui pengguna.
   
Fungsi yang dipakai:
1. class itemMenu: Mewakili sebuah item/menu yang dijual.

   Atribut: nama, jenis, harga, ukuran, stok

   Metode:
   1. tambahStok(jumlah)
   2. kurangiStok(jumlah)
   
3. class Pemesanan: Mencatat item-item yang dipesan oleh pelanggan.

   Atribut: daftar_item

   Metode:
   1. tambah_item(item, total)
   2. hitung_total()
   3. tampilkan_detail()
      
5. class Pembayaran: Menangani proses pembayaran.

   Atribut: metode

   Metode:
   1. proses_pembayaran(total)
   2. cetak_struk(pemesanan)
      
7. class ManajerStok: Memperbarui stok barang setelah transaksi.

   Metode:
   1. update_stok_barang(pemesanan, nama_item, jumlah, operasi)
      
9. class LaporanPenjualan: Mencatat dan menampilkan laporan penjualan.

    Atribut: data_penjualan

   Metode:
   1. catat_penjualan(pemesanan)
   2. tampilkan_laporan()

## Fitur Utama
1. Pencatatan Pemesanan: Menambahkan item ke pesanan dan menghitung total otomatis.
2. Analisis Tren Penjualan: Menentukan produk terlaris dari data yang tercatat.
3. Manajemen Stok: Menambahkan atau mengurangi stok barang.
4. Cetak Struk dan Pembayaran: Mendukung berbagai metode pembayaran dan mencetak struk sederhana.
5. Laporan Penjualan: Menampilkan rekap jumlah barang terjual dan total pendapatan.
