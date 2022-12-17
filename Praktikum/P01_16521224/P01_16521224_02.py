# Problem 2

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 6 Oktober 2021
# Deskripsi : Membuat program yang menentukan kelas dan harga tiket pesawat Tuan Kil.

# KAMUS
# no_kursi, harga = int
# posisi, deskripsi = str

# ALGORITMA
no_kursi = int(input("Tentukan Nomor Kursi: "))
posisi = input("Tentukan Posisi Kursi: ")

if (1 <= no_kursi <= 20) or (51 <= no_kursi <= 60):
    deskripsi = "Hot Seat"
    if (posisi == "A") or (posisi == "F"):
        harga = 1600000
    elif (posisi == "B") or (posisi == "E"):
        harga = 1550000
    elif (posisi == "C") or (posisi == "D"):
        harga = 1500000
    else:
        print("Silahkan masukkan posisi yang benar.")
elif (21 <= no_kursi <= 50) or (61 <= no_kursi <= 100):
    deskripsi = "Regular"
    if (posisi == "A") or (posisi == "F"):
        harga = 1000000
    elif (posisi == "B") or (posisi == "E"):
        harga = 950000
    elif (posisi == "C") or (posisi == "D"):
        harga = 900000
    else:
        print("Silahkan masukkan posisi yang benar.")
else:
    print("Silahkan masukkan nomor kursi yang benar.")

print("Tuan Kil memilih kursi " + deskripsi + " dengan harga", str(harga) + ".")