def Topla(s1,s2):
    return s1+s2

def Cikar(s1,s2):
    return s1-s2

def Carp(s1,s2):
    return s1*s2

def Bol(s1,s2):
    if(s2!=0):
        return s1//s2
    else:
        return -1
print("Burası hep çalışır!")

if(__name__== '__main__'):
    print("Sadece bu dosyadan çalıştırılırsa burası çalışır!")