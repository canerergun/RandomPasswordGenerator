# Parola Oluşturma Kodu

Bu Python kodu, rastgele parolalar oluşturmak için kullanılır.

## Kod Açıklaması

Bu kod, belirli bir uzunluktaki rastgele parolaları oluşturmak için bir fonksiyon içerir. `parolaOlusturma` adlı bu fonksiyon, varsayılan olarak 12 karakter uzunluğunda parolalar oluşturur. Parolalar, harf, rakam ve özel karakterlerden oluşur.

Kullanıcıdan parola uzunluğunu girmesi istenir. Ardından, girilen uzunlukta bir parola oluşturulur ve ekrana yazdırılır.

## Örnek Kullanım

Parola uzunluğunu belirleyerek `parolaOlusturma` fonksiyonunu çağırabilirsiniz. Örneğin:

```python
parolaUzunlugu = int(input("Kaç karakterli parola istersin: "))
parola = parolaOlusturma(parolaUzunlugu)
print(f"Oluşturulan Parola: {parola}")
```

## Notlar

- Kod, harf, rakam ve özel karakterler içeren güçlü parolalar oluşturur.
- Parola uzunluğunu kullanıcı belirleyebilir.

## Lisans

Bu kod [MIT lisansı](https://opensource.org/licenses/MIT) altında sunulmuştur.
