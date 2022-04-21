# 1. menyambungkan string (concatenate)
nama_awal = "Arif"
nama_tengah = "Nur"
nama_akhir = "Ramadhan"

nama_lengkap = nama_awal + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang karakter = " + str(panjang))

# 3. mengecek karakter

nama = "Nur"
status = nama in nama_lengkap
print(nama + " ada di " + nama_lengkap + " = " + str(status))

nama = "Nur"
status = nama not in nama_lengkap
print(nama + " tidak ada di " + nama_lengkap + " = " + str(status))


# 4. mengulang string
print("wkwk"*10)
print(10*"hahah")

# 5. Indexing
print("Nilai indeks ke 0 adalah " + nama_lengkap[0])
print("Nilai indeks ke 1 adalah " + nama_lengkap[1])
print("Nilai indeks ke 2 adalah " + nama_lengkap[2])
print("Nilai indeks ke 3 adalah " + nama_lengkap[3])
print("Nilai indeks ke 4 adalah " + nama_lengkap[4])
print("Nilai indeks ke 5 adalah " + nama_lengkap[5])

print("Nilai indeks ke -1 adalah " + nama_lengkap[-1])
print("Nilai indeks ke -2 adalah " + nama_lengkap[-2])
print("Nilai indeks ke -3 adalah " + nama_lengkap[-3])
print("Nilai indeks ke -4 adalah " + nama_lengkap[-4])
print("Nilai indeks ke -5 adalah " + nama_lengkap[-5])
print("Nilai indeks ke -6 adalah " + nama_lengkap[-6])
print("Nilai indeks ke -7 adalah " + nama_lengkap[-7])
print("Nilai indeks ke -8 adalah " + nama_lengkap[-8])

# Range
print("Nilai indeks 0 ke 4 = " + nama_lengkap[0:4])

print("Nilai indeks ke-[0,2,4,6,8,10] = " + nama_lengkap[0:100:2])

# item paling kecil
print("Nilai paling kecil = " + min(nama_lengkap)) # " "
#item paling besar
print("Nilai paling besar = " + max(nama_lengkap))

# ascii code
ascii_code = ord(" ")
print("ASCII code untuk nilai spasi adalah " + str(ascii_code))

data = 117
print("Char untuk nilai 117 adalah " + chr(data))

data = "otong surotong montong popotong pararotong"
jumlah = data.count("o")
print("jumlah o pada " + data + " adalah " + str(jumlah))

