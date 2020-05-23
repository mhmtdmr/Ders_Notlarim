import sqlite3
from VeriTabani import VeriTabani
class Kullanici:
    def __init__(self):
        self.id = int()
        self.adsoyad = str()
        self.eposta = str()

    def Kaydet(self):
        komut = f"UPDATE tb_kullanici SET adsoyad='{self.adsoyad}', eposta='{self.eposta}';"
        VeriTabani.Kaydet(komut)
