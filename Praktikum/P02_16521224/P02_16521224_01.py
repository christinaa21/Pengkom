# Problem 1

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 27 Oktober 2021
# Deskripsi : Menentukan berapa banyak langkah yang diperlukan untuk mengubah bilangan
#             bulat positif N menjadi 1 dengan syarat-syarat yang disebutkan pada soal.

# KAMUS
# N, langkah = int

# ALGORITMA
N = int(input("Masukkan bilangan N: "))
langkah = 0
if N > 0:
    while N > 1:
        if (N%2 == 1):
            N -= 1
            langkah += 1
        else:
            N /= 2
            langkah += 1
    print("Banyak langkah yang diperlukan adalah", langkah, end=".")
else:
    print("N harus merupakan bilangan bulat positif.")