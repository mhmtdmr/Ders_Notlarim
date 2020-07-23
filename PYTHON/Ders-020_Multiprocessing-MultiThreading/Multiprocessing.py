# Multiprocess olmadan, sıralı çalışma.
'''
import time
if __name__ == "__main__":
    start = time.perf_counter()
    def fonksiyon():
        print("1 saniye bekleniyor...")
        time.sleep(1)
        print("Bekleme bitti.")
    fonksiyon()
    fonksiyon()
    finish =  time.perf_counter()
    print(f"İşlemin tamamlanma süresi: {round(finish-start,2)} saniye.")
'''


# Multiprocess kulllanımlı hali.
'''
import time
import multiprocessing
start = time.perf_counter()

def fonksiyon():
    print("1 saniye bekleniyor...")
    time.sleep(1)
    print("Bekleme bitti.")


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=fonksiyon)
    p2 = multiprocessing.Process(target=fonksiyon)
    p1.start()
    p2.start()
    # Sonraki komutların çalışmasından önce üstteki processlerin tamamlanmasını beklemek için join kullanıoruz.
    p1.join()
    p2.join()
    finish =  time.perf_counter()
    print(f"İşlemin tamamlanma süresi: {round(finish-start,2)} saniye.")
'''
'''
# Çoklu kullanıma bir örnek
import time
import multiprocessing
start = time.perf_counter()

def fonksiyon(saniye):
    print(f"{saniye} saniye bekleniyor...")
    time.sleep(saniye)
    print("Bekleme bitti.")

if __name__ == "__main__":
    islemler = []
    for _ in range(10):
        p = multiprocessing.Process(target=fonksiyon,args=[3])
        p.start()
        islemler.append(p)

    for islem in islemler:
        islem.join()

    finish =  time.perf_counter()
    print(f"İşlemin tamamlanma süresi: {round(finish-start,2)} saniye.")
'''

# Farklı bir çoklu kullanım şekli.
# Çoklu kullanıma bir örnek
import time
import concurrent.futures

start = time.perf_counter()

def fonksiyon(saniye):
    print(f"{saniye} saniye bekleniyor...")
    time.sleep(saniye)
    return f" {saniye} bekleme bitti."

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executer:
        # executer ile process başlatma.
        #f1 = executer.submit(fonksiyon,4)
        #print(f1.result())

        # 5 process döngü ile.
        saniyeler = [2,2,3,4,5]

        #results = [executer.submit(fonksiyon,saniye) for saniye in saniyeler]
        #for f in concurrent.futures.as_completed(results):
        #    print(f.result())

        # map kullanarak.
        results = executer.map(fonksiyon,saniyeler)
        for result in results:
            print(result)

    finish =  time.perf_counter()
    print(f"İşlemin tamamlanma süresi: {round(finish-start,2)} saniye.")



    # Source: https://www.youtube.com/watch?v=fKl2JW_qrso
    # Thanks to Corey Schafer