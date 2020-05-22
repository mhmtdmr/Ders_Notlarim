##########################################################
###################### Property ##########################
##########################################################

#Property.py
'''
class Personel:
    def __init__(self,parametre):
        self.__isim=parametre

    def setisim(self,parametre):
        print("self.__isim değişti.")
        self.__isim=parametre

    def getisim(self):
        print("self.__isim okundu.")
        return  self.__isim

    def delisim(self):
        print("self.__isim silindi.")
        del self.__isim
    ad = property(getisim,setisim,delisim) #fonksiyon isimleri get,set,delete şeklinde sıralı olmalıdır.

#SORU: vize ve final notunu alarak ortalama hesaplayan( Ortalama() ) universite isminde bir sınıf tanımlayınız.

class universite():
    def __init__(self):
        self.__vize=0
        self.__final=0

    def getvize(self):
        return self.__vize;

    def setvize(self,parametre):
        if (parametre < 0 or parametre > 100):
            print("Hatalı not girdiniz")
            while(True):
                vizenot = int(input("Vize notunu giriniz:"))
                if(vizenot<0 or vizenot>100):
                    print("Hatalı not girdiniz")
                else:
                    self.__vize=vizenot
                    break
        else:
            self.__vize = parametre

    vize = property(getvize,setvize)
# Üstteki property oluşturmanın kısa yöntemi.
    @property
    def final(self):
        return self.__final
    @final.setter
    def final(self,parametre):
        self.__final=parametre

    def Ortalama(self):
        print("Ders ortalaması:",((self.__vize*0.4)+(self.__final*0.6)))
'''

#import Property
"""
nesne = Property.Personel("Sevgi")
print(nesne.getisim())
nesne.setisim("Sevim")
print(nesne.getisim())
nesne.delisim()
"""

"""
nesne2 = Property.Personel("Ali")
nesne2.ad = "Ömer Ali"
print(nesne2.ad)
"""
"""
nt1 = Property.universite()
#nt1.setvize(150)
#print(nt1.getvize())

nt1.vize = 150
print(nt1.vize)

nt1.final = 90
print(nt1.final)
"""


####################   ALIŞTIRMALAR   ################


"""
class IstanbulMarket:
    def __init__(self):
        self.Unvan = ''
        self.SicilNumarasi = ''
        self._SahipTC = ''
        self.__Adres = ''

    @property
    def Adres(self):
        return self.__Adres

    @Adres.setter
    def Adres(self,adr):
        self.__Adres = adr

    @Adres.deleter
    def delAdres(self):
        print("Özellik silindi.")
        del self.__Adres


mrkt = IstanbulMarket()
mrkt.Adres = 'Kadıköy...'
print(mrkt.Adres)
del mrkt.Adres
"""






"""

    def setTC(self,tc):

        if(len(tc)==11):
            self._SahipTC = tc
        else:
            print("TC numarası hatalı!!!")

    def getTC(self):
        return self._SahipTC

    TC = property(getTC,setTC)


class SariyerMarket(IstanbulMarket):
    def __init__(self):
        self.MarketNumarasi = 0


market = IstanbulMarket()
market.TC = '123123'
print(market.TC)"""
"""
market.Unvan = 'Bim Marketleri'
market.SicilNumarasi = 'TR123654789'
market.setTC('98765432132')
print(market.getTC())
"""










##########################################################
###################### iterator ##########################
##########################################################
"""
rakamlar = [0,1,2,3,4,5,6,7,8,9]

for rakam in rakamlar:
    print(rakam)"""
"""
basamak = iter(rakamlar)
print(next(basamak)) # ilk elemanı elde ettik.
print(next(basamak)) # 2. elemana
print(next(basamak)) # 3. elemana
print(next(basamak)) # 4. elemana
print(next(basamak)) # 5. elemana
print(next(basamak)) # 6. elemana
print(next(basamak)) # 7. elemana
print(next(basamak)) # 8. elemana
print(next(basamak)) # 9. elemana
print(next(basamak)) # 10. elemana
basamak = iter(rakamlar)  # Başa sarmanının ilkel yöntemi.
print(next(basamak)) # 1. elemana

"""
##########################################################
###################### generator #########################
##########################################################
"""
def onKatlari():
    yield 10
    yield 20
    yield 30

test = onKatlari()
print(next(test))
print(next(test))
print(next(test))
"""
##########################################################
######################    map    #########################
##########################################################

def kareBul(x):
    return x**2
sayilar = [1,3,5,7]

kareler = list(map(kareBul,sayilar)) # listedeki her bir elemanı kareBul metoduna parametre olarak gönderecek.
print(kareler)

"""
def carp(x,y):
    return x*y

ilk = [1,2,3,4,5]
ikinci = [6,7,8,9,10]
carpimlar = list(map(carp,ilk,ikinci))
print(carpimlar)
"""