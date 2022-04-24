# membuat program sederhana
data_mobil = []
while True:
    print("\nMasukan data baru!")
    mobil = input("masukan nama mobil : ")
    tahun = input("masukan tahun mobil : ")

    data_baru = [mobil,tahun]
    data_mobil.append(data_baru)

    # print(data_mobil)

    for index,mobil in enumerate(data_mobil):
        print(f"{index+1} | {mobil[0]} | {mobil[1]}")

    isLanjut = input("\napakah lanjut?(y/n)")

    if isLanjut == "n":
        break

print("\nPROGRAM SELESAI\n")