---------------------
-- INSERT SORGULARI--
---------------------

SELECT * FROM Ogrenci

INSERT INTO Ogrenci (Ad,Soyad) VALUES('Serhat','ÇELÝK');
INSERT INTO Ogrenci (Ad,Soyad) VALUES('Selda','BOSTANCI');

-- Veriler kolonsýrasýna göre verilirse kolon adlarý belirtilmeden akyýt eklenebilir.
INSERT INTO Ogrenci VALUES('Veli','CAN');

--GO
--INSERT INTO Ogrenci (Ad,Soyad) VALUES('Serhat','ÇELÝK');
--GO 15

-- DELETE --
------------

-- Numarasý 7 25 arasýnda olan Ad=Serhat Soyad=Çelik olanlarý sil.
DELETE FROM Ogrenci WHERE Numara BETWEEN 7 AND 25 AND Ad='Serhat' AND Soyad='ÇELÝK';

SELECT * FROM Ogrenci;

-- Soyadý küçük harfle can olanlarý sil.
DELETE FROM Ogrenci WHERE Soyad COLLATE SQL_Latin1_General_CP1_CS_AS LIKE 'can';

--// Tablodaki kayýtlarýn tamamýný siler
DELETE FROM Ogrenci;

--// Tablodaki kayýtlarýn tamamýný siler. Ayrýca Identity kolonunu sýfýrlar.
TRUNCATE TABLE Ogrenci;
-- Ýliþkisel tablolardan dolayý önce OgrenciDers tablosunu sildik.,
-- Bunu yapmadan Ogrenci tablosunu silmemize izin vermedi.
DELETE FROM OgrenciDers;


-- UPDATE --
------------
UPDATE Ogrenci SET Ad = 'Necla' WHERE Numara=5;

UPDATE Ogrenci SET Ad='Mehmet', Soyad = 'Demir' WHERE Numara<2;

SELECT * FROM Ogrenci;

