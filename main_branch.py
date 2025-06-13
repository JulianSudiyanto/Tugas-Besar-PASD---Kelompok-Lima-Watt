# ##Functional Programming

# def hitung_total_pemesanan(daftar_item):
#     total = 0
#     for i in daftar_item:
#         total += i['item'].harga* i['jumlah']
#     return total

# def analisis_tren_item(data_penjualan):
#     penjualan ={}
#     for i in data_penjualan:
#         nama = i['item'].nama
#         jum = i['jumlah']
#         if nama in penjualan:
#             penjualan[nama] += jum
#         else:
#             penjualan[nama] = jum
    
#     item_terlaris = max(penjualan, key=penjualan.get)
#     return item_terlaris

# #Object Oriented Programming

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
        print("\n🧾 Detail Pemesanan Anda:")
        print("-" * 66)
        print(f"| {'Item':<18} | {'Jumlah':>6} | {'Harga Satuan':>15} | {'Subtotal':>13} |")
        print("|" + "-"*20 + "|" + "-"*8 + "|" + "-"*17 + "|" + "-"*15 + "|")

        for item_data in self.daftar_item:
            item = item_data['item']
            jumlah = item_data['jumlah']
            subtotal = item.harga * jumlah

            # Format harga dengan titik ribuan dan koma desimal
            harga_satuan = f"Rp{item.harga:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            subtotal_fmt = f"Rp{subtotal:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

            print(f"| {item.nama:<18} | {jumlah:>6} | {harga_satuan:>15} | {subtotal_fmt:>13} |")

        print("-" * 66)
        total = self.hitung_total()
        total_fmt = f"Rp{total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"🧮 Total Pembelian:{'':>25}{total_fmt:>13}")
        print("-" * 66)

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
            dataframe.to_csv(filename, index=False)
            print(f"Data berhasil disimpan ke {filename}")
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
        print("4. Lihat Data Penjualan")
        print("5. Download Data Hasil")
        print("6. Keluar")

        choice = input("Pilih opsi (1-6): ")

        if choice == '1':
            print('\n========================= DAFTAR MENU =========================')
            print(f"| {'Nama':<20} | {'Kategori':<14} | {'Harga (Rp)':>11} | {'Stok':>4} |")
            print(f"|{'-'*22}|{'-'*16}|{'-'*13}|{'-'*6}|")
            if not menu_restoran:
                print("| Menu Kosong                                               |")
            else:
                for nama, item in menu_restoran.items():
                    print(f"| {item.nama:<20} | {item.jenis:<14} | {item.harga:11,.2f} | {item.stok:>4} |")
            print('='*60)
        elif choice == '2':
            pesanan_sekarang = Pemesanan()
            print("\n" + "="*60)
            print("                 📦  PEMBUATAN PEMESANAN  📦")
            print("="*60)
            print("Ketik 'selesai' untuk menyelesaikan pesanan.")
            print("Ketik 'batal' untuk membatalkan pesanan.")
            print("-"*60)

            while True:
                item_nama = input("Masukkan nama item: ").strip().lower()

                if item_nama == 'selesai':
                    break
                elif item_nama == 'batal':
                    pesanan_sekarang = Pemesanan()
                    print("\n❌ Pemesanan dibatalkan.\n")
                    break
                elif item_nama in menu_restoran:
                    item_obj = menu_restoran[item_nama]
                    try:
                        jumlah = int(input(f"Masukkan jumlah '{item_obj.nama}' (Stok tersedia: {item_obj.stok}): "))
                        if jumlah <= 0:
                            print("⚠️  Jumlah harus lebih dari 0.\n")
                            continue
                        if pesanan_sekarang.tambah_item(item_obj, jumlah):
                            print(f"✅ '{item_obj.nama}' sebanyak {jumlah} berhasil ditambahkan ke pesanan.\n")
                        else:
                            print(f"⚠️  Gagal menambahkan '{item_obj.nama}' ke pesanan.\n")
                    except ValueError:
                        print("⚠️  Input tidak valid! Harap masukkan angka.\n")
                else:
                    print("❗ Item tidak ditemukan di menu. Coba lagi.\n")

            if pesanan_sekarang.daftar_item:
                pesanan_sekarang.tampilkan_detail()
                total_bayar = pesanan_sekarang.hitung_total()

                if total_bayar > 0:
                    print("-"*60)
                    metode_bayar = input("💳 Pilih metode pembayaran (Cash / Credit Card / Digital Wallet): ").strip()
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
                                if df_log_penjualan.empty:
                                     df_log_penjualan = pd.DataFrame(columns=new_record.columns)

                                current_df_menu_for_concat = pd.concat([current_df_menu_for_concat, new_record], ignore_index=True)
                            else:
                                print(f"❌ Gagal mengurangi stok '{item_obj.nama}'. Pembayaran dibatalkan.")
                                break
                        else:
                            laporan_penjualan.catat_penjualan(pesanan_sekarang)
                            pembayaran.cetak_struk(pesanan_sekarang)
                    else:
                        print("❌ Pembayaran gagal. Pemesanan tidak diproses.")
                else:
                    print("❗ Total pesanan 0. Tidak ada pembayaran yang dilakukan.")
            else:
                print("\n📭 Tidak ada item yang ditambahkan ke pesanan.")
        elif choice == '3':
            print("\n" + "="*30)
            print(" TAMBAH STOK ITEM ".center(30, "="))
            print("="*30)

            item_nama = input("Masukkan nama item yang ingin ditambah stoknya: ").strip().lower()

            if item_nama in menu_restoran:
                item_obj = menu_restoran[item_nama]
                print(f"\nStok saat ini untuk '{item_obj.nama}': {item_obj.stok}")
                try:
                    jumlah_tambah = int(input(f"Masukkan jumlah stok yang ingin ditambahkan: "))
                    if jumlah_tambah > 0:
                        manajer_stok.update_stok(item_obj, jumlah_tambah, "tambah")
                        print(f"✅ Stok berhasil ditambahkan! Total stok baru: {item_obj.stok}")
                    else:
                        print("⚠️ Jumlah harus berupa angka positif.")
                except ValueError:
                    print("❌ Input tidak valid. Jumlah harus berupa angka.")
            else:
                print("❌ Item tidak ditemukan di menu.")
        elif choice == '4':
            from tabulate import tabulate
            print("\n=== 10 Transaksi Terakhir ===\n")
            print(tabulate(current_df_menu_for_concat.tail(10), headers='keys', tablefmt='pretty', showindex=False))
        elif choice == '5':
            if current_df_menu_for_concat is not None and not current_df_menu_for_concat.empty:
                filename = "data_gabungan.csv"
                download_data(current_df_menu_for_concat, filename)
                import subprocess

                subprocess.run(["streamlit", "run", "ui.py"])
                print("Program selesai")
                break
        elif choice == '6':
            break
        else:
            print("Pilihan tidak valid. Input pilihan lagi")


if __name__ == "__main__":
    url_menu = 'https://raw.githubusercontent.com/JulianSudiyanto/Tugas-Besar-PASD---Kelompok-Lima-Watt/refs/heads/main/dataset/Cleaned_200_Price_Data_Final.csv'

    menu_restoran, initial_df_menu = load_data(url_menu)

    if menu_restoran is not None and initial_df_menu is not None: # Cek kedua nilai
        run_app(menu_restoran, initial_df_menu) 
    else:
        print("Gagal memuat menu restoran atau DataFrame. Aplikasi tidak dapat dimulai.")


