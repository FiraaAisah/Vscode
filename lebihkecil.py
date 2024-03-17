bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))
bilangan3 = int(input("Masukkan bilangan ketiga: "))

if bilangan1 <= bilangan2 and bilangan1 <= bilangan3:
    print("Bilangan pertama ({}) lebih kecil.".format(bilangan1))
elif bilangan2 <= bilangan1 and bilangan2 <= bilangan3:
    print("Bilangan kedua ({}) lebih kecil.".format(bilangan2))
else:
    print("Bilangan ketiga ({}) lebih kecil.".format(bilangan3))
