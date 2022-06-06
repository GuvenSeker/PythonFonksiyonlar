max_sayi = int(input("max sayi değerini girin"))
min_sayi = int(input("min sayi değerini girin"))
bolen_sayi = int(input("bolen sayi değerini girin"))
bolunecekler = []
tam_bolunenler = []

def bolme_islemi(max_sayi, min_sayi, bolen_sayi):

    while min_sayi <= max_sayi:
        bolunecekler.append(min_sayi)
        min_sayi += 1

    i = 0

    while i < len(bolunecekler):
        if 0 == (bolunecekler[i] % bolen_sayi):
            tam_bolunenler.append(bolunecekler[i])
            i += 1
        else:
            i += 1
    return (tam_bolunenler)

print(bolme_islemi(max_sayi, min_sayi, bolen_sayi))
