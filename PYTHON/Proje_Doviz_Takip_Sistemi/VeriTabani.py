import sqlite3

class VeriTabani:
    @staticmethod
    def Kaydet(komut):
        vt = sqlite3.connect('C:\\UCUNCUBINYIL\\Duzenlenecek\\PYTHON_1\\Proje_Ders3\\PyPara.db')
        try:
            cur = vt.cursor()
            cur.execute(komut)
            vt.commit()
            print("Kayıt başarılı.")
        except:
            print("Kayıt sırasında bir hata oluştu.")
        vt.close()
    @staticmethod
    def KurGetir(komut):
        vt = sqlite3.connect('C:\\UCUNCUBINYIL\\Duzenlenecek\\PYTHON_1\\Proje_Ders3\\PyPara.db')
        try:
            cur = vt.cursor()
            cur.execute(komut)
            listekur = cur.fetchall()
            listekur.reverse()
        except:
            print("Kur verisi çekilirken hata oluştu.")
        vt.close()
        return listekur
    @staticmethod
    def EsikGetir(komut):
        vt = sqlite3.connect('C:\\UCUNCUBINYIL\\Duzenlenecek\\PYTHON_1\\Proje_Ders3\\PyPara.db')
        try:
            cur = vt.cursor()
            cur.execute(komut)
            esik = cur.fetchone()
        except:
            print("Alarm verisi çekilirken hata oluştu.")
        vt.close()
        return esik[0]

    @staticmethod
    def KullaniciGetir(komut):
        vt = sqlite3.connect('C:\\UCUNCUBINYIL\\Duzenlenecek\\PYTHON_1\\Proje_Ders3\\PyPara.db')
        try:
            cur = vt.cursor()
            cur.execute(komut)
            bilgi = cur.fetchone()
        except:
            print("Kullanıcı verisi çekilirken hata oluştu.")
        vt.close()
        return bilgi[0],bilgi[1]

    @staticmethod
    def AlarmGetir():
        vt = sqlite3.connect('C:\\UCUNCUBINYIL\\Duzenlenecek\\PYTHON_1\\Proje_Ders3\\PyPara.db')
        try:
            cur = vt.cursor()
            cur.execute("SELECT esik,eposta from tb_alarm;")
            esikler = cur.fetchmany(6)
        except:
            print("Alarm verisi çekilirken hata oluştu.")
        vt.close()
        return esikler

    @staticmethod
    def EsikGetir(komut):
        vt = sqlite3.connect('C:\\UCUNCUBINYIL\\Duzenlenecek\\PYTHON_1\\Proje_Ders3\\PyPara.db')
        try:
            cur = vt.cursor()
            cur.execute(komut)
            esik = cur.fetchone()
        except:
            print("Alarm verisi çekilirken hata oluştu.")
        vt.close()
        return esik[0]
"""
bilgi = VeriTabani.AlarmGetir()
for b in bilgi:
    print(b)
"""


