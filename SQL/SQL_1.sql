-- A��klama Sat�r�. Veritaban� taraf�ndan i�leme al�nmayan sat�rlar.
-- * T�m kolonlar� ifade eder. 
-- Ders tablosundaki t�m kay�tlar�n t�m kolonlar�n� listele
SELECT * FROM Ders;
SELECT * FROM [Ders];
SELECT * FROM OKUL_VT.dbo.Ders;
SELECT * FROM [OKUL_VT].[dbo].[Ders];

-- T�m kay�tlar�n sadece Ad kolonunu getir.
SELECT Ad FROM Ders;
-- �ekilen Ad bilgisini DersAd� kolonu olarak listele.
SELECT Ad AS DersAd� FROM Ders;

-- T�m kay�tlar�n sadece Ad ve Saat kolonunu getir.
select Ad,Saat FROM Ders;
-- DersNu su 4 olan kayd� getir.
SELECT * FROM Ders WHERE DersNu = 4;

-- Ad� Matematik olan ders bilgilerini listele.
SELECT * FROM Ders WHERE Ad = 'Matematik';

-- Ders Saati 4 ten b�y�k olanlar� getir.
SELECT * FROM Ders WHERE Saat > 4;

-- ilk 3 kayd� getir.
SELECT TOP 3 * FROM Ders

-- Ders Saati 2 veya 6 olanlar� listele.
SELECT * FROM Ders WHERE Saat IN(2,6);
SELECT * FROM Ders WHERE Saat=2 OR Saat=6;

-- Ders Saati 2 veya 6 olmayanlar� listele.
SELECT * FROM Ders WHERE Saat NOT IN(2,6);
SELECT * FROM Ders WHERE Saat<>2 AND Saat<>6;
SELECT * FROM Ders WHERE Saat!=2 AND Saat!=6;

-- Ders Saati 3 ve 5 aras�nda olanlar� listele.
SELECT * FROM Ders WHERE Saat BETWEEN 3 AND 5;
SELECT * FROM Ders WHERE Saat>2 AND Saat<6;

-- Ders tablosundaki kay�t say�s�n� bana getir.
SELECT COUNT(*) FROM Ders;



-- DersNu s� en k���k olan kay�t numaras�
SELECT MIN(DersNu) FROM Ders;

-- DersNu s� en k���k olan kayd�n bilgileri
SELECT * FROM Ders WHERE DersNu = (SELECT MIN(DersNu) FROM Ders);

SELECT * FROM OgrenciDers;
SELECT * FROM Ogrenci;

-- Ad� Ceyda olan ��rencinin not bilgileri
SELECT Numara FROM Ogrenci WHERE Ad = 'Ceyda';
SELECT * FROM OgrenciDers WHERE O_ID = (SELECT Numara FROM Ogrenci WHERE Ad = 'Ceyda');

-- Ad� Ceyda olan ��rencinin ald��� dersin ad�.
SELECT Ad FROM Ders WHERE DersNu IN (SELECT D_ID FROM OgrenciDers WHERE O_ID = (SELECT Numara FROM Ogrenci WHERE Ad = 'Ceyda'));

-- SELECT'de 1 ka� konu kald�




