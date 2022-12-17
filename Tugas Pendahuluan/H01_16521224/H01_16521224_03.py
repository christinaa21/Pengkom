# Problem 3

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 4 Oktober 2021
# Deskripsi : Membuat program yang menentukan apakah sebuah bilangan adalah bilangan positif, negatif, atau nol.
#             Dan khusus untuk bilangan positif, juga akan ditentukan apakah bilangan tersebut ganjil atau genap.

# KAMUS
# X = int

# ALGORITMA
X = int(input("Masukkan X: "))

if (X > 0):
    if (X % 2 == 0):
        print("X adalah bilangan positif genap")
    else: #(X % 2 == 1)
        print("X adalah bilangan positif ganjil")
elif (X < 0):
    print("X adalah bilangan negatif")
else: #(X == 0)
    print("X adalah bilangan nol")