-- INSERT INTO Ogrenci (Ad,Soyad,Numara) VALUES('Utku','Koçlar',1);
/*
	
*/
-- INSERT INTO Ogrenci (Ad,Soyad,Numara) VALUES('Ayþe','Kuzular',1);
-- Sadece deðerleri yazarak kayýt ekleme. Deðerler kolonlara sýralý þekilde eklenir.
-- INSERT INTO Ogrenci VALUES('Aysel','Demir',2);

--INSERT INTO Ogrenci VALUES('Mahir','Demir',3);


-- *: hERÞEY
SELECT * FROM Ogrenci;
SELECT * FROM [KURS].[dbo].[Ogrenci];

-- Ogrenci adlarýný listeleyen sorgu:
SELECT Ad FROM Ogrenci;

-- Ogrenci adlarýný ve numaralarýný listeleyen sorgu:
SELECT Ad,Numara FROM Ogrenci;

-- Ogrenci numarasý 2 olan kayýtý getiren sorgu.
SELECT * FROM Ogrenci WHERE Numara = 2;

-- Ogrenci numarasý 2'den küçük olan kayýtlarý getiren sorgu.
SELECT * FROM Ogrenci WHERE Numara < 2;

-- Ogrenci numarasý 2 veya 3 olan kayýtlarý getiren sorgu.
SELECT * FROM Ogrenci WHERE Numara = 2 OR Numara = 3;

-- Ogrenci numarasý 2 ve soyadý Demir olan kayýtlarý getiren sorgu.
SELECT * FROM Ogrenci WHERE Numara = 2 AND Soyad = 'Demir';

-- Sýralama
SELECT * FROM Ogrenci ORDER BY Numara ASC;  -- ASCending: artan: varsayýlandýr. yazmasak da artan sýralar.
SELECT * FROM Ogrenci order by Numara DESC; -- DESCending: azalan sýralama.

SELECT * FROM Ogrenci;
-- Adý Ahmet Soyadý Kuzular olan kaydýn Numarasýný 4 olarak deðiþtir.
UPDATE Ogrenci SET Numara=4 WHERE Ad='Ahmet' AND Soyad='KUZULAR';

-- Adý Ay ile baþlayanlarýn numarasýný 5 yap
UPDATE Ogrenci SET Numara=5 WHERE Ad LIKE 'Ay%';

-- Soyadý K ile baþlayýp sonrasýnda 5 harf alanlarý getir.
SELECT * FROM Ogrenci WHERE Soyad LIKE 'K_____';


INSERT INTO Ogrenci VALUES('Fýrat','Koç','150');

INSERT INTO Ogrenci VALUES('Ece','Öz','155');
INSERT INTO Ogrenci VALUES('Ýdris','Akbulut','165');

SELECT * FROM Ogrenci WHERE Numara LIKE '1%';

SELECT * FROM Ogrenci WHERE Numara LIKE '16_';

-- Ad'ýnýn ilk harfi A veya E olanlarý listele.
SELECT * FROM Ogrenci WHERE (Ad LIKE 'A%') OR (Ad LIKE 'E%');
SELECT * FROM Ogrenci WHERE Ad LIKE '[AE]%';

-- Ad'ýnýn ilk harfi A veya E olmayanlarý listele.
SELECT * FROM Ogrenci WHERE Ad LIKE '[^AE]%';
SELECT * FROM Ogrenci WHERE Ad NOT LIKE '[AE]%';

-- Numara'sý 1 olan kaydý sil.
DELETE FROM Ogrenci WHERE Numara=5;

INSERT INTO Ogrenci VALUES('Ali','AKÇA');

-- Numarasý 100'den büyük olanlarýn adýný yazdýr.
SELECT Ad FROM Ogrenci WHERE Numara IN (SELECT Numara FROM Ogrenci WHERE Numara>100)