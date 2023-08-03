print("Kullanıcıdan 3 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın")

birler=["sıfır","bir","iki","üç","dört","beş","alti","yedi","sekiz","dokuz"]
onlar=["","on","yirmiz","otuz","kırk","elli","altmiş","yetmiş","seksen","doksan"]
yuzler=["","yüz","ikiyüz","üçyüz","dörtyüz","beşyüz","altıyüz","yediyüz","sekizyüz","dokuzyüz"]

def okunus(sayi):
    birinci=sayi%10
    ikinci=(sayi//10)%10
    ucuncu=sayi//100


    return yuzler[ucuncu]+" "+ onlar[ikinci]+" "+birler[birinci]

sayi=int(input("Sayi giriniz"))

print(okunus(sayi))
