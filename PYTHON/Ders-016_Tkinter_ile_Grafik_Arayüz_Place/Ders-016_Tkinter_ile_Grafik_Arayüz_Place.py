# File -> Settings -> Project -> Project Interpreter -> + tuşu ile tkinter paketini ekliyoruz.

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

def yaziDegistir():
    metin = txt.get()
    yazi["text"] = metin

def yaziTemizle():
    txt.delete(0,END) #txt içindeki verileri 0'ıncı indisten sonuna kadar sil.
    yazi["text"] = ""

def tipGoster():
    #messagebox.showinfo("Bilgi",type(txt.get()))
    #messagebox.showerror("Hata", type(txt.get()))
    messagebox.showwarning("Uyarı",type(txt.get()))

pencere = Tk() # Program çalıştığında ekranda görünecek olan pencere(grafik arayüz)
pencere.title("İlk GUI Programımız") #Pencere başlığı
pencere.geometry("500x500+200+150") # Boyut ve ekranda konumlandırma.

yazi = Label(pencere,text="Merhaba Grafik",fg="purple",font=("Consolas",18))
yazi.place(x=5,y=10)

btn_Degistir = Button(pencere,text="Değiştir",font=("Consolas",16),bd=3,width=20,command=yaziDegistir)
btn_Degistir.place(x=210,y=8)

txt = Entry(pencere,text="",bd=3,font=("Consolas",14))
txt.place(x=5,y=50)

btn_Temizle = Button(pencere,text="Temizle",font=("Consolas",16),bd=3,width=20,command=yaziTemizle)
btn_Temizle.place(x=210,y=60)

btn_TipGoster = Button(pencere,text="txt veri tipi",font=("Consolas",16),bd=3,width=20,command=tipGoster)
btn_TipGoster.place(x=210,y=110)

"""
# ÖDEV: Hesap Makinesi: Aşağısı ipucu: 1 adet Entry kullanılarak. Her rakam için bir buton ile yapılacak.
def SagdanEkle():
    eklenecek = txt2.get()
    txt.insert(END,eklenecek)

btn_Degistir = Button(pencere,text="Değiştir",font=("Consolas",16),bd=3,width=20,command=SagdanEkle)
btn_Degistir.place(x=210,y=8)

txt = Entry(pencere,text="",bd=3,font=("Consolas",14))
txt.place(x=5,y=50)

txt2 = Entry(pencere,text="",bd=3,font=("Consolas",14))
txt2.place(x=5,y=90)
"""
pencere.mainloop() # Grafik arayüzün sürekli ekranda kalması için gerekli fonksiyon.