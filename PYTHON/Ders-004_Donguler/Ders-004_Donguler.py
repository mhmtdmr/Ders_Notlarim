
####################################################
################### DÖNGÜLER #######################
####################################################

###    WHILE   ###
"""
while(kosul):
    kosul sağlandığı sürece çalışacak komutlar # 1 tab boşluk: döngü içini ifade eder.
"""
# 1-10 arasındaki sayıları ekrana yazdırınız.
"""
sayi = 1
while(sayi<=10):
    print(sayi)
    sayi = sayi +1
"""
# 90-100 arasındaki sayıları ekrana yazdıran program.
"""
sayi = 90
while(sayi<100):
    print(sayi,"100'den küçüktür!")
    sayi+=1
"""
#SORU1: 70-55 arasındaki sayıları ekrana büyükten küçüğe yazdıran program.
"""
sayi=70
while(sayi>=55):
    print(sayi)
    sayi = sayi -1
"""
#SORU2: 70-55 arasında 3'te tam bölünenleri ekrana yazdırın
"""
sayac = 70
while(sayac>=55):
    if(sayac%3==0):
        print(sayac)
    sayac = sayac - 1
"""
# Sayı 0 dan büyük ve 999 dan küçük olduğu sürece ekrana Merhaba yazdıran Program.
"""
sayi = 775
while(sayi>0 and sayi<999): #(sayi>0 and sayi<999) or (sayi%2==1) :
    print(sayi)
    sayi += 10
"""
# 7- 77 arasındaki tüm sayıları toplayıp ekrana yazdıran program.
"""
sayi = 7
toplam=0
while(sayi<=77):
    toplam+=sayi
    sayi += 1
print(toplam)
"""
# SORU: 1'den klavyeden girilen sayıya kadar olan sayıların karelerini toplayan program.
"""
kgs = int(input("Bir sayı giriniz:"))
sayi = 1
toplam = 0
while(sayi<=kgs):
    toplam += (sayi**2)
    sayi+=1

print("1'den",kgs,"sayısına kadar olan sayıların karelerinin toplamı:",toplam)
"""
### BREAK: Döngüden çıkma. ###  continue: döngünün bir adım ilerletilmesi
"""
sayi = 1
while(sayi<=10):
    if(sayi==2):
        sayi+=1
        pass
        print("2 numara yazılmayacak!!!")
    if(sayi==3):
        sayi+=1
        continue # Bu satırdan sonraki kısım çalıştırılmadan döngüye geri döner.
    print(sayi)
    sayi+=1
    if(sayi==8):
        break     # sayı 8 ise döngüden çık!!
"""
# SORU: Klavyeden girilen değer 'cık' ise döngüden çıksın. Değilse girilen sayıları toplayıp cıkılınca ekrana yazdırsın.


#print(1==1)  => True değerini üretir.
"""
toplam = 0
while(True):
    yazi = input("Sayı giriniz:")
    if(yazi=="cık"):
        break
    else:
        sayi = int(yazi)
        toplam += sayi
print(toplam)
"""
# 1-100 arasındaki sayıların toplayan program. Ancak aşağıdaki durumlarda sayıyı toplama eklemeyecek.
# * Sayı 7'nin katı ise toplama eklenmesin.
# * Sayı'nın 3 katının 3 fazlası 37'nın katı ise döngüden çıksın.
"""
print((3*(7)+3))

sayi = 1
toplam = 0
while(sayi<=100):
    if(sayi%7==0):
        sayi+=1
        continue
    kat = 3*(sayi)+7
    if(kat%37==0):
        print("Kat:",kat)
        break
    toplam += sayi
    sayi+=1

print("Toplam:",toplam)

"""

#İşlem adımları:   Sayı giriniz:...
                   #Çıkmak istiyor musunuz: Evet se çıkacak Başka birşeyse devam edecek
#Sonunda girilen sayıların çarpımını ekrana yazdıran program
'''
carpim = 1
while(True):
    sayi = int(input("Sayı giriniz:"))
    carpim *= sayi
    cevap = input("Çıkmak ister misiniz?(Evet/Hayır) ").upper()
    print("harfler büyütüldükten sonra:",cevap)
    if(cevap=="EVET"):
        break
    else:
        continue
print("Sayıların çarpımı:",carpim)
'''


###############################         ALIŞTIRMALAR        ####################################


#1: 1-99 arasındaki tek sayıları ekrana yazdıran program.
#2: Kullanıcının girdiği ismi kullanıcının girdiği sayı kadar ekrana yazdıran program.
#3: Klavyeden girilen sayının faktoriyelini bulan programı while döngüsü kullanarak yazınız.
#4: Klavyeden girilen 2 değer arasındaki sayıları toplayan program.





###   FOR DÖNGÜSÜ   ###
# Aralık tanımlama
range(5)  # 0,1,2,3,4   (bitiş)
range(2, 5)  # 2,3,4     (başlangıç,bitiş)
range(1, 9, 3)  # 1,4,7   (başlangıç,bitiş,artış)  #bitiş değeri hariç!!!
"""
#0'dan 5'e kadar olan sayıları ekrana yazdır.
for sayi in range(5):
    print(sayi,end="")
print()
for sayi in range(2,5):
    print(sayi,end="")
print()
for sayi in range(1,9,3):
    print(sayi,end="")

"""

"""
ilce = "KADIKÖY"
for harf in ilce:
    print(harf)
    print(type(harf))
"""
###############################         ALIŞTIRMALAR        ####################################

# 1 ile 40 arasındaki sayıları toplayan program.(1,40 dahil)
"""
toplam = 0
for i in range(41):
    toplam += i
print("Sayıların toplamı:",toplam)
"""
# 20-40 arasındaki çift sayıları for döngüsü ile ekrana yazdıran program.
"""
for i in range(20,40,2):
    print(i)
"""
# for örneği: 1'den klavyeden girilen sayıya kadar olan sayılardan 4'e tam bölünenlerin çarpımını yazdıran program.
"""
carpim = 1
sayi = int(input("Sayı giriniz:"))
for i in range (1,sayi):
    if(i%4==0):
        carpim *= i
        print(i,"* ",end="")
print("=",carpim)
"""

# Klavyeden girilen sayının rakamları toplamını bulan program.
"""
toplam=0
sayi = input("Sayı Giriniz:")
for r in sayi:
    toplam += int(r)
print("Rakamlar Toplamı:",toplam)
"""
# print("*"*7)
# Aşağıdaki çıktıyı veren kodu for döngüsü ile yazınız.
"""
*
**
***
****
*****
"""
"""
for i in range(1,6):
    print("*"*i) # Satır numarası kadar yıldızı tekrar et.

"""
"""
***********
*         *  # 1 yıldız + 8 boşluk + 1 yıldız
*         *
*         *
***********
"""
"""
for i in range(1,6):
    if(i==1 or i==5):
        print("*"*10)
    else:
        print("*",(" "*8),"*",sep="")

"""
"""
                *
               ***
              *****
             *******
            *********   
"""
"""
sayac=1
for satir in range(1,6):
    print(" "*(5-satir),end="")
    print("*"*sayac)
    sayac += 2
"""
"""
for i in range(10,0,-1):
    print(i)
"""
"""

for i in range(1,10):
    for j in range(1,10):
        print(i,"x",j,"=",(i*j),end="  ")
    print()

"""

# Kullanıcı: personel sayısını girsin. Her personel için çocuk sayısı sorulsun.
# Program her çocuk için : "Çocuğunuz adına 1 ağaç dikilmiştir."
# Toplam dikilen ağaç sayısını yazsın.
"""
toplamAgac=0
while(True):
    p = input("personel sayını giriniz:")
    if(p.isnumeric()):
        break
    else:
        print("Lütfen sayısal değer giriniz.")
p=int(p)

for i in range(1,p+1):
    while (True):
        mesaj = str(i)+" numaralı personel için çocuk sayısını giriniz:"
        c = input(mesaj)
        if (c.isnumeric()):
            break
        else:
            print("Lütfen sayısal değer giriniz.")
    c=int(c)
    for j in range(c):
        print("Çocuğunuz adına 1 ağaç dikilmiştir.")
        toplamAgac+=1
print("Toplam Ağaç Sayısı:",toplamAgac)


"""
"""
a = "15"
print(a.isnumeric())
if(a.isnumeric()):
    a = int(a)
else:
    print("Lütfen sayısal değer giriniz.")
"""
"""

for i in range(10):
    if(i==6):
        continue
    if(i==8):
        break
    print(i)
"""
import random

a = random.randint(1, 10)
# print(a)
# Yukarıda üretilen sayıyı tahmin etme oyunu:
# Kullanıcının 4 hakkı olsun.
# 3. hakkınızda bildiniz ya da bilemedeniz
# mesaj verelim.
for i in range(4):
    mesaj = str((i + 1)) + ". Tahmininiz:"
    tahmin = input(mesaj)
    if (tahmin.isnumeric()):
        tahmin = int(tahmin)
    if (tahmin == a):
        print((i + 1), ". hakkınızda bildiniz.")
        break;
    else:
        print("Bilemediniz.")


# Aynı soruyu 1-100 arasında sayı üreterek. 6 hak ile yapınız.
# Farklı olarak daha büyük,daha küçük sayı giriniz gibi yönerge olsun.
# Klavyeden girilen metnin harflerinin ASCII tablosundaki sayısal değerleri toplamını bulan program.

# ÖDEV: Klavyeden girilen metindeki karakterlerin sayısal ortalamasını bulup;
# karaktere çevirip. Ortalama olarak "X" karakteri girdiniz yazdırsın.
# ÖDEV: Bir değişkene atadığımız 1--100 arsındaki sayıyı tahmin etme oyunu.
    # Her olumsuz cevapta aşağı veya yukarı diye yönlendirme olacak.
    # Deneme sayısı 15 olacak.
    # En son kaç tahminde bildiğini yazacak.

# ÖDEV: Klavyeden girilen metindeki karakterlerin sayısal ortalamasını bulup;
# karaktere çevirip. Ortalama olarak "X" karakteri girdiniz yazdırsın.
#cvp1


"""
fat =input("bir keliime giriniz: ")
toplam = 0
c = 0

for k in fat :
    c+=1
    toplam += int(ord(k))


    print("giriken kelimedeki harflerin toplamı: ")
print("ortalama : ", toplam/c)

#Q2
x = 30
i = 1
for i in range(1,16):
    while True:
        sayi = input ("1'den 100'e kadar bir sayı giriniz: ")
        if sayi.isnumeric():
            break
        else:
            pass
            print("Yanlış giriş yaptınız: ")

    sayi = int(sayi)
    if sayi == x:
        print("Kazandınız!")
        print(i,"denemede bildiniz")
        break
    elif sayi < x:
        print("Yukarı!")
    else:
        print("Aşağı!")
if i==15:
    print("Tüm haklarınızı kullandınız")

"""