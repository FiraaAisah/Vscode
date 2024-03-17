bilangan = int(input("Masukkan bilangan: "))

if bilangan > 0:
    print("Bilangan {} adalah bilangan positif.".format(bilangan))
elif bilangan < 0:
    print("Bilangan {} adalah bilangan negatif.".format(bilangan))
else:
    print("Bilangan {} adalah nol.".format(bilangan))
