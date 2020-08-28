---------------------
-- INSERT SORGULARI--
---------------------

SELECT * FROM Ogrenci

INSERT INTO Ogrenci (Ad,Soyad) VALUES('Serhat','�EL�K');
INSERT INTO Ogrenci (Ad,Soyad) VALUES('Selda','BOSTANCI');

-- Veriler kolons�ras�na g�re verilirse kolon adlar� belirtilmeden aky�t eklenebilir.
INSERT INTO Ogrenci VALUES('Veli','CAN');

--GO
--INSERT INTO Ogrenci (Ad,Soyad) VALUES('Serhat','�EL�K');
--GO 15

-- DELETE --
------------

-- Numaras� 7 25 aras�nda olan Ad=Serhat Soyad=�elik olanlar� sil.
DELETE FROM Ogrenci WHERE Numara BETWEEN 7 AND 25 AND Ad='Serhat' AND Soyad='�EL�K';

SELECT * FROM Ogrenci;

-- Soyad� k���k harfle can olanlar� sil.
DELETE FROM Ogrenci WHERE Soyad COLLATE SQL_Latin1_General_CP1_CS_AS LIKE 'can';

--// Tablodaki kay�tlar�n tamam�n� siler
DELETE FROM Ogrenci;

--// Tablodaki kay�tlar�n tamam�n� siler. Ayr�ca Identity kolonunu s�f�rlar.
TRUNCATE TABLE Ogrenci;
-- �li�kisel tablolardan dolay� �nce OgrenciDers tablosunu sildik.,
-- Bunu yapmadan Ogrenci tablosunu silmemize izin vermedi.
DELETE FROM OgrenciDers;


-- UPDATE --
------------
UPDATE Ogrenci SET Ad = 'Necla' WHERE Numara=5;

UPDATE Ogrenci SET Ad='Mehmet', Soyad = 'Demir' WHERE Numara<2;

SELECT * FROM Ogrenci;

