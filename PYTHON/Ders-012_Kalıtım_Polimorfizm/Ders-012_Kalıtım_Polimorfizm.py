
############################           Kalıtım            ##########################

#Ders-012_Arac.py
class Arac:
    def __init__(self):
        self.Marka = str()
        self.Model = ""
        self.Renk = ""
        self.UretimYili = 1900
        self.Fiyat = 0.0
        from datetime import datetime
        self.IlanTarihi = datetime.today().date()

    def BilgiYazdir(self):
        print(f"""ARAÇ BİLGİLERİ
            Marka: {self.Marka}
            Model: {self.Model}
            Renk: {self.Renk}
            Üretim Yılı: {self.UretimYili}
            Fiyat: {self.Fiyat}
            İlan tarihi: {self.IlanTarihi}""")

# Arac sınıfından kalıtım  ile özellik ve fonksiyonları devalması için, parantez içinde üst sınıf ismini
#  belirttik.
class Otomobil(Arac):
    def __init__(self):
        self.KasaTipi = "Sedan"
        self.VitesTipi = "Otomatik"

    def BilgiYazdir(self):
        super().BilgiYazdir()
        print(f"""
            Kasa tipi: {self.KasaTipi}
            Vites tipi: {self.VitesTipi}""")

class Kamyon(Arac):
    def __init__(self):
        self.Tasimakapasitesi = 0
        self.YakitDepoSayisi = 1

    def BilgiYazdir(self):
        super().BilgiYazdir()
        #super().Marka    # üst sınıftaki özellik ve fonksiyonlara super() ile erişim.
        print(f"""
            Taşıma kapasitesi: {self.Tasimakapasitesi}
            Yakıt deposu sayısı: {self.YakitDepoSayisi}""")


#from Ders-012_Arac import Arac,Otomobil,Kamyon
"""

import datetime

oto1 = Otomobil()
oto1.Marka = "Mercedes"
oto1.Model = "C180"
oto1.Renk = "Siyah"
oto1.Fiyat = 200000
oto1.IlanTarihi = datetime.datetime(2010,5,10)
oto1.UretimYili = 2015
oto1.KasaTipi = "Sedan"
oto1.VitesTipi= "Otomatik"
oto1.BilgiYazdir()

kamyon1 = Kamyon()
kamyon1.Marka = "Mercedes"
kamyon1.Model = "Actros"
kamyon1.Renk = "Kırmızı"
kamyon1.Fiyat = 500000
kamyon1.IlanTarihi = datetime.datetime(2018,5,10)
kamyon1.UretimYili = 2018
kamyon1.Tasimakapasitesi = 40000
kamyon1.YakitDepoSayisi = 4
kamyon1.BilgiYazdir()

"""


#################       ALIŞTIRMALAR        ###################
# Ders-12_BeyazEsya.py
# Ders-12_Buzdolabi.py
# Ders-12_CamasirMakinesi.py

#from Ders-012_Buzdolabi import Buzdolabi
'''
b1 = Buzdolabi()
b1.Marka = "Bosch"
b1.Model = "B560"
b1.Enerji = "A+++"
b1.Fiyat = 2700
b1.KapakSayisi = 2
b1.Hacim = 560
'''
#b1.BilgiListele()
#b1.Kaydet()

#from Ders-012_CamasirMakinesi import CamasirMakinesi
'''
c1 = CamasirMakinesi()
c1.Marka = "Vestel"
c1.Model = "V46"
c1.Enerji = "A++"
c1.Fiyat = 3000
c1.HizliYikama = True
c1.YikamaKapasitesi = 10
#c1.Kaydet()
'''

#### Polimorfizm: Çok biçimlilik: 1 fonksiyon ile farklı işler yapmış olduk.  ####
'''
def Bilgi(beyazesya):
    beyazesya.BilgiListele() # Hangi tipte nesne gelirse o tipin fonksiyonu çalışır.

Bilgi(c1)
Bilgi(b1)
'''


#######################################
'''
ANASINIF: Banka: AdSoyad,IBAN,Bakiye

EFT(hedefIBAN,miktar):
eft_ucreti=0
Önce bakiye kontrolü yapsın. Daha sonra transferi yapıp. Şu IBAN'dan şu IBAN'a
Şu Miktarda transfer gerçekleşmiştir.
miktarı bakiyeden düşsün.

ALTSINIF:
Garanti: Takim

EFT(hedefIBAN,miktar):
eft_ucreti=10
Önce bakiye kontrolü yapsın. Daha sonra transferi yapıp. Şu IBAN'dan şu IBAN'a
Şu Miktarda transfer gerçekleşmiştir.
miktarı bakiyeden düşsün.

#EK: print edilen cümleyi bir dosyaya yazsın. txt.

Akbank: Bank sınıfından kullanacağım
Garanti: Kendi sınıfımdan kullanacağım.
'''