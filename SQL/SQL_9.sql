---- hackerrank.com
---- github.com
---- kaggle.com

---- Northwind - Ürün kategorilerine göre satışlarım nasıl?(Hangi kategoriden kaç adet ürün)
--USE Northwind;
----SELECT TOP(5) * FROM [Order Details];
----SELECT * FROM Products;
----SELECT TOP(9) * FROM Categories; -- sonradan yapılsın. Önce CategoryID ile gruplansın.
----SELECT * FROM Orders;

--SELECT SUM(OD.Quantity) AS SatışAdet,C.CategoryName  FROM [Order Details] OD
--INNER JOIN Products P ON OD.ProductID=P.ProductID
--RIGHT JOIN Categories C ON C.CategoryID=P.CategoryID
--GROUP BY C.CategoryName ORDER BY SatışAdet DESC;

--INSERT INTO Categories (CategoryName,[Description])
--VALUES ('Alakasızlar','Alakası yok');
----(Hangi kategoriden kaç dolarlık ürün)
--DECLARE @DolarKur tinyint;
--SET @DolarKur=6;
--SELECT CONCAT(25,' $') AS Fiyat, CONCAT((25*@DolarKur),' TL') AS TL;

--SELECT C.CategoryName,SUM(OD.Quantity*OD.UnitPrice) AS ToplamFiyat
--FROM Categories C LEFT JOIN Products P ON P.CategoryID= C.CategoryID
--LEFT JOIN [Order Details] OD ON OD.ProductID = P.ProductID
--GROUP BY C.CategoryName;




--VIEW:  
--Order Details Birim Fiyat ve İndirim 'in görünmesini istemiyorum. Çözüm:

--ALTER VIEW OD2 WITH ENCRYPTION AS
--SELECT OrderID,ProductID,Quantity FROM [Order Details];

--SELECT * FROM OD2;

-- VIEW: Hangi kategoriden kaç ürünüm var? Bu sorunun cevabını bir VİEW ile verin.
--CREATE VIEW KategoriUrunAdet AS
--SELECT COUNT(ProductID) AS UrunAdet, Categories.CategoryName FROM  Products INNER JOIN Categories ON
--Products.CategoryID=Categories.CategoryID
--GROUP BY Categories.CategoryName;

--SELECT * FROM KategoriUrunAdet;

-- VIEW: Hangi Şehirden kaç müşterim var Ülkeye göre sıralama?
--SELECT * FROM Customers;

--CREATE VIEW UlkeMusteri AS
--SELECT Count(Customers.City) AS Sayı,City,Country AS MusteriAdet FROM Customers
--GROUP BY City,Country;

----UNION: Dikey birleştirme. Aynı kolonları tekrar yazmaz.
--SELECT 'Müşteri' AS Tip, City AS Sehir,Country, CONCAT('Şirket Adı: ',Customers.CompanyName) AS [Şirket/Yetkili Ad] FROM Customers 
--WHERE Country='France'
--UNION
--SELECT 'Tedarikçi' AS Tip, City,Country,CONCAT('Yetkili Adı: ',Suppliers.ContactName) AS [Şirket/Yetkili Ad] FROM Suppliers 
--WHERE Country='France';


----UNION ALL: Dikey birleştirme. Aynı kolonları tekrar eder.
--SELECT 'Müşteri' AS Tip, City AS Sehir,Country FROM Customers WHERE Country='France'
--UNION ALL
--SELECT 'Tedarikçi' AS Tip, City,Country FROM Suppliers WHERE Country='France';


---- Hangi ülkelerden müşterim var?
--SELECT DISTINCT(Country) FROM Customers ORDER BY Country;

--SELECT COUNT(*) FROM Customers;

--CREATE VIEW Alt20Pro AS
--SELECT * FROM Products WHERE UnitPrice<20;

--CREATE VIEW Alt20ProKat3 AS
--SELECT * FROM Alt20Pro WHERE CategoryID=3;

--SELECT * FROM Alt20ProKat3;


--DECLARE @isim NVARCHAR(MAX);
--SET @isim='Sertaç'; -- Değer atama
--PRINT @isim;
--SELECT @isim = 'Sercan'; -- Değer atama
--PRINT @isim;

--GO

--DECLARE @s int;
--SET @s=1;
--WHILE(@s<=20)
--BEGIN
--	PRINT CONCAT(@s,'. Sayı')
--	SET @s=@s+1;
--END

--GO
--DECLARE @yas TINYINT;
--SET @yas=23;
--IF (@yas>15 AND @yas<18)
--BEGIN
--	PRINT 'Liselilere sigara satışı yasaktır';
--END
--ELSE IF(@yas>18)
--BEGIN
--	PRINT 'Sigara alabilirsiniz. Ama içmeyin yine de.';
--END
--ELSE
--BEGIN
--	PRINT 'Sigara almaya yaşınız tutmuyor. Sağlığa da zararlı zaten.'
--END

--GO


CREATE PROCEDURE ProcAdi
(
@parametre1 int,
@parametre2 tinyint
)
AS
BEGIN
	SELECT * FROM Categories WHERE CategoryID=@parametre1;
END


-- Parametre olarak aldığı şehirdeki tüm Tedarikçi ve Müşteri 'lerin
-- CompanyName ContactName Address Country Phone
-- Tip kolonunda Tedarikçi mi Müşteri mi olduğu yazsın.
-- bilgilerini birleşik olarak listeleyen SP'yi yazınız.
CREATE PROC SP_Getir
(@sehir nvarchar(max))
AS
SELECT 'Müşteri' AS Tip, CompanyName, ContactName, [Address], Country, Phone FROM Customers 
WHERE City=@sehir
UNION ALL
SELECT 'Tedarikçi' AS Tip, CompanyName, ContactName, [Address], Country, Phone FROM Suppliers 
WHERE City=@sehir

EXECUTE SP_Getir 'London';

-- 2 tane sayısal değer alıp
-- Ürünler tablosundan fiyatı bu iki değer arasında olanları listeleyen SP
CREATE PROC SP_UrunFiyat
(
	@kucukDeger int,
	@buyukDeger int
)
AS
SELECT * FROM Products WHERE UnitPrice BETWEEN @kucukDeger AND @buyukDeger;


EXEC SP_UrunFiyat 18,25;