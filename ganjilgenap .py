bilangan = int(input("Masukkan bilangan: "))

if bilangan == 0:
    print("Bilangan 0 adalah nol.")
elif bilangan % 2 == 0:
    if bilangan > 0:
        print("Bilangan {} adalah bilangan genap positif.".format(bilangan))
    else:
        print("Bilangan {} adalah bilangan genap negatif.".format(bilangan))
else:
    if bilangan > 0:
        print("Bilangan {} adalah bilangan ganjil positif.".format(bilangan))
    else:
        print("Bilangan {} adalah bilangan ganjil negatif.".format(bilangan))
