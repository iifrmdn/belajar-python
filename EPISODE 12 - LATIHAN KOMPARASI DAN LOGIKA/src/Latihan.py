# membuat gabungan rentang angka

# ++++++4--------8+++++++
print("Masukan angka kurang dari 4 atau lebih dari 8")

inputUser = float(input("Masukan angka disini! = "))

# ++++++4------
# memeriksa apakah angka kurang dari 4
isKurang = (inputUser < 4)
print("Kurang dari 3 = ", isKurang)

# -----8+++++++
# memeriksa apakah angka lebih dari 10
isLebih = (inputUser > 8)
print("Lebih dari 10 = ", isLebih)

isCorrect = isKurang or isLebih
print("Angka yang anda masukan adalah : ", isCorrect)