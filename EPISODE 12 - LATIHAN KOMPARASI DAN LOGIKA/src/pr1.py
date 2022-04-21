# soal no 1. -------0++++++5------8++++++11------

print("Masukan angka lebih dari 0 dan kurang dari 5 atau\nlebih dari 8 dan kurang dari 11\n")
angka = float(input("Masukan angka disni! : "))

isCorrect = (angka > 0 and angka < 5) or (angka > 8 and angka < 11)
print("Angka yang masukan bernilai = ", isCorrect)