from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver_path = "C:\\UCUNCUBINYIL\\Ders_Notlarim\\PYTHON\\Ders-018_Tkinter_ile_Grafik_Arayüz_Grid\chromedriver.exe"

opsiyonlar = Options()
opsiyonlar.add_argument("--headless") #Veri çekme arka planda gerçekleşir.

#tarayıcı tanımladık.
browser = webdriver.Chrome(executable_path=driver_path,options=opsiyonlar)
browser.get("https://www.haberturk.com/")

#sayfadaki altin-tl-gr id li elementin içindeki text verilerini al.
#icerik = browser.find_element_by_id("altin-tl-gr").text
icerik = browser.find_element_by_css_selector("#altin-tl-gr").text
parcalar = icerik.split("\n")  # icerik 3 satırlık veri getirdiği için
#bu verideki her satırı ayrı ayrı ele almamızı sağladık.
#her satırdaki veriyi listenin bir elemanı olacak şekilde parçaladık.
#Satır satır parçalamak için \n den ayır dedik.
#print(parcalar[0]," -> ",parcalar[1])
#print(type(parcalar[1]))

altin = float(parcalar[1].replace(",",".")) # float'a dönüştürebilmek için. , ile . yı değiştirdik.
print(altin)
print(type(altin))



### Çeşitli Kaynaklar  ###
#  https://www.w3schools.com/css/css_selectors.asp
