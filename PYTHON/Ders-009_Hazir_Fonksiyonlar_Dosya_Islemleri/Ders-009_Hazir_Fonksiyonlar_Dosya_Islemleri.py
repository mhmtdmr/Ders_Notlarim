
###################################     Hazır String Fonksiyonları    ##################################
"""
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle() 	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""

"""
# metin parçalama
kelimeler = "Bugün.hava.çok.sıcak.değildi."
#kelimeListe = kelimeler.split(".") # kelimeler metnini parçala. . lardan itibaren.
kelimeListe = kelimeler.split(".",3) # kelimeler metnini parçala. . lardan itibaren. ilk 3 parçayı .'lardan parçala
for k in kelimeListe:
    print(k)
    print(len(k))
"""




############################    Datetime Kütühanesi    #####################################3

"""
import datetime

zaman = datetime.datetime.now()
print(zaman)
print(zaman.day)
print(zaman.month)
print(zaman.year)
#print(zaman.fold)
z2 = datetime.datetime(2019,1,20)
print(z2)
print(z2.date()) # Zamana ait sadece tarih kısmını aldı.
print("zaman değişkeninin formatlı hali:",zaman.strftime("%d_%m_%Y"))
"""
"""
%d : rakam ile gün bilgisi
%m : ay iki haneli rakam
%b: Üç haneli ay,yazı ile.
%y: 2 haneli rakam ile yıl
%Y: 4 haneli rakam ile yıl
%H: saat
%M: dakika
%S: saniye
%a: 3 haneli gün.yazı ile.
%A: Günün tam adı. yazı ile.
%D: Ay/Gun/Yil
"""

"""
#YIL-AY-GUN--Saat:Dakika:Saniye--GünAdı
print(zaman.strftime("Bugün günlerden: %A"))
import locale
locale.setlocale(locale.LC_ALL,'Turkish_Turkey.1254') # Zaman bilgisini vb bilgileri Türkçe yazdırmak için. Bölgesel ayarları yaptık.
print(zaman.strftime("Bugün günlerden: %A"))

zaman = datetime.datetime.now()
formatliZaman = zaman.strftime("%Y-%m-%d--%H:%M:%S--%A")
print("zaman bilgisi üzerinde format değişikliği:",formatliZaman)

zList = formatliZaman.split("--")
for eleman in zList:
    print(eleman)
tarih=zList[0]
saat=zList[1]
gun=zList[2]
print("PARÇALI: ",saat,gun,tarih)




from datetime import  timedelta,date,datetime # Kısmi import
from locale import * # locale kütüphanesindeki herşeyi import et.
#eskizaman = datetime(1995,4,9)

bugun = date.today()
print(bugun)
birhaftaonce = bugun-timedelta(7)
print("1 hafta önce tarih: ",birhaftaonce)

"""

#################################        Dizin ve Dosya İşlemleri        ################################

#DIRECTORY
"""
from os import open,listdir,getcwd,mkdir,chdir,path,rmdir

print("Hangi klasördeyiz:",getcwd()) # Şuan hangi klasördeyiz.
chdir("C:\\") # Change Directory: dizin değiştirme.
print("Hangi klasördeyiz:",getcwd())

klasorYolu = "C:\\TEST"
klasorVarMi = path.exists(klasorYolu) # Klasör varsa True yoksa False döndürür.
if(klasorVarMi==False):
    mkdir(klasorYolu)

"""
###### ALIŞTIRMALAR ########
"""
#SORU1:  C:\TEST\YIL-AY-GUN ismi ile klasör oluştur.

from datetime import  datetime,timedelta,date
import time
zaman = datetime.now()
dosyaAdi = zaman.strftime("%Y-%m-%d")
dosyaYolu = "C:\\TEST\\"+dosyaAdi

if(not path.exists(dosyaYolu)):
    mkdir(dosyaYolu)
    print(dosyaYolu,"isimli klasör oluşturuldu.")
    print("Oluşturulma tarihi:",path.getctime(dosyaYolu)) # Klasörün oluşturulma tarihi # 1579542572.4046376
    gunRaw = time.ctime(path.getctime(dosyaYolu)) # Formatlamak için parçaladık.
    parsed = time.strptime(gunRaw)
    formatLi = time.strftime("%Y-%m-%d %H:%M:%S",parsed)

dun = date.today()-timedelta(1)
print(dun)
dunKlasorYolu = "C:\\TEST\\"+str(dun)
if(path.exists(dunKlasorYolu)): #Klasör mevcutsa
    rmdir(dunKlasorYolu) #Klasörü sil.
"""

####   Dizin İşlemleri   ####
#from os import write,open,remove,listdir,chdir,path
import os
"""
dizin = "C:\\TEST\\"
dosyaveklasorlistesi = listdir(dizin)
for eleman in dosyaveklasorlistesi:
    print(eleman)
"""
"""
os.chdir("C:\\TEST\\2020-01-20")
dosyaYolu="C:\\TEST\\2020-01-20\\ikincidosyam.txt"
#if(not path.exists(dosyaYolu)):
    #dosya = open(dosyaYolu,mode="a+")
dosya = open(dosyaYolu,mode="a+")
dosya.write("Merhaba Dünya 2,3,4\n")
dosya.close()
"""


'''
dosyaAdres = "C:\\Ders11\\Personel.txt"

txtdosyasi = open(dosyaAdres,"r")
'''
"""
# Tüm dosyayı okuyup satırları tutan bir listeye atadık
satirlar = txtdosyasi.readlines()  

for satir in satirlar:
    print(satir)
"""
#Satır satır okumak için...
'''
satir = txtdosyasi.readline()
while(satir != ""):
    if not (satir.startswith("Kayıt") or satir.startswith("--")):
        #print(satir,end="")
        parcaliSatir = satir.split("\t\t")
        parcaliSatir[3] = parcaliSatir[3].replace("\n","")
        #print(parcaliSatir)
        print(f"Ad: {parcaliSatir[1]} Soyad: {parcaliSatir[2]} Yaş: {parcaliSatir[3]}")
    satir = txtdosyasi.readline()
txtdosyasi.close()
'''








"""
Dosya yetki modları
w:  sadece yazma yetkisi ile açar. (dosya yeniden oluşturulur)
r:  sadece okuma yetkisi ile açar.
a:  sona ekleme yetkisi ile açar.  (dosya yoksa oluşturulur)
x:  yazma yetkisi ile açar. Dosya varsa hata verir. Yoksa oluşturur.

w+ : yazma + okuma yetkisi ile açar. (dosya yeniden oluşturulur)
r+ : okuma + yazma yetkisi ile açar.
a+ : ekleme + okuma yetkisi ile açar. (dosya yoksa oluşturulur)
"""


###   ALIŞTIRMALAR   ###
#SORU1: 1-10 arasındaki sayıların karelerini aşağıdaki formatta bir dosyaya yazan program.
"""
    1 sayısının karesi: 1
    2 sayısının karesi: 4
    ...
    ...
"""
"""
import os
dosyaAdres="C:\\TEST\\Cevap1.txt"
dosya=open(dosyaAdres,"a+")
for i in range(11):
    dosya.write(str(i)+" sayısının karesi: "+str(i**2)+"\n")
dosya.close()

#komut = "calc" # Hesap makinesi açma komutu
#os.system(komut)# Hesap makinesi açma komutu
"""
"""
komut="hostname"
bilgisayarAdi = os.system(komut)

komut="ipconfig"
bilgisayarAdi = os.system(komut)
"""
# 1-100 arası üretilen 10 adet sayıyı Rastgele.txt isimli bir dosyaya yazdıran program. Aşağıdaki formatta yazılacak.
"""
    BİLGİSAYAR ADI
    Zaman                   OlaySırası  RastgeleSayı
    -----                   ----------  ------------
    20.01.2020 21:40:35         1           15
    20.01.2020 21:40:36         2           65
    20.01.2020 21:40:37         3           68
"""
"""
import os,random,datetime
dosyaAdres= "C:\\TEST\\Cevap2.txt"
dosya = open(dosyaAdres,"a+")
dosya.write(str(os.system("hostname")))
#dosya.write("""
#    Zaman                   OlaySırası          RastgeleSayı
#    -----                   ----------          ------------
#""")
"""
"""
#for i in range(10):
 #   sayi = random.randint(1,100)
 #   zm = datetime.datetime.now()
 #   dosya.write("""
  #  """+str(zm)+"""                 """+str(i)+"""           """+str(sayi)+"""
  #  """)
#dosya.close()



# Kullanıcının girdiği küçük sayıdan büyük sayıya kadar olan sayıları bir txt dosyasına alt alta yazınız.
# C:\\TEST\\sayiliste.txt
"""
import os
klasor = "C:\\TEST\\"
if(not os.path.exists(klasor)):
    os.mkdir(klasor)

kucuk = int(input("Küçük sayıyı giriniz:"))
buyuk = int(input("Büyük sayıyı giriniz:"))
dosya = klasor+"sayiliste.txt"   # C:\TEST\sayiliste.txt
aktifDosya = open(dosya,mode="a")  # açılmış olan dosyaya aktifDosya ismi ile erişeceğiz.
for i in range(kucuk,buyuk+1):
    satir = str(i)+"\n"
    #print(satir)
    aktifDosya.write(satir)
aktifDosya.close()
"""




###   Dosya Okuma İşlemleri   ###

import os
#dosya = "C:\\TEST\\personeller.txt"

#aktifDosya = open(dosya,mode="r+")
"""
#  readline():  dosyadaki bir satırı okumamızı sağlar. Her çalışmasında 1 sonraki satıra atlar.

print(aktifDosya.readline()) # 1. satırı okur
print(aktifDosya.readline()) # 2. satırı okur
print(aktifDosya.readline()) # 3. satırı okur
print(aktifDosya.readline()) # 4. satırı okur

aktifDosya.write("\nSelvi Kahraman") # r+ olursa yazar. yoksa nor writable hatası.
"""
# readlines(): bütün satırları alıp bir liste olarak döndürür.
#personelListesi = aktifDosya.readlines()
#print(personelListesi[2])

#print(aktifDosya.read()) # dosyanın tamammını döndürür.
#print(aktifDosya.read(15)) # ilk 15 karakteri döndürür.


# Dosya ismini dolaylı yoldan değiştirme.
"""
import shutil
shutil.copy("C:\\TEST\\personeller.txt","C:\\TEST\\yenipersoneller.txt")   # dosyayı yeni isimle kopyaladık.
os.remove(dosya) # Daha sonra eskisini sildik.
"""

#Dosya ismini değiştirme.
# os.rename("C:\\TEST\\personeller.txt","C:\\TEST\\enyenipersoneller.txt")
# DOsyayı satır satır okuduk. Ve ad soyad bilgisini ayırdık.
"""
satir = aktifDosya.readline()
while satir!='':
    adsoyad = satir.split(' ')
    print("Personel Adı:",adsoyad[0])
    print("Personel Soyadı:", adsoyad[1])
    satir=aktifDosya.readline()
"""

# Satır satır veri okumanın diğer bir yolu.
#for satir in aktifDosya:
#    print("For ile satır okuyoruz: ",satir)

# işlemler bittikten sonra dosyaya bağlantımızı kapattık.
#aktifDosya.close()


# C:\\TEST\\sayiliste.txt dosyadaki sayıları okyuyup bu sayıların karelerini başka bir txt dosyasına(kareliste.txt) yazdırın.

"""
import  os
acilanDosya = open("C:\\TEST\\sayiliste.txt","r")
sayilar = acilanDosya.readlines()  # sayiları bir listeye atadık.
acilanDosya.close()

kareDosyasi = open("C:\\TEST\\kareliste.txt","w")

for sayi in sayilar:
    kare = int(sayi)**2 # sayının karesini değişkene atadık
    satir = "\n"+str(kare)
    kareDosyasi.write(satir)

kareDosyasi.close()
"""
"""
while (sayi!=''):
    print(sayi)
    sayi = acilanDosya.readline()

"""
#ÖDEV: Kullanıcıdan personel sayısı bilgisini al: Her personel için:
    # Ad Soyad Dogum yili bilgilerini alarak PersonelKayilari.txt dosyasına
"""
        AD      SOYAD       YAŞ
        --      -----       ---
        Hatice  KARACA      34
"""



















