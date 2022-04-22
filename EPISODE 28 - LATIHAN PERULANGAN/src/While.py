# menggunakan while

batas = int(input("Masukan jumlah sisi : "))
count = 1

while True:
    print("*"*count)
    count += 1

    if count > batas:
        break