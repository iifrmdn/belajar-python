# operasi list
data_angka = [1,10,3,4,5,6,9,4,8,6,2,1,4,9,6,4,2]
print(f"data angka = {data_angka}")


# count = menghitung jumlah atau banyak data
jumlah_data_4 = data_angka.count(4)
jumlah_data_6 = data_angka.count(6)

print(f"jumlah data 4 = {jumlah_data_4}")
print(f"jumlah data 6 = {jumlah_data_6}")

# ambil posisi data (index)
data_car = ["Avanza", "Fortuner", "Alphard", "Kijang Innova", "Pazero"]
index_fortuner = data_car.index("Fortuner")
index_pazero = data_car.index("Pazero")
print(f"index fortuner = {index_fortuner}")
print(f"index pazero = {index_pazero}")

# mengurutkan data list
# data numbers
print(f"data angka sebelum sort = {data_angka}")
data_angka.sort()
print(f"data angka sesudah sort = {data_angka}")

# data string
print(f"data string sebelum sort = {data_car}")
data_car.sort()
print(f"data car sesudah sort = {data_car}")

# mengurutkan dari akhir ke keawal
data_angka.reverse()
data_car.reverse()

print(f"data angka sesudah reverse = {data_angka}")
print(f"data car sesudah reverse = {data_car}")
