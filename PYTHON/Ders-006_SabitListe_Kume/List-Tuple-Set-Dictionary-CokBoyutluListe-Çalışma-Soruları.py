
# SORU1:
# 1-15 arasında rastgele  10 adet sayı üretip bir listeye atıp ekrana yazdırdıktan sonra;
# Listede 1 den fazla kez bulunan değerleri silerek listeyi tekrar ekrana yazdıran program.
# Listeye atamada kontrol yapılmayacak olup. Liste oluşturulduktan sonra silme işlemi yapılmalıdır.

#SORU2:
# 1-10 arasında rastgele 5'er sayı üretip iki listeye atan ve daha sonra listenin elemanlarından kaçının
# aynı olup olmadığını ekrana yazdıran program. Örn: l1 = [11,22,33,44,55] l2 = [55,66,77,88,99] 
# l1 ile l2'nin 1 ortak elemanı vardır.

#SORU3:
# 1-100 arasında rastgele  20 sayı üretip bir listeye atan, ekrana yazdıran ve 
# daha sonra asal sayıları bu listeden silen ve listeyi ekrana yazdıran programı yazınız.

#SORU4:
# 1-10 arasında rastgele 5'er sayı üretip iki listeye atan ve daha sonra listenin elemanlarından 
# iki listede ortak olmayanları başka birlisteye atarak ekrana yazdıran program.
# Örn: l1 = [11,22,33,44,55] l2 = [55,66,77,88,99]  l3 = [11,22,33,44,66,77,88,99]

# SORU5: 1-100 arasında 20'şer adet rastgele sayı üretip bunları 2 kümeye aktaran ve 
# bu iki kümenin: farkını, kesişimini ve birleşimini ekrana yazdıran program.

# SORU6: anahtarları key1-den key10'a kadar olan 2 adet sözlük'e rastgele atılan değerleri karşılaştırıp
# anahtar-değer ikilisi aynı olanları ekrana yazdıran program
# Örn: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Çıktı: key1: değeri iki sözlükte de eşittir: 1

# SORU7: 
# İçerisinde 10 adet ingilizce kelime bulunan bir listedeki kelimelerin türkçelerini
# ingilizce leri anahtar olacak şekilde bir sözlüğe atayan programı yazınız.s
# Her kelimenin türkçe kaşılığı kullanıcıdan alınarak sözlüğe atılacak

# Çok Boyutlu Liste Soruları
############################

#SORU8: 3*4 lük bir liste oluşturup sırasıyla her satıra aşağıdaki aralıklarda rastgele değer atayan program.
# 1. satır: 10-20 arasında
# 2. satır: 20-30 arasında
# 3. satır: 30-40 arasında

# SORU9: 4x4'lük bir liste oluşturup. çift satılardaki kolonlara
#  0-9 arasında bir sayıyı rastgele atayıp,
# tek satılara da önceki satırın aynı kolonunda bulunan sayının karesini atayan programı yazınız.
# Örnek: d[0][0] = 3 ise d[1][0] = 9
# Örnek: d[2][3] = 5 ise d[3][3] = 25

#SORU10: 3x4x5 lik biz dizi tanımlayıp. Her hücreye bulunduğu satır+sütun+derinlik değerini yazdırın.
# ÖRN: dizi[1][2][2] = 5 şeklinde.
# 3 boyutlu dizi tanımalamaya örnek: 3x4x6 'lık dizi her elemanı *
array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(array)
