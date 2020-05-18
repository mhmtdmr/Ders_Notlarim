def sansur(cumleListesi,yasakliKelime,yeniKelime):
    for i in range(len(cumleListesi)):
        cumleListesi[i] = cumleListesi[i].replace(yasakliKelime,yeniKelime)
    return cumleListesi

