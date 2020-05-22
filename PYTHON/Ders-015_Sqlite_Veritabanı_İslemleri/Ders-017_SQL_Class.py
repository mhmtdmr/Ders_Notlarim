import sqlite3

"""
def SQL_Ac():
    try:
        vt = sqlite3.connect('C:\\SQLITE\\kurs.db')
    except(Exception):
        print("Bağlantı yapılamadı.",Exception)

def SQL_Kapat():
    try:
        vt.close();
    except(Exception):
        print("Bağlantı kapatılamadı.",Exception)
"""

class Ogrenci:
    def __init__(self,nu,ad,so):
        self.numara = nu
        self.ad = ad
        self.soyad = so

    def Kaydet(self):
        vt = sqlite3.connect('C:\\SQLITE\\kurs.db')
        try:
            komut = "INSERT INTO Ogrenci (numara,ad,soyad) VALUES(?,?,?);"
            cur = vt.cursor()
            cur.execute(komut, (self.numara, self.ad, self.soyad))
            vt.commit()
            print("Kayıt başarılı.")
        except:
            print("Kayıt sırasında bir hata oluştu.")
        vt.close()

    @classmethod
    def Listele(cls):
        vt = sqlite3.connect('C:\\SQLITE\\kurs.db')
        try:
            komut = "SELECT * FROM Ogrenci;"
            cur = vt.cursor()
            cur.execute(komut)
            while(True):
                kayit = cur.fetchone() # Getirilen kayıtları satır satır okumak için.
                if(kayit==None):
                    break
                else:
                    print(kayit)
        except:
            print("Listeleme sırasında bir hata oluştu!")
        vt.close()

    # Parametre olarak alınan no'lu öğrencinin ad,soyad bilgisini döndüren fonk.
    @classmethod
    def Bul(cls,no):
        vt = sqlite3.connect("C:\\SQLITE\\kurs.db")
        komut = "SELECT ad,soyad FROM Ogrenci WHERE numara="+str(no)+";"
        cur = vt.cursor()
        cur.execute(komut)
        kayit = cur.fetchone()
        if(kayit==None):
            print("Böyle bir numara bulunamadı.")
        else:
            return kayit
        vt.close()



#ogr = Ogrenci(10,'Aysel','KILIÇ')
#ogr.Kaydet()
#Ogrenci.Listele()
print(Ogrenci.Bul(3))






