# Problem 3

# NIM/Nama  : 16521224/Christina Wijaya
# Tanggal   : 17 November 2021
# Deskripsi : Menentukan keliling pulau yang diberikan dalam grid.
# Asumsi    : Pada peta tersebut, hanya terdapat 1 pulau dan dalam pulau tersebut tidak memiliki danau, dalam kata lain, tidak ada angka 0 di dalam pulau.

# KAMUS
# brs, klm, i, j, keliling = int
# grid = matriks

# ALGORITMA
brs = int(input("Masukkan nilai brs: "))
klm = int(input("Masukkan nilai klm: "))

if brs > 0 and klm > 0:
    grid = [[0 for j in range(klm)] for i in range(brs)]

    for i in range(brs):
        for j in range(klm):
            grid[i][j] = int(input("Masukkan nilai petak baris " + str(i+1) + " kolom " + str(j+1) + ": "))

    keliling = 0
    for i in range(brs):
        for j in range(klm):
            if grid[i][j] == 1:
                if i == 0 and j == 0:
                    if brs == 1 and klm == 1:
                        keliling += 4
                    else:
                        keliling += 2
                        if (grid[i+1][j] == 0):
                            keliling += 1
                        if (grid[i][j+1] == 0):
                            keliling += 1
                elif i == 0 and j != 0:
                    keliling += 1
                    if j != klm-1:
                        if (grid[i][j-1] == 0):
                            keliling += 1
                        if (grid[i+1][j] == 0):
                            keliling += 1
                        if (grid[i][j+1] == 0):
                            keliling += 1
                    else:
                        if (grid[i-1][j] == 0):
                            keliling += 1
                        if (grid[i+1][j] == 0):
                            keliling += 1
                        if (grid[i][j-1] == 0):
                            keliling += 1
                elif j == 0 and i != 0:
                    keliling += 1
                    if i != brs-1:
                        if (grid[i-1][j] == 0):
                            keliling += 1
                        if (grid[i+1][j] == 0):
                            keliling += 1
                        if (grid[i][j+1] == 0):
                            keliling += 1
                    else:
                        if (grid[i][j-1] == 0):
                            keliling += 1
                        if (grid[i-1][j] == 0):
                            keliling += 1
                        if (grid[i][j+1] == 0):
                            keliling += 1
                else:
                    if i!= brs-1 and j!= klm-1:
                        if (grid[i-1][j] == 0):
                            keliling += 1
                        if (grid[i+1][j] == 0):
                            keliling += 1
                        if (grid[i][j+1] == 0):
                            keliling += 1
                        if (grid[i][j-1] == 0):
                            keliling += 1
                    elif i == brs-1 and j != klm-1:
                        keliling += 1
                        if (grid[i][j-1] == 0):
                            keliling += 1
                        if (grid[i-1][j] == 0):
                            keliling += 1
                        if (grid[i][j+1] == 0):
                            keliling += 1
                    elif j == klm-1 and i != brs-1:
                        keliling += 1
                        if (grid[i-1][j] == 0):
                            keliling += 1
                        if (grid[i+1][j] == 0):
                            keliling += 1
                        if (grid[i][j-1] == 0):
                            keliling += 1
                    elif i == brs-1 and j == klm-1:
                        keliling += 2
                        if (grid[i-1][j] == 0):
                            keliling += 1
                        if (grid[i][j-1] == 0):
                            keliling += 1

    print("Keliling pulau tersebut adalah", keliling)
else:
    print("Nilai baris dan kolom harus merupakan bilangan bulat positif.")  