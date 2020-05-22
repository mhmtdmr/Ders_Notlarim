from tkinter import *

AnaPencere = Tk()
AnaPencere.geometry("800x850+20+20")
AnaPencere.title("Tkinter ile Pack İşlemleri")
#AnaPencere.maxsize(1024,768)
AnaPencere.config(bg="beige")  #bg="#A94752" 16'lık sistemdeki renk kodları da çalışır.

##### Cerceve_1'de elemanları alt alta hizaladık.

Cerceve_1 = Frame(AnaPencere,bg="firebrick",cursor="pirate")
Cerceve_1.pack(fill=X,padx=10,pady=5,ipadx=4,ipady=4)

yazi_1 = Label(Cerceve_1,bg="#DAB123",text="MERHABA",font=("Comic Sans",16),fg="#455625")
yazi_1.pack(fill=X,padx=50,pady=50,ipadx=25,ipady=25)

girdi_1 = Entry(Cerceve_1,bg="pink",font=("Consolas",15),fg="red")
girdi_1.pack(fill=X,pady=50,padx=50)

#Cerceve_2 de yan yana hizalama örneği yapacağız.

Cerceve_2 = Frame(AnaPencere,bg="teal",cursor="star")
Cerceve_2.pack(fill=X,padx=10,pady=10,ipadx=4,ipady=5)

yazi_2 = Label(Cerceve_2,bg="#DAB456",text="DÜNYA",font=("Times New Roman",16),fg="indigo")
yazi_2.pack(side=LEFT,padx=10,pady=5,ipadx=10,ipady=10)

btn_2 = Button(Cerceve_2,bg="khaki",text="BUTON 2",font=("Consolas",14))
btn_2.pack(side=LEFT,padx=10,pady=10,ipadx=6,ipady=5)

girdi_2 = Entry(Cerceve_2,fg="#456789",font=("Consolas",16))
girdi_2.pack(side=RIGHT,padx=10,pady=10,ipadx=6,ipady=5)


Cerceve_3 = Frame(AnaPencere,bg="chocolate",cursor="clock")
Cerceve_3.pack(fill=X,padx=10,pady=10,ipadx=10,ipady=10)


img = PhotoImage(file = "kus.gif")
img1 = img.subsample(5,5)
Label(Cerceve_3,image=img1).pack(side=LEFT,padx=10,pady=10)


AnaPencere.mainloop()