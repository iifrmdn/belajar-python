data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0,data_1]
print(f"data = {data_2D}")

data = data_2D[0][0]
print(data)
data = data_2D[0][1]
print(data)
data = data_2D[1][0]
print(data)
data = data_2D[1][1]
print(data)

data_2D_copy = data_2D.copy()

print(f"address data asli = {hex(id(data_2D))}")
print(f"address data copy = {hex(id(data_2D_copy))}")

# addres data member atau list didalam sama saja 
print("addres dalam/jero menggunakan copy biasa :")
print(f"address data member asli = {hex(id(data_2D[0]))}")
print(f"address data member copy = {hex(id(data_2D_copy[0]))}") 

# merubah data asli member bukan copy
data_2D[0][0] = 0
data_2D[0][1] = 0

print(data_2D)
print(data_2D_copy) # data copy dalam member ikut berubah

# kita gunakan deepcopy
print("Menggunakan deepcopy : ")
from copy import deepcopy

data_2D = [data_0,data_1]
data_2D_deepcopy = deepcopy(data_2D)

print(f"address data asli = {hex(id(data_2D))}")
print(f"address data deepcopy = {hex(id(data_2D_deepcopy))}")

print("addres dalam/jero menggunakan deepcopy :")
print(f"address data asli = {hex(id(data_2D[0]))}")
print(f"address data deepcopy = {hex(id(data_2D_deepcopy[0]))}")

print(data_2D)
print(data_2D_deepcopy)