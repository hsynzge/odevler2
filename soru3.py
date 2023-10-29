sayi1=int(input("Birinci sayıyı giriniz : "))
sayi2=int(input("Ikıncı sayıyı giriniz : "))

if(sayi1>sayi2):
    kucuksayi=sayi2
else:
    kucuksayi = sayi1
for i in range(1,kucuksayi+1):
    if(sayi1 % 1 ==0) and (sayi2 % 1 ==0):
        ebob=1
        ekok=(sayi1*sayi2)//ebob

print("Girdiğiniz sayıların ebobu : ",ebob)
print("Girdiğiniz sayıların ekoku : ",ekok)