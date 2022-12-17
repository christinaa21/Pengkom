# Problem 1

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 3 November 2021
# Deskripsi : Menentukan berapa huruf vokal dan huruf konsonan dari string tersebut.
# Asumsi    : String yang dimasukkan hanya berisi alfabet dalam huruf kecil dan spasi.

# KAMUS
# N, jumlah_huruf, vokal, konsonan, spasi, j = int
# string = list
# i = str

# ALGORITMA
N = int(input("Masukkan N: "))
jumlah_huruf = 0
vokal = 0
konsonan = 0
spasi = 0

if N > 0:
    string = list(input("Masukkan string: "))
    for i in string:
        jumlah_huruf += 1
    if jumlah_huruf == N:
        for j in range(N):
            if (string[j] == 'a') or (string[j] == 'i') or (string[j]  == 'u') or (string[j]  == 'e') or (string[j] == 'o'):
                vokal += 1
            elif (string[j] == ' '):
                spasi += 1
            else:
                konsonan += 1
        print("Terdapat", vokal, "huruf vokal dan", konsonan, "huruf konsonan.")
    elif jumlah_huruf < N:
        print("Panjang string kurang dari N.")
    else:
        print("Panjang string lebih dari N.")
else:
    print("N harus merupakan bilangan bulat positif.")