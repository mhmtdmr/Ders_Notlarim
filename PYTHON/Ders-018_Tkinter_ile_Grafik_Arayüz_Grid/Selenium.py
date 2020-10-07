from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

if (__name__ == '__main__'):
    chrome = "C:\\selenium\\chromedriver.exe"
    opsiyonlar = Options()
    opsiyonlar.add_argument("--headless") # Veri çekme sırasında tarayıcı açılmaz. Arka plan çalışır.

    browser = webdriver.Chrome(executable_path=chrome,options=opsiyonlar)
    browser.get("https://www.haberturk.com")
    #time.sleep(5)

    # xpath'i sayfada sağ tıklayıp copy dedikten sonra elde ettik.
    altin = browser.find_element_by_xpath('//*[@id="altin-tl-gr"]/span[2]').text
    print(altin,end="  ")
    print(type(altin))

    # html id'ye göre içeriği getirir.
    #dolar = browser.find_element_by_id('dolar').text

    # css seçici ile içeriği getirdik.
    # https://www.w3schools.com/css/css_selectors.asp
    # https://www.w3schools.com/cssref/css_selectors.asp
    dolar = browser.find_element_by_css_selector('#dolar span:nth-child(2)').text
    print(dolar)

    euro = browser.find_element_by_xpath('//*[@id="euro"]/span[2]').text
    print(euro)




from Doviz import *

from selenium import webdriver
import time

'''
altin,dolar,euro = KurGetir()

print("Altın :",altin)
print("Dolar :",dolar)
print("Euro :",euro)
'''

# Youtube'da arama yapma
chrome = "C:\\selenium\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome)
browser.get("https://www.youtube.com")
time.sleep(2)
arama_kutusu = browser.find_element_by_name('search_query')
#arama_kutusu.send_keys("Adam Savage's Spot Robot Rickshaw Carriage!")
arama_kutusu.send_keys("Youtube Originals AI")

time.sleep(1)
arama_butonu = browser.find_element_by_id('search-icon-legacy')
arama_butonu.click()
time.sleep(2)

# aramada çıkan ilk elemana tıklıyoruz.
ilk_video = browser.find_element_by_xpath('//*[@id="contents"]/ytd-video-renderer[1]')
ilk_video.click()





