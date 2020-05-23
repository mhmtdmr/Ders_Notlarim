
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from VeriTabani import VeriTabani
import Eposta

class Kur:
    @staticmethod
    def Getir(doviztipi):
        driver_path = "C:\\Proje\\chromedriver.exe"
        opsiyonlar = Options()
        opsiyonlar.add_argument("--headless") #Veri çekme arka planda gerçekleşir.
        browser = webdriver.Chrome(executable_path=driver_path,options=opsiyonlar)
        browser.get("https://www.haberturk.com/")
        if(doviztipi.lower()=="altin"):
            icerik = browser.find_element_by_css_selector("a#altin-tl-gr span:nth-child(2)").text
        if (doviztipi.lower() == "dolar"):
            icerik = browser.find_element_by_css_selector("a#dolar span:nth-child(2)").text
        if (doviztipi.lower() == "euro"):
            icerik = browser.find_element_by_css_selector("a#euro span:nth-child(2)").text
            #açıklama: html kaynak dosyasında; id'si euro olan a elementinin altındaki 2. span'ın verisini al.

        deger = float(icerik.replace(",",".")) # float'a dönüştürebilmek için. , ile . yı değiştirdik.
        tablo = "tb_" + str(doviztipi)
        zaman = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        print(zaman)
        komut = f"INSERT INTO {tablo} (zaman,kur) VALUES('{zaman}',{deger});"
        VeriTabani.Kaydet(komut)


        ### Çeşitli Kaynaklar  ###
        #  https://www.w3schools.com/css/css_selectors.asp
        #https://code.tutsplus.com/tr/tutorials/the-30-css-selectors-you-must-memorize--net-16048
    @staticmethod
    def AlarmKontrol(doviztipi,komut):
        esikler = VeriTabani.AlarmGetir()

        altinAlt = esikler[0][0]
        altinUst = esikler[1][0]
        dolarAlt = esikler[2][0]
        dolarUst = esikler[3][0]
        euroAlt = esikler[4][0]
        euroUst = esikler[5][0]
        altinAltEposta = esikler[0][1]
        altinUstEposta = esikler[1][1]
        dolarAltEposta = esikler[2][1]
        dolarUstEposta = esikler[3][1]
        euroAltEposta = esikler[4][1]
        euroUstEposta = esikler[5][1]


        deger = VeriTabani.EsikGetir(komut)
        adsoyad,eposta = VeriTabani.KullaniciGetir("SELECT adsoyad,eposta FROM tb_kullanici;")

        if(doviztipi=="altin"):
            if((deger<=altinAlt) and (altinAlt != 0.0) and altinAltEposta=='HAYIR'):
                Eposta.Gonder(eposta,"altin","dusme",altinAlt,deger)
                VeriTabani.Kaydet("UPDATE tb_alarm SET eposta='EVET' WHERE doviztipi = 'altin' AND alarmtipi = 'dusme';")
                print("Altın alt değerde")
            if((deger>=altinUst) and (altinUst != 0.0)and altinUstEposta=='HAYIR'):
                Eposta.Gonder(eposta, "altin", "yukselme", altinUst, deger)
                VeriTabani.Kaydet("UPDATE tb_alarm SET eposta='EVET' WHERE doviztipi = 'altin' AND alarmtipi = 'yukselme';")
                print("Altın üst değerde")
        elif(doviztipi.lower()=="dolar"):
            if(deger<=dolarAlt and dolarAlt != 0.0 and dolarAltEposta=='HAYIR'):
                Eposta.Gonder(eposta, "dolar", "dusme", dolarAlt, deger)
                VeriTabani.Kaydet("UPDATE tb_alarm SET eposta='EVET' WHERE doviztipi = 'dolar' AND alarmtipi = 'dusme';")
                print("Dolar alt değerde")
            if(deger>=dolarUst and dolarUst != 0.0 and dolarUstEposta=='HAYIR'):
                Eposta.Gonder(eposta, "dolar", "yukselme", dolarUst, deger)
                VeriTabani.Kaydet("UPDATE tb_alarm SET eposta='EVET' WHERE doviztipi = 'dolar' AND alarmtipi = 'yukselme';")
                print("Dolar üst değerde")
        elif(doviztipi.lower()=="euro"):
            if(deger<=euroAlt and euroAlt != 0.0 and euroAltEposta=='HAYIR'):
                Eposta.Gonder(eposta, "euro", "dusme", euroAlt, deger)
                VeriTabani.Kaydet("UPDATE tb_alarm SET eposta='EVET' WHERE doviztipi = 'euro' AND alarmtipi = 'dusme';")
                print("Euro alt değerde")
            if(deger>=euroUst and euroUst !=0.0 and euroUstEposta=='HAYIR'):
                Eposta.Gonder(eposta, "euro", "yukselme", euroUst, deger)
                VeriTabani.Kaydet("UPDATE tb_alarm SET eposta='EVET' WHERE doviztipi = 'euro' AND alarmtipi = 'yukselme';")
                print("Euro üst değerde")

        # TODO: Eposta ve Alarm tablosuna bool ekleme kaldı.
        # TODO: Kontrol işleminden sonra alarmlog tablosuna uid(kur+esik+doviztipi ?) işlenmesi lazım.(önceden yoksa)
        # TODO: Kontrol'den sonra eposta kolonu (bool) göre eposta fonksyonu çalıştırılabilir.
