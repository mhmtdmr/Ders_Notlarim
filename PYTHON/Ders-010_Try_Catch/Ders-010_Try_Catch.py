
###      TRY CATCH
"""
try:
    #Hata oluşturma ihtimali olan kodlar
except:
    #Hata oluşması durumunda çalıştırılacak kod bloğu.
"""

## sayi1 = int(input("Sayı1 'i giriniz:")) # Değer olarak ELLİBEŞ yaazdık hata aldık.
"""
try:
    sayi1 = int(input("Sayı1 'i giriniz:"))
except:
    print("Sayı1'i girerken hata yaptın")
"""
# Sayının doğru girilmesini sağlayan kod.
while(True):
    try:
        sayi1 = int(input("Sayı1 'i giriniz:"))
        break #Hatasız girilmişse
    except:  # Tüm hata durumlarında aşağıdaki kod bloğu çalışsın.
        pass
        print("Sayıyı doğru dürüst gir.!!!")

while(True):
    try:
        sayi2 = int(input("Sayı2 'i giriniz:"))
        break #Hatasız girilmişse
    except ValueError:   # Sadece değerden kaynaklı hata durumlarında aşağıdaki kod bloğu çalışsın.
        pass
        print("Sadece rakamlardan oluşan değer giriniz...!!!")
    except MemoryError:  # Sadece bilgisayar belleği kaynaklı hata durumlarında aşağıdaki kod bloğu çalışsın.
        print("Bilgisayarınızda yeterince bellek bulunmamaktadır.")

try:
    import os
except ImportError:
    print("os kütüphane dosyasına ulaşılamıyor. Ufaklığın silmediğinden emin olun :D")


try:
    bolum=sayi1/sayi2
except ZeroDivisionError:
    print("Bölünen sıfır olamaz!!!!!")
"""
ValueError: veri tipi uymadığında.
#Import error: içeri aktarılmaya çalışan modül aktarılırken bir hata oluşursa.
#ModuleNotFoundError: içeri aktarılmaya çalışan modül yerinde yoksa bu hata üretilir.
#MemoryError: Bellek programa yetmediği zaman üretilir.
#ZeroDivisionError: 0'a bölünme hatası.
#OverflowError: bir değişkene kapasitesinden fazla değer atamak istediğimizde üretilen hatadır.(int 32 bit ise: 11 basamaklı sayı alamaz.)
#IndexError: 4 elemanlı bir listenin 5. elemanına ulaşmaya çalıştığımızda bu hata ile karşılaşırız.
"""



###################   Hata Tanımlama:Fırlatma   ###################
"""
El Yordamı ile Hata Fırlatma
not1 = int(input("Ders notunuzu giriniz:"))
if(not1<0 or not1>100):
    #raise Exception("Not aralığı hatalı!!!") #: Exception olarak forlatılır.
    raise OverflowError("Not aralığı hatalı!!!") #: OverflowError olarak fırlatmak için
"""
"""
ASSERT
eposta = input("E-posta adresinizi giriniz:")
assert eposta == "sercan@ucuncubinyil.com" #eposta sercan@ucuncubinyil.com değilse AssertionError üretir.
print("Eposta'yı doğru girdiniz.")
"""

#################     ALIŞTIRMALAR     #################

"""
def bolmeYap():
    bolunen = int(input("Bölünen:"))
    bolen = int(input("Bölen :"))
    bolum = bolunen / bolen
    print(bolum)


while(True):
    try:
        bolmeYap()
        break
    except ZeroDivisionError:
        print("Bölen 0 olamaz !!!")
    except ValueError:
        print("Sadece rakam giriniz !!!")
    except:
        print("Başka bir hata oluştu !!")
"""



# Kullanıcıdan 2 sayı 1 'de işlem alıp önceden tanımladığımız fonksiyonlara alınan değerleri göndereceğiz.
    # işlem topla,çıkar,çarp ve böl'den birisi değilse assert fırlatılsın.
    # Kullanıcıdan veri alınırken ValueError verdiğinde tekrar veri istensin
    # ZeroDivisionError için tekrar veri istenmesin!

#Fonksiyonlar: topla(s1,s2),cikar(s1,s2),carp(s1,s2),bol(s1,s2),islemYap(s1,s2)

"""
def topla(s1,s2):
    print(s1+s2)
def cikar(s1,s2):
    print(s1-s2)
def carp(s1,s2):
    print(s1*s2)
def bol(s1,s2):
    print(s1/s2)
def islemYap():
    s1 = int(input("s1:"))
    s2 = int(input("s2:"))
    islem = input("işlem:")
    assert islem == "topla" or islem == "çarp" or islem == "böl" or islem == "çıkar"
    if(islem=="topla"):
        topla(s1,s2)
    elif(islem=="çıkar"):
        cikar(s1,s2)
    elif(islem=="çarp"):
        carp(s1,s2)
    elif(islem=="böl"):
        bol(s1,s2)
while(True):
    try:
        islemYap()
        break
    except ValueError:
        islemYap()
    except ZeroDivisionError:
        print("Tekrar hakkınız yok. Bölen 0 olamaz !")
"""