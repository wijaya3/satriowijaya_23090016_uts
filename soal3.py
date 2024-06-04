def hitung_total_harga():
    # Meminta pengguna untuk memasukkan jumlah barang
    jumlah_barang = int(input("Masukkan jumlah barang: "))

    total_harga = 0

    # Loop untuk meminta pengguna memasukkan harga setiap barang
    for i in range(1, jumlah_barang + 1):
        harga = float(input(f"Masukkan harga barang ke-{i}: "))
        total_harga += harga

    return total_harga

# Memanggil fungsi hitung_total_harga untuk menghitung total harga
total = hitung_total_harga()
print("Total harga dari seluruh barang adalah:", total)
