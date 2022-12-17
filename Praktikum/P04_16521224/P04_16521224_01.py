# Problem 1

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 17 November 2021
# Deskripsi : Membuat program yang menerima input panjang sisi kubus dan tinggi limas, serta memberikan output volume rumah tersebut.
#             Program harus memanfaatkan 2 subprogram yang dapat menghitung volume kubus dan limas.

# KAMUS
# s, t = int
# v, v_rumah = float

# ALGORITMA
def v_kubus(s):
    v = s**3
    return v

def v_limas(s, t):
    v = (1/3)*s*s*t
    return v

s = int(input("Masukkan panjang sisi kubus: "))
t = int(input("Masukkan tinggi limas: "))

if (s > 0) and (t > 0):
    v_rumah = v_kubus(s) + v_limas(s, t)
    print("Volume rumah yang terbentuk adalah", v_rumah, "meter kubik.")
else:
    print("Panjang sisi kubus dan tinggi limas harus merupakan bilangan bulat positif.")