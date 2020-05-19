class Ders:
    def __init__(self,dersAdi,dersSaati,dersOgretmeni,dersBaslamaTarihi):
        self.DersAdi = dersAdi
        self.DersSaati = dersSaati
        self.DersOgretmeni = dersOgretmeni
        self.DersBaslamaTarihi = dersBaslamaTarihi
        self.DersKaydet() # Ders otomatik olarak keydedilsin.

    def DersKaydet(self):
        try:
            import  os
            dizin = "C:\\UBY\\"
            kayitDosyasi = "C:\\UBY\\Dersler.txt"
            if(not os.path.exists(dizin)):
                os.mkdir(dizin)
            dosya = open(kayitDosyasi,mode="a")

            yazi = "\n"+"Ders Adı:\t"+str(self.DersAdi)+"\n"+"Ders Saati:\t"+str(self.DersSaati)+"\n"+"Ders Öğretmeni:\t"+str(self.DersOgretmeni)+"\n"\
                   +"Başlama Tarihi:\t"+str(self.DersBaslamaTarihi)
            dosya.write(yazi)
            dosya.close()
            print("Ders başarı ile kaydedildi.")
        except:
            print("Dosya kaydedilirken bir hata oluştu.")