# Problem 3

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 27 Oktober 2021
# Deskripsi : Membuat program yang 

# KAMUS
# N, n_max, tes = int

# ALGORITMA
N = int(input("Masukkan bilangan N: "))
n_max = 0
tes = 0

if N > 1:
    for i in range(1, N+1):
        for j in range(1, N+1):
            n_sementara = i+j
            if n_sementara < N:
                for k in range(1, N+1):
                    n_sementara += k
                    while n_sementara < N:
                        n_sementara += k
                    
                

else:
    print("N haruslah bilangan bulat yang lebih besar dari 1.")

#Maaf kak, waktunya tidak cukup bagi saya untuk menyelesaikan Problem 3.