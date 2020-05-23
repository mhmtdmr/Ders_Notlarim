import threading
from tkinter import *
from tkinter.ttk import *
from Grafik import Grafik  # Grafik.py'den Grafik sınıfını içeri aktardık.import
from Kur import Kur
from VeriTabani import VeriTabani
from Kullanici import Kullanici
import datetime



def alarmKur(a, b, c):
    print(a, b, c)
class Doviz:
    pencere = Tk()
    # TAB oluşturma ve çerçeveleri ekleme.
    tab_control = Notebook(pencere)
    #Çerçeveleri oluşturuyoruz.
    tab_altin = Frame(tab_control)
    tab_dolar = Frame(tab_control)
    tab_euro = Frame(tab_control)
    tab_kullanici = Frame(tab_control)
    #Çerçeve başlıklarını oluşturuyoruz.
    tab_control.add(tab_altin,text="Altın")
    tab_control.add(tab_dolar,text="Dolar")
    tab_control.add(tab_euro,text="Euro")
    tab_control.add(tab_kullanici,text="Kullanıcı")
    #tab'ı konumlandırıyoruz.
    tab_control.grid(row=0,column=0,ipadx=10,ipady=10)


    #Düşüş Alarmı Nesneleri
    lbl_altin_dusus = Label(tab_altin, text="Düşüş Alarmı",font=("Consolas",16))
    txt_altin_dusus = Entry(tab_altin,font=("Consolas",16))

    @staticmethod
    def alarmAltinDusus():
        print("asdasdasd")
        """
        esik = Doviz.txt_altin_dusus.get()
        print(esik)
        """

    btn_altin_dusus = Button(tab_altin, text="Ayarla",command=alarmAltinDusus)
    lbl_altin_dusus.grid(row=1,column=0,padx=5,pady=5)
    txt_altin_dusus.grid(row=1,column=1,padx=5,pady=5)
    btn_altin_dusus.grid(row=1,column=2,padx=5,pady=5)

    #Yükselme Alarmı Nesneleri.
    lbl_altin_yukselme = Label(tab_altin, text="Yükselme Alarmı",font=("Consolas",16))
    txt_altin_yukselme = Entry(tab_altin,font=("Consolas",16))
    btn_altin_yukselme = Button(tab_altin, text="Ayarla")
    lbl_altin_yukselme.grid(row=2,column=0,padx=5,pady=5)
    txt_altin_yukselme.grid(row=2,column=1,padx=5,pady=5)
    btn_altin_yukselme.grid(row=2,column=2,padx=5,pady=5)

    @classmethod
    def zamanFormat(cls,zamanStr):
        zamanKisa = []
        for z in zamanStr:
            zmn = datetime.datetime.strptime(z, '%d.%m.%Y %H:%M:%S')
            zmn = zmn.strftime("%d.%m  %H:%M")
            zamanKisa.append(zmn)
        return zamanKisa

    @classmethod
    def tekrar(cls):

        komut = "SELECT zaman,kur FROM tb_altin ORDER BY (zaman) DESC LIMIT 14;"  # Son 7 kaydı getir.
        altinKur = VeriTabani.KurGetir(komut)
        x = [row[0] for row in altinKur]
        xf = cls.zamanFormat(x)
        y = [row[1] for row in altinKur]
        Grafik.Ciz(cls.tab_altin, xf, y, "Altın Kuru")



        komut = "SELECT zaman,kur FROM tb_dolar ORDER BY (zaman) DESC LIMIT 14;"  # Son 7 kaydı getir.
        dolarKur = VeriTabani.KurGetir(komut)
        x = [row[0] for row in dolarKur]
        xf = cls.zamanFormat(x)
        y = [row[1] for row in dolarKur]
        Grafik.Ciz(cls.tab_dolar,xf,y,"Dolar Kuru")

        komut = "SELECT zaman,kur FROM tb_euro ORDER BY (zaman) DESC LIMIT 14;"  # Son 7 kaydı getir.
        euroKur = VeriTabani.KurGetir(komut)
        x = [row[0] for row in euroKur]
        xf = cls.zamanFormat(x)
        y = [row[1] for row in euroKur]
        Grafik.Ciz(cls.tab_euro,xf,y,"Euro Kuru")

        altin = threading.Thread(target=Kur.Getir, args=["altin"])
        dolar = threading.Thread(target=Kur.Getir, args=["dolar"])
        euro = threading.Thread(target=Kur.Getir, args=["euro"])
        altin.start()
        dolar.start()
        euro.start()

        cls.pencere.after(30000,cls.tekrar) #pencere açıldıktan sonra 30 saniyede bir tekrar fonskiyonunu çalıştır.


"""
k = Kullanici()
k.adsoyad = "Mehmet DEMİR"
k.eposta = "mail.mehmetdemir@gmail.com"
k.Kaydet()

"""

"""
altin = threading.Thread(target=Kur.Getir,args=["altin"])
dolar = threading.Thread(target=Kur.Getir,args=["dolar"])
euro = threading.Thread(target=Kur.Getir,args=["euro"])
altin.start()
dolar.start()
euro.start()
"""
Doviz.tekrar()
Doviz.pencere.mainloop()