class Arac:
    def __init__(self):
        self.Marka = str()
        self.Model = ""
        self.Renk = ""
        self.UretimYili = 1900
        self.Fiyat = 0.0
        from datetime import datetime
        self.IlanTarihi = datetime.today().date()

    def BilgiYazdir(self):
        print(f"""ARAÇ BİLGİLERİ
            Marka: {self.Marka}
            Model: {self.Model}
            Renk: {self.Renk}
            Üretim Yılı: {self.UretimYili}
            Fiyat: {self.Fiyat}
            İlan tarihi: {self.IlanTarihi}""")

# Arac sınıfından kalıtım  ile özellik ve fonksiyonları devalması için, parantez içinde üst sınıf ismini
#  belirttik.
class Otomobil(Arac):
    def __init__(self):
        self.KasaTipi = "Sedan"
        self.VitesTipi = "Otomatik"

    def BilgiYazdir(self):
        super().BilgiYazdir()
        print(f"""
            Kasa tipi: {self.KasaTipi}
            Vites tipi: {self.VitesTipi}""")

class Kamyon(Arac):
    def __init__(self):
        self.Tasimakapasitesi = 0
        self.YakitDepoSayisi = 1

    def BilgiYazdir(self):
        super().BilgiYazdir()
        #super().Marka    # üst sınıftaki özellik ve fonksiyonlara super() ile erişim.
        print(f"""
            Taşıma kapasitesi: {self.Tasimakapasitesi}
            Yakıt deposu sayısı: {self.YakitDepoSayisi}""")