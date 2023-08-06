print("Tam Bölen Bulma")

def tambolmebulma(sayi):
    tambolenler=list()

    for i in range(2,sayi):
        if(sayi%i==0):
            tambolenler.append(i)
    return tambolenler


while True:
    sayi=input("Sayiyi giriniz")
    if(sayi=="q"):
        print("Tam Bölen Bulma Programından Çıkılıyor")
        break
    else:
        sayi=int(sayi)
        print(sayi,"tam bölenler",tambolmebulma(sayi))
