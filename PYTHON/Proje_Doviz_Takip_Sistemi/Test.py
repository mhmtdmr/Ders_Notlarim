import threading
from tkinter import *
from tkinter.ttk import *
from Grafik import Grafik  # Grafik.py'den Grafik sınıfını içeri aktardık.import
from Kur import Kur
from VeriTabani import VeriTabani
from Kullanici import Kullanici
from datetime import datetime


komut = "SELECT zaman,kur FROM tb_altin ORDER BY (zaman) DESC LIMIT 1;"  # Son 7 kaydı getir.
altinKur = VeriTabani.KurGetir(komut)
x = [row[0] for row in altinKur]
y = [row[1] for row in altinKur]


print(x)

xd = []
for z in xd:
    print(z)
    print(type(z))
