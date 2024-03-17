bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))
bilangan3 = int(input("Masukkan bilangan ketiga: "))

if bilangan1 == bilangan2 == bilangan3:
    print("Semua bilangan ({}, {}, {}) sama besar.".format(bilangan1, bilangan2, bilangan3))
elif bilangan1 > bilangan2 and bilangan1 > bilangan3:
    print("Bilangan pertama ({}) lebih besar.".format(bilangan1))
elif bilangan2 > bilangan1 and bilangan2 > bilangan3:
    print("Bilangan kedua ({}) lebih besar.".format(bilangan2))
elif bilangan3 > bilangan1 and bilangan3 > bilangan2:
    print("Bilangan ketiga ({}) lebih besar.".format(bilangan3))
else:
    print("Dua bilangan lebih besar dari yang lain.")
