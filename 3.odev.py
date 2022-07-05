def kontrol(sayi):
    if (sayi < 0) & (sayi > 100):
        print("girmiş olduğunuz değer geçerli aralıkta değildir")
        sayi = int(input("Lütfen sınav notunu girin :"))

        kontrol(sayi)
    else:
        return sinav_sonucu.append(sayi)


sinav_sonucu = []

vize1 = float(input("1.Vize değerini giriniz "))
kontrol(vize1)
vize2 = float(input("2.Vize değerini giriniz "))
kontrol(vize2)
final = float(input("Final değerini giriniz "))
kontrol(final)

genel_not = (sinav_sonucu[0] * 30 / 100) + (sinav_sonucu[1] * 30 / 100) + (sinav_sonucu[2] * 40 / 100)

print("Genel not ortalamanız :", genel_not)

if (genel_not >= 90):
    print("AA")
elif (genel_not >= 85):
    print("BA")
elif (genel_not >= 80):
    print("BB")
elif (genel_not >= 75):
    print("CB")
elif (genel_not >= 70):
    print("CC")
elif (genel_not >= 65):
    print("DC")
elif (genel_not >= 60):
    print("DD")
elif (genel_not >= 55):
    print("FD")
else:
    print("FF")
