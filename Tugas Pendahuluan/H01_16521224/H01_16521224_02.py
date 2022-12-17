# Problem 2

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 4 Oktober 2021
# Deskripsi : Membuat program kalkulator sederhana yang menerima 2 buah angka dan sebuah karakter operasi,
#             dan menuliskan hasil perhitungannya.

# KAMUS
# angka_pertama, angka_kedua = int
# operator = string

# ALGORITMA
angka_pertama = int(input("Masukkan angka pertama: "))
angka_kedua = int(input("Masukkan angka kedua: "))
operator = input("Masukkan operator: ")

if (operator == '+'):
    print(str(angka_pertama), operator, str(angka_kedua), "=", str(angka_pertama + angka_kedua))
elif (operator == '-'):
    print(str(angka_pertama), operator, str(angka_kedua), "=", str(angka_pertama - angka_kedua))
elif (operator == '*'):
    print(str(angka_pertama), operator, str(angka_kedua), "=", str(angka_pertama * angka_kedua))
elif (operator == '/'):
    print(str(angka_pertama), operator, str(angka_kedua), "=", str(angka_pertama // angka_kedua))
elif (operator == '%'):
    print(str(angka_pertama), operator, str(angka_kedua), "=", str(angka_pertama % angka_kedua))
else: #(operator bukan +, -, *, /, ataupun %)
    print("Operator yang dimasukkan salah.")