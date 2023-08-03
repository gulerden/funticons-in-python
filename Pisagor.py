print("1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın")

def PisagorBulma():
    pisagor=list()

    for i in range(1,101):
        for x in range(1,101):

            c= (i**2 +x**2)**0.5

            if(c==int(c)):

                pisagor.append((i,x,int(c)))

    return pisagor

for i in PisagorBulma():

    print(i)