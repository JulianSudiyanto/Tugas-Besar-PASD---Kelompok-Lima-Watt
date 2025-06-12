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
    def __init__(self,nama,jenis,harga,ukuran,stock):
        self.nama=nama
        self.jenis=jenis
        self.harga=harga
        self.ukuran=ukuran
        self.stok=stock
    
    def tambahStok(self,jumlah):
        self.stok += jumlah
    
    def kurangiStok(self,jumlah):
        if self.stok >= jumlah:
            self.stok -= jumlah
        else:
            print("Stok Tidak Cukup!")
    
class Pemesanan:
    def __init__(self):
        self.daftar_item =[]

    def tambah_item(self, item, jumlah):
        self.daftar_item.append({'item':item, 'jumlah':jumlah})

    def hitung_total(self):
        total = 0
        for i in self.daftar_item:
            total += i['item'].harga * i['jumlah']
        return total

    def tampilkan_detail(self):
        for i in self.daftar_item:
            item = i['item']
            jumlah = i['jumlah']
            print(f"{item.nama} x{jumlah} = Rp{item.harga * jumlah}")
        total = hitung_total_pemesanan(self.daftar_item)
        print(f"Total: Rp.{total}")

class Pembayaran:
    def __init__(self):
        self.metode = metode
    def proses_pembayaran(self,total):
        print(f"Pembayaran sebesar Rp.{total} menggunakan {self.metode} berhasil!")
    def cetak_struk(self,pemesanan):
        print("\n====== STRUK PEMBELIAN ======")
        pemesanan.tampilkan_detail()
        print(f"Metode Pembayaran: {self.metode}")
        print("="*10)

class ManajerStok:
    def update_stok(self, pemesanan, nama_item, jumlah, operasi):
        for i in pemesanan.daftar_item:
            if i['item'].nama == nama_item:
                if operasi == "kurangi":
                    i['item'].kurangiStok(jumlah)
                    break
                elif operasi == "tambah":
                    i['item'].tambahStok(jumlah)
                    break

class LaporanPenjualan:
    def __init__(self):
        self.data_penjualan = {}

    def catat_penjualan(self,pemesanan):
        for i in pemesanan.daftar_item:
            nama = i['item'].nama
            pendapatan = i['item'].harga * i['jumlah']
            if nama in self.data_penjualan:
                self.data_penjualan[nama]['jumlah'] += i['jumlah']
                self.data_penjualan[nama]['pendapatan'] += pendapatan
            else:
                self.data_penjualan[nama] = {'jumlah':i['jumlah'], 'pendapatan':pendapatan}
    
    def tampilkan_laporan(self):
        print("\n====== LAPORAN PENJUALAN ======")
        for nama, data in self.data_penjualan.items():
            print(f"{nama} - Terjual:{data['jumlah']}| Pendapatan: Rp{data['pendapatan']}")
        print('='*10)
