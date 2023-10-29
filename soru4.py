sayi = int(input("Sayı Giriniz: "))
adet = 0

for i in range(2, sayi):
    if sayi % i == 0:
        adet += 1

if adet == 0 and sayi > 1:
    print(sayi, "sayısı asaldır.")
else:
    print(sayi, "sayısı asal değildir.")