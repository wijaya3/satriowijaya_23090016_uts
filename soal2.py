def cek_tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

tahun_input = int(input("Masukkan tahun yang ingin diperiksa: "))

if cek_tahun_kabisat(tahun_input):
    print(tahun_input, "adalah tahun kabisat.")
else:
    print(tahun_input, "bukan tahun kabisat.")
