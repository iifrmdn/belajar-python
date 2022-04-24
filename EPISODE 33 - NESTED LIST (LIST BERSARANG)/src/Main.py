data_0 = [0,1]
data_1 = [2,3]

data_biasa = [0,1,2,3]
print(f"data biasa = {data_biasa}")

# list 2d
list_2d = [data_0,data_1]
print(f"data list 2D = {list_2d}")

# list 2d campuran
list_2d = [data_0, data_1, data_biasa, 10, 11]
print(f"data list 2D = {list_2d}")

karakter1 = ["Alex",20,"Laki-laki"]
karakter2 = ["Kira",19,"Wanita"]
karakter3 = ["Sye",25,"Laki-Laki"]
karakter4 = ["Zed",40,"Laki-laki"]

list_karakter = [karakter1,karakter2,karakter3,karakter4]
print(list_karakter)

# menampilkan menggunakan for
for karakter in list_karakter:
    print(f"Nama : {karakter[0]}")
    print(f"Umur : {karakter[1]}")
    print(f"Jenis Kelamin : {karakter[2]}\n")
