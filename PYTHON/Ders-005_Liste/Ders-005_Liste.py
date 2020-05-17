#################    Ders5: list()    ###################
"""
sayilar1 = []   # Boş bir liste tanımlamış olduk.
sayilar2 = list()  # Boş bir liste tanımlamış olduk.

sayilar3 = [0,1,2,3,4,5]  # Dolu bir liste tanımladık.

#print(sayilar3)      # tüm listeyi ekrana yazdırdık.
print(sayilar3[0])    # listenin ilk elemanına indis numarası ile eriştik. indis'ler 0'dan başlar.
print(sayilar3[3])    # listenin 4. elemanına eriştik.
"""
"""
sayiListe = [10,7,6,5,33,44,19]  # indis aralığı: 0-6
print(sayiListe[6]) #listenin 6. indisi yani 7. elemanını getirdik.
"""
'''
karisikListe = [34,"İstanbul",46,"Kahramanmaraş",58,"Sivas",61,"Trabzon"] #int ve str tipinde veriler olan bir liste

#listeye veri ekleme işlemleri
karisikListe += [60]   #listemize 60 elemanını ekledik.
karisikListe += ["Tokat"] # "Tokat" elemanını ekledik.


karisikListe.append(17) #listenin sonuna 17 değerini ekledik
karisikListe.append("Çanakkale")  #listeye "Çanakkale" değerini ekledik.
print(karisikListe)

#listeden veri silme işlemleri
karisikListe.remove(61)
karisikListe.remove("Trabzon")
print(karisikListe)

#indis ile silme.
del karisikListe[6] # 60 verisini sildik.
del karisikListe[6] # "Tokat" verisini sildik.

#çoklu eleman ekleme
karisikListe += [10,"Balıkesir",41,"Kocaeli"] #4 eleman ekledik.
print(karisikListe)
'''
"""
rakamlar = [1,2,3,7,8,9]
rakamlar.insert(0,0)    #0. indise 0 verisini ekledik.

print(rakamlar)
rakamlar.insert(4,4)
rakamlar.insert(5,5)
rakamlar.insert(6,6)
print(rakamlar)

#liste elemanının indis numarasına ulaşma

print("7 değerinin indisi: ",rakamlar.index(7))
"""
"""
sayilar = [10,20,30,40,20,20,20]

print(sayilar.index(10))   # ilk 10 değerinin indisini yazdır.
print(sayilar.index(20))   # ilk 20 değerinin indisini yazdır.
print(sayilar.index(20,2)) # 2. indisten başlayıp ara: ilk 20 değerinin indisini yazdır.
print(sayilar.index(20,5)) # 5. indisten başlayıp ara: ilk 20 değerinin indisini yazdır.
"""



"""
#print(len(sayilar)) # eleman sayısına ulaşma.
sayilar = [10,20,30,40,20,20,20]

print("Listedeki 20 adeti: ",sayilar.count(20)) #listede kaç tane 20 olduğunu yazdırır.
# Listedeki 20 elemanlarının indislerini ekrana yazdıran program.

indis = 0
for i in range(sayilar.count(20)):  # listedeki 20 adedinde döngü açtık.
    print(sayilar.index(20,indis))
    indis = sayilar.index(20,indis) + 1 # her seferinde son bulunan indisten 1 sonraki indisten aramaya başlaması için.
"""

"""
listem = ["Manisa","Çanakkale","Kocaeli","Konya","Sivas","Gaziantep"]
print(listem[-1])  #-1 indisi son elemanı temsil eder.
print(listem[-2])  #sondan 2. elemana ulaşmak için.
print(listem)
listem.sort()  # liste elemanlarını küçükten büyüğe sıralar. (harf-sayı)
print(listem)
listem.reverse() #elemanları terse çevirir.
print(listem)
"""

"""
sayilar = [10,20,30,40,50]
soneleman = sayilar.pop()  # listedeki son elemanı listede çıkarark getirir.
print(soneleman)
print(sayilar)
eleman3 =sayilar.pop(2) #3. elemanı al ve listeden çıkar.
print(eleman3)
print(sayilar)
"""
"""
rakamlar = [1,4,5,6,7,8]
kontrol = 5 in rakamlar # 5 rakamlar listesinde varsa True yoksa False değerini alır.

if(5 in rakamlar):
    print("5 rakamlar listesinde vardır")
"""

"""
harfler = ["a","c"]
harfler += ["ç"]  # sona ekleme
harfler += ["d","e"] # sona birden fazla ekleme
harfler.insert(1,"b") # araya eleman ekleme. 1. indise değer ekleme
harfler[2:2] = ["o"]*3 # o elemanını 2. indisten başlayıp 3 adet ekle.
print(harfler)
"""
"""
list1 = [1,2,3]
list2 = [4,5,6]
listeler = list1+list2
print(listeler)
print(min(listeler))
print(max(listeler))
print(f"listeler deki sayıların toplamı: {sum(listeler)}")
"""
"""
rakamlar = [i for i in range(10)] # 0-9 aralığındaki değerleri liste olarak atar.
print(rakamlar)

# 10 ile 100 arasındaki çift sayıları bir listeye atayın.

ciftliste_10_100 = [i for i in range(10,101,2)]
print(ciftliste_10_100)

print(f"Rakamlar listesinde 7 var mı? Cevap: {7 in rakamlar}") #True/False
print(f"ciftliste_10_100 listesinde 21 var mı? Cevap: {21 in ciftliste_10_100}")
"""
"""
liste1 = [11,22,33]
#liste2 = liste1     #ram/bellekteki adresleri eşitler.
# Yani yeni bir liste oluşturulmadan aynı listeye farklı bir isim daha vermiş oluruzç

liste2 = liste1.copy() # liste2 için ram/bellekte yeni bir alan oluşturularak.
# liste1 deki veriler buraya kopyalanır.
print(liste1)
print(liste2)

liste1.append(44)

print(liste1)
print(liste2)

print(f"liste1 nesnesinin bellekteki adresi: {id(liste1)}")
print(f"liste2 nesnesinin bellekteki adresi: {id(liste2)}")
"""

"""
cokBoyutlu = [[1,3,5],[7,8,9]] # 2x3 lük bir dizi oluşturduk.

[1,3,5]
[7,8,9]
"""
"""
print(cokBoyutlu[0][0]) #1
print(cokBoyutlu[1][0]) #7
print(cokBoyutlu[0][1]) #3
print(cokBoyutlu[1][1]) #8
print(cokBoyutlu[0][2]) #5
cokBoyutlu[1][2]=58 # dizideki değeri değiştirme.
print(cokBoyutlu[1][2])
"""
#cokBoyutlu2 = [0]*5  # elemanları 5 tane 0 olan bir liste oluşturan kod.
"""
cokBoyutlu2 = [0, 0, 0, 0, 0]
"""
"""
satir = 5
sutun = 3
cokBoyutlu2
for i in range(satir):
    cokBoyutlu2[i] = [0] * sutun
"""

"""
#nxn lik bir liste oluşturma
satir = 3
sutun = 4
cokBoyutlu = [0]*satir
#print(cokBoyutlu)
for i in range(satir):
    cokBoyutlu[i] = [0]*sutun
print(cokBoyutlu)

# Yukarıdaki işlemin tek satırlı hali.
cokBoyutlu2 = [[0]*sutun for i in range(satir)]
print(cokBoyutlu2)
"""

#######################################      ALIŞTIRMALAR     ##############################################

#SORU: Kullanicidan 10 sayı alıp bir listeye atın ve sonra listenin aritemetik ortalamasını bulun.
"""
liste = list()
toplam = 0

for i in range(10):

    sayi = int(input("Sayı giriniz:")) # girilen değeri int'e çevirdik.
    print("Girilen sayı",sayi)
    liste.append(sayi)  # girilen değeri listeye ekledik.
    toplam += sayi # her sayıyı toplama eklemiş olduk.

print("Sayıların ortalaması: ",(toplam/len(liste)))
"""

# 1: 1-100 arasında 20 adet sayı üretip bir listeye atınız.
"""
###   1:
import random
sayilar = []

for i in range(5):
    sayi = random.randint(1,10)
    sayilar.append(sayi)
print("Liste oluşturuldu.")

sayilar.sort()
print(sayilar)
"""

# 2: Sonra kullanıcıya 3 tahmin hakkı verip listeden 1 sayı tutturabileceği bir tahmin oyunu yazınız.
"""
###  2:

for i in range(3):
    tahmin = int(input("Tahmininiz:"))
    if(tahmin in sayilar):
        print("Tebrikler buldunuz.")
    else:
        print("Bu sayı listede yok !")

"""

# 3: Listedeki asal sayıları asallar isminde başka bir listeye atayan kodu yazınız.
"""

###  3:
asallar = []
for eleman in sayilar:
    asalMi=True
    if(eleman<2):
        continue
    for bolen in range(2,eleman):
        if(eleman%bolen==0):
            asalMi=False
            break
    if(asalMi):
        asallar.append(eleman)
print(asallar)

# 7   =>  2,3,4,5,6 sayılarından birisine tam bölünürse asal değildir. Hiçbirine tam bölünmezse asaldır.
"""
## ASAL SAYI BULMA KODU
"""
sayi = 5
asalMi=True

for bolen in range(2,sayi):
    if(sayi%bolen==0):
        asalMi=False
        break

if(asalMi==True):
    print("Sayı asaldır.")
else:
    print("Sayı asal değildir.")

"""



# SORU: 1-200 arasında 20 sayı üretip bunu sayilar isimli listeye atadıktan sonra.
#import random
"""
from random import randint  #dosya ismi belirtmeden kullanabilmek için.
sayilar = []
tekler = []
ciftler = []

for i in range(20):
    #sayi = random.randint(1,200)
    sayi = randint(1, 200) #dosya ismi belirtmeden kullandık.
    sayilar.append(sayi)
"""

# Farklı döngüde bu listedeki tek ve çift sayıları ayrı 2 listeye atan programı yazınız.
"""
for i in range(len(sayilar)):  # sayilar listesinin eleman sayısı kadar dönen döngü.
    #print(f"{i+1}. sayı {sayilar[i]}")
    if(sayilar[i]%2==0):
        ciftler.append(sayilar[i])
    else:
        tekler.append(sayilar[i])
"""
# listeler: sayilar,tekler,ciftler
"""
for eleman in sayilar: # sayilar listesinin elemanlarını teker teker değerlendirdik.
    if(eleman%2==0):
        ciftler.append(sayilar[i])
    else:
        tekler.append(sayilar[i])

print(sayilar)
print(tekler)
print(ciftler)
"""

# SORU: Klavyeden alınan 5 kelimeyi bir listeye atan.
#     : Girilen 6 kelimenin bu listede olup olmadığını ekrana yazdıran program.
"""
kelimeler = []
sayac = 1
while(sayac<=5):
    kelime = input("Kelime yazınız:")
    kelimeler.append(kelime)
    sayac += 1

arananKelime = input("Hangi kelimeyi arıyorsunuz?:")

if(arananKelime in kelimeler):
    print(f"{arananKelime} listede mevcut.")
else:
    print(f"{arananKelime} listede yok.")

"""


#Örnek: 4x4'lük 0'lardan oluşan bir matris oluşturun(liste)
# 1. satırı 1-100 arası rastgele sayılardan oluşturunuz.
# 2. satırı Kullanıcıdan alınız.
# 3. satırda 1. satırın karelerini saklayınız.
# 4. satırda 2. satırdaki verilerin 5'er fazlasını saklayınız.

"""
Açıklama Amaçlı
li1 = [[5,10,15],[20,25,30]]

print(li1[0]) #5,10,15  li1[0][0] = 5
print(li1[1]) #20,25,30
"""
"""
import random
satir = 4
sutun = 4

matris = [0]*satir
#print(matris)
for i in range(satir):
    matris[i] = [0]*sutun
#print(matris)
for x in range(satir):
    for y in range(sutun):
        if(x==0):
            rast = random.randint(1,100)
            matris[x][y] = rast
        elif(x==1):
            sayi = int(input("Sayı giriniz:"))
            matris[x][y] = sayi
        elif(x==2):
            matris[x][y] = (matris[0][y])**2
        elif(x==3):
            matris[x][y] = (matris[1][y])+5

for x in range(satir):
    for y in range(sutun):
        print(matris[x][y],end="  ")
    print() # her satır bittiğinde alt satıra geçsin
"""



#SORU1: Klavyeden -1 girilene kadar
# girilen sayıları bir listeye atın. Ve listeyi sıralayarak ekrana yazın.
"""
sayilar = list() # aldığım değerleri atayacağım listeyi oluşturdum.
while True:
    sayi = int(input("Sayı giriniz:"))
    if sayi == -1:
        break
    else:
        sayilar+= [sayi]
sayilar.sort()
print(sayilar)
"""
#SORU2: SORU1'de alınan listedeki çift sayıları listeleyen listeyi oluşturun.
"""FOR İLE
ciftSayilar = []
for sayi in sayilar:
    if sayi%2==0:
        ciftSayilar+=[sayi]

print("Listedeki çift sayılar",ciftSayilar)
"""
"""WHILE İLE
boyut = len(sayilar)
cSayilar = []
i = 0
while (i<boyut):
    if (sayilar[i] % 2)==0:
        cSayilar += [sayilar[i]]
    i += 1
print("Listedeki çift sayılar",cSayilar)
"""
# Ekrana aşağıdaki çıktıyı yazdırın.
"""
1
22
333
4444
55555
666666
7777777
88888888
999999999


"""
"""
# KISA YÖNTEM
for i in range(1,10):
    print(str(i)*i)

# UZUN YÖNTEM

for i in range(10):
    for j in range(i):
        print(i,end="") # end="" alt satıra atmaması için.
    print() # alt satıra atlamak için.
"""




# 1-50 arasında 15 adet sayı üretip bir listeye atın.
# Listedeki sayıların toplamını ve ortalamasını bulun.

"""
import random
sayiListesi = []
for i in range(15):
    rast = random.randint(1,50)
    sayiListesi.append(rast)

toplam=0
for sayi in sayiListesi:
    toplam += sayi

print("Toplam:",toplam)
print("Ortalama:",(toplam//(len(sayiListesi))))
"""

#Yukarıdaki soruya ek olarak üretilen sayıların faktörüyelini ayrı bir listede tutun.
"""
import random
sayiListesi = []
faktoriyelListesi = []
for i in range(15):
    rast = random.randint(1,5)
    sayiListesi.append(rast)

    carpim = 1
    for j in range(1,rast+1):
        carpim *= j
    faktoriyelListesi.append(carpim)


print(sayiListesi)
print(faktoriyelListesi)

print("Sayı Listesi Eleman Sayısı:",len(sayiListesi))
print("Faktöriyel Listesi Eleman Sayısı:",len(faktoriyelListesi))
"""