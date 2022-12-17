# Problem 1

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 16 November 2021
# Deskripsi : Membuat program yang menerima A dan B, lalu menuliskan semua nilai dari f(A), f(A+1),..., f(B)
#             dengan f(x) = x^2 - 2x + 5. Implementasikan fungsi dalam hal ini!

# KAMUS
# A, B, x, f = int

# ALGORITMA
A = int(input("Masukkan A: "))
B = int(input("Masukkan B: "))

def fungsi(x):
    f = x**2 - 2*x + 5
    return f

while A <= B:
    print("f(" + str(A) + ") = " + str(fungsi(A)))
    A += 1