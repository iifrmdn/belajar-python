print(18*"=")
print("PROGRAM KALKULATOR")
print(18*"=")
angka1 = float(input("masukan angka pertama : "))
operator = input("masukan operaotor +,-,x,/ : ")
angka2 = float(input("masukan angka kedua : "))

if operator == "+":
    hasil = angka1 + angka2
    print(f"hasilnya adalah = {int(hasil)}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"hasilnya adalah = {int(hasil)}")
elif operator == "x" or operator == "*":
    hasil = angka1 * angka2
    print(f"hasilnya adalah = {int(hasil)}")
elif operator == "/":
    hasil = angka1 / angka2
    print(f"hasilnya adalah = {int(hasil)}")
else:
    print("operator salah!")
