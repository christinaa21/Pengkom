# Problem 3

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 26 Oktober 2021
# Deskripsi : Membuat program yang menerima bilangan X dan menentukan apakah X adalah bilangan prima atau bukan.

# KAMUS
# X, tes, i = int

# ALGORITMA
X = int(input("Masukkan X: "))
if X >= 0:
    if X == 0 or X == 1:
        print(X, "bukan biangan prima")
    else:
        tes = 0
        for i in range(2, X):
            if X%i == 0:
                tes += 1
        if tes > 0:
            print(X, "bukan bilangan prima")
        else:
            print(X, "adalah bilangan prima")
else:
    print("X tidak boleh negatif")
