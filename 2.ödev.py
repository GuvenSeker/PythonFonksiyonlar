def sayi_atama(sayi):
    if sayi > 100:
        print("girmiş olduğunuz değer geçerli aralıkta değildir")
        sayi = int(input("Lütfen iki basamaklı bir sayı girin :"))

        sayi_atama(sayi)

    elif sayi < 10:
        print("girmiş olduğunuz değer geçerli aralıkta değildir")
        sayi = int(input("Lütfen iki basamaklı bir sayı girin :"))

        sayi_atama(sayi)

    else:
        birler_basamagi = sayi % 10
        onlar_basamagi = sayi // 10

        return sayi_okunusu(birler_basamagi, onlar_basamagi)


def sayi_okunusu(birler, onlar):
    birler_okunusu = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
    onlar_okunusu = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]

    print(onlar_okunusu[onlar] + " " + birler_okunusu[birler])


sayi = int(input("Sayı:"))
sayi_atama(sayi)
