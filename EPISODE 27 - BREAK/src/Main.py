# break berfungsi untuk menghentikan perulangan

data_int = int(input("Masukan angka : "))

angka = 0

while True:
    angka += 1

    print(angka)

    if angka == data_int:
        break

print("akhir dari program")

