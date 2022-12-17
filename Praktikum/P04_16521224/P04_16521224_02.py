# Problem 2

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 17 November 2021
# Deskripsi : Membuat program yang dapat menghitung banyak kemungkinan kata berbeda yang dapat dibentuk dari kumpulan huruf yang diberikan.
# Asumsi    : String yang dimasukkan adalah huruf kecil (a - z)

# KAMUS
# p, x, hasil, i, j, penyebut, jumlah_huruf = int
# string, list_huruf, jumlah_huruf = list
# kemungkinan = float

# ALGORITMA
def faktorial(x):
    hasil = 1
    for i in range(x, 1, -1):
        hasil *= i
    return hasil

p = int(input("Masukkan panjang string: "))
if p > 0:
    string = list(input("Masukkan string: "))
    jumlah_huruf = 0
    for i in string:
        jumlah_huruf += 1
    if jumlah_huruf == p:
        list_huruf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        jumlah_huruf = [0 for i in range(26)]
        for i in range(p):
            for j in range(26): # 26 = jumlah abjad
                if string[i] == list_huruf[j]:
                    jumlah_huruf[j] += 1
                    break
        penyebut = 1
        for i in range(26):
            if jumlah_huruf[i] > 1:
                penyebut *= faktorial(jumlah_huruf[i])
        kemungkinan = faktorial(p)/penyebut
        print("String tersebut dapat membentuk", int(kemungkinan), "kata berbeda.")
    else:
        print("Jumlah huruf pada string yang dimasukkan tidak sama dengan panjang string.")
else:
    print("Panjang string harus merupakan bilangan bulat positif.")