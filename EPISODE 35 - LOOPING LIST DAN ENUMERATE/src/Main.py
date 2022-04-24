# looping dari list

# menggunakan for loop
print("For Loop")
kumpulan_angka = [1,4,5,7,2,4,6]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

kumpulan_mobil = ["Alphard", "Avanza", "Kijang Innova", "Pazero"]

for mobil in kumpulan_mobil:
    print(f"mobil = {mobil}")

# menggunkana for dan range
print("For dan range")
kumpulan_angka = [8,2,3,6,7,4,3,]
panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

# menggunakan while loop dan range
print("While dan range")
kumpulan_angka = [8,2,3,6,7,4,3,]
panjang = len(kumpulan_angka)

i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1


# menggunakan compherension
print("List Compherension")
kumpulan_angka = [8,2,3,6,7,4,3,]

[print(f"angka = {i}") for i in kumpulan_angka]

# Enumerate
print("Enumerate")
kumpulan_mobil = ["Alphard", "Avanza", "Kijang Innova", "Pazero"]

for index, data in enumerate(kumpulan_mobil):
    print(f"index = {index}, data = {data}")