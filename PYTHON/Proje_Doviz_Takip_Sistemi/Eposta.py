import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#import tkinter as tk
from tkinter import *
from tkinter import messagebox


def Gonder(kime,doviztipi,alarmtipi,esik,kur):
    eposta = MIMEMultipart()
    eposta["From"] = "test.mehmetdemir@gmail.com"
    eposta["To"] = kime
    eposta["Subject"] = f"{str.capitalize(doviztipi)} {str.capitalize(alarmtipi)} => Eşik: {esik} => Değer: {kur}"
    body =f"""

    Menekşeli Menkul Değerler,
    Hayırlı kazançlar diler.
    {eposta["Subject"]}

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

