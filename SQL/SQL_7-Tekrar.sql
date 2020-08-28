SELECT * FROM Kurs_VT.INFORMATION_SCHEMA.TABLES;

SELECT * FROM Dersler;
SELECT * FROM Ogrenciler;
SELECT * FROM Ogretmenler;
SELECT * FROM Danismanlar;
SELECT * FROM Egitim;
-- % joker anlamý taþýr. 0 veya daha fazla her karakter anlamýna gelir.

-- Eposta adresinde necip geçen kayýtlarý listeleyen sorgu:
SELECT * FROM Ogretmenler WHERE Ogretmenler.Eposta LIKE '%necip%';

-- Eposta adresinde ncp harflerinden birisi bulunanlarý listeleyen sorgu.
SELECT * FROM Ogretmenler WHERE Eposta LIKE '%[ncp]%';

-- Eposta adresinde np harflerinden birisi bulunmayanlarý listeleyen sorgu.
SELECT * FROM Ogretmenler WHERE Eposta NOT LIKE '%[np]%';

-- Ad'ý A ile baþlayýp 2. harfi l olmayanlarý listeleyen sorgu.
SELECT * FROM Ogretmenler WHERE Ad LIKE 'A[^l]%';

-- Öðretmenlerden soyadý 4 harfli olanlarý getiren sorgu
SELECT * FROM Ogretmenler WHERE Soyad LIKE '____'; -- her bir _ bir karakterlik alaný temsil eder.

-- Soyadý A-K arasýndaki harfler ile baþlayanlarý getir.
SELECT * FROM Ogretmenler WHERE Soyad LIKE '[A-K]%';

-- Toplam saati 100'ün altýnda olanlardan adýnda Excel geçen dersleri listeleyen sorgu.
SELECT * FROM Dersler WHERE ToplamSaat<100 AND Ad LIKE '%Excel%';

-- Ogrenciler tablosuna kayýt ekleyen INSERT sorgusunu yazýnýz.
INSERT INTO Ogrenciler (Ad,Soyad,TC,Telefon,Eposta)
VALUES('Sefa','Karataþ','96385274123','05462923058','serfa@gmail.com');

-- mail adresi gmail olan öðrencileri listeleyen sorgu.
SELECT * FROM Ogrenciler WHERE Eposta LIKE '%gmail%'

-- ID'si 3 ve 5 olanlarýn dersSaatini toplamý ve toplamýnýn 5 katýný gösteren select sorgusu
DECLARE @toplamSaat int;
SELECT @toplamSaat = (SELECT SUM(ToplamSaat) as ToplamDersSaati FROM Dersler WHERE ID IN(3,5));
print(@toplamSaat*5);

-- Öðretmenlerden adý Ahmet veya Mehmet'den birisi olanlarý listeleyen sorgu.
SELECT * FROM Ogretmenler WHERE Ad IN('Ahmet','Mehmet');
SELECT * FROM Ogretmenler WHERE Ad ='Ahmet' OR Ad='Mehmet';

-- Ders saatlerinin ortalamasýný getiren sorgu.
SELECT AVG(ToplamSaat) as [Ders Saati Ortalamasi] FROM Dersler;

-- Kaç öðrenci olduðunu sayan sorgu
-- ID'si 3 olan öðrencinin TC sini ve Eposta'sýný güncelleyen sorgu.
SELECT * FROM Ogrenciler;
UPDATE Ogrenciler SET TC='1233453223',Eposta='skaraca@gmail.com' WHERE ID=3;
SELECT * FROM Ogrenciler;

SELECT * FROM Dersler;
SELECT * FROM Ogrenciler;
SELECT * FROM Ogretmenler;
SELECT * FROM Danismanlar;
SELECT * FROM Egitim;
SELECT * FROM Siniflar;
SELECT * FROM OgrenciEgitim;

INSERT INTO Egitim (Ders_ID,Ogretmen_ID,Sinif_ID,Tarih,SaatAralik)
VALUES (2,1,3,GETDATE(),'10:00-13:00');
INSERT INTO Egitim (Ders_ID,Ogretmen_ID,Sinif_ID,Tarih,SaatAralik)
VALUES (2,1,2,GETDATE(),'13:00-16:00');

DELETE FROM Egitim WHERE ID= 5;

INSERT INTO OgrenciEgitim (Egitim_ID,Ogrenci_ID,Danisman_ID)
VALUES (6,3,3);

INSERT INTO OgrenciEgitim (Egitim_ID,Ogrenci_ID,Danisman_ID)
VALUES (6,4,3);
INSERT INTO OgrenciEgitim (Egitim_ID,Ogrenci_ID,Danisman_ID)
VALUES (6,2,3);

-- 6 numaralý eðitimi alan öðrencilerin adlarý.

SELECT Ogrenciler.Ad FROM Ogrenciler
INNER JOIN OgrenciEgitim ON Ogrenciler.ID = OgrenciEgitim.Ogrenci_ID;

--Açýk olan Excel egitimlerini Öðretmen adý ve saati ile birlikte listeleyen sorgu

DECLARE @id int;
SELECT @id = (SELECT ID FROM Dersler WHERE Ad='Excel');
print @id;

SELECT 'Excel' AS [Egitim Adý],Ogretmenler.Ad,Ogretmenler.Soyad,Egitim.SaatAralik FROM Egitim INNER JOIN Ogretmenler ON
Egitim.Ogretmen_ID=Ogretmenler.ID
WHERE Egitim.Ders_ID = @id;

DECLARE @ucret float;
SET @ucret = 1000;
SELECT @ucret AS [KDV'siz],(@ucret*1.18) AS [KDV'li];

-- Hangi dersten kaç eðitim olduðunu listeleyen sorgu;
SELECT COUNT(*) AS EðitimSayýsý,Dersler.Ad from Egitim 
INNER JOIN Dersler ON Egitim.Ders_ID=Dersler.ID
GROUP BY Dersler.Ad;

-- Hiç Eðitim almayan öðrencilerin ad soyad'larýný listeleyen sorgu.
SELECT Ogrenciler.Ad,Ogrenciler.Soyad FROM Ogrenciler
WHERE Ogrenciler.ID NOT IN (SELECT OgrenciEgitim.Ogrenci_ID FROM OgrenciEgitim);

SELECT * FROM Ogrenciler;




