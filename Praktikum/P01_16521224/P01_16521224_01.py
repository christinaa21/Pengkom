# Problem 1

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 6 Oktober 2021
# Deskripsi : Membuat program yang menghitung besar pajak penghasilan yang harus dibayar oleh
#             Tuan Ric sesuai ketentuan pada soal.

# KAMUS
# penghasilan = float
# pajak = int

# ALGORITMA
penghasilan = float(input("Masukkan penghasilan Tuan Ric: "))

if penghasilan < 50000000:
    pajak = penghasilan * (5/100)
elif (50000000 <= penghasilan <= 249999999):
    pajak = penghasilan * (15/100)
elif (250000000 <= penghasilan <= 499999999):
    pajak = penghasilan * (25/100)
else:
    pajak = penghasilan * (30/100)

print("Pajak yang harus dibayar Tuan Ric sebesar", str(int(pajak)), "rupiah.")