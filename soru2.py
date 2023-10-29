def mukemmelsayimi(sayi):
    carpimtoplami = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            carpimtoplami += i

    return carpimtoplami == sayi

sayi = int(input("Bir sayı girin : "))

if mukemmelsayimi(sayi):
    print(sayi, "mükemmel bir sayıdır.")
else:
    print(sayi, "mükemmel bir sayı değildir.")