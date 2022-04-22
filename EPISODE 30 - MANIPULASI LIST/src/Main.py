# manipulasi list

# index     0(-4)       1(-3)      2(-2)     3(-1)
data_car = ["Pazero", "Fortuner", "Avanza", "Xpander"]

data_0 = data_car[0]
print(f"Data Mobil index 0 = {data_0}")

print(f"Data Mobil index -1 = {data_car[-1]}")

# menghitung panjang data
panjang_data = len(data_car)
print(panjang_data)


print(f"data sebelum ditambah = {data_car}")
# menambahkan data baru pada list sesuai posisi(index)
data_car.insert(1, "Kijang Innova")
print(f"data sesudah ditambah = {data_car}")

# menambahkan data diakhir list
data_car.append("Rubicon")
print(f"data sesudah ditambah = {data_car}")

# menggabungkan list
data_baru = ["ferrari","jeep","lamborghini"]
data_car.extend(data_baru)
print(data_car)

# merubah data
data_car[5] = "Alphard"
print(data_car)

# menghapus data "huruf harus sesuai"
data_car.remove("ferrari")
data_car.remove("jeep")
data_car.remove("lamborghini")
print(data_car)

# meremove data paling akhir
data_akhir = data_car.pop()
print(data_car)

# mengakses data pop atau data yang diremove
print(data_akhir)