# Problem 2

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 16 November 2021
# Deskripsi : Membuat program yang menerima N dan M, lalu membaca matriks A berukuran N x M, dan menuliskan
#             berapa banyak bilangan positif di dalam matriks beserta menuliskan isi matriks itu sendiri.

# KAMUS
# N, M, positif, i, j = int
# A = matriks

# ALGORITMA
N = int(input("Masukkan N: "))
M = int(input("Masukkan M: "))

A = [[0 for j in range(M)] for i in range(N)]
positif = 0

for i in range(N):
    for j in range(M):
        A[i][j] = int(input("Masukkan nilai A[" + str(i+1) + "][" + str(j+1) + "]: "))
        if A[i][j] > 0:
            positif += 1

if positif > 0:
    print("Ada", positif, "bilangan positif di matriks.")
else:
    print("Tidak ada bilangan positif di matriks.")

for i in range(N):
    for j in range(M):
        print(A[i][j], end=" ")
    print("")