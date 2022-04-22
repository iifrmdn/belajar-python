# LIST

# kumpulan data numbers
data_angka = [1, 2, 3, 4, 5, 6, 7]
print(data_angka)

# kumpulan data string
data_string = ["pazero", "fortuner", "avanza", "xpander"]
print(data_string)

# kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# kumpulan data campuran
data_campuran = [1, "pazero", True, 2, "kijang", False]
print(data_campuran)

# cara alternatif membuat list
data_range = range(0, 10, 2)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop list compherension
datalist_for = [i for i in range(0,10)]
print(datalist_for)
datalist_for = [i**2 for i in range(0,10)]
print(datalist_for)

# membuat list pake for dan if
data_for_if = [i for i in range(0,10) if i != 5]
print(data_for_if)

# ganjil
data_for_if = [i for i in range(0, 10) if i%2 != 0]
print(data_for_if)

# genap
data_for_if = [i for i in range(0, 9) if i%2 == 0]
print(data_for_if)