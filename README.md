# Tugas Besar PASD - Kelompok Lima Watt
Repository Tugas Besar Mata Kuliah PASD - Kelompok Lima Watt

## Deskripsi
Aplikasi Kasir Kita adalah program yang dirancang untuk membantu pelaku usaha dalam mengelola transaksi penjualan, stok barang, serta menghasilkan laporan penjualan secara otomatis. Dengan pendekatan Functional Programming (FP) dan Object-Oriented Programming (OOP), aplikasi ini memudahkan penggunanya dalam melakukan pencatatan pemesanan, pengelolaan stok barang, hingga pembuatan laporan penjualan.

## Functional Program
FP adalah paradigma pemrograman yang berfokus pada penggunaan fungsi-fungsi murni (pure functions), di mana data bersifat immutable (tidak diubah setelah dibuat) dan tidak ada efek samping (side effect).
1. hitung_total_pemesanan(daftar_item):
   Menghitung total harga semua item dalam pemesanan.
2. analisis_tren_item(data_penjualan):
   Menentukan item yang paling banyak terjual dari data penjualan.

## Object-Oriented Program
OOP adalah pemrograman yang berfokus pada penggunaan objek—struktur yang menggabungkan data dan fungsi yang berkaitan—untuk membangun program yang modular, terorganisir, dan mudah dipelihara.

Prinsip OOP:
1. Encapsulation (Enkapsulasi)
   Enkapsulasi adalah proses menyatukan data (atribut) dan perilaku (fungsi/metode) ke dalam satu kesatuan objek, serta menyembunyikan data agar tidak bisa diakses langsung dari luar. Tujuannya
   adalah untuk menjaga keamanan data dan membatasi akses langsung ke atribut.

   |Contoh code dari enkapsulasi adalah:

   |class itemMenu:

   |def init(self, nama, harga):

   |self.nama = nama

   |self.__harga = harga # disembunyikan dari luar class


   Kenapa kode itemMenu termasuk prinsip enkapsulasi?

   Karena seluruh data penting seperti nama, jenis, harga, dan stok disimpan di dalam objek itemMenu, sehingga data tersebut tidak disebar bebas di luar class. Data ini hanya bisa diakses dan
   dimodifikasi melalui metode resmi seperti tambahStok() dan kurangiStok(). Dengan begitu, pengguna tidak bisa sembarangan mengubah nilai stok langsung (misalnya item.stok -= 5), melainkan
   harus mengikuti prosedur yang sudah disediakan oleh class. Selain itu, di dalam metode seperti kurangiStok(), terdapat proses validasi (pengecekan apakah stok mencukupi) sebelum data diubah
   Hal ini menunjukkan bahwa akses terhadap data dikendalikan dan diamankan, yang merupakan inti dari prinsip enkapsulasi.
   
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
