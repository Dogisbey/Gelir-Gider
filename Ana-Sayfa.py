print("Tekrar'dan Hoşgeldin")

#Günlük Para 
Para = int(input("Bugünkü Bakiyeni Gir: "))

#Gelir Hesaplama
print("Kalan Bakiyeniz:" + str(Para))
z = int((input)(("Gelirlerinizi Hesaplayın: ")))
Gelir = int(z) + Para
print("Gelirlerinizden Sonra Kalan Para: "  + str(Gelir))

#Gider Hesaplama
x = int(input("Giderlerinizi Yazın: "))
Gider = x
Kalan = Gelir - Gider
print("Giderlerinizden Sonra Kalan Bakiyeniz " + str(Kalan))

#Cevaplar
if Gelir > Gider:
    print("Gelirler Ve Giderlerinizi Olması Gerektiği Gibi ")
else:
    print("Bu Gün çok Fazla Harcama Yaptın Lütfen Daha Az Harcama Yap")


