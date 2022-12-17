# Problem 2

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 3 November 2021
# Deskripsi : Membuat program yang menentukan kondisi akhir tombol-tombol berlampu sesuai dengan syarat yang tertera pada soal.

# KAMUS
# banyak_lampu, jumlah_klik, i, tekan, kondisi = int
# list_lampu = list
# keadaan_akhir = str
# error = boolean

# ALGORITMA
banyak_lampu = int(input("Masukkan banyak lampu: "))
list_lampu = [0 for i in range(banyak_lampu)]
error = False

if banyak_lampu > 0:
    jumlah_klik = int(input("Masukkan berapa kali Tuan Kil menekan tombol: "))
    for i in range(jumlah_klik):
        tekan = int(input("Tombol yang ditekan ke " + str(i+1) + ": "))
        if tekan <= banyak_lampu:
            tekan -= 1
            if banyak_lampu == 1:
                if list_lampu[tekan] == 0:
                    list_lampu[tekan] = 1
                else:
                    list_lampu[tekan] = 0
            if banyak_lampu > 1:
                if tekan == 0:
                    if list_lampu[tekan] == 0:
                        list_lampu[tekan] = 1
                        if list_lampu[tekan+1] == 0:
                            list_lampu[tekan+1] = 1
                        else:
                            list_lampu[tekan+1] = 0
                    else:
                        list_lampu[tekan] = 0
                        if list_lampu[tekan+1] == 0:
                            list_lampu[tekan+1] = 1
                        else:
                            list_lampu[tekan+1] = 0
                elif tekan == banyak_lampu-1:
                    if list_lampu[tekan] == 0:
                        if list_lampu[tekan-1] == 0:
                            list_lampu[tekan-1] = 1
                        else:
                            list_lampu[tekan-1] = 0
                        list_lampu[tekan] = 1
                    else:
                        if list_lampu[tekan-1] == 0:
                            list_lampu[tekan-1] = 1
                        else:
                            list_lampu[tekan-1] = 0
                        list_lampu[tekan] = 0
                else:
                    if list_lampu[tekan] == 0:
                        if list_lampu[tekan-1] == 0:
                            list_lampu[tekan-1] = 1
                        else:
                            list_lampu[tekan-1] = 0
                        list_lampu[tekan] = 1
                        if list_lampu[tekan+1] == 0:
                            list_lampu[tekan+1] = 1
                        else:
                            list_lampu[tekan+1] = 0
                    else:
                        if list_lampu[tekan-1] == 0:
                            list_lampu[tekan-1] = 1
                        else:
                            list_lampu[tekan-1] = 0
                        list_lampu[tekan] = 0
                        if list_lampu[tekan+1] == 0:
                            list_lampu[tekan+1] = 1
                        else:
                            list_lampu[tekan+1] = 0
        else:
            error = True
            break
    if error == False:
        keadaan_akhir = ""
        for kondisi in list_lampu:
            keadaan_akhir += str(kondisi)

        print("Keadaan akhir rangkaian lampu adalah", keadaan_akhir)
    else:
        print("Tombol yang kamu tekan melebih banyak lampu yang ada.")
else:
    print("Banyak lampu harus lebih dari 0.")