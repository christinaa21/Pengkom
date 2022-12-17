# Problem 1

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 26 Oktober 2021
# Deskripsi : Membuat program yang menerima bilangan N dan menuliskan 1 sampai N dalam satu baris.

# KAMUS
# N, i = int

# ALGORITMA
N = int(input("Masukkan N: "))
if N >= 1:
    for i in range(1,N+1):
        print(i, end=" ")
else:
    for i in range(1, N-1, -1):
        print(i, end=" ")