SELECT * FROM Kurs_VT.INFORMATION_SCHEMA.TABLES;

SELECT * FROM Dersler;
SELECT * FROM Ogrenciler;
SELECT * FROM Ogretmenler;
SELECT * FROM Danismanlar;
SELECT * FROM Egitim;
-- % joker anlam� ta��r. 0 veya daha fazla her karakter anlam�na gelir.

-- Eposta adresinde necip ge�en kay�tlar� listeleyen sorgu:
SELECT * FROM Ogretmenler WHERE Ogretmenler.Eposta LIKE '%necip%';

-- Eposta adresinde ncp harflerinden birisi bulunanlar� listeleyen sorgu.
SELECT * FROM Ogretmenler WHERE Eposta LIKE '%[ncp]%';

-- Eposta adresinde np harflerinden birisi bulunmayanlar� listeleyen sorgu.
SELECT * FROM Ogretmenler WHERE Eposta NOT LIKE '%[np]%';

-- Ad'� A ile ba�lay�p 2. harfi l olmayanlar� listeleyen sorgu.
SELECT * FROM Ogretmenler WHERE Ad LIKE 'A[^l]%';

-- ��retmenlerden soyad� 4 harfli olanlar� getiren sorgu
SELECT * FROM Ogretmenler WHERE Soyad LIKE '____'; -- her bir _ bir karakterlik alan� temsil eder.

-- Soyad� A-K aras�ndaki harfler ile ba�layanlar� getir.
SELECT * FROM Ogretmenler WHERE Soyad LIKE '[A-K]%';

-- Toplam saati 100'�n alt�nda olanlardan ad�nda Excel ge�en dersleri listeleyen sorgu.
SELECT * FROM Dersler WHERE ToplamSaat<100 AND Ad LIKE '%Excel%';

-- Ogrenciler tablosuna kay�t ekleyen INSERT sorgusunu yaz�n�z.
INSERT INTO Ogrenciler (Ad,Soyad,TC,Telefon,Eposta)
VALUES('Sefa','Karata�','96385274123','05462923058','serfa@gmail.com');

-- mail adresi gmail olan ��rencileri listeleyen sorgu.
SELECT * FROM Ogrenciler WHERE Eposta LIKE '%gmail%'

-- ID'si 3 ve 5 olanlar�n dersSaatini toplam� ve toplam�n�n 5 kat�n� g�steren select sorgusu
DECLARE @toplamSaat int;
SELECT @toplamSaat = (SELECT SUM(ToplamSaat) as ToplamDersSaati FROM Dersler WHERE ID IN(3,5));
print(@toplamSaat*5);

-- ��retmenlerden ad� Ahmet veya Mehmet'den birisi olanlar� listeleyen sorgu.
SELECT * FROM Ogretmenler WHERE Ad IN('Ahmet','Mehmet');
SELECT * FROM Ogretmenler WHERE Ad ='Ahmet' OR Ad='Mehmet';

-- Ders saatlerinin ortalamas�n� getiren sorgu.
SELECT AVG(ToplamSaat) as [Ders Saati Ortalamasi] FROM Dersler;

-- Ka� ��renci oldu�unu sayan sorgu
-- ID'si 3 olan ��rencinin TC sini ve Eposta's�n� g�ncelleyen sorgu.
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

-- 6 numaral� e�itimi alan ��rencilerin adlar�.

SELECT Ogrenciler.Ad FROM Ogrenciler
INNER JOIN OgrenciEgitim ON Ogrenciler.ID = OgrenciEgitim.Ogrenci_ID;

--A��k olan Excel egitimlerini ��retmen ad� ve saati ile birlikte listeleyen sorgu

DECLARE @id int;
SELECT @id = (SELECT ID FROM Dersler WHERE Ad='Excel');
print @id;

SELECT 'Excel' AS [Egitim Ad�],Ogretmenler.Ad,Ogretmenler.Soyad,Egitim.SaatAralik FROM Egitim INNER JOIN Ogretmenler ON
Egitim.Ogretmen_ID=Ogretmenler.ID
WHERE Egitim.Ders_ID = @id;

DECLARE @ucret float;
SET @ucret = 1000;
SELECT @ucret AS [KDV'siz],(@ucret*1.18) AS [KDV'li];

-- Hangi dersten ka� e�itim oldu�unu listeleyen sorgu;
SELECT COUNT(*) AS E�itimSay�s�,Dersler.Ad from Egitim 
INNER JOIN Dersler ON Egitim.Ders_ID=Dersler.ID
GROUP BY Dersler.Ad;

-- Hi� E�itim almayan ��rencilerin ad soyad'lar�n� listeleyen sorgu.
SELECT Ogrenciler.Ad,Ogrenciler.Soyad FROM Ogrenciler
WHERE Ogrenciler.ID NOT IN (SELECT OgrenciEgitim.Ogrenci_ID FROM OgrenciEgitim);

SELECT * FROM Ogrenciler;




