import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

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
        st.write(f"Stok {self.nama} bertambah {jumlah}. Total: {self.stok}")
    
    def kurangiStok(self,jumlah):
        if self.stok >= jumlah:
            self.stok -= jumlah
            st.write(f"Stok {self.nama} berkurang {jumlah}. Stok sekarang: {self.stok}")
            return True
        else:
            st.write("Stok Tidak Cukup!, (Tersedia: {self.stock}, Diminta: {jumlah})")
            return False
    
class Pemesanan:
    def __init__(self):
        self.daftar_item =[]

    def tambah_item(self, item, jumlah):
        if item.stok >= jumlah:
            self.daftar_item.append({'item':item, 'jumlah':jumlah})
            st.write(f"{item.nama} sejumlah {jumlah} ditambahkan ke pesanan")
            return True
        else:
            st.write(f"Tidak dapat menambahkan {item.nama}")
            return False
        
    def hitung_total(self):
        total = 0
        for i in self.daftar_item:
            total += i['item'].harga * i['jumlah']
        return total

    def tampilkan_detail(self):
        st.write('\n--- Detail Pemesanan ---')
        if not self.daftar_item:
            st.write("Pemesanan Kosong\n")
            return 
        for i in self.daftar_item:
            item = i['item']
            jumlah = i['jumlah']
            st.write(f'{item.nama} x {jumlah} = Rp.{item.harga * jumlah}')
        
        total = self.hitung_total()
        st.write('-'*10)
        st.write(f"Total Pembelian: Rp.{total}")
        st.write('-'*10)

class Pembayaran:
    def __init__(self, metode_pembayaran):
        self.metode = metode_pembayaran

    def proses_pembayaran(self,total):
        st.write(f"Pembayaran sebesar Rp.{total} menggunakan {self.metode} berhasil!")
        return True
        
    def cetak_struk(self,pemesanan):
        st.write("\n====== STRUK PEMBELIAN ======")
        pemesanan.tampilkan_detail()
        st.write(f"Metode Pembayaran: {self.metode}")
        st.write("="*27)

class ManajerStok:
    def update_stok(self, item_obj, jumlah, operasi):
        if operasi == "kurangi":
            return item_obj.kurangiStok(jumlah)
        elif operasi == "tambah":
            item_obj.tambahStok(jumlah)
            return True
        else:
            st.write(f"Operasi stok tidak valid")
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
        st.write("Pemesanan telah dicatat\n")

    def tampilkan_laporan(self):
        st.write("\n====== LAPORAN PENJUALAN ======")
        if not self.data_penjualan:
            st.write("Belum ada data penjualan")
            st.write('='*27)
            return
    
        total_semua_penjualan = 0
        total_pendapatan = 0

        for nama, data in self.data_penjualan.items():
            st.write(f"{nama} - Terjual:{data['jumlah']}| Pendapatan: Rp{data['pendapatan']}")
            total_semua_penjualan += data['jumlah']
            total_pendapatan += data['pendapatan']
        st.write('-'*27)
        st.write(f"Total Item Terjual: {total_semua_penjualan}")
        st.write(f"Total Pendapatan: Rp.{total_pendapatan}")
        st.write('='*27)

    def analisis_tren_item(self):
        if not self.data_penjualan:
            return "Belum ada data penjualan"
        
        penjualan_per_item = {nama: data['jumlah'] for nama, data in self.data_penjualan.items()}

        if not penjualan_per_item:
            return "Tidak ada item yang terjual"
        
        item_terlaris = max(penjualan_per_item, key=penjualan_per_item.get)
        st.write(f"item Terlaris: {item_terlaris}, terjual: {penjualan_per_item[item_terlaris]}")
        return item_terlaris
    

@st.cache_data # Cache data agar tidak di-load ulang setiap rerun
def load_data(file_path):

    daftar_objek_item = {}
    try:
        df_menu = pd.read_csv(file_path)
        st.write("Berhasil Dimuat")

        for index, row in df_menu.iterrows():
            nama = str(row['Item'])
            jenis = str(row['Category'])

            #Konversi harga menjadi numerikal
            try:
                harga_str = str(row['Price']).replace('.',''.replace(',','.'))
                harga = float(harga_str)
            except:
                st.warning("Gagal Konversi harga untuk item {nama}")
                harga = 0.0

            #Konversi Stok 
            try: 
                stok = int(row['Quantity'])
            except ValueError:
                st.warning("Gagal Konversi Stok untuk item {nama}")


            #Objek itemMenu baru
            item = itemMenu(
                nama=nama,
                jenis=jenis,
                harga=harga,
                stock=stok
            )

            daftar_objek_item[nama.lower()] = item
        
        st.info(f"Berhasil membuat {len(daftar_objek_item)} objek itemMenu dari data.")
        return daftar_objek_item
    
    except FileNotFoundError:
        st.error(f"ERROR: File tidak ditemukan")
        return None
    except KeyError as e:
        st.error(f"ERROR: Kolom {e} tidak ditemukan")
        return None
    except Exception as e:
        st.error(f"ERROR: Terjadi kesalahan saat memuat data: {e}")
        return None

url_menu = 'https://raw.githubusercontent.com/JulianSudiyanto/Tugas-Besar-PASD---Kelompok-Lima-Watt/refs/heads/main/Clean_Data_Restaurant_Final.csv'
menu_restoran = load_data(url_menu)

# Inisialisasi objek di session state agar persisten
if 'pesanan_sekarang' not in st.session_state:
    st.session_state.pesanan_sekarang = Pemesanan()
if 'laporan_penjualan_global' not in st.session_state:
    st.session_state.laporan_penjualan_global = LaporanPenjualan()
if 'manajer_stok_obj' not in st.session_state: # Instance untuk ManajerStok (jika ada state di dalamnya)
    st.session_state.manajer_stok_obj = ManajerStok()

def data_pesanan():
    #with st.form(key='add_order_form'):
    customer_id = st.text_input("Masukkan ID Customer:")
    item_nama = st.text_input("Masukkan Nama Item:").lower()
    quantity = st.number_input("Masukkan Jumlah:")
    date = st.date_input("Masukkan Tanggal:")
    method = st.selectbox("Pilih Metode Pembayaran:", ["Credit Card", "Cash", "Digital Wallet"])

    if st.button("Submit"):
        if item_nama in menu_restoran:
            item_obj = menu_restoran[item_nama]
            try:
                if quantity <= 0:
                    st.write("Jumlah harus lebih dari 0.")
                    pass
                if pesanan_sekarang.tambah_item(item_obj, quantity):
                    pass
                else:
                    pass
            except ValueError:
                st.write("Jumlah tidak valid, masukkan angka")
        else:
            st.warning("Item tidak ditemukan, cek menu item")


def transaksi():
    st.title("Data Transaksi Customer")
    st.write("Selamat masukan detail pesanan.")
    # Tampilkan menu sebelum input
    tampil_menu_btn = st.button("Tampilkan Daftar Menu", help="Klik untuk melihat menu yang tersedia.")
    if tampil_menu_btn:
        st.subheader("DAFTAR MENU RESTORAN")
        if not menu_restoran:
            st.warning("Menu Kosong")
        else:
            for item_name, item_obj in menu_restoran.items():
                st.write(f"{item_obj.nama:<20} ({item_obj.jenis:<10}) - Rp{item_obj.harga:10,.2f} - Stok: {item_obj.stok:<5}")
        st.write('='*80)
        data_pesanan()


def laporan_penjualan():
    pass


# Navigasi Menu
with st.sidebar:
    selected = option_menu(
        menu_title="Menu Utama",
        options=["Transaksi", "Laporan Penjualan", "Manajemen Produk", "Analisis Tren Produk"],        
        icons=["clipboard-data", "clipboard-data", "clipboard-data"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "0 !important", "background-color": "#f5f5f5"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "purple"},
        }
    )
if selected == "Transaksi":
    transaksi()
elif selected == "Laporan Penjualan":
    laporan_penjualan()
elif selected == "Manajer Produk":
    manajemen_produk()
elif selected == "Analisis Tren Produk":
    analisis()
else:
    st.title("Aplikasi Penjualan")
    st.write("Selamat datang di aplikasi KasirKita. Silahkan pilih menu di samping untuk melakukan transaksi.")
