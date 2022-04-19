print("PROGRAM KONVERSI TEMEPRATUR\n")

celcius = float(input("Masukan suhu dalam celcius : "))
print("Data dalam celcius : ", celcius)

# konversi ke reamur
reamur = (4/5) * celcius
print("Reamur : ", reamur)

# konversi ke fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Fahrenheit : ", fahrenheit)

# konversi ke kelvin
kelvin = celcius + 273
print("Kelvin : ", kelvin)