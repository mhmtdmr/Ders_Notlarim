#################    Tuple    ################
# list'den farklı olarak ekleme çıkarma yapılamaz.
"""
sabitListe = ()
sabitListe = tuple()
sabitListe = (1,3,4,5,6,"A","B","C")

print(sabitListe)
print(sabitListe.index("A"))
print(sabitListe.count("B"))
print(len(sabitListe))
print(sabitListe[0])
del sabitListe  # sabitListe'yi ram/bellekten tamamen siler
#sabitListe[2] = 16 # atama gerçekleştirilemez!!!
"""


###########     Set: Küme     ##########
"""
kume = set() # boş küme tanımladık
kume = {}

kume = {11,22,33,44} # dolu küme tanımladık.

kume.add(55) #kümeye eleman ekleme
#kume.remove(11) #kümeden eleman silme.(eleman yoksa hata verir !)
kume.discard(11) #kümeden eleman çıkarma. (eleman yoksa hata vermez.)
kume.discard(11) #kümeden eleman çıkarma. (eleman yoksa hata vermez.)
kume.add(55) # kümeye aynı elemanı 2. kez eklemek anlamsızdır.
print(kume)

kume2 = {33,44,66,77,88,99}

kumeFark = kume-kume2 # İki küme farkı
kumeFark = kume.difference(kume2) # yukarıdaki satır ile aynı işi yapar
print("kume nin kume2'den farkı:",kumeFark)

kumeKesisim = kume & kume2 # İki küme kesişimi
kumeKesisim = kume.intersection(kume2)# yukarıdaki satır ile aynı işi yapar
print("kesişim kümesi:",kumeKesisim)

kumeBirlesim = kume.union(kume2)
print("kesişim birleşimi:",kumeBirlesim)

print(f"kume kumeBirlesim in alt kümesi mi?: {kume.issubset(kumeBirlesim)}")
print(f"kume kume2 nin üs kümesi mi?: {kume.issuperset(kume2)}")
print(f"kume kume2 ayrık kümeler mi?: {kume.isdisjoint(kume2)}")
"""
"""
1-15 arasında 5'er adet  sayı üretip 2 iki farklı kümeye kaydediniz.
Daha snra : iki küme farkını ekrana yazdırınız.
Bonus: Üretilen sayı kümelerde varsa tekrar üretilip atansın.
"""
"""
from random import randint
kume1 = set()
kume2 = set()
farkKumesi = set()

for i in range(5):
    while(True):
        sayi = randint(1,15)
        if(sayi not in kume1):
            kume1.add(sayi)
            break
        else:
            print("Bu sayı 1. kumede var: ",sayi)

    while(True):
        sayi = randint(1,15)
        if(sayi not in kume2):
            kume2.add(sayi)
            break
        else:
            print("Bu sayı 2. kumede var: ",sayi)
print(kume1)
print(kume2)
farkKumesi = kume1-kume2
print(farkKumesi)
"""

##################################     ALIŞTIRMALAR     ######################################

#SORU: 1-100 arasında rastgele 10 sayı üretip bir listeye atayın.
#Daha sonra bu listedeki en büyük ve en küçük elemanları hazır fonksiyon kullanmadan bulun.
"""
import random
liste = list()
for i in range(10):
    liste.append(random.randint(1,100))

kucuk = 100
buyuk = 0

for eleman in liste:
    if(eleman>buyuk):
        buyuk=eleman  # listedeki eleman buyukse en büyük onu kabul edelim her adımda.

    if(eleman<kucuk):
        kucuk=eleman

print(liste)
print(buyuk)
print(kucuk)
"""


