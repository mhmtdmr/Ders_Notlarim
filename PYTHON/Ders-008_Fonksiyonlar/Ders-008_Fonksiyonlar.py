######################################      FONKSİYONLAR     ############################################

"""
Programımızda belirli bir işi yapan kod bloklarının tekrar kullanılması durumunda tekrar yazılmadan çağırılmasını sağlayan modüllerdir.
Yani bir modülü 1 defa tanımlayıp istediğimiz kadar kullanabilmemizi sağlar.
Fonksiyonlar yazdığımız programın modüler olmasını sağlar, ayrıca okunabilirliği artırır.
"""

# Fonksiyon çağırıldığı yerden önce tanımlanmalıdır.
"""
def fonksyiyonismi(varsa parametre):
        #Fonksiyon içinde çaalışacak kodlar
"""
# şeklinde tanımlanır.


#Fonksiyonu tanımladık.
def MerhabaYaz():
    print("Merhaba Dünya")


#Fonksiyonu çağırdık.(2 defa çalıştırmış olduk)
MerhabaYaz()
MerhabaYaz()

# Parametre alan fonksiyon tanımladık.
def Topla(s1,s2):
    sonuc = s1+s2
    print("Toplama sonucu:",sonuc)
# Parametreli fonksiyonu çağırdık.
Topla(48,52)




##########      ALIŞTIRMALAR (Parametresiz ve parametreli değer döndürmeyen fonksiyonlar)     #########

# 2 sayı 1 işlem alıp sonucu ekrana yazdıran fonk.
def DortIslem(s1,s2,islem):
    if(islem=='+'):
        sonuc=s1+s2
    elif(islem=='-'):
        sonuc=s1-s2
    elif(islem=='*' or islem=='x'):
        sonuc=s1*s2
    elif(islem=='/'):
        if(s2==0):
            sonuc= "Bölen 0 olamaz kardeş!!!"
        else:
            sonuc=s1/s2
    print(sonuc)

DortIslem(13,5,'+')
DortIslem(13,5,'-')
DortIslem(13,5,'/')
DortIslem(13,5,'x')

#Kendisine gönderilen ismi kendisine gönderilen sayı kadar ekrana yazdıran program.
def CokYazdir(isim,sayi):
    for i in range(sayi):
        print(isim)
CokYazdir('Mahir',5)


#Kendisine gönderilen sayı adedince klavyeden isim alıp listeye atan program.
def isimListesiAl(sayi):
    for i in range(sayi):
        isim = input("isim:")
        isimler.append(isim)
isimler = list()
isimListesiAl(5)
print(isimler)

# Kendisine gönderilen sayının  tek mi çift mi olduğunu ekrana yazdıran fonksiyonu yazınız.
def TekmiCiftMi(sayi):
    if(sayi%2==0):
        print(sayi,"çifttir.")
    else:
        print(sayi,"tektir.")
TekmiCiftMi(7665169)

# Parametre olarak aldığı listedeki tek elemanları yazdıran fonksiyonu yazınız.
def ListeninTekleri(listem):
    for eleman in listem:
        if(eleman%2==1):
            print(eleman)

listem = {1,2,3,4,5}
ListeninTekleri(listem)

# Belirsiz sayıda aldığı parametreler ile işlem yapan fonksiyon.
def CokluGoster(*sayilar):
    for i in sayilar:
        print(i)

CokluGoster(2,3,4)
CokluGoster(12,12,12,321,456,899,123)


# Kendisine gönderilen karakter,en,boy  parametrelerine göre ekrana
# karakterden dikdörtgen çizen programı yazınız. en boy'a göre.
"""
DikdortgenCiz("o",10,5)

oooooooooo
oooooooooo
oooooooooo
oooooooooo
oooooooooo

"""
"""
def DikdortgenCiz(karakter,en,boy):
    for i in range(boy):
        print(karakter*en)

DikdortgenCiz("*",10,3)
"""



# DEĞER DÖNDÜREN FONKSİYONLAR

kare4 = pow(4,2)
print("4'ün karesi:",kare4)

def kuvvet(sayi,us):
    sonuc = sayi**us
    return sonuc   # Sonucu döndürmek için.

kare4_2 = kuvvet(4,2)
print("4'ün karesi:",kare4_2)

# Kendisine gönderilen 4 sayının ortalamasını döndüren gonksiyonu yazınız.
def Ortalama(s1,s2,s3,s4):
    return (s1+s2+s3+s4)//4

print(Ortalama(10,20,30,40))


# Kendisine gönderilen listedeki sayıların aritmetik ortalamasını bulan program.
def ListeOrtalama(liste):
    toplam=0
    sayac=0
    for s in liste:
        toplam += s
        sayac += 1
    return toplam//sayac

liste = [14,15,18,19,12,13,25,45,65,85]
print("Liste ortalaması",ListeOrtalama(liste))


# Soru: Kendisine parametre olarak gönderilen sayının faktörüyelini hesaplayıp döndüren fonksiyonu yazınız.
#faktoriyel(5) => 120      f= 5*4*3*2*1   f= 1*2*3*4*5

def faktoriyel(sayi):
    carpim=1
    for s in range(1,sayi+1): # range(sayi,1,-1): gelen sayıdan 1 e kadar 1 er 1 er azalt.
        carpim*=s
    return carpim

f = faktoriyel(45)
print("45 sayısının faktörüyeli:",f)


# Kendisine gönderilen sayının asal olup olmadığını döndüren fonksiyonu yazınız.
# Asalsa: True değilse: False
# Asal Değil :2'den sayının 1 eksiğine kadar olan sayılardan herhangi biri ile tam bölünüyor mu?

def AsalMi(sayi):
    if(sayi==1):
        return False
    if(sayi==2):
        return True
    for  i in range(2,sayi):
        if(sayi%i==0):
            return False
    return True
#AsalMi(78)?"Doğru":"Yanlış"

if(AsalMi(78)):
    durum="78 Asaldır"
else:
    durum="78 Asal Değildir"
print(durum)



"""
c=100
def Ornek(a,b):
    return a*b*c #global değişkene erişilir.

print(Ornek(5,4))
"""

#bir fonksiyon içinde başka bir fonksiyon çağırmak mümkündür.

# Parametre olarak aldığı 2 sayıdan büyük olanı döndüren fonksiyon
def buyuk2(a,b):
    if(a>b):
        return a
    if(b>a):
        return b
    if(a==b):
        return a
# Parametre olarak aldığı 3 sayıdan büyük olanı döndüren fonksiyon
def buyuk3(x,y,z):
    return buyuk2(x,buyuk2(y,z))






## Tek satırda fonksiyon tanımlama
kare = lambda s:s*s # tek satır fonksiyon

topla = lambda a,b:a+b #önce parametreler,sonra sonucu döndürülecek işlem

print("lambda dan gelen kare 5: ",kare(5))
print("lambda'dan gelen toplama:",topla(14,74))

# import ile modül kullanımı.

import Matematik

sonuc = Matematik.Topla(3,4)
print(sonuc)

from Matematik import *

sonuc = Topla(5,6)
print(sonuc)


#####   import Alıştırma   #####


# Kendi isminiz ile bir modül oluşturup
# Modül içerisinde sansur(cumleListesi,yasakKelime,yeniKelime) isminde bir metot oluşturun.
# Bu metot kendisine gönderilen cümle listesinde ve yasaklı kelimeye göre sansürleme yapacak.
# sansur("Çocuklar kahve içerse kararır.","kahve","k")

#Ders9.py dosyasında input ile aldığımız 3 metnin sağında ve solundaki boşlukları silip.
#bir listeye atın.
#import Sansur
"""
from Sansur import sansur
cumleler=[]
for i in range(3):
    cumle = input("Cumle giriniz:")
    cumle=cumle.strip()
    cumleler.append(cumle)

yeniListe = sansur(cumleler,"kahve","K")
print(yeniListe)
"""
import webbrowser as web

from os import name
print(name)


#web.open("www.ucuncubinyil.com")

# Soru: Klavyeden alınan cümledeki aranan kelimenin yarısını "yok" olarak değiştiren
# fonksiyon. cumleDegistir(cumle,kelime):
#                   return cumle
"""
cumle = input()
cumleDegistir(cumle,"test")
"""
def cumleDegistir(cumle,kelime):
    sayi=cumle.count(kelime)/2
    cumle = cumle.replace(kelime,"yok",sayi)
    return  cumle
yaz=input("Cümle:")

print(cumleDegistir(yaz,"A"))