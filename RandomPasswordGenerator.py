import random
import string
import sys

def parola_olusturma(uzunluk=12):
    karakterler = string.ascii_letters + string.digits + string.punctuation
    parola = "".join(random.choice(karakterler) for _ in range(uzunluk))
    return parola

while True:
    parola_uzunlugu = int(input("Kaç karakterli parola istersin: "))
    parola = parola_olusturma(parola_uzunlugu)
    print(f"Oluşturulan Parola: {parola}")


    #Çıkmak için
    kapat = input('Çıkmak için (E/H): ').upper()

    if kapat == 'E':
        sys.exit()