from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

# Butona tıklandığında checkbox değerini okuyan fonksiyon.
def Hatirla():
    k = onayKutuDegisken.get()
    messagebox.showinfo("Hatırla",str(k))

# Butona tıklandığında elementlerin değerlerini okuyup sonuc bölümünde gösteren fonksiyon.
def Sonuc():
    lbl_sonuc_ad["text"]= str(txt_ad.get())
    lbl_sonuc_soyad["text"]= str(txt_soyad.get())
    lbl_sonuc_kontrol["text"]= "Hatırla kutusu işaretli mi? "+str(onayKutuDegisken.get())
    lbl_sonuc_cbx["text"]=str(cbx.get())
    #lbx
    seciliindisler = lbx.curselection()
    lbl_sonuc_lbx["text"] = ""
    for i in seciliindisler:
        lbl_sonuc_lbx["text"] +=  str(lbx.get(i))+"\n"
    #rdb
    lbl_sonuc_radio["text"]=str(rdb_degisken.get())

#Program penceresini tanımladık.
pencere = Tk()
pencere.geometry("640x480+250+200") #boyutlandırma ve konumlandırma
pencere.config(bg="lightgray")
pencere.title("Ders 20: Grid Kullanımı") # pencere başlığını değiştirdik.
pencere.minsize(640,480)# Minimum çözünürlük.
#pencere.maxsize(800,600) # Maksimum çözünürlük.
pencere.maxsize(False,True)  # Genişlik tam olabilsin. Yükseklik değiştirilemesin.

# pencerenin sol üstündeki ikonu değiştirdik.
kus_ikon = PhotoImage(file="icon.png")
pencere.iconphoto(False,kus_ikon)


#Temel elementleri oluşturduk
lbl_ad = Label(pencere,text="Ad",bg="pink",font=("Consolas",16))
txt_ad = Entry(pencere,font=("Consolas",16))

lbl_soyad = Label(pencere,text="Soyad",bg="pink",font=("Consolas",16))
txt_soyad = Entry(pencere,font=("Consolas",16))

img = PhotoImage(file="kus.gif")
img = img.subsample(10,10)
lbl_img =Label(pencere,image=img,bg="olive")

onayKutuDegisken = StringVar()
onayKutu = Checkbutton(pencere,text="Hatılansın mı?",variable=onayKutuDegisken,onvalue="Evet",offvalue="Hayır",font=("Consolas",13))

btn_kontrol = Button(pencere,text="Kontrol Et",font=("Consolas",15),command=Sonuc)

#Temel elementleri konumlandırdık.

lbl_ad.grid(row=0,column=0,padx=5,pady=5,ipadx=2,ipady=2)
txt_ad.grid(row=0,column=1,padx=5,pady=5,ipadx=2,ipady=2)

lbl_soyad.grid(row=1,column=0,padx=5,pady=5,ipadx=2,ipady=2)
txt_soyad.grid(row=1,column=1,padx=5,pady=5,ipadx=2,ipady=2)

lbl_img.grid(row=0,column=2,rowspan=3,columnspan=2,padx=5,pady=5,ipadx=4,ipady=4)
onayKutu.grid(row=2,column=0,padx=5,pady=5,ipadx=2,ipady=2)

btn_kontrol.grid(row=2,column=1,padx=5,pady=5,ipadx=2,ipady=2)



# ALT SONUÇ BÖLÜMÜ BAŞLANGICI
cerceve_sonuc = Label(pencere,bg="lavender",height=4,width=10)
cerceve_sonuc.grid(row=4,column=1,columnspan=4)



lbl_sonuc_ad = Label(cerceve_sonuc,text="",font=("Consolas",16))
lbl_sonuc_ad.grid(row=0,column=0,columnspan=4)

lbl_sonuc_soyad = Label(cerceve_sonuc,text="",font=("Consolas",16))
lbl_sonuc_soyad.grid(row=1,column=0,columnspan=4)

lbl_sonuc_kontrol = Label(cerceve_sonuc,text="",font=("Consolas",16))
lbl_sonuc_kontrol.grid(row=2,column=0,columnspan=4)

lbl_sonuc_cbx = Label(cerceve_sonuc,text="",font=("Consolas",16))
lbl_sonuc_cbx.grid(row=3,column=0,columnspan=4)

lbl_sonuc_lbx = Label(cerceve_sonuc,text="",font=("Consolas",16))
lbl_sonuc_lbx.grid(row=4,column=0,columnspan=4)

lbl_sonuc_radio = Label(cerceve_sonuc,text="",font=("Consolas",16))
lbl_sonuc_radio.grid(row=5,column=0,columnspan=4)

# ALT SONUÇ BÖLÜMÜ SONU



# ComboBox Başı
liste = ["İstanbul","Ankara","İzmir","Kayseri","Sivas"]
cbx = Combobox(pencere,values=liste)
cbx.current(4) # Sivas seçili
cbx.grid(row=3,column=0)
# ComboBox Sonu


# Listbox Başı

liste2 = ["Gaziantep","Şanlıurfa","Mardin","Diyarbakır"]
lbx=Listbox(pencere,height=5,selectmode="multiple")

for eleman in liste2:
    lbx.insert(END,eleman)
"""
lbx.insert(END,"Gaziantep")
lbx.insert(END,"Şanlıurfa")
lbx.insert(END,"Mardin")
lbx.insert(END,"Diyarbakır")
"""
lbx.grid(row=3,column=1)
# Listbox Sonu

# Radiobutton başı

rdb_degisken = StringVar()
rdb_degisken.set("kadın")
rdb1 = Radiobutton(pencere,text="Erkek",value="erkek",variable=rdb_degisken)
rdb1.grid(row=3,column=2)
rdb2 = Radiobutton(pencere,text="Kadın",value="kadın",variable=rdb_degisken)
rdb2.grid(row=3,column=3)


# Radiobutton sonu










#lbl_ad.place(x=80,y=40)
#lbl_ad.pack(side=LEFT,padx=40,pady=20,ipadx=10,ipady=10) #fill=X side yerine gelir
#txt_ad.pack(side=LEFT,padx=40,pady=20,ipadx=10,ipady=10)


pencere.mainloop()


