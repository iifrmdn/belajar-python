# --------4++++++++8--------
print("Masukan angka lebih dari 4 dan kurang dari 8")
angka = float(input("Masukan angka disini! : "))

# ------4+++++++
# memeriksa apakah angka lebih dari 4
isLebih = (angka > 4)
print("Angka lebih dari 4 = ", isLebih)

# ++++++8------
# memeriksa apakah angka kurang dari 8
isKurang = (angka < 8)
print("Angka kurang dari 8 = ", isKurang)

isCorrect = isLebih and isKurang
print("Angka yang anda masukan bernilai = ", isCorrect)