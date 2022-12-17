# Problem 2

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 27 Oktober 2021
# Deskripsi : Membuat program yang menghitung berapa kali ember x dan ember y perlu diisi penuh untuk kemudian mengisi kolam z.

# KAMUS
# x, y, z, v_sementara, v_sisa, jumlah_y, jumlah_x = int

# ALGORITMA
x = float(input("Masukkan x: "))
y = float(input("Masukkan y: "))
z = float(input("Masukkan z: "))
v_sementara = 0
v_sisa = z
jumlah_y = 0
jumlah_x = 0

while v_sementara < z:
    while (v_sisa%x != 0) and (v_sisa >= 0):
        v_sementara += y
        jumlah_y = v_sementara/y
        v_sisa = z - v_sementara
    v_sementara += v_sisa
    jumlah_x += v_sisa/x

if (jumlah_x >= 0) and (jumlah_y >= 0):
    print(jumlah_x, "kali ember x,", jumlah_y, "kali ember y")
else:
    print("Tidak mungkin")