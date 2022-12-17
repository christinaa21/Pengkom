# Problem 3

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 3 November 2021
# Deskripsi : Membuat program yang dapat menghitung berapa banyak kemunculan sebuah string sebagai sebuah substring pada string lain.
# Asumsi    : String yang dimasukkan hanya terdiri dari huruf kecil (a - z), dan string 1 tidak lebih panjang dari string 2.

# KAMUS
# p1, p2, i, j, jumlah, muncul = int
# string1, string2 = list

# ALGORITMA
p1 = int(input("Masukkan panjang string 1: "))
string1 = list(input("Masukkan string 1: "))
p2 = int(input("Masukkan panjang string 2: "))
string2 = list(input("Masukkan string 2: "))

i = 0
j = 0
jumlah = 0
muncul = 0
while i < p2:
    if string1[j] == string2[i]:
        jumlah += 1
        j += 1
    else:
        if string2[i] == string1[0]:
            jumlah = 1
            j = 1
        else:
            jumlah = 0
            j = 0
    i += 1
    if j-1 == p1-1:
        if jumlah == p1:
            muncul += 1    
        j = 0
        jumlah = 0
print("String 1 muncul sebanyak", muncul, "kali.")