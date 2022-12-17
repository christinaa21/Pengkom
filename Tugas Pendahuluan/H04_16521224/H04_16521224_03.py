# Problem 3

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 16 November 2021
# Deskripsi : Membuat program yang menerima masukkan N dan menuliskan matriks segitiga pascal berukuran N x N.

# KAMUS
# N, i, j = int
# A = matriks

# ALGORITMA
N = int(input("Masukkan N: "))
A = [[1 for j in range(N)] for i in range(N)]
for i in range(1, N):
    for j in range(1, N):
        A[i][j] = A[i-1][j] + A[i][j-1]

for i in range(N):
    for j in range(N):
        print(A[i][j], end=" ")
    print("")