####################################       Dictionary: Sözlük     ############################################
"""

sozluk1 = {"renk1":"Kırmızı","renk2":"Beyaz","renk3":"Turuncu"}
print(sozluk1)
print(sozluk1["renk1"])
sozluk1["renk1"]="Siyah"
print(sozluk1["renk1"])
#print(sozluk1["renk4"]) # key olmadığı için hata verir.
print(sozluk1.get("renk4")) # key yoksa hata vermez none döndürür.
sozluk2 = {1:"Ahmet",2:"Mustafa",3:5}
print(sozluk2)
sozluk2.clear() # içerideki verileri sil.
del sozluk2 # sil.
print(sozluk1.items())
print(sozluk1.keys())
print(sozluk1.values())
print("sozluk1 uzunluk:",len(sozluk1))
print("renk1" in sozluk1)
print("renk4" in sozluk1)
print("Turkuaz" in sozluk1.values())
print("Turkuaz" not in sozluk1.values())
s1 = {"ad":"Selim","soyad":"Kaçar"}
s2 = {"soyad":"Kaçar","ad":"Selim"}
s3 = {"soyad":"Varan","ad":"Selim"}
print("s1 s2 ye eşit mi?: ",s1==s2)
print("s2 s3 e eşit mi?: ",s3==s2)
for key in sozluk1:
    print(key)
for val in sozluk1.values():
    print(val)
s2.update(s3)
print(s2)
s4 = s2.copy() # ram'da farklı adresleri gösterir.
s5= s2# ram de aynı adresleri gösterir.
s3.clear()
isim = sozluk1.pop("renk1") # veriyi sözlükten kpyala ve sözlükten sil.
print(isim)
print(sozluk1)
"""

"""
s3lu = {}
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,0]
list3 = [11,22,33]
s3lu["x"]=list1
s3lu["y"]=list2
s3lu["z"]=list3

print(s3lu)
"""

##########################             ALIŞTIRMALAR               ###############################

# Kullanıcıdan alınan: ad,soyad,yas,cinsiyet bilgilerini Personel isimli bir sözlükte saklayın ve
# ad soyad bilgisini sözlükten alarak ekrana yazdırın.
"""
Personel = {}

Personel["ad"]= input("Ad Giriniz:")
Personel["soyad"]=input("Soyad Giriniz:")
Personel["yas"] = int(input("Yaş Giriniz:"))
Personel["cinsiyet"] = input("Cinsiyet Giriniz:")

print(Personel["ad"],Personel["soyad"])
"""


#Sadece anahtarları bulunan bir sözlük düşünelim
# EnglishtoTurkce = {"car":"","cloud":"","cat":"","driver":""}
#Bu sözlükteki her bir anahtar değeri ekrana yazdırıp türkçe karşılığını kullanıcıdan alarak
#sözlüğe ekleyelim.
"""
EnglishtoTurkce = {"car":"","cloud":"","cat":"","driver":""}
for anahtar in EnglishtoTurkce.keys():
    EnglishtoTurkce[anahtar] = input(anahtar+" kelimesinin türkçesi:")

#print(EnglishtoTurkce)

for deger in EnglishtoTurkce.values():
    print(deger)
"""


