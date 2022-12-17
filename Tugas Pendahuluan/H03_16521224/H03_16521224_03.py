# Problem 3

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 2 November 2021
# Deskripsi : Membuat program yang menerima sebuah string dan menuliskan apakah string tersebut palindrom.
# Asumsi    : String hanya berisi huruf kecil (a-z).

# KAMUS
# panjang, i = int
# string = str
# cek_palindrom, list_string = list

# ALGORITMA
panjang = int(input("Masukkan panjang string: "))
cek_palindrom = [0 for i in range(panjang)]
string = input("Masukkan string: ")
list_string = list(string)

if panjang == len(list_string):
    for i in range(panjang):
        cek_palindrom[panjang-i-1] = list_string[i]
    if list_string == cek_palindrom:
        print(string, "adalah palindrom")
    else:
        print(string, "bukan palindrom")
elif panjang < len(list_string):
    print("String yang dimasukkan melebihi panjang string.")
else:
    print("String yang dimasukkan kurang dari panjang string.")