def hitung_bmi(berat_badan, tinggi_badan):
    return berat_badan / (tinggi_badan ** 2)

def rekomendasi_bmi(bmi):
    if bmi < 18.5:
        return "Kurang berat badan"
    elif 18.5 <= bmi < 25:
        return "Berat badan normal"
    elif 25 <= bmi < 30:
        return "Kelebihan berat badan"
    else:
        return "Obesitas"

# Meminta pengguna untuk memasukkan berat badan dan tinggi badan
berat_badan = float(input("Masukkan berat badan (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan (m): "))

# Menghitung BMI
bmi = hitung_bmi(berat_badan, tinggi_badan)

# Memberikan rekomendasi berdasarkan BMI
rekomendasi = rekomendasi_bmi(bmi)

# Menampilkan hasil
print("BMI Anda adalah:", bmi)
print("Rekomendasi:", rekomendasi)soa
