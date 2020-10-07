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




