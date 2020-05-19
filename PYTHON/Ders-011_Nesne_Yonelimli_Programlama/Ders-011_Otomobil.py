class Otomobil:
    tanim = "Bu sınıf Otomobil sınıfıdır. Bu özellik nesnelere değil doğrudan sınıfın kendisine aittir."

    # Sınıf nesnelerine ait özellikleri belirtmiş olursunuz.
    def __init__(self,marka,model,renk,motorHacmi,uretimYili):
        self.Marka = marka
        self.Model = model
        self.Renk = renk
        self.MotorHacmi = motorHacmi
        self.UretimYili = uretimYili
        self.Kaydet() #Kaydet fonksiyonu otomatik çalıştı.

    #Bu metotlar sınıfın kendisine değil. Örneklere ait metotlardır.

    def Kaydet(self):
        import os
        import datetime
        dizin = "C:\\DERS13\\"
        dosya = dizin+"OTO_" + str(datetime.date.today()) + ".txt"
        if(not os.path.exists(dizin)):
            os.mkdir(dizin)
        acikDosya = open(dosya,mode="a")

        kayit = str(self.Marka)+" "+str(self.Model)+" "+str(self.Renk)+" "+str(self.MotorHacmi)+" "+str(self.UretimYili)+"\n";
        acikDosya.write(kayit)
        acikDosya.close()