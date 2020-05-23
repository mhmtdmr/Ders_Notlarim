# SMTP Kütüphanesi kullanarak Gmail üzerinden eposta gönderimi.
# gmail'de erişime izin verme linki:
# https://myaccount.google.com/lesssecureapps
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#import tkinter as tk
from tkinter import *
from tkinter import messagebox

def Epostala():
    eposta = MIMEMultipart()
    eposta["From"] = "test.mehmetdemir@gmail.com"
    eposta["To"] = str(txt_alici.get())
    eposta["Subject"] = str(txt_konu.get())
    body = txt_eposta.get("1.0",END)
    body_text = MIMEText(body,"plain")
    eposta.attach(body_text)
    try:
        gmail = smtplib.SMTP("smtp.gmail.com",587) # Gmail SMTP bilgileri
        gmail.ehlo()
        gmail.starttls()
        gmail.login("test.mehmetdemir@gmail.com","Fast**BJK")
        gmail.sendmail(eposta["From"],eposta["To"],eposta.as_string())
        messagebox.showinfo("Epostala","E-posta gönderimi başarılı.")
        gmail.close()
    except Exception as e:
        messagebox.showerror("Epostala","E-posta gönderilirken bir hata oluştu.")
        #print("E-posta gönderilirken bir hata oluştu.",str(e))

pencere = Tk()
pencere.title("Epostala")
pencere.geometry("1024x768+415+100")
pencere.config(bg="bisque")

lbl_alici = Label(pencere,text="Alici eposta adresi:",font=("Consolas",16))
txt_alici = Entry(pencere,text="",font=("Consolas",16),width=60)

lbl_alici.grid(row=0,column=0,padx=10,pady=10)
txt_alici.grid(row=0,column=1,padx=10,pady=10,columnspan=3)

lbl_konu = Label(pencere,text="Konu:",font=("Consolas",16))
txt_konu = Entry(pencere,text="",font=("Consolas",16),width=60)

lbl_konu.grid(row=1,column=0,padx=10,pady=10)
txt_konu.grid(row=1,column=1,padx=10,pady=10,columnspan=3)


lbl_eposta = Label(pencere,text="Eposta",font=("Consolas",16))
txt_eposta = Text(pencere,font=("Consolas",16),width=60)

lbl_eposta.grid(row=2,column=0,padx=10,pady=10)
txt_eposta.grid(row=2,column=1,padx=10,pady=10)

btn_gonder = Button(pencere,text="Gönder",font=("Consolas",16),command=Epostala)
btn_gonder.grid(row=3,column=0,padx=10,pady=10,columnspan=2)

pencere.mainloop()






