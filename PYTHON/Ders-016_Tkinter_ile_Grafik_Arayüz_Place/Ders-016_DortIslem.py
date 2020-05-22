from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from functools import partial


pencere = Tk()
pencere.title("Dört İşlem")
pencere.geometry("600x175+200+150")

def Islem(tip):
    sayi1 = int(txt_sayi1.get())
    sayi2 = int(txt_sayi2.get())

    if(tip=="+"):
        sonuc = sayi1+sayi2
    if(tip=="-"):
        sonuc = sayi1-sayi2
    if (tip=="/"):
        sonuc = sayi1//sayi2
    if(tip=="*"):
        sonuc = sayi1*sayi2

    txt_sonuc.delete(0,END) # kutuyu temizledik.
    txt_sonuc.insert(0,str(sonuc))

lbl_sayi1 = Label(pencere,text="Sayı 1: ",font=("Consolas",16))
lbl_sayi2 = Label(pencere,text="Sayı 2: ",font=("Consolas",16))

lbl_sayi1.place(x=20,y=25)
lbl_sayi2.place(x=20,y=65)

txt_sayi1 = Entry(pencere,text="",font=("Consolas",16),bd=3)
txt_sayi2 = Entry(pencere,text="",font=("Consolas",16),bd=3)

txt_sayi1.place(x=100,y=25)
txt_sayi2.place(x=100,y=65)

ftopla=partial(Islem,"+") # parametreli fonksiyonu butona eklemek için. =>  Islem("+")
btn_topla = Button(pencere,text="+",width=5,height=2,font=(20),bd=3,command=ftopla)
btn_topla.place(x=110,y=105)

fcikar = partial(Islem,"-")
btn_cikar = Button(pencere,text="-",width=5,height=2,font=(20),bd=3,command=fcikar)
btn_cikar.place(x=170,y=105)

fbol = partial(Islem,"/")
btn_bol = Button(pencere,text="/",width=5,height=2,font=(20),bd=3,command=fbol)
btn_bol.place(x=230,y=105)

fcarp = partial(Islem,"*")
btn_carp = Button(pencere,text="x",width=5,height=2,font=(20),bd=3,command=fcarp)
btn_carp.place(x=290,y=105)

lbl_sonuc = Label(pencere,text="Sonuc",font=("Consolas",14),bd=3)
lbl_sonuc.place(x=370,y=23)

txt_sonuc = Entry(pencere,text="",font=("Consolas",14),bd=3)
txt_sonuc.place(x=370,y=63)
pencere.mainloop()
