class Personel:
    Bilgi=""
    def __init__(self):
        print("Personel Bilgilerini Giriniz")
        self.ad = input("İsim: ")
        self.soyad = input("Soyisim: ")
        self.tc = input("Tc: ")
        self.telefon = input("Telefon: ")
        self.adres = input("Adres: ")
        self.maas = float(input("Maaş: "))

    #nesne metodu
    def Kaydet(self):
        import os
        dizin = "C:\\Ders13"
        dosya = "C:\\Ders13\\Personel.txt"
        if(not os.path.exists(dizin)):
            os.mkdir(dizin)
        dosyam = open(dosya,"a")
        dosyam.write(f""" Personel: {self.ad} {self.soyad}  T.C. Kimlik Numarası: {self.tc}  Telefon: {self.telefon}  Adres: {self.adres}  Maaş: {self.maas}""")
        dosyam.close()

    @staticmethod
    def Listele():
        import os
        dosya = "C:\\Ders13\\Personel.txt"
        if(not os.path.exists(dosya)):
            print("Dosya bulunamadı!!")
            return
        else:
            dosyam = open(dosya,"r")
            satirlar = dosyam.readlines()
            for satir in satirlar:
                print(satir)