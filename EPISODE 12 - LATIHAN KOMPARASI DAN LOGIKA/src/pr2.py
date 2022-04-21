# soal no 2. +++++++0------5++++++8------11++++++
print("Masukan angka kurang dari 0 atau lebih dari 5 dan kurang dari 8 atau \n lebih dari 11")

angka = float(input("masukan angka disini! : "))
isCorrect = (angka < 0 or angka > 5) and (angka < 8 or angka > 11)

print("Angka yang dimasukan bernilai = ", isCorrect)
