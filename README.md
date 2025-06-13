# Tugas Besar PASD - Kelompok Lima Watt
Repository Tugas Besar Mata Kuliah PASD - Kelompok Lima Watt

## Deskripsi
Aplikasi Kasir Kita adalah program yang dirancang untuk membantu pelaku usaha dalam mengelola transaksi penjualan, stok barang, serta menghasilkan laporan penjualan secara otomatis. Dengan pendekatan Functional Programming (FP) dan Object-Oriented Programming (OOP), aplikasi ini memudahkan penggunanya dalam melakukan pencatatan pemesanan, pengelolaan stok barang, hingga pembuatan laporan penjualan.

## Functional Program
1. hitung_total_pemesanan(daftar_item):
   Menghitung total harga semua item dalam pemesanan.
2. analisis_tren_item(data_penjualan):
   Menentukan item yang paling banyak terjual dari data penjualan.

## Object-Oriented Program
1. class itemMenu:

   Mewakili sebuah item/menu yang dijual.

   Atribut: nama, jenis, harga, ukuran, stok

   Metode:
   1. tambahStok(jumlah)
   2. kurangiStok(jumlah)
   
3. class Pemesanan:

   Mencatat item-item yang dipesan oleh pelanggan.

   Atribut: daftar_item

   Metode:
   1. tambah_item(item, total)
   2. hitung_total()
   3. tampilkan_detail()
      
5. class Pembayaran
6. class ManajerStok
7. class LaporanPenjualan

## Fitur Utama
1. Pencatatan Pemesanan: Menambahkan item ke pesanan dan menghitung total otomatis.
2. Analisis Tren Penjualan: Menentukan produk terlaris dari data yang tercatat.
3. Manajemen Stok: Menambahkan atau mengurangi stok barang.
4. Cetak Struk dan Pembayaran: Mendukung berbagai metode pembayaran dan mencetak struk sederhana.
5. Laporan Penjualan: Menampilkan rekap jumlah barang terjual dan total pendapatan.
