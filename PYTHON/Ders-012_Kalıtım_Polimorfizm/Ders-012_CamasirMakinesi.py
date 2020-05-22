from BeyazEsya import BeyazEsya
import os
class CamasirMakinesi(BeyazEsya):
    def __init__(self):
        self.YikamaKapasitesi = 0
        self.HizliYikama = False

    def BilgiListele(self):
        super().BilgiListele()
        hizli = ""
        if(self.HizliYikama==True):
            hizli = "Var"
        else:
            hizli = "Yok"
        print(f"Kapasite : {self.YikamaKapasitesi}\nHızlı Yıkama : {hizli} ")

    def Kaydet(self):
        dizin = "C:\\Ders14\\"
        dosya = dizin+"Camasir.txt"

        if(not os.path.exists(dizin)):
            os.mkdir(dizin)
            print(dizin, "oluşturuldu.")
        if(not os.path.exists(dosya)):
            text = open(dosya, "a+")
            text.write("Marka\t\tModel\t\tEnerji\t\tFiyat\t\tYıkama Kapasisi\t\tHızlı Yıkama\n")
            text.write("-----\t\t-----\t\t------\t\t-----\t\t---------------\t\t------------\n")
            print(dosya,"oluşturuldu.")
        else:
            text = open(dosya, "a+")

        text.write(f"{self.Marka}\t\t{self.Model}\t\t{self.Enerji}\t\t{self.Fiyat}\t\t       {self.YikamaKapasitesi}     \t\t{self.HizliYikama}\n")
        text.close()