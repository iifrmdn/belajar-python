# contoh generic

# string
from asyncio import format_helpers


nama = "iif"
format_str = f"hello {nama}"
print(format_str)

# angka
angka = 2019
format_str = f"angka = {angka}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 10000
format_str = f"ribuan = {angka:,}"
print(format_str)


# bilangan desimal 
angka = 1000.421723
format_str = f"desimal = {angka:.2f}"
print(format_str)

# menampilkan tanda + dan -
angka_plus = 10.24492
angka_minus = -10
format_plus = f"plus = {angka_plus:+.2f}"
format_minus = f"minus = {angka_minus:+d}"

print(format_plus)
print(format_minus)

# memformat persen
persen = 0.045
format_persen = f"persen = {persen:.1%}"
print(format_persen)

# melakukan opersai aritmatika
harga = 10000
jumlah = 4
format_total = f"total = Rp.{harga*jumlah:,}"
print(format_total)

# format angka binary oct hex 
angka = 34
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}" 
format_hexa = f"hexa = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hexa)