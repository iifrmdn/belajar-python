# latihan date and time 

import datetime as dt
print(10*"="+"PROGRAM DATE AND TIME"+"="*10)
print("Masukan tanggal, bulan, dan tahun lahir anda dibawah!")

tanggal = int(input("Tanggal \t= "))  
bulan = int(input("Bulan \t\t= "))
tahun = int(input("Tahun \t\t= "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda = {tanggal_lahir}")
print(f"anda lahir pada hari = {tanggal_lahir:%A}")

hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
print(f"umur anda adalah : {umur_tahun} tahun")