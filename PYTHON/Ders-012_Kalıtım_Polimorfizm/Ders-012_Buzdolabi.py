from BeyazEsya import BeyazEsya
import os
class Buzdolabi(BeyazEsya):
    def __init__(self):
        self.KapakSayisi = 1
        self.Hacim = 0

    def BilgiListele(self):
        super().BilgiListele()
        print(f"""Kapak sayısı : {self.KapakSayisi}\nHacim : {self.Hacim}""")

    def Kaydet(self):
        dizin = "C:\\Ders14\\"
        dosya = dizin+"Buzdolabi.txt"

        if(not os.path.exists(dizin)):
            os.mkdir(dizin)
            print(dizin, "oluşturuldu.")
        if(not os.path.exists(dosya)):
            text = open(dosya, "a+")
            text.write("Marka\t\tModel\t\tEnerji\t\tFiyat\t\tKapak Sayısı\t\tHacim\n")
            text.write("-----\t\t-----\t\t------\t\t-----\t\t------------\t\t-----\n")
            print(dosya,"oluşturuldu.")
        else:
            text = open(dosya, "a+")

        text.write(f"{self.Marka}\t\t{self.Model}\t\t{self.Enerji}\t\t{self.Fiyat}\t\t      {self.KapakSayisi}    \t\t{self.Hacim}\n")
        text.close()

