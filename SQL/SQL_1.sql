-- Açýklama Satýrý. Veritabaný tarafýndan iþleme alýnmayan satýrlar.
-- * Tüm kolonlarý ifade eder. 
-- Ders tablosundaki tüm kayýtlarýn tüm kolonlarýný listele
SELECT * FROM Ders;
SELECT * FROM [Ders];
SELECT * FROM OKUL_VT.dbo.Ders;
SELECT * FROM [OKUL_VT].[dbo].[Ders];

-- Tüm kayýtlarýn sadece Ad kolonunu getir.
SELECT Ad FROM Ders;
-- Çekilen Ad bilgisini DersAdý kolonu olarak listele.
SELECT Ad AS DersAdý FROM Ders;

-- Tüm kayýtlarýn sadece Ad ve Saat kolonunu getir.
select Ad,Saat FROM Ders;
-- DersNu su 4 olan kaydý getir.
SELECT * FROM Ders WHERE DersNu = 4;

-- Adý Matematik olan ders bilgilerini listele.
SELECT * FROM Ders WHERE Ad = 'Matematik';

-- Ders Saati 4 ten büyük olanlarý getir.
SELECT * FROM Ders WHERE Saat > 4;

-- ilk 3 kaydý getir.
SELECT TOP 3 * FROM Ders

-- Ders Saati 2 veya 6 olanlarý listele.
SELECT * FROM Ders WHERE Saat IN(2,6);
SELECT * FROM Ders WHERE Saat=2 OR Saat=6;

-- Ders Saati 2 veya 6 olmayanlarý listele.
SELECT * FROM Ders WHERE Saat NOT IN(2,6);
SELECT * FROM Ders WHERE Saat<>2 AND Saat<>6;
SELECT * FROM Ders WHERE Saat!=2 AND Saat!=6;

-- Ders Saati 3 ve 5 arasýnda olanlarý listele.
SELECT * FROM Ders WHERE Saat BETWEEN 3 AND 5;
SELECT * FROM Ders WHERE Saat>2 AND Saat<6;

-- Ders tablosundaki kayýt sayýsýný bana getir.
SELECT COUNT(*) FROM Ders;



-- DersNu sý en küçük olan kayýt numarasý
SELECT MIN(DersNu) FROM Ders;

-- DersNu sý en küçük olan kaydýn bilgileri
SELECT * FROM Ders WHERE DersNu = (SELECT MIN(DersNu) FROM Ders);

SELECT * FROM OgrenciDers;
SELECT * FROM Ogrenci;

-- Adý Ceyda olan öðrencinin not bilgileri
SELECT Numara FROM Ogrenci WHERE Ad = 'Ceyda';
SELECT * FROM OgrenciDers WHERE O_ID = (SELECT Numara FROM Ogrenci WHERE Ad = 'Ceyda');

-- Adý Ceyda olan öðrencinin aldýðý dersin adý.
SELECT Ad FROM Ders WHERE DersNu IN (SELECT D_ID FROM OgrenciDers WHERE O_ID = (SELECT Numara FROM Ogrenci WHERE Ad = 'Ceyda'));

-- SELECT'de 1 kaç konu kaldý




