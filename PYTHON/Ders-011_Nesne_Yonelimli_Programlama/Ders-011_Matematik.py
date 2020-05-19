class Matematik:
    @classmethod
    def topla(self,*sayilar):
        toplam=0
        for sayi in sayilar:
            toplam += sayi
        print("Sayıların toplamı:",toplam)

    @classmethod
    def cikar(cls,s1,s2):
        print("Sayıların farkı:",(s1-s2))

    @classmethod
    def carp(cls,*sayilar):
        carpim=1
        for sayi in sayilar:
            carpim *= sayi
        print("Sayıların çarpımı:",carpim)
    @classmethod
    def bol(cls,s1,s2):
        try:
            bolum = s1//s2
            print("Sayıların bölümü",bolum)
        except ZeroDivisionError:
            print("Bölüm 0 olmamalı!")
