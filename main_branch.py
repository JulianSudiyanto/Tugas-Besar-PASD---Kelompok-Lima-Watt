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

