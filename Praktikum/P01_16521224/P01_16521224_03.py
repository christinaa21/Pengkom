# Problem 3

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 6 Oktober 2021
# Deskripsi : Membuat program yang dapat menentukan apakah data banyak kaki yang menginjak lantai Sabuga
#             dari Tuan Dip mungkin benar atau tidak berdasarkan syarat tertentu yang disebutkan dalam soal.

# KAMUS
# kaki, orang_tua, anak = int
# data = str

# ALGORITMA
kaki = int(input("Banyak kaki yang menginjak lantai: "))
orang_tua = int(input("Banyak orang tua: "))
anak = int(input("Banyak anak: "))

ketentuan_anak = 2 * orang_tua + ((kaki - orang_tua * 2)/2)
# ketentuan_anak ini akan digunakan pada kondisi jumlah 2 kali orang tua <= total kaki yang menginjak lantai Sabuga.
# Pada kondisi tersebut, jumlah anak tidak boleh lebih dari ketentuan_anak.
# pada ketentuan_anak ini, pertama-tama dihitung (total kaki yang menginjak lantai Sabuga dikurangi jumlah kaki orang tua) kemudian dibagi 2.
# kondisi pertama perlu dibagi dua untuk menentukan jumlah anak yang ada karena setiap orang masing-masing memiliki 2 kaki.
# kemudian, dilanjutkan dengan menghitung jumlah orang tua dikali 2 (dikali 2 karena satu orang tua bisa menggendong 2 anak) kemudian
# ditambahkan dengan hasil perhitungan kondisi pertama tadi.
# perhitungan ini akan menghasilkan jumlah anak maksimal yang mungkin.

if (kaki % 2 == 0):
    if ((orang_tua * 2) <= kaki) and (anak <= ketentuan_anak):
        data = "mungkin benar."
    else:
        data = "tidak mungkin benar."
else:
    data = "tidak mungkin benar."

print("Data Tuan Dip " + data)