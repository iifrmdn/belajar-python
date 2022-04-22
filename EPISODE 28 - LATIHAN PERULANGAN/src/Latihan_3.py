# membuat segitiga

batas = 10
spasi = int(batas/2)
count = 1

while True:
    if count%2:
        print(" "*spasi,"*"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue

    if count > batas:
        break