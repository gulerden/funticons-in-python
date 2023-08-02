print("""Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

""")

def EbobBulma(sayi1,sayi2):
    ebob=1
    i=1
    while(i<=sayi1 and i<=sayi2):
        if (not (sayi1 % i) and not (sayi2 % i)):
            ebob=i
        i+=1
    return ebob



sayi1=int(input("1. Sayiyi Giriniz"))
sayi2=int(input("2. Sayiyi Giriniz"))

print("EBOB:",EbobBulma(sayi1,sayi2))