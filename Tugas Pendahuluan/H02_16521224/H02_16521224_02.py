# Problem 2

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 26 Oktober 2021
# Deskripsi : Membuat program yang menerima bilangan N dan menuliskan 10^x terkecil yang lebih dari N.

# KAMUS
# N, i, x = int

# ALGORITMA
N = int(input("Masukkan N: "))
i = 0
x = 0
if N >= 0:
    while i <= N:
        i = 10**x
        x += 1
    print(i)
else:
    print(10**i)

#Cara 2:
N = int(input("Masukkan N: "))
i = 1
while i <= N:
    i = i * 10
print(i)