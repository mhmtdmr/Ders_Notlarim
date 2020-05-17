###     Tip Dönüşümleri    ###
"""
x = input("Sayı giriniz:")   # Kalvyeden girilen değeri str tipinde döndürür.
#print(x)
print(type(x))      #    <class 'str'>
x = int(x)          # int tipine dönüştürme
print(type(x))      #    <class 'int'>
x = float(x)        # float tipine dönüştürme
"""
"""
y = 7.3
print(type(y))      # <class 'float'>
y = str(y)          # str tipine dönüşürme
print(type(y))      # <class 'float'>
"""

"""
z = True
z = str(z)
print(type(z))      # <class 'str'>

b = ""              # Boşsa False, karakter varsa True olarak dönüşür.
b = bool(b)
print(b)
print(type(b))      # <class 'bool'>
"""
"""
harf = chr(65)      # ASCII tablosundaki sayısal değeri girip harf karşılığını alıyoruz.
print(harf)
harf = chr(97)      # ASCII tablosundaki sayısal değeri girip harf karşılığını alıyoruz.
print(harf)

sayi = ord("A")     # ASCII tablosundaki karakteri girip sayı karşılığını alıyoruz.
print(sayi)
sayi = ord("a")
print(sayi)

del sayi            # sayi değişkeni ram'den silinmiştir.
print(sayi)         # tanımsız gözükür NameError verir.
"""

"""
#  16: lık sayı sisteminde rakamlar: 0 1 2 3 4 5 6 7 8 9 A B C D E F
harf = 'D'
sayi = int(harf,16)
print(sayi)

bitler = '0101'
sayi = int(bitler,2)
print(sayi)
"""

###############################         ALIŞTIRMALAR        ####################################
"""
#SORU: Klavyeden alınan 3 değeri toplayıp sonucu ekrana yazdıran programı yazınız.

s1 = input("1. sayıyı giriniz:")
s1 = int(s1)

s2 = int(input("2. sayıyı giriniz:"))
s3 = int(input("2. sayıyı giriniz:"))

ortalama = (s1+s2+s3)//3
print("Girilen sayıların ortalaması",ortalama)
"""


"""
# SORU : Klavyeden girilen 2 sayıdan 1. nin büyük olup olmadığını ekrna yazdıran program.(True/False)
            #float tipinde alın.
            
f1 = float(input("1. sayı:"))
f2 = float(input("2. sayı:"))

kontrol = f1>f2
print("1. sayı büyük mü?",kontrol)
"""


###     Operatörler    ###


# Atama / İşlemli Atama Operatörleri
"""
sayi = 5

sayi += 3 # sayi = sayi + 3
sayi *= 2 # sayi = sayi * 2
sayi /= 4 # sayi = sayi / 4
sayi -= 2 # sayi = sayi - 2
"""


###  Aritmetik Operatörler   ###

"""
    +,-,*   : toplama,çıkarma,çarpma
    /  : onndalıklı bölme (10/4=2.5)
    // : tamsayı bölme (10//4=2)
    ** : üs alma (5**2)=25

"""

# Karşılaştırma Operatörleri
"""
sayi1 = 4
sayi2 = 8
bool1 = sayi1 == sayi2 # eşitse True değilse False
bool2 = sayi1 != sayi2 # eşitse False değilse True
bool3 = sayi1 >= sayi2 # büyük veya eşitse True, küçükse False
bool4 = sayi1 <= sayi2 # küçük veya eşitse True, küçük False
"""


# Mantıksal Operatörler

"""
MANTIKSAL VE(AND)
00 = 0
01 = 0
10 = 0
11 = 1
"""

"""
MANTIKSAL VEYA(OR)
00 = 0
01 = 1
10 = 1
11 = 1
"""


"""
sayi=5
kontrol = (sayi==3) or (sayi==5) # Koşullardan 1 tanesinin çalışması yeterli.

kontrol2 = (sayi<9) and (sayi>6) # Koşulların hepsi sağlanmak zorunda.
#print(kontrol)  # True
#print(kontrol2) # False

kontrol3 = ( sayi>1 and sayi<99 ) or (sayi == 999) # sayı 1-99 arasında ise VEYA sayı 999 ise True çıkar.
#print("Kontrol3:",kontrol3)

sayi4 = 88
#kontrol4 = not (sayi4>55) # False (Parantez içerisindeki değerin tersini alır.)

bool7 = not (True) # False

# aşağıdaki iki satır aynı koşulu ifade eder.
(sayi1==5)
not(sayi1!=5)

sayi10 = 100
sayi20 = 100
esitKontrol1 = (sayi10==sayi20)
print("sayi10 ve sayi20 eşit mi?:",esitKontrol1)

esitKontrol2 = sayi10 is sayi20
print("sayi10, sayi20 mi?:",esitKontrol2)

esitKontrol3 = sayi10 is not sayi20
print("sayi10 sayi20 den farklı mı?:",esitKontrol3)

print("adı" in "Kadıköy") # Kadıköy içerisinde adı var mı?

print("arı" in "Kadıköy") # Kadıköy içerisinde arı var mı?
print("arı" not in "Kadıköy") # Kadıköy içerisinde yok mu?

print("esitKontrol1 değişkeninin bellekteki(ram) adresi:",id(esitKontrol1))
"""


###############################         ALIŞTIRMALAR        ####################################
"""
# SORU: Kullanıcıdan alınan 1. sayının, kullanıcının girdiğe 2. sayıya kuvvetini ekrana yazdıran program.
# Örnek: sayi1 = 10 sayi2 = 2 Sonuç=100

#taban = int(input("Taban değerini giriniz:"))
#us = int(input("Üs değerini giriniz:"))
#print(taban,"sayısının",us,". kuvveti:",(taban**us))
"""