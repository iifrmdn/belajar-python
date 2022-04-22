# menggunkan while

batas = 5
count = 1

while True:
    # akan print jika ganjil
    if count%2:
        print("*"*count)
        count+=1
    else:
        # akan continue jika genap
        count += 1
        continue

    # akan break jika melebihi batas
    if count > 5:
        break
