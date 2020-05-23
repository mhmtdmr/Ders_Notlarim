# SMTP Kütüphanesi kullanarak Gmail üzerinden eposta gönderimi.
#gmail'de erişime izin verme linki:
#https://myaccount.google.com/lesssecureapps
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#import tkinter as tk
from tkinter import *
from tkinter import messagebox

def Epostala():
    eposta = MIMEMultipart()
    eposta["From"] = "test.mehmetdemir@gmail.com"
    eposta["To"] = "mail.mehmetdemir@gmail.com"
    eposta["Subject"] = "Python ile e-posta gönderim testi."
    body ="""
    Bu e-posta test amaçlı gönderilmiştir.
    Üçüncü Bin Yıl
    """
    body_text = MIMEText(body,"plain")
    eposta.attach(body_text)
    try:
        gmail = smtplib.SMTP("smtp.gmail.com",587) # Gmail SMTP bilgileri
        gmail.ehlo()
        gmail.starttls()
        gmail.login("test.mehmetdemir@gmail.com","Parolayı_Yaz")
        gmail.sendmail(eposta["From"],eposta["To"],eposta.as_string())
        print("E-posta gönderimi başarılı.")
        gmail.close()
    except Exception as e:
        print("E-posta gönderilirken bir hata oluştu.",str(e))