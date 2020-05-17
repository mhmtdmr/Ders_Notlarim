############################### AKIŞ KONTROL: IF, elif, ELSE  ##################################
'''
sayi = 11

if (sayi>9): # 1. Koşul
    print("Sayı 9 dan büyüktür") # 1. Koşul sağlandığında çalışacak kodlar.
    print("if'ten sonra gelen 4 karakter boşluk içindeki kodlar çalışır.")# 1. Koşul sağlandığında çalışacak kodlar.
elif(sayi<9): # 2. Koşul
    print("Sayı 9'dan küçüktür.")# 2. Koşul sağlandığında çalışacak kodlar.
else: # Üstteki koşullar sağlanmadığında
    print("Sayı 9'a eşittir.") # 1 ve 2. koşul sağlanmadığında çalışacak kodlar.

print("Koşul kontrolü bitti") # Burası IF şartına bağlı değil.
'''
###############################         ALIŞTIRMALAR        ####################################

# SORU: Klavyueden girilen değer: 100'den büyükse karesini ekrana yazdırın, küçükse küpünü ekrana yazdırın.
        #100'e eşitse kendisini ekrana yazdırın.


"""
deger = int(input("Sayı giriniz:"))
if(deger>100):
    print("Sayının karesi:",(deger**2))
elif(deger<100):
    print("Sayının küpü:",(deger**3))
else:
    print("Sayı:",deger)
"""

# SORU: Kalvyeden girilen sayı çift ise: Ekrana sayı çifttir yazdıracak ve 4 ile çarpımını yazdıracak,
# değilse sayı tektir yazdıracak ve 9 ile çarpımını yazdıracak..
"""
sayi = 10
kalan = sayi % 2
if(kalan==0):
    print("Sayı çifttir.",(sayi*4))
else:
    print("Sayı tektir.",(sayi*9))
"""
#ÖDEV1: Klavyeden girilen 3 sayının ortalamasını ondalıklı olarak hesaplayan programı yazınız.

#ÖDEV3: Klavyeden girilen 2 harfin ASCII tablosundaki değerlerini toplayıp ekrana yazdıran program.


"""
sayi7 = 78
if(sayi7>10 and sayi7<100 ): #sayı 100 ile 10 arasında ise
    if(sayi7<50):
        print("Sayı7 10 ile 50 arasındadır.")
    else:
        print("Sayı7 50 ile 100 arasındadır.")
else:
    print("Sayı 10-100 arasında değildir.")
"""
#ÖDEV2: Klavyeden girilen 4 sayıdan tek ve çift olanları toplayan program. (Önce algoritma akış şemasını çiziniz)
"""
tektoplam = 0
cifttoplam = 0
s1 = int(input("s1:"))
if((s1%2)==0):
    cifttoplam += s1
else:
    tektoplam += s1

s2 = int(input("s2:"))
if((s2%2)==0):
    cifttoplam += s2
else:
    tektoplam += s2

s3 = int(input("s3:"))
if((s3%2)==0):
    cifttoplam += s3
else:
    tektoplam += s3

s4 = int(input("s4:"))
if((s4%2)==0):
    cifttoplam += s4
else:
    tektoplam += s4

print("Tek sayıların toplamı:",tektoplam,"Çift sayıların toplamı:",cifttoplam)
"""
#ÖDEV4: Klavyeden girilen not değerini kontrol edip. 0 ile 100 arasında değilse ekrana "Hatalı aralık!!" yazdırsın.
#       0-44: Kaldınız
#       45-69: Geçtiniz:
#       70-84: İyi
#       85-100: Pekiyi
# Nota göre yukarıdaki mesajı ekrana yazdırınız.
""" CEVAP Başlangıç
dersNotu = int(input("Not giriniz:"))
if(dersNotu>=0 and dersNotu<=100):
    # Ders Notu 0-100 arasındadır.
    if(dersNotu<45):
        print("Kaldınız")
    elif(dersNotu<70):
        print("Geçtiniz")
    elif(dersNotu<85):
        print("İyi")
    else:
        print("Pekiyi")
else:
    print("Hatalı Aralık!!")
 CEVAP Bitiş"""


# Klavyeden girilen sayı 100'den küçükse YA Da 9'un katı ise ekrana UYGUN SAYI GİRDİNİZ yazsın.
# Şartlardan herhangi birini sağlamıyorsa UYGUN OLMAYAN BİR SAYI GİRDİNİZ yazsın.

"""
girilenSayi = int(input("Sayı giriniz:"))
kalan9 = girilenSayi%9

if(girilenSayi<100 or kalan9==0):
    print("UYGUN SAYI GİRDİNİZ")
else:
    print("UYGUN OLMAYAN BİR SAYI GİRDİNİZ")
"""

# Soru Kullanıcıdan isim, yaş ve çocuk sayısı alınsın.
"""
    Eğer kulanıcının yaşı 45'in altındaysa;
    Çocuk sayısına bakılacak. Ve çocuk sayısı 3'ten az ise çocuk başına 250₺ çok ise çocuk başına 200₺ 
    maaşa ekleme yapılacak.(Temel Maaş= 3000₺)
    45'in üzerinde ise çocuk başına para verilmeyecek ancak 500₺ ekleme yapılacak.
    Son olarak ekrana : "Nesrin Yılmaz, Maaşınız: 4000₺" yazılacak.  


isim = input("İsminiz:")
yas = int(input("Yaşınız:"))
cocuk = int(input("Çocuk Sayınız:"))
maas = 3000;

if yas<45 :
    if cocuk<3:
        maas+=(cocuk*250)
    else:
        maas+=(cocuk*200)
else:
    maas+=500;

print(isim,"maaşınız:",maas)

"""

