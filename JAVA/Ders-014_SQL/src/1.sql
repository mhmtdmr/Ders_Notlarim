-- INSERT INTO Ogrenci (Ad,Soyad,Numara) VALUES('Utku','Ko�lar',1);
/*
	
*/
-- INSERT INTO Ogrenci (Ad,Soyad,Numara) VALUES('Ay�e','Kuzular',1);
-- Sadece de�erleri yazarak kay�t ekleme. De�erler kolonlara s�ral� �ekilde eklenir.
-- INSERT INTO Ogrenci VALUES('Aysel','Demir',2);

--INSERT INTO Ogrenci VALUES('Mahir','Demir',3);


-- *: hER�EY
SELECT * FROM Ogrenci;
SELECT * FROM [KURS].[dbo].[Ogrenci];

-- Ogrenci adlar�n� listeleyen sorgu:
SELECT Ad FROM Ogrenci;

-- Ogrenci adlar�n� ve numaralar�n� listeleyen sorgu:
SELECT Ad,Numara FROM Ogrenci;

-- Ogrenci numaras� 2 olan kay�t� getiren sorgu.
SELECT * FROM Ogrenci WHERE Numara = 2;

-- Ogrenci numaras� 2'den k���k olan kay�tlar� getiren sorgu.
SELECT * FROM Ogrenci WHERE Numara < 2;

-- Ogrenci numaras� 2 veya 3 olan kay�tlar� getiren sorgu.
SELECT * FROM Ogrenci WHERE Numara = 2 OR Numara = 3;

-- Ogrenci numaras� 2 ve soyad� Demir olan kay�tlar� getiren sorgu.
SELECT * FROM Ogrenci WHERE Numara = 2 AND Soyad = 'Demir';

-- S�ralama
SELECT * FROM Ogrenci ORDER BY Numara ASC;  -- ASCending: artan: varsay�land�r. yazmasak da artan s�ralar.
SELECT * FROM Ogrenci order by Numara DESC; -- DESCending: azalan s�ralama.

SELECT * FROM Ogrenci;
-- Ad� Ahmet Soyad� Kuzular olan kayd�n Numaras�n� 4 olarak de�i�tir.
UPDATE Ogrenci SET Numara=4 WHERE Ad='Ahmet' AND Soyad='KUZULAR';

-- Ad� Ay ile ba�layanlar�n numaras�n� 5 yap
UPDATE Ogrenci SET Numara=5 WHERE Ad LIKE 'Ay%';

-- Soyad� K ile ba�lay�p sonras�nda 5 harf alanlar� getir.
SELECT * FROM Ogrenci WHERE Soyad LIKE 'K_____';


INSERT INTO Ogrenci VALUES('F�rat','Ko�','150');

INSERT INTO Ogrenci VALUES('Ece','�z','155');
INSERT INTO Ogrenci VALUES('�dris','Akbulut','165');

SELECT * FROM Ogrenci WHERE Numara LIKE '1%';

SELECT * FROM Ogrenci WHERE Numara LIKE '16_';

-- Ad'�n�n ilk harfi A veya E olanlar� listele.
SELECT * FROM Ogrenci WHERE (Ad LIKE 'A%') OR (Ad LIKE 'E%');
SELECT * FROM Ogrenci WHERE Ad LIKE '[AE]%';

-- Ad'�n�n ilk harfi A veya E olmayanlar� listele.
SELECT * FROM Ogrenci WHERE Ad LIKE '[^AE]%';
SELECT * FROM Ogrenci WHERE Ad NOT LIKE '[AE]%';

-- Numara's� 1 olan kayd� sil.
DELETE FROM Ogrenci WHERE Numara=5;

INSERT INTO Ogrenci VALUES('Ali','AK�A');

-- Numaras� 100'den b�y�k olanlar�n ad�n� yazd�r.
SELECT Ad FROM Ogrenci WHERE Numara IN (SELECT Numara FROM Ogrenci WHERE Numara>100)