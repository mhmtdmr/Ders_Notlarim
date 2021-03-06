#  Sqlite veritabanı ile temel işlemleri anlattıktan sonra bu dosya işlenecek.
#  Önce komut satırı sonra Sqlite Browser ile anlatılacak.

##############      Sqlite Veritabanına Bağlantı      ################

import sqlite3
vt=sqlite3.connect('C:\\SQL\\kurs.db')  # veri tabanı yolunu tanımladık.

##################      Kayıtları Okuma      ###################

# Ogrenci tablosundaki tüm kayıtları tek tek getiren kod bloğu.
'''
try:
    komut = "SELECT * FROM Ogrenci"
    cur = vt.cursor()               # Veri tabanında işlem yapmak için cursor nesnesi oluşturduk.
    cur.execute(komut)              # SQL komutunu execute fonksiyonu ile çalıştırdık.
    while True:
        record = cur.fetchone()     # Sorgudan dönen kayıtlara tek tek ulaşıyoruz.
        if record==None:
            break                   # Kayıtlar bittiyse döngüden çık.
        else:
            print(record)
except:
    print("Veri tabanına bağlanırken bir hata oluştu.")
'''


#Ogrenci tablosundaki kayıtları bir listeye atan kod bloğu.
'''
ogrenciler=[]
try:
    komut = "SELECT * FROM Ogrenci"
    cur = vt.cursor()
    cur.execute(komut)
    ogrenciler = cur.fetchall() # tüm kayıtları liste şeklinde döndürür.
except:
    print("Veri tabanına bağlanırken bir hata oluştu.")

print(ogrenciler)
'''

###############   Veri tabanına kayıt ekleme   ###############
'''
try:
    komut = "INSERT INTO Ogrenci (numara,ad,soyad) VALUES(3,'Ali','TEMİZKAN')"
    cur = vt.cursor()
    cur.execute(komut)
    vt.commit()  #Yazdığımız komutu işle anlamına gelir.
except:
    print("Veri tabanına bağlanırken bir hata oluştu.")
'''

# Klavyeden alınan 3 numara,ad,soyad bilgisini veritabanına kaydedin.
'''
for i in range(3):
    numara = input("Öğrenci numarası:")
    ad = input("Öğrenci adı:")
    soyad = input("Öğrenci soyadı:")
    try:
        komut = "INSERT INTO Ogrenci (numara,ad,soyad) VALUES("+numara+",'"+ad+"','"+soyad+"')"
        cur = vt.cursor()
        cur.execute(komut)
        vt.commit()
    except:
        print("Veri tabanına bağlanırken bir hata oluştu.")
'''


#Ogrenci tablosundaki kayıtları bir listeye atan ve yazdıran kod bloğu.
def OgrenciListele():
    ogrenciler=[]
    try:
        komut = "SELECT * FROM Ogrenci"
        cur = vt.cursor()
        cur.execute(komut)
        ogrenciler = cur.fetchall() # tüm kayıtları liste şeklinde döndürür.
    except:
        print("Veri tabanına bağlanırken bir hata oluştu.")
    print(ogrenciler)

OgrenciListele()

###################     Veritabanından Silme İşlemleri    #################

# Kullanıcıdan aldığınız numaraya ait kayıtı veritabanından siliniz.
silinecekNumara = input("Silmek istediğiniz öğrencinin numarasını giriniz:")
komut = "DELETE FROM Ogrenci WHERE numara = "+ silinecekNumara
#print(komut)
try:
    cur = vt.cursor()
    cur.execute(komut)
    vt.commit()
    print("Kayıt başarı ile silinmiştir.")
except:
    print("Veri tabanına bağlanırken bir hata oluştu.")

OgrenciListele()

vt.close()                          # Veri tabanı bağlantısını sonladırır.




## Sql Injection'a uygun veri kayıt işlemi.
"""
try:
    numara = int(input("Numara giriniz:"))
    ad = input("ad:")
    soyad = input("soyad:")

    komut = "INSERT INTO Ogrenci (numara,ad,soyad) VALUES("+str(numara)+",'"+ad+"','"+soyad+"');"
    print(komut)
    cur = vt.cursor()
    cur.executescript(komut)
    vt.commit()
    vt.close()
    print("Kayıt başarılı.")
except:
    print("Kayıt sırasında bir hata oluştu.")
"""

## PARAMETRELİ INSERT SQL INJECTION'ı engeller.
"""
try:
    numara = int(input("Numara giriniz:"))
    ad = input("ad:")
    soyad = input("soyad:")

    komut = "INSERT INTO Ogrenci (numara,ad,soyad) VALUES(?,?,?);"
    print(komut)
    cur = vt.cursor()
    cur.execute(komut,(numara,ad,soyad))
    vt.commit()
    vt.close()
    print("Kayıt başarılı.")
except:
    print("Kayıt sırasında bir hata oluştu.")
"""

## Listeyi veritabanındaki tabloya kaydetme.
"""
ogrenciler = [(3,'Selin','Kahraman'),(4,'Tuba','Kaynarca'),(5,'Eray','Erdem'),(6,'Türker','Baltacı')]
try:
    komut = "INSERT INTO Ogrenci (numara,ad,soyad) VALUES(?,?,?);"
    cur = vt.cursor()
    cur.executemany(komut,ogrenciler)
    vt.commit()
    vt.close()
    print("Kayıt başarılı.")
except:
    print("Kayıt sırasında bir hata oluştu.")
"""

# Ders-015_SQL_Class.py dosyası ile sınıf yapısı ile veri tabanı erişimleri anlatılacak.

# Daha fazlası için: https://www.sqlitetutorial.net/






