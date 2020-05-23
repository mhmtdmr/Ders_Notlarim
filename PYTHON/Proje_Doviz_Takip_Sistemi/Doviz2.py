import threading
from tkinter import *
from tkinter.ttk import *
from Grafik import Grafik  # Grafik.py'den Grafik sınıfını içeri aktardık.import
from Kur import Kur
from VeriTabani import VeriTabani
from Kullanici import Kullanici
import datetime
from tkinter import messagebox


def alarmAltinDusme():
    esik = Doviz.txt_altin_dusus.get()
    komut = f"UPDATE tb_alarm SET esik={esik} WHERE doviztipi='altin' AND alarmtipi='dusme';"
    VeriTabani.Kaydet(komut)
    VeriTabani.Kaydet("UPDATE tb_alarm SET eposta='HAYIR' WHERE doviztipi = 'altin' AND alarmtipi = 'dusme';")

def alarmDolarDusme():
    esik = Doviz.txt_dolar_dusus.get()
    komut = f"UPDATE tb_alarm SET esik={esik} WHERE doviztipi='dolar' AND alarmtipi='dusme';"
    VeriTabani.Kaydet(komut)
    VeriTabani.Kaydet("UPDATE tb_alarm SET eposta='HAYIR' WHERE doviztipi = 'dolar' AND alarmtipi = 'dusme';")
def alarmEuroDusme():
    esik = Doviz.txt_euro_dusus.get()
    komut = f"UPDATE tb_alarm SET esik={esik} WHERE doviztipi='euro' AND alarmtipi='dusme';"
    VeriTabani.Kaydet(komut)
    VeriTabani.Kaydet("UPDATE tb_alarm SET eposta='HAYIR' WHERE doviztipi = 'euro' AND alarmtipi = 'dusme';")




def alarmAltinYukselme():
    esik = Doviz.txt_altin_yukselme.get()
    komut = f"UPDATE tb_alarm SET esik={esik} WHERE doviztipi='altin' AND alarmtipi='yukselme';"
    VeriTabani.Kaydet(komut)
    VeriTabani.Kaydet("UPDATE tb_alarm SET eposta='HAYIR' WHERE doviztipi = 'altin' AND alarmtipi = 'yukselme';")


def alarmDolarYukselme():
    esik = Doviz.txt_dolar_yukselme.get()
    komut = f"UPDATE tb_alarm SET esik={esik} WHERE doviztipi='dolar' AND alarmtipi='yukselme';"
    VeriTabani.Kaydet(komut)
    VeriTabani.Kaydet("UPDATE tb_alarm SET eposta='HAYIR' WHERE doviztipi = 'dolar' AND alarmtipi = 'yukselme';")

def alarmEuroYukselme():
    esik = Doviz.txt_euro_yukselme.get()
    komut = f"UPDATE tb_alarm SET esik={esik} WHERE doviztipi='euro' AND alarmtipi='yukselme';"
    VeriTabani.Kaydet(komut)
    VeriTabani.Kaydet("UPDATE tb_alarm SET eposta='HAYIR' WHERE doviztipi = 'euro' AND alarmtipi = 'yukselme';")

def KullaniciKaydet():
    k = Kullanici()
    k.adsoyad = Doviz.txt_kullanici_adsoyad.get()
    k.eposta = Doviz.txt_kullanici_eposta.get()
    k.Kaydet()


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
    #altın
    lbl_altin_dusus = Label(tab_altin, text="Düşüş Alarmı",font=("Consolas",16))
    txt_altin_dusus = Entry(tab_altin,font=("Consolas",16))
    btn_altin_dusus = Button(tab_altin, text="Ayarla",command=alarmAltinDusme)
    lbl_altin_kur_baslik = Label(tab_altin,text="Anlık Kur",font=("Consolas",16))
    lbl_altin_kur = Label(tab_altin,text="",font=("Consolas",16))
    lbl_altin_dusus.grid(row=1,column=0,padx=5,pady=5)
    txt_altin_dusus.grid(row=1,column=1,padx=5,pady=5)
    btn_altin_dusus.grid(row=1,column=2,padx=5,pady=5)
    lbl_altin_kur_baslik.grid(row=1,column=3,padx=5,pady=5)
    lbl_altin_kur.grid(row=2,column=3,padx=5,pady=5)

    #dolar
    lbl_dolar_dusus = Label(tab_dolar, text="Düşüş Alarmı",font=("Consolas",16))
    txt_dolar_dusus = Entry(tab_dolar,font=("Consolas",16))
    btn_dolar_dusus = Button(tab_dolar, text="Ayarla",command=alarmDolarDusme)
    lbl_dolar_kur_baslik = Label(tab_dolar,text="Anlık Kur",font=("Consolas",16))
    lbl_dolar_kur = Label(tab_dolar,text="",font=("Consolas",16))

    lbl_dolar_dusus.grid(row=1,column=0,padx=5,pady=5)
    txt_dolar_dusus.grid(row=1,column=1,padx=5,pady=5)
    btn_dolar_dusus.grid(row=1,column=2,padx=5,pady=5)
    lbl_dolar_kur_baslik.grid(row=1,column=3,padx=5,pady=5)
    lbl_dolar_kur.grid(row=2,column=3,padx=5,pady=5)
    #euro
    lbl_euro_dusus = Label(tab_euro, text="Düşüş Alarmı",font=("Consolas",16))
    txt_euro_dusus = Entry(tab_euro,font=("Consolas",16))
    btn_euro_dusus = Button(tab_euro, text="Ayarla",command=alarmEuroDusme)
    lbl_euro_kur_baslik = Label(tab_euro,text="Anlık Kur",font=("Consolas",16))
    lbl_euro_kur = Label(tab_euro,text="",font=("Consolas",16))

    lbl_euro_dusus.grid(row=1,column=0,padx=5,pady=5)
    txt_euro_dusus.grid(row=1,column=1,padx=5,pady=5)
    btn_euro_dusus.grid(row=1,column=2,padx=5,pady=5)
    lbl_euro_kur_baslik.grid(row=1,column=3,padx=5,pady=5)
    lbl_euro_kur.grid(row=2,column=3,padx=5,pady=5)

    #Yükselme Alarmı Nesneleri.
    #altin
    lbl_altin_yukselme = Label(tab_altin, text="Yükselme Alarmı",font=("Consolas",16))
    txt_altin_yukselme = Entry(tab_altin,font=("Consolas",16))
    btn_altin_yukselme = Button(tab_altin, text="Ayarla",command=alarmAltinYukselme)
    lbl_altin_yukselme.grid(row=2,column=0,padx=5,pady=5)
    txt_altin_yukselme.grid(row=2,column=1,padx=5,pady=5)
    btn_altin_yukselme.grid(row=2,column=2,padx=5,pady=5)

    #dolar
    lbl_dolar_yukselme = Label(tab_dolar, text="Yükselme Alarmı",font=("Consolas",16))
    txt_dolar_yukselme = Entry(tab_dolar,font=("Consolas",16))
    btn_dolar_yukselme = Button(tab_dolar, text="Ayarla",command=alarmDolarYukselme)
    lbl_dolar_yukselme.grid(row=2,column=0,padx=5,pady=5)
    txt_dolar_yukselme.grid(row=2,column=1,padx=5,pady=5)
    btn_dolar_yukselme.grid(row=2,column=2,padx=5,pady=5)

    #euro
    lbl_euro_yukselme = Label(tab_euro, text="Yükselme Alarmı",font=("Consolas",16))
    txt_euro_yukselme = Entry(tab_euro,font=("Consolas",16))
    btn_euro_yukselme = Button(tab_euro, text="Ayarla",command=alarmEuroYukselme)
    lbl_euro_yukselme.grid(row=2,column=0,padx=5,pady=5)
    txt_euro_yukselme.grid(row=2,column=1,padx=5,pady=5)
    btn_euro_yukselme.grid(row=2,column=2,padx=5,pady=5)

    #Kullanıcı Sayfası
    lbl_kullanici_adsoyad = Label(tab_kullanici, text="Ad soyad :",font=("Consolas",16))
    txt_kullanici_adsoyad = Entry(tab_kullanici,font=("Consolas",16),width=30)

    lbl_kullanici_eposta = Label(tab_kullanici, text="Eposta :",font=("Consolas",16))
    txt_kullanici_eposta = Entry(tab_kullanici,font=("Consolas",16),width=30)
    btn_kullanici_kaydet = Button(tab_kullanici, text="Kaydet", command=KullaniciKaydet,width=30)

    lbl_kullanici_adsoyad.grid(row=0,column=0,padx=5,pady=5)
    txt_kullanici_adsoyad.grid(row=0,column=1,padx=5,pady=5)
    lbl_kullanici_eposta.grid(row=1,column=0,padx=5,pady=5)
    txt_kullanici_eposta.grid(row=1,column=1,padx=5,pady=5)
    btn_kullanici_kaydet.grid(row=2,column=0,padx=5,pady=5,columnspan=2)

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
        altin = threading.Thread(target=Kur.Getir, args=["altin"])
        dolar = threading.Thread(target=Kur.Getir, args=["dolar"])
        euro = threading.Thread(target=Kur.Getir, args=["euro"])
        altin.start()
        dolar.start()
        euro.start()
        altin.join()
        dolar.join()
        euro.join()


        Kur.AlarmKontrol("altin", "SELECT kur FROM tb_altin ORDER BY (zaman) DESC LIMIT 1;")
        Kur.AlarmKontrol("dolar", "SELECT kur FROM tb_dolar ORDER BY (zaman) DESC LIMIT 1;")
        Kur.AlarmKontrol("euro", "SELECT kur FROM tb_euro ORDER BY (zaman) DESC LIMIT 1;")

        komut = "SELECT zaman,kur FROM tb_altin ORDER BY (zaman) DESC LIMIT 120;"  # Son 60 kaydı getir.
        #komut = "SELECT zaman,kur FROM tb_altin ORDER BY (zaman) DESC;"
        altinKur = VeriTabani.KurGetir(komut)
        x = [row[0] for row in altinKur]
        xf = cls.zamanFormat(x)
        y = [row[1] for row in altinKur]
        cls.lbl_altin_kur["text"] = str(VeriTabani.EsikGetir("SELECT kur FROM tb_altin ORDER BY (zaman) DESC LIMIT 1;"))
        Grafik.Ciz(cls.tab_altin, xf, y, "Altın Kuru")

        komut = "SELECT zaman,kur FROM tb_dolar ORDER BY (zaman) DESC LIMIT 14;"  # Son 14 kaydı getir.
        dolarKur = VeriTabani.KurGetir(komut)
        x = [row[0] for row in dolarKur]
        xf = cls.zamanFormat(x)
        y = [row[1] for row in dolarKur]
        cls.lbl_dolar_kur["text"] = str(VeriTabani.EsikGetir("SELECT kur FROM tb_dolar ORDER BY (zaman) DESC LIMIT 1;"))
        Grafik.Ciz(cls.tab_dolar,xf,y,"Dolar Kuru")

        komut = "SELECT zaman,kur FROM tb_euro ORDER BY (zaman) DESC LIMIT 14;"  # Son 14 kaydı getir.
        euroKur = VeriTabani.KurGetir(komut)
        x = [row[0] for row in euroKur]
        xf = cls.zamanFormat(x)
        y = [row[1] for row in euroKur]
        cls.lbl_euro_kur["text"] = str(VeriTabani.EsikGetir("SELECT kur FROM tb_euro ORDER BY (zaman) DESC LIMIT 1;"))
        Grafik.Ciz(cls.tab_euro,xf,y,"Euro Kuru")

        cls.pencere.after(180000,cls.tekrar) #pencere açıldıktan sonra 180saniyede bir tekrar fonskiyonunu çalıştır.

altinalt =  VeriTabani.EsikGetir("SELECT esik FROM tb_alarm WHERE doviztipi='altin' AND alarmtipi='dusme';")
Doviz.txt_altin_dusus.insert(0,altinalt)
altinust =  VeriTabani.EsikGetir("SELECT esik FROM tb_alarm WHERE doviztipi='altin' AND alarmtipi='yukselme';")
Doviz.txt_altin_yukselme.insert(0,altinust)

dolaralt =  VeriTabani.EsikGetir("SELECT esik FROM tb_alarm WHERE doviztipi='dolar' AND alarmtipi='dusme';")
Doviz.txt_dolar_dusus.insert(0,dolaralt)
dolarust =  VeriTabani.EsikGetir("SELECT esik FROM tb_alarm WHERE doviztipi='dolar' AND alarmtipi='yukselme';")
Doviz.txt_dolar_yukselme.insert(0,dolarust)

euroalt =  VeriTabani.EsikGetir("SELECT esik FROM tb_alarm WHERE doviztipi='euro' AND alarmtipi='dusme';")
Doviz.txt_euro_dusus.insert(0,euroalt)
euroust =  VeriTabani.EsikGetir("SELECT esik FROM tb_alarm WHERE doviztipi='euro' AND alarmtipi='yukselme';")
Doviz.txt_euro_yukselme.insert(0,euroust)

adsoyad,eposta = VeriTabani.KullaniciGetir("SELECT adsoyad,eposta FROM tb_kullanici;")
Doviz.txt_kullanici_adsoyad.insert(0,adsoyad)
Doviz.txt_kullanici_eposta.insert(0,eposta)

Doviz.tekrar()
Doviz.pencere.mainloop()