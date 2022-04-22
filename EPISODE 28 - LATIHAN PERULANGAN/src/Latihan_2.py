# latihan perulangan

batas = 5
count = 1

while True:
    if count%2:
        # print jika genap
        count += 1
        print("*"*count)
    else:
        # lewat jika ganjil
        count += 1
        continue

    # akan berhenti jika melebihi batas
    if count > batas:
        break