##Functional Programming

def hitung_total_pemesanan(daftar_item):
    total = 0
    for i in daftar_item:
        total += i['item'].harga* i['jumlah']
    return total

def analisis_tren_item(data_penjualan):
    penjualan ={}
    for i in data_penjualan:
        nama = i['item'].nama
        jum = i['jumlah']
        if nama in penjualan:
            penjualan[nama] += jum
        else:
            penjualan[nama] = jum
    
    item_terlaris = max(penjualan, key=penjualan.get)
    return item_terlaris

#Object Oriented Programming

class itemMenu:
    def __init__(self,nama,jenis,harga,stock):
        self.nama=nama
        self.jenis=jenis
        self.harga=harga
        self.stok=stock
    
    def tambahStok(self,jumlah):
        self.stok += jumlah
        print(f"Stok {self.nama} bertambah {jumlah}. Total: {self.stok}")
    
    def kurangiStok(self,jumlah):
        if self.stok >= jumlah:
            self.stok -= jumlah
            print(f"Stok {self.nama} berkurang {jumlah}. Stok sekarang: {self.stok}")
            return True
        else:
            print("Stok Tidak Cukup!, (Tersedia: {self.stock}, Diminta: {jumlah})")
            return False
    
class Pemesanan:
    def __init__(self):
        self.daftar_item =[]

    def tambah_item(self, item, jumlah):
        if item.stok >= jumlah:
            self.daftar_item.append({'item':item, 'jumlah':jumlah})
            print(f"{item.nama} sejumlah {jumlah} ditambahkan ke pesanan")
            return True
        else:
            print(f"Tidak dapat menambahkan {item.nama}")
            return False
        
    def hitung_total(self):
        total = 0
        for i in self.daftar_item:
            total += i['item'].harga * i['jumlah']
        return total

    def tampilkan_detail(self):
        print('\n--- Detail Pemesanan ---')
        if not self.daftar_item:
            print("Pemesanan Kosong\n")
            return 
        for i in self.daftar_item:
            item = i['item']
            jumlah = i['jumlah']
            print(f'{item.nama} x {jumlah} = Rp.{item.harga * jumlah}')
        
        total = self.hitung_total()
        print('-'*10)
        print(f"Total Pembelian: Rp.{total}")
        print('-'*10)

class Pembayaran:
    def __init__(self, metode_pembayaran):
        self.metode = metode_pembayaran

    def proses_pembayaran(self,total):
        print(f"Pembayaran sebesar Rp.{total} menggunakan {self.metode} berhasil!")
        return True
        
    def cetak_struk(self,pemesanan):
        print("\n====== STRUK PEMBELIAN ======")
        pemesanan.tampilkan_detail()
        print(f"Metode Pembayaran: {self.metode}")
        print("="*27)

class ManajerStok:
    def update_stok(self, item_obj, jumlah, operasi):
        if operasi == "kurangi":
            return item_obj.kurangiStok(jumlah)
        elif operasi == "tambah":
            item_obj.tambahStok(jumlah)
            return True
        else:
            print(f"Operasi stok tidak valid")
            return False

class LaporanPenjualan:
    def __init__(self):
        self.data_penjualan = {}

    def catat_penjualan(self,pemesanan):
        for i in pemesanan.daftar_item:
            nama = i['item'].nama
            jumlah = i['jumlah']
            pendapatan = i['item'].harga * jumlah

            if nama in self.data_penjualan:
                self.data_penjualan[nama]['jumlah'] += i['jumlah']
                self.data_penjualan[nama]['pendapatan'] += pendapatan
            else:
                self.data_penjualan[nama] = {'jumlah':i['jumlah'], 'pendapatan':pendapatan}
        print("Pemesanan telah dicatat\n")

    def tampilkan_laporan(self):
        print("\n====== LAPORAN PENJUALAN ======")
        if not self.data_penjualan:
            print("Belum ada data penjualan")
            print('='*27)
            return
    
        total_semua_penjualan = 0
        total_pendapatan = 0

        for nama, data in self.data_penjualan.items():
            print(f"{nama} - Terjual: {data['jumlah']} | Pendapatan: Rp{data['pendapatan']}")
            total_semua_penjualan += data['jumlah']
            total_pendapatan += data['pendapatan']
        print('-'*27)
        print(f"Total Item Terjual: {total_semua_penjualan}")
        print(f"Total Pendapatan: Rp.{total_pendapatan}")
        print('='*27)

    def analisis_tren_item(self):
        if not self.data_penjualan:
            return "Belum ada data penjualan"
        
        penjualan_per_item = {nama: data['jumlah'] for nama, data in self.data_penjualan.items()}

        if not penjualan_per_item:
            return "Tidak ada item yang terjual"
        
        item_terlaris = max(penjualan_per_item, key=penjualan_per_item.get)
        print(f"item Terlaris: {item_terlaris}, terjual: {penjualan_per_item[item_terlaris]}")
        return item_terlaris
    

# ===============================================
# Aplikasi Utama
# ===============================================

import pandas as pd
import numpy as np
import random

df_log_penjualan = pd.DataFrame(columns=['Timestamp', 'Item', 'Category', 'Price_per_Unit', 'Quantity_Sold', 'Total_Revenue'])

def load_data(file_path):
    daftar_objek_item = {}
    df_menu_original = None # Inisialisasi df_menu di sini
    try:
        df_menu_original = pd.read_csv(file_path) # df_menu yang dibaca dari CSV

        for index, row in df_menu_original.iterrows():
            nama = str(row['Item'])
            jenis = str(row['Category'])

            try:
                harga_str = str(row['Price']).replace('.', '').replace(',', '.')
                harga = float(harga_str)
            except:
                print(f"Gagal Konversi harga untuk item {nama}")
                harga = 0.0

            stok = random.randint(1,10)

            item = itemMenu(
                nama=nama,
                jenis=jenis,
                harga=harga,
                stock=stok
            )
            daftar_objek_item[nama.lower()] = item
        
        # Mengembalikan kedua nilai: daftar_objek_item dan df_menu
        return daftar_objek_item, df_menu_original.copy() 
    
    except FileNotFoundError:
        print(f"ERROR: File tidak ditemukan")
        return None, None
    except KeyError as e:
        print(f"ERROR: Kolom {e} tidak ditemukan")
        return None, None
    except Exception as e:
        print(f"ERROR: Terjadi kesalahan saat memuat data: {e}")
        return None, None
    
def update_df_menu_with_sales(current_df_menu, new_sales_log_entries):
    df_combined = pd.concat([current_df_menu, new_sales_log_entries], ignore_index=True)
    return df_combined

def download_data(dataframe, filename='data_gabungan.csv'):
    try:
        if filename.endswith('.csv'):
            dataframe.to_csv(filename, index=False)
            print(f"Data berhasi disimpan ke {filename}.CSV")
        elif filename.endswith('.xlsx'):
            print(f"Data berhasi disimpan ke {filename}.XLSX")
        else:
            print(f"Data berhasi disimpan ke {filename}.XLSX")
    except Exception as e:
        print(f"\nGagal menyimpan data: {e}")

    

# ===============================================
# APLIKASI UTAMA (MAIN LOOP)
# ===============================================

def run_app(menu_restoran, df_menu_original):
    global current_df_menu_for_concat
    if not menu_restoran or df_menu_original is None:
        print("Menu restoran tidak dappat dimuat")
        return
    
    laporan_penjualan = LaporanPenjualan()
    manajer_stok = ManajerStok()
        

    current_df_menu_for_concat = df_menu_original.copy()

    while True:
        print("\n=== Aplikasi Restoran ===")
        print("1. Lihat Menu")
        print("2. Buat Pemesanan Baru")
        print("3. Tambah Stok Item")
        print("4. Lihat Laporan Penjualan")
        print("5. Analisis Tren Item Terlaris")
        print("6. Lihat Data Penjualan")
        print("7. Keluar")
        print("8. Download Data Hasil")

        choice = input("Pilih opsi (1-8): ")

        if choice == '1':
            print('\n====== DAFTAR MENU ======')
            if not menu_restoran:
                print("Menu Kosong")
            else:
                for item_name, item_obj in menu_restoran.items():
                    print(f"{item_obj.nama:<20} ({item_obj.jenis:<10}) - Rp{item_obj.harga:10,.2f} - Stok: {item_obj.stok:<5}")
            print('='*80)
        elif choice == '2':
            pesanan_sekarang = Pemesanan()
            print('\n--- Buat Pemesanan ---')
            print("Ketik 'selesai' untuk mengakhiri, 'batal' untuk membatalkan")

            while True:
                item_nama = input("Masukkkan nama item: ").lower()

                if item_nama == 'selesai':
                    break
                if item_nama == 'batal':
                    pesanan_sekarang = Pemesanan()
                    print('Pemesanan Dibatalkan')
                    break
                if item_nama in menu_restoran:
                    item_obj = menu_restoran[item_nama]
                    try:
                        jumlah = int(input(f"Masukkan jumlah '{item_obj.nama}' (Stok: {item_obj.stok}): "))
                        if jumlah <= 0:
                            print("Jumlah harus lebih dari 0.")
                            continue
                        if pesanan_sekarang.tambah_item(item_obj, jumlah):
                            pass
                        else:
                            pass
                    except ValueError:
                        print("Jumlah tidak valid, masukkan angka")
                else:
                    print("Item tidak ditemuka, cek menu item")
            if pesanan_sekarang.daftar_item:
                pesanan_sekarang.tampilkan_detail()
                total_bayar = pesanan_sekarang.hitung_total()

                if total_bayar > 0:
                    metode_bayar = input("Pilih metode pembayaran (Cash/Credit Card/Digital Wallet): ")
                    pembayaran = Pembayaran(metode_bayar) 

                    if pembayaran.proses_pembayaran(total_bayar):
                        timestamp_transaksi = pd.Timestamp.now()
                        for item_data in pesanan_sekarang.daftar_item:
                            item_obj = item_data['item']
                            jumlah = item_data['jumlah']

                            if manajer_stok.update_stok(item_obj, jumlah, "kurangi"):
                                new_record = pd.DataFrame([{
                                    'Timestamp': timestamp_transaksi,
                                    'Item': item_obj.nama,
                                    'Category': item_obj.jenis,
                                    'Price_per_unit': item_obj.harga,
                                    'Quantity_Sold': jumlah,
                                    'Total_Revenue': item_obj.harga * jumlah
                                }])

                                global df_log_penjualan
                                df_log_penjualan = pd.concat([df_log_penjualan, new_record], ignore_index=True)
                        

                                
                                current_df_menu_for_concat = pd.concat([current_df_menu_for_concat, new_record],ignore_index=True)
                            else:
                                print(f"Gagal mengurangi stok, pembayaran dibatalkan")
                                break
                        else:
                            laporan_penjualan.catat_penjualan(pesanan_sekarang)
                            pembayaran.cetak_struk(pesanan_sekarang)
                    else:
                        print("Pembayaran gagal. Pemesanan tidak dapat diselesaikan")
                else:
                    print("Pesanan kosong, tidak ada pembayaran")
            else:
                print("Tidak ada item yang ditambahkan ke pemesanan")

        elif choice == '3':
            print('\n--- Tambah Stok Item ---')
            item_nama = input("Masukkan nama item yang ingin ditambahi stok: ").lower()
            if item_nama in menu_restoran:
                item_obj = menu_restoran[item_nama]
                try: 
                    jumlah_tambah = int(input(f"Masukkan jumlah stok yang ingin ditambahkan untuk {item_obj.nama}: "))
                    if jumlah_tambah > 0:
                        manajer_stok.update_stok(item_obj, jumlah_tambah, "tambah")
                    else:
                        print("Jumlah harus angka positif")
                except ValueError:
                    print("Jumlah harus berupa angka")
            else:
                print("Item tidak ditemukan")
        elif choice == '4':
            laporan_penjualan.tampilkan_laporan()
        elif choice == '5':
            laporan_penjualan.analisis_tren_item()
        elif choice == '6':
            print(current_df_menu_for_concat.tail(10))

        elif choice == '7':
            break
        elif choice == '8':
            if current_df_menu_for_concat is not None and not current_df_menu_for_concat.empty:
                filename = "data_gabungan.csv"
                download_data(current_df_menu_for_concat, filename)
                import subprocess

                subprocess.run(["streamlit", "run", "dashboard.py"])
                print("Program selesai")
                break
        else:
            print("Pilihan tidak valid. Input pilihan lagi")


if __name__ == "__main__":
    url_menu = 'https://raw.githubusercontent.com/JulianSudiyanto/Tugas-Besar-PASD---Kelompok-Lima-Watt/refs/heads/main/Cleaned_200_Price_Data.csv'

    menu_restoran, initial_df_menu = load_data(url_menu)

    if menu_restoran is not None and initial_df_menu is not None: # Cek kedua nilai
        run_app(menu_restoran, initial_df_menu) 
    else:
        print("Gagal memuat menu restoran atau DataFrame. Aplikasi tidak dapat dimulai.")


