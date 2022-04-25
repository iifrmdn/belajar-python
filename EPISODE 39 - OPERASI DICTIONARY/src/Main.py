# operator dictionary

data_dict = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung"
}

print(data_dict)

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang data = {LENDICT}")

# mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah '{KEY}' ada di data dict = {CHECKKEY}")

# mengakses value(read) dengan get()
print(data_dict.get("cup"))
# secara default ketika menggunakan get data tidak ada akan muncul None
print(data_dict.get("dang")) 
# kita bisa ganti None dengan pesan yang kita inginkan
print(data_dict.get("dang","data tidak ditemukan")) 

# merubah data
data_dict["cup"] = "ucup siricup"
print(data_dict)
data_dict["cup"] = "ucup surucup"
print(data_dict)

# menambah data
data_dict["dang"] = "dadang suradang"
print(data_dict)

 # mengupdate data
data_dict.update({"tang":"atang suratang"})
print(data_dict)

# menghapus data
del data_dict["tang"]
print(data_dict)
