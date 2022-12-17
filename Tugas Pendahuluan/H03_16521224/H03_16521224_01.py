# Problem 1

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 2 November 2021
# Deskripsi : Membuat program yang menerima N buah bilangan dan menuliskan kembali bilangan tersebut secara terbalik.

# KAMUS
# N, i = int
# bilangan = list

# ALGORITMA
N = int(input("Masukkan N: "))
bilangan = [0 for i in range(N)]
for i in range(N):
    bilangan[i] = int(input())
print("Hasil dibalik:")
for i in range(N-1, -1, -1):
    print(bilangan[i])