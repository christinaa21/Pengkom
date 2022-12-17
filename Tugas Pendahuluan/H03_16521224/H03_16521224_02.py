# Problem 2

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 2 November 2021
# Deskripsi : Membuat program yang dapat memeriksa apakah B merupakan anagram dari A.
# Asumsi    : Elemen pada array A dan B maksimal 10 (0-10)

# KAMUS
# A, B, i, angka, = int
# list_A, frekuensi_A, list_B, frekuensi_B = list
# lanjut = boolean

# ALGORITMA
lanjut = True

# Bagian A
while lanjut == True:
    A = int(input("Masukkan banyaknya elemen A: "))
    if A <= 0:
        print("Banyak elemen A harus lebih besar dari 0.")
        lanjut = False
    else:
        list_A = [0 for i in range(A)]
        frekuensi_A = [0 for i in range(11)]
        for i in range(A):
            list_A[i] = int(input("Masukkan elemen A ke-" + str(i+1) + ": "))
            if (list_A[i] < 0):
                print("Elemen A tidak boleh negatif.")
                lanjut = False
                break
            elif (list_A[i] > 10):
                print("Elemen A tidak boleh lebih dari 10.")
                lanjut = False
                break

        if lanjut == True:
            for i in range(11):
                for angka in list_A:
                    if i == angka:
                        frekuensi_A[i] += 1

            # Bagian B
            B = int(input("Masukkan banyaknya elemen B: "))
            if B <= 0:
                print("Banyak elemen B harus lebih besar dari 0.")
                lanjut = False
            else:
                list_B = [0 for i in range(B)]
                frekuensi_B = [0 for i in range(11)]
                for i in range(B):
                    list_B[i] = int(input("Masukkan elemen B ke-" + str(i+1) + ": "))
                    if (list_B[i] < 0):
                        print("Elemen B tidak boleh negatif.")
                        lanjut = False
                        break
                    elif (list_B[i] > 10):
                        print("Elemen B tidak boleh lebih dari 10.")
                        lanjut = False
                        break

                if lanjut == True:
                    for i in range(11):
                        for angka in list_B:
                            if i == angka:
                                frekuensi_B[i] += 1

                    # Pengecekan
                    if frekuensi_A == frekuensi_B:
                        print("B adalah anagram dari A")
                    else:
                        print("B bukan anagram dari A")
                    lanjut = False