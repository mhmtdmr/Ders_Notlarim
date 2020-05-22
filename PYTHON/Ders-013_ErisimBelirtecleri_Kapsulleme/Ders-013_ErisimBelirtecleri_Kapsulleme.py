class Ust:
    def __init__(self):#public
        self.Ad = "NoName" # public
        self.__Soyad = "NoSurName"# private
        self._Yas = 18 # protected

    def Merhaba(self):
        self._Yas = 15
        self.__Soyad = "Çelik"

#public: Python'da varsayılan olarak herşey tam erişilirdir.
#private: iki adet _ (alt çizgi) ile özellik veya fonksiyonlar sadece sınıf içnden erişilir hale getirilebilir
#protected: Sınıf içinden ve alt sınıflardan erişilebilir.

class Alt(Ust):
    #public ve protected alan,kendi sınıfımız için private.

    def YasGir(self,yas):
        if(yas<0 or yas>150):
            print("Yaş 0-150 arasında girilmelidir.")
        else:
            self._Yas=yas

    def YasYaz(self):
        print(self._Yas)


#public alan
#-------------
nesne = Ust()
nesne.Ad = "Mehmet"

nesne2 = Alt()
nesne2.Ad = "Ahmet"
nesne2.YasGir(25)
nesne2.YasYaz()


class Kapsul:
    def __init__(self):
        self.__gizliOzellik = "Varsayılan Değer" #private
        self.__gizli2 = "Varsayılan Değer"

    def getOzellik(self):       #readonly: sadece okuma yapılabilri.
        return self.__gizliOzellik
# getter metotları private özelliklerin değerini döndürmek için kullanılır.
# setter metotları private özelliklere değer atamak için kullanılır.
# Bu atamayı kontrol etmemizi sağlar.
    def getGizli2(self):
        return self.__gizli2

    def setGizli2(self,deger):
        if(len(deger)>40):
            print("Değer çok uzun.")
        else:
            self.__gizli2 = deger
            print("40 harf ve daha az uzunlukta.")



#######################             ALIŞTIRMALAR            #########################

# Kapslsyn Ornek:
"""
ana sınıf: DovizKullanici: HesapNo(pri,init sırasında atansın), AdSoyad(pub),Tel(pub),Bakiye(pro) setHesapNo(deger)
alt sınıf: Dolar: Kur(pri), Kur init edilirken ayarlansın, getKur(),setBakiye(deger)
"""

class DovizKullanici:
    def __init__(self):
        self.__HesapNo = ""
        self._Bakiye = 0
        self.AdSoyad = ""
        self.Tel = ""

    def setHesapNo(self,yeni_hesapNo):
        self.__HesapNo=yeni_hesapNo

class DolarKullanici(DovizKullanici):
    __Kur = 6

    def __init__(self,anlikDeger):
        self.__Kur = anlikDeger

    def getKur(self):
        return self.__Kur

    def setBakiye(self,yeniBakiye):
        self._Bakiye = yeniBakiye



# Kapslsyn Ornek:
"""
ana sınıf: Doviz: HesapNo(pri,init sırasında atansın), AdSoyad(pub),Tel(pub),Bakiye(pro) setHesapNo(deger)
alt sınıf: Dolar: Kur(pri), Kur init edilirken ayarlansın, getKur(),setBakiye(deger)
"""
"""
import Doviz
dk = Doviz.DolarKullanici(3)
dk.AdSoyad = "Serhan KARA"
dk.Tel = "+903164975236"
dk.setHesapNo("TR03216549887")
dk.setBakiye(1000)
"""









