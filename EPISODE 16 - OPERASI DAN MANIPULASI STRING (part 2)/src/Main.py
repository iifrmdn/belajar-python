from cgi import print_form


alay = "aKu keCe AbiEEezZzZ"
print("Normal = " + alay)

# merubah ke uppercase
upper = alay.upper()
print("Upper = " + upper)

#merubah ke lowercase
lower = alay.lower()
print("Lower = " + lower)

# pengecekan upper case
is_upper = upper.isupper()
print(upper + " is Upper = " + str(is_upper))

# pengecekan lower case
is_lower = lower.islower()
print(lower + " is lower = " + str(is_lower))

# pengecekan judul
judul = "Young Mother"
is_judul = judul.istitle()
print(judul + " is title = " + str(is_judul))

# startswith dam endswith
awal = "Parabowo"
akhir = "Subianto"
nama_lengkap = awal + " "+  akhir
print(nama_lengkap)
cek_start = "Prabowo Subianto".startswith(awal)
print("diawali dengan " + awal + " = " + str(cek_start))

cek_start = "Prabowo Subianto".endswith(akhir)
print("diakhiri dengan " + akhir + " = " + str(cek_start))

# join() dan split()
nama_lengkap = ['arif', 'nur', 'ramadhan']
join = ' '.join(nama_lengkap)
print(join)

nama_lengkap = "arifonuroramadhan"
print(nama_lengkap.split("o"))

# alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10,"=")
print("'"+tengah+"'")

# menghilangkan strip()
remove = "tengah".strip("=")
print("'"+remove+"'")
