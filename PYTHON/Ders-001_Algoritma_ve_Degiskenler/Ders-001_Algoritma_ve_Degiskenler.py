#######################################            Algoritma           #############################################
'''
Algoritma: Bir sorunu çözmek veya belirlenmiş bir amaca ulaşmak için tasarlanan yola,
takip edilen işlem basamaklarına denir. Algoritmalar açıkça belirtilmiş bir başlangıcı
ve sonu olan işlemler kümesidir.

Amaca ulaşmak için işlenecek çözüm yolları ve sıralamaları belirlenir ve algoritma bu sırayı takip ederek en mantıklı
çözüme ulaşır.


    Giriş/Çıkış Bilgisi: Algoritmalarda giriş ve çıkış bilgileri olmalıdır. Dışarıdan gelen verilere giriş bilgisi denir.
        Bu veriler algoritmada işlenir ve çıkış bilgisini oluşturur. Çıkış bilgisi her algoritmada mutlaka vardır.
        Algoritmaların temel amacı giriş bilgisini işleyerek çıkış bilgisi oluşturmaktır.

    Sonluluk: Her türlü olasılık için algoritma sonlu adımda bitmelidir. Algoritma sonsuz döngüye girmemelidir.
        Başı ve sonu belli olmalıdır.
    Kesinlik: Her komut kişinin kalem ve kağıt ile yürütebileceği kadar basit olmalıdır. Algoritmanın her adımı anlaşılır,
        basit ve kesin bir biçimde ifade edilmiş olmalıdır. Kesinlikle yorum gerektirmemeli ve belirsiz ifadelere sahip
        olmamalıdır.
    Etkinlik: Yazılan algoritmalar etkin ve dolayısıyla gereksiz tekrarlardan uzak oluşturulmalıdır.
        Bu algoritmanın temel özelliklerinden birisidir. Ayrıca algoritmalar genel amaçlı yazılıp yapısal bir ana
        algoritma ve alt algoritmalardan oluşturulmalıdır.
        Böylece daha önce yazılmış bir algoritma daha sonra başka işlemler için de kullanılabilir.
        Buna örnek vermek gerekirse eğer elimizde, verilen n adet sayının ortalamasını bulmakta kullandığımız algoritma
        varsa bu algoritma, bir sınıfta öğrencilerin yaş ortalamasını bulan bir algoritma için de kullanılabilmelidir.
    Başarım ve Performans: Amaç donanım gereksinimi (bellek kullanımı gibi), çalışma süresi gibi performans kriterlerini
        dikkate alarak yüksek başarımlı programlar yazmak olmalıdır. Gereksiz tekrarlar ortadan kaldırılmalıdır.
        Bir algoritmanın performans değerlendirmesinde aşağıdaki temel kriterler göz önünde bulundurulur.
            Birim İşlem Zamanı
            Veri Arama ve Getirme Zamanı
            Kıyaslama Zamanı
            Aktarma Zamanı





İlk algoritma, El-Harezmi’nin ‘Hisab-el Cebir ve El Mukabala’ kitabında sunulmuştur
ve algoritma kelimesi de El-Harezmi’nin isminden gelmiştir.


Örnek 1: Kullanıcı tarafından belirlenen 3 farklı sayının ortalamasını alalım.

Bu algoritmadaki değişkenlerimiz : x,y,z,sonuc

İ0: Başla.
İ1: x sayısını gir.
İ2: y sayısını gir.
İ3: z sayısını gir.
İ4: sonuc = (x+y+z)/3 işlemini yap.
İ5: sonuc değişkenini göster.
İ6: Dur.


Akış Diyagramları: algoritmanın okunması ve takibi karıştırmaya müsait bir yapı olmasından dolayı
    algoritmanın görselleştirilmiş halidir.

ÖDEV: Görsellere bak!

'''

"""
Python kurulumundan bahset.  Python yorumlayıcını anlat. Daha sonra IDE kavramından bahsedip devam et.
"""

#Yorum Satırı(tek satır) (Comment Line)
"""
Yorum Bloğu (çoklu satır)(MultiLine Comment)
"""



#######################################            Değişkenler           #############################################
#AÇIKLAMA: Bilgisayarın çalışma prensibinden bahset.(CPU-RAM-Disk) Değişkenlerin kullanım amacını açıkla.

# isimlendirme kuralları(case-sensitive)
# yanlışlar: 5Sayi,Sayi-5,kucuk sayi
# doğrular: Sayi5,Sayi_5,_Sayi5,KucukSayi,Kucuk_Sayi


# Veri Tipleri
# Python'da veriler 3 tür olarak sınıflandırılır.
# Sayısal Türler(int,float,complex(karmaşık sayılar(3+5j))),Karakter Dizileri, Mantıksal Veri Türü
"""
int: Tamsayı değerlerini tutan veri türüdür. (i = 1)
float: Ondalıklı sayı değerlerini tutan veri türüdür. (f = 4.5)
complex: Karmaşık sayıları tutan veri türüdür. (c = 5+3j)
"""

### Sayısal Veri Tipleri ###
i = 5
print(type(i))

j = 9.4
print(type(j))

x=5
y = 4+3j
print(y)      #print fonksiyonu ile ekrana veri yadırabiliriz.
print(y.real) #reel kısım
print(y.imag) #sanal kısım
print(type(y))



kucuk_Sayi = 5
buyuk_Sayi = 6
toplam = kucuk_Sayi + buyuk_Sayi
c1=c2=c3 = 34 # 3 değişkene birden 34 değerini atadık.
print("c1:",c1) #print komutu metinsel ifadeler ile degiskenlerdeki veriyi birlikte yazmamıza imkân verir. ,  ile.
print("c2:",c2)
print("c3:",c3)

v1,v2,v3 = 3,4,5 #Tek seferde 3 değişkene farklı değerler atadık. Sıralı atama.
print("v1:",v1)
print("v2:",v2)
print("v3:",v3)

#Değerler karşılıklı olarak yer değiştirildi.
x1 = 5
x2 = 7
x1,x2=x2,x1
print(x1)
print(x2)

# Bu aşamada hesap makinesine giden yol ile ilgili bir projeksiyon çizilebilir.
# Bu sayede öğrenci değişken kavramını daha iyi kavrayacaktır.



### Karakter Dizileri (String) ###

# isim = "Cansu"
# soyisim = "Akdağ"
# harf = "S"
degiskenAdi1 = "Bu sene şampiyon 'Sivasspor' olsun..."
print(degiskenAdi1)
print(type(degiskenAdi1))


degiskenAdi2 = 'Kursumuzun adı "Üçüncü Binyıl Eğitim Akademisi"dir'
print(degiskenAdi2)


# Kaçış karakterleri (Escape Characters)
yazi = "Merhaba\nDünya" #  \n : new line : alt satıra atar.
#print(yazi)
yazi = "Merhaba\t\t\t\tDünya" # \t: tab: 1 tab boşluk bırakır. 1 tab = 4 space
#print(yazi )
#print("Dosya Yolu: C:\\Programlar\\") # metinin içinde \ kullanmak için 2 adet yazdık.
degiskenAdi3 = "Programın dosyaları C:\\\\Program Files\\ altındadır."
print(degiskenAdi3)



print("Bugün","hava","güneşli")
print("Bugün","hava","güneşli",sep="")
print("Bugün","hava","güneşli",sep="_")
print("Bugün","hava","güneşli",end="!")# print metodu varsayılan olarak metinin sonuna \n ekler. Bunu engelledik.
print("\n")
print(1,2,3,4,5,6,7,8,9, sep="x")
print(*"123456789", sep="x")
print("Bir tab boşluk\tolsun.")
print("Bir alt satıra\ngeçsin.")

print("""
*********************************************
*********************************************
        Merhaba Dünyalılar
        Bugün nasılsınız bakayım? :D
*********************************************
*********************************************
""")


### Mantıksal Veri Türü: Boolean ###
dogruMu = True
dogruMu = False
soldakiBuyukMu = 3>5
print(soldakiBuyukMu)
print(type(soldakiBuyukMu))


'''
#ad: str=input("Adınızı giriniz:");
#print(ad)

sayiMi = False
while(sayiMi==False):
    sayi:str=input("Sayı giriniz:")
    sayiMi = sayi.isnumeric()
iSayi = int(sayi)
print(iSayi*iSayi)
'''
