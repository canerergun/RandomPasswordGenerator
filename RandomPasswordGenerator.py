import random
import string


def parolaOlusturma(uzunluk=12):
    karakterler = string.ascii_letters + string.digits + string.punctuation
    parola = "".join(random.choice(karakterler) for i in range(uzunluk))
    return parola


# Parola uzunluğunu belirleyebilirsiniz! (varsayılan: 12)
parolaUzunlugu = int(input("Kaç karakterli parola istersin: "))
parolaOlusturma = parolaOlusturma(parolaUzunlugu)

print(f"Oluşturulan Parola: {parolaOlusturma}")
