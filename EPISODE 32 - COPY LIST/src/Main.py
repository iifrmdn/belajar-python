# copy list

car1 = ["Alphard", "Pazero", "Xpander"]

car2 = car1

# merubah data car
print("="*10+"cara salah"+"="*10)
car2[0] = "Avanza" # merubah data car2 merubah data car juga
print(f"data car1 = {car1}")
print(f"data car2 = {car2}")

# addres dari kedua data 
print("addres lama")
print(f"addres dari data car1 = {hex(id(car1))}")
print(f"addres dari data car2 = {hex(id(car2))}") # kedua address data sama

# cara menduplikat data yang benar menggunakan .copy()
car1 = ["Alphard", "Pazero", "Xpander"]
car3 = car1.copy()
print("addres baru")
print(f"addres dari data car1 = {hex(id(car1))}")
print(f"addres dari data car2 = {hex(id(car2))}") 
print(f"addres dari data car3 = {hex(id(car3))}") 

# merubah data car3
print("="*10+"cara benar"+"="*10)
car1 = ["Alphard", "Pazero", "Xpander"]
car3[1] = "Avanza"
print(f"data car1 = {car1}")
print(f"data car3 = {car3}")


