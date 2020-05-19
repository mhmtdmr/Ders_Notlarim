#######################################################################################
######################                                      ###########################
######################       OOP: Object Oriented P.        ###########################
######################       Nesneye Yönelik Pogramlama     ###########################
######################                                      ###########################
#######################################################################################

class Ogrenci:
    # Sınıf nitelikleri
    sinif_bilgi = "Bu sınıf kurstaki öğrenci işlemlerini kolaylaştırmak için yazıldı."

    # Sınıf fonksiyonları. #cls: sınıfı temsil eder. Kullanılması zorunludur. Farklı isim alabilir. İlk sırada olmalı!
    @classmethod
    def BilgiListele(cls):
        print("Öğrencilerin geneli ile ilgili bilgileri sınıf metotlarında listeleriz.")
        print("Bu fonksiyon kullanım amacı açısından kurs müdürünün kullanacağı bir fonksiyon olabilir.")
        print("Müdür tüm öğrencilere ait bilgileri listelemek istediğinde bu fonksiyon çalıştırılır.")

    # Nesne oluşturulurken otomatik çalışan yapıcı(constructer) fonksiyon.
    # Aynı zamanda nesneye ait özellikleri(değişkenler) burada tanımlarız.
    # self: nesneyi temsil eder. Kullanılması zorunludur.Farklı isim alabilir. İlk sırada olmalı!
    def __init__(self):
        print("Yeni bir nesne oluşturuldu, init fonksiyonu otomatik çalıştı.")
        self.ad = str()
        self.dogumTarihi = ""
        self.sinifNo = 0

    # Bu metotlar sınıfın kendisine değil. Örneklere ait metotlardır.(belirteç yok)
    def Kaydet(self):
        print(self.ad,self.dogumTarihi,self.sinifNo,"bilgileri veritabanına kaydedildi.")

    def Bilgi(self):
        print("**************************    Öğrenci  Bilgileri   **********************************")
        print(f"Öğrenci adı:{self.ad}\nÖğrenci doğum tarihi:{self.dogumTarihi}\nÖğrenci sınıf numarası:{self.sinifNo}")
        print("-------------------------------------------------------------------------------------")

    #Sınıf veya nesne ile ilgili bir işlem yapılmayacaksa static metot kullanılır.(self,veya cls yok!)
    @staticmethod
    def Topla(sayi1,sayi2):
        print("Sayıların Toplamı:",(sayi1+sayi2))

# Sınıf nitelik ve fonksiyonlarına erişim.
print(Ogrenci.sinif_bilgi)
Ogrenci.BilgiListele()


# Sınıftan nesne tanımlama.
ogrenci1 = Ogrenci()

ogrenci1.ad = "Ensar"
ogrenci1.dogumTarihi = "2001.09.10"
ogrenci1.sinifNo = 106
print(f"Öğrenci Bilgileri:{ogrenci1.ad},{ogrenci1.sinifNo},{ogrenci1.dogumTarihi}")
ogrenci1.Bilgi()

ogrenci2 = Ogrenci()
ogrenci2.ad = "Yavuz"
ogrenci1.dogumTarihi = "2000.09.10"
ogrenci2.sinifNo = 106
print(f"Öğrenci Bilgileri:{ogrenci2.ad},{ogrenci2.sinifNo},{ogrenci2.dogumTarihi}")
ogrenci1.Bilgi()

# Static fonksiyon kullanımı.
Ogrenci.Topla(5,4)

#######################           ALIŞTIRMALAR           ###########################

# SORU1
# Matematik isminde bir sınıf oluşturun.(farklı dosyada)
# Matematik sınıfına ait sınıf metotları: topla(n parametreli),carp(n parametre)..
# Mevcut dosyaya import yapıp kullanın.

"""
#Ders-011_Matematik.py
class Matematik:
    @classmethod
    def topla(self,*sayilar):
        toplam=0
        for sayi in sayilar:
            toplam += sayi
        print("Sayıların toplamı:",toplam)

    @classmethod
    def cikar(cls,s1,s2):
        print("Sayıların farkı:",(s1-s2))

    @classmethod
    def carp(cls,*sayilar):
        carpim=1
        for sayi in sayilar:
            carpim *= sayi
        print("Sayıların çarpımı:",carpim)
    @classmethod
    def bol(cls,s1,s2):
        try:
            bolum = s1//s2
            print("Sayıların bölümü",bolum)
        except ZeroDivisionError:
            print("Bölüm 0 olmamalı!")
"""
"""
from Ders-011_Matematik import  Matematik

Matematik.topla(3,5,7)
Matematik.bol(9,3)
Matematik.carp(1,2,3)
Matematik.cikar(9,5)
"""




# SORU2

# Aşağıdaki sınıfı Ders.py isimli dosyada tanımlattırıp, kullandır.
# class Ders: DersAdi,DersSaati,DersOgretmeni,DersBaslamaTarihi
# init(parametreli)    DersKaydet(): C:\\UBY\Dersler.txt'ye ekleyin.
"""
class Ders:
    def __init__(self,dersAdi,dersSaati,dersOgretmeni,dersBaslamaTarihi):
        self.DersAdi = dersAdi
        self.DersSaati = dersSaati
        self.DersOgretmeni = dersOgretmeni
        self.DersBaslamaTarihi = dersBaslamaTarihi
        self.DersKaydet() # Ders otomatik olarak keydedilsin.

    def DersKaydet(self):
        try:
            import  os
            dizin = "C:\\UBY\\"
            kayitDosyasi = "C:\\UBY\\Dersler.txt"
            if(not os.path.exists(dizin)):
                os.mkdir(dizin)
            dosya = open(kayitDosyasi,mode="a")

            yazi = "\n"+"Ders Adı:\t"+str(self.DersAdi)+"\n"+"Ders Saati:\t"+str(self.DersSaati)+"\n"+"Ders Öğretmeni:\t"+str(self.DersOgretmeni)+"\n"\
                   +"Başlama Tarihi:\t"+str(self.DersBaslamaTarihi)
            dosya.write(yazi)
            dosya.close()
            print("Ders başarı ile kaydedildi.")
        except:
            print("Dosya kaydedilirken bir hata oluştu.")
"""
# Kullanımı
"""
import Ders-011_Ders
ders1 = Ders-011_Ders.Ders("Photoshop","72","Ahmet Gülfidan","01.02.2020")
#print(ders1.DersAdi)
#ders1.DersKaydet()
"""


### ÖDEV ###
#1: Otomobil isimli sınıfı Otomobil.py dosyasında tanımlayın.
#   Nesne Nitelikleri: Marka,Model,Renk,MotorHacmi,UretimYili
#   Nesne Fonksiyonları: __init()__: Parametre olarak nesne niteliklerini alacak. Nesneyi oluşturacak.
#   init otomatik olarak Kaydet() fonksiyonunu çağırsın
#   Kaydet(): metodu sınıfa ait bilgileri o güne ait OTO_29_01_2020.txt şeklinde bir dosyaya kaydetsin.

# Ders-011_Otomobil.py
"""
class Otomobil:
    tanim = "Bu sınıf Otomobil sınıfıdır. Bu özellik nesnelere değil doğrudan sınıfın kendisine aittir."

    # Sınıf nesnelerine ait özellikleri belirtmiş olursunuz.
    def __init__(self,marka,model,renk,motorHacmi,uretimYili):
        self.Marka = marka
        self.Model = model
        self.Renk = renk
        self.MotorHacmi = motorHacmi
        self.UretimYili = uretimYili
        self.Kaydet() #Kaydet fonksiyonu otomatik çalıştı.

    #Bu metotlar sınıfın kendisine değil. Örneklere ait metotlardır.

    def Kaydet(self):
        import os
        import datetime
        dizin = "C:\\DERS13\\"
        dosya = dizin+"OTO_" + str(datetime.date.today()) + ".txt"
        if(not os.path.exists(dizin)):
            os.mkdir(dizin)
        acikDosya = open(dosya,mode="a")

        kayit = str(self.Marka)+" "+str(self.Model)+" "+str(self.Renk)+" "+str(self.MotorHacmi)+" "+str(self.UretimYili)+"\n";
        acikDosya.write(kayit)
        acikDosya.close()
"""

#import Ders-011_Otomobil
"""
oto1 = Ders-011_Otomobil.Otomobil("Mazda","CX5","Kırmızı",1800,2019)
#oto1.Kaydet()
"""


# SORU4
"""

    Personel isimli sınıfı tanımlayınız.

    Nesne özellikleri: ad,soyad,tc,telefon,adres,maas
    __init__ fonksiyonunda kullanıcıdan nesne özelliklerine karşılık veriler istensin.

    Kaydet isimli nesne fonksiyonunu tanımlayın. Bu fonksiyon C:\Ders13\Personel.txt
    dosyasına kullanıcıdan alınmış olan verileri kaydetsin.

    Sınıf metodu: Listele:
    C:\Ders13\Personel.txt dosyasındaki öğrenci verilerini ekranda listelesin.


"""

#Ders-011_Personel.py
"""
class Personel:
    Bilgi=""
    def __init__(self):
        print("Personel Bilgilerini Giriniz")
        self.ad = input("İsim: ")
        self.soyad = input("Soyisim: ")
        self.tc = input("Tc: ")
        self.telefon = input("Telefon: ")
        self.adres = input("Adres: ")
        self.maas = float(input("Maaş: "))

    #nesne metodu
    def Kaydet(self):
        import os
        dizin = "C:\\Ders13"
        dosya = "C:\\Ders13\\Personel.txt"
        if(not os.path.exists(dizin)):
            os.mkdir(dizin)
        dosyam = open(dosya,"a")
        dosyam.write(f''' Personel: {self.ad} {self.soyad}  T.C. Kimlik Numarası: {self.tc}  Telefon: {self.telefon}  Adres: {self.adres}  Maaş: {self.maas}''')
        dosyam.close()

    @staticmethod
    def Listele():
        import os
        dosya = "C:\\Ders13\\Personel.txt"
        if(not os.path.exists(dosya)):
            print("Dosya bulunamadı!!")
            return
        else:
            dosyam = open(dosya,"r")
            satirlar = dosyam.readlines()
            for satir in satirlar:
                print(satir)
"""
#import Ders-011_Personel
"""
prsnl = Personel()
prsnl.Kaydet()

Personel.Listele()
"""



