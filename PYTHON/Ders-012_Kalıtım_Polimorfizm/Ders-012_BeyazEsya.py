class BeyazEsya:
    def __init__(self):
        self.Marka = ''
        self.Model = ""
        self.Enerji = ""
        self.Fiyat = 0.0

    def BilgiListele(self):
        print(f"""Bilgiler
        Marka : {self.Marka}
        Model : {self.Model}
        Enerji : {self.Enerji}
        Fiyat : {self.Fiyat}""")