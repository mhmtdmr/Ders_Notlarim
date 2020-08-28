--DECLARE @sayi INT;
--SET @sayi=2;
--SELECT * FROM Shippers WHERE ShipperID=@sayi;

-- De�er D�nd�ren Stored Procedure, sonunda OUTPUT yaz�larak parametreye atanan de�er 
-- SP'nin �al��t�r�ld��� yere d�nd�r�l�r.
--ALTER PROC SP_ShipperName
--(
--@id int, -- IN y�n�nde bir parametre.
--@CompName NVARCHAR(MAX) OUTPUT -- ��k�� y�n�nde bir parametre.
--)
--AS
--SELECT @CompName = CompanyName FROM Shippers WHERE ShipperID=@id;

--DECLARE @gelen NVARCHAR(MAX);
--EXEC SP_ShipperName 1, @gelen OUTPUT;
--SELECT @gelen

-- Sipari� ID 'si verilen sipari�in CustomerID'sini d�nd�ren SP'yi yaz�n�z.

--CREATE PROC SP_CID_Getir
--(
--@oid INT,
--@cid NCHAR(5) OUTPUT
--)
--AS
--BEGIN
--	SELECT @cid = Orders.CustomerID FROM Orders WHERE OrderID=@oid;
--END

--DECLARE @customer NCHAR(5);
--EXEC SP_CID_Getir 10250, @customer OUTPUT;
----SELECT @customer AS M��teriID;
--PRINT @customer;


---- Dizi �eklinde veri tablo tipi ile tutulabilir.
--declare @sayilar table(sayi int);
--INSERT INTO @sayilar (sayi) VALUES(4)
--INSERT INTO @sayilar (sayi) VALUES(5)
--INSERT INTO @sayilar (sayi) VALUES(6)
--INSERT INTO @sayilar (sayi) VALUES(7)




------------------------------------------------
-----------------  TRIGGER'LAR -----------------
------------------------------------------------

-- �art sa�land���nda otomatik olarak �al��an SQL sorgular� olu�turmam�z� sa�lar.
-- AFTER: Bir komut �al��t�ktan sonra otomatik olarak �al��acak olan sorgular� belirtmemizi sa�lar.
-- INSTEAD OF: Bir komutun yerine �al��mas�n� istedi�imiz sorgular� belirtmemizi sa�lar.



--ALTER TRIGGER TR_ShipperSilmeEngelleme
--ON Northwind.dbo.Shippers
--INSTEAD OF DELETE -- Yerine. DELETE yerine ben ne yazd�ysam o �al��acak.
--AS
--BEGIN
--	DECLARE @cn NVARCHAR(MAX);
--	SELECT @cn = CompanyName FROM DELETED; -- DELETED
--	PRINT CONCAT(@cn,' silinemez !  Silme i�lemleri engellenmi�tir.');
--END

--DELETE FROM Shippers WHERE ShipperID=6;
--UPDATE Shippers SET CompanyName='Be�ikta� Nakliyat' WHERE ShipperID=6;
--SELECT * FROM Shippers;


--- Shippers_Yeni isimli tabloyu olu�turduk.
-------------------------------------------
--USE [Northwind]
--GO

--/****** Object:  Table [dbo].[Shippers]    Script Date: 19.01.2019 17:06:31 ******/
--SET ANSI_NULLS ON
--GO

--SET QUOTED_IDENTIFIER ON
--GO

--CREATE TABLE [dbo].[Shippers_Yeni](
--	[ShipperID] [int] IDENTITY(1,1) NOT NULL,
--	[CompanyName] [nvarchar](40) NOT NULL,
--	[Phone] [nvarchar](24) NULL,
-- CONSTRAINT [PK_Shippers_Yeni] PRIMARY KEY CLUSTERED 
--(
--	[ShipperID] ASC
--)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
--) ON [PRIMARY]
--GO





CREATE TRIGGER TR_ShipEkle
ON Shippers
INSTEAD OF INSERT
AS
BEGIN
	DECLARE @cn NVARCHAR(MAX);
	DECLARE @pn NVARCHAR(MAX);
	SELECT @cn = CompanyName FROM INSERTED;
	SELECT @pn = Phone FROM INSERTED;
	INSERT INTO Shippers_Yeni (CompanyName,Phone) VALUES(@cn,@pn)
END

INSERT INTO Shippers (CompanyName,Phone) VALUES('CAN Nakliyat','7896542')

SELECT * FROM Shippers;
SELECT * FROM Shippers_Yeni;

DISABLE TRIGGER TR_ShipperSilmeEngelleme ON Shippers;
--ENABLE TRIGGER TR_ShipperSilmeEngelleme ON Shippers;


-- Shippers tablosundan veri silindi�inde silinen veriyi Shippers_Eski isimli tabloya ekleyen trigger.
-- �nceki b�l�mlerde olu�turdu�umuz INSTEAD OF DELETE trigger'�n� disable ettik!!

SELECT * FROM Shippers;


--USE [Northwind]
--GO
--/****** Object:  Table [dbo].[Shippers]    Script Date: 19.01.2019 17:53:15 ******/
--SET ANSI_NULLS ON
--GO
--SET QUOTED_IDENTIFIER ON
--GO
--CREATE TABLE [dbo].[Shippers_Eski](
--	[Shipper_Eski_ID] [int] IDENTITY(1,1) NOT NULL,
--	[CompanyName] [nvarchar](40) NOT NULL,
--	[Phone] [nvarchar](24) NULL,
--	[ShipperID] [int]
-- CONSTRAINT [PK_Shippers_Eski] PRIMARY KEY CLUSTERED 
--(
--	[ShipperID] ASC
--)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
--) ON [PRIMARY]
--GO


--CREATE TRIGGER TR_Delete_Yedek
--ON Shippers
--AFTER DELETE
--AS
--BEGIN
--DECLARE @id INT;
--DECLARE @cname NVARCHAR(MAX);
--DECLARE @phone NVARCHAR(MAX);
--SELECT @id = ShipperID, @cname = CompanyName, @phone = Phone FROM DELETED;
--INSERT INTO Northwind.dbo.Shippers_Eski (CompanyName,Phone,ShipperID) VALUES(@cname,@phone,@id);
--END



--SELECT * FROM Shippers;
--SELECT * FROM Shippers_Eski;


--DELETE FROM Shippers WHERE ShipperID=6;

-- Shippers tablosunda bir g�ncelleme yap�ld���nda g�ncellenen eski veriyi (ShipperID,CompanyName ve Phone)
-- Shippers_Eski tablosuna kayededen trigger.

--CREATE TRIGGER TR_Shipper_Guncelleme
--ON Shippers
--AFTER UPDATE
--AS
--DECLARE @id INT;
--DECLARE @cname NVARCHAR(MAX);
--DECLARE @phone NVARCHAR(MAX);
--SELECT @id = ShipperID, @cname = CompanyName, @phone = Phone FROM DELETED;
--INSERT INTO Northwind.dbo.Shippers_Eski (CompanyName,Phone,ShipperID) VALUES(@cname,@phone,@id);


--UPDATE Shippers SET CompanyName='�stanbul Nakliyat' WHERE ShipperID=5;
--SELECT * FROM Shippers;
--SELECT * FROM Shippers_Eski;

-- Categories tablosunda bir silme i�lemini engelleyin. ve ekrana Bu tabloda silme yap�lamaz yazd�r�n.
-- Trigger ile.
--ALTER TRIGGER TR_Cat_Silme_Engelle
--ON Categories
--INSTEAD OF DELETE -- FOR=INSTEAD OF
--AS
--PRINT 'Bu tabloyda silme i�lemi yap�lamaz!!!';




---- INSTEAD OF DELETE trigger'� i�inde silme yap�ld���nda silme ger�ekle�ir.!!!

--ALTER TRIGGER TR_Cat_Silme_Engelle
--ON Categories
--INSTEAD OF DELETE
--AS
--DECLARE @id INT;
--SELECT @id = CategoryID FROM deleted;
--DELETE FROM Categories WHERE Categories.CategoryID=@id;
--PRINT 'Bu tabloda silme i�lemi sadece trigger i�inden yap�labilir.!!!';

-- Categories tablosunda g�ncelleme yap�ld���nda eski veriyi ve i�lem tarihini Categories_Eski isimli
-- tabloda tutan Trigger'� yaz�n�z.

--USE [Northwind]
--GO
--CREATE TABLE [dbo].[Categories_Eski](
--	[GuncellenenID] [int] IDENTITY(1,1) NOT NULL,
--	[CategoryID] [int] NOT NULL,
--	[CategoryName] [nvarchar](15) NOT NULL,
--	[Description] [ntext] NULL,
--	[Picture] [image] NULL,
--	[Guncelleme_Tarihi] [DATETIME] NOT NULL,
-- CONSTRAINT [PK_Categories_Eski] PRIMARY KEY CLUSTERED 
--(
--	[GuncellenenID] ASC
--)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
--) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
--GO


--CREATE TRIGGER TR_Cat_Guncelle
--ON Categories
--AFTER UPDATE
--AS
--BEGIN
--DECLARE @cid INT;
--DECLARE @cname NVARCHAR(15);
--DECLARE @desc NVARCHAR(MAX);
--DECLARE @tarih DATETIME;
--SET @tarih = GETDATE();

--SELECT @cid = CategoryID,@cname = [CategoryName],@desc=[Description] FROM DELETED;
--INSERT INTO Categories_Eski (CategoryID,CategoryName,[Description],Guncelleme_Tarihi)
--VALUES (@cid,@cname,@desc,@tarih);

--END


--UPDATE Categories SET Categories.CategoryName = 'YeniTest', Categories.Description='YeniTest' WHERE CategoryID=9;
--SELECT * FROM Categories_Eski;
--SELECT * FROM Categories;

--SELECT CURRENT_USER; -- dbo
--SELECT SUSER_SNAME(); -- DESKTOP-NHCKD45\105UBY00
--SELECT ORIGINAL_LOGIN(); -- DESKTOP-NHCKD45\105UBY00





DELETE FROM Categories WHERE Categories.CategoryID=11;

SELECT * FROM Categories;

INSERT INTO [dbo].[Categories]
           ([CategoryName]
           ,[Description])
     VALUES
           ('ASD','asdasdasd')


-- 