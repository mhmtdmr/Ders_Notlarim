----DECLARE @ad NVARCHAR(MAX);
----DECLARE @soyad NVARCHAR(MAX);
----SET @ad = 'Ömer';
----SET @soyad = 'Göksoy';

------ Sýnýflar tablosuna ekleme(kayýt) yapan Stored Procedure 'ü yazýnýz.

----SELECT TOP (1000) [ID]
----      ,[Ad]
----      ,[Kapasite]
----      ,[Kat]
----  FROM [Kurs_VT].[dbo].[Siniflar]

----  ALTER PROC SP_SinifEkle
----  ( 
----	@ad NVARCHAR(50) = 'isimsiz', -- Varsayýlan deðer atamasý.
----	@kapasite tinyint ,
----	@kat tinyint
----  )
----  AS
----  BEGIN
----	INSERT INTO Siniflar (Ad,Kapasite,Kat) VALUES(@ad,@kapasite,@kat);
----	SELECT TOP(1) * FROM Siniflar ORDER BY ID DESC;
----  END

----  -- SP'yi çaðýrma.
---- EXEC SP_SinifEkle @ad='305',@kapasite=34,@kat=3;
---- EXEC SP_SinifEkle '205',24,2;

---- -- Siniflar tablosundan silme iþlemi yapan SP: Parametre olarak sýnýf Adi alabilir. Yada ID alabilir. (Tek Parametre)

ALTER PROCEDURE  SP_SinifSil
( @p NVARCHAR(50))
AS
BEGIN
	DELETE FROM Siniflar WHERE ID=CAST(@p AS int) OR Ad=@p;
END
SELECT * FROM Siniflar;
EXEC SP_SinifSil '305'

------ Öðretmenler tablosunda isme göre arama yapan SP. Parametre olarak metin tipinde 1 parametre alacak.
----CREATE PROCEDURE SP_OGRETMENARA
----(@anahtar NVARCHAR(100))
----AS
----BEGIN
----	SELECT * FROM Ogretmenler WHERE Ad LIKE '%'+@anahtar+'%';
----END

---- EXECUTE SP_OGRETMENARA 'hme';





---- Tabloyu kopyaladýk.
----USE [Kurs_VT]
----GO

----/****** Object:  Table [dbo].[Egitim_Eski]    Script Date: 5.01.2019 17:15:55 ******/
----SET ANSI_NULLS ON
----GO

----SET QUOTED_IDENTIFIER ON
----GO

----CREATE TABLE [dbo].[Egitim_Eski](
----	[ID] [int] IDENTITY(1,1) NOT NULL,
----	[Ders_ID] [tinyint] NOT NULL,
----	[Ogretmen_ID] [smallint] NOT NULL,
----	[Sinif_ID] [tinyint] NOT NULL,
----	[Tarih] [date] NOT NULL,
----	[SaatAralik] [nvarchar](15) NOT NULL,
---- CONSTRAINT [PK_Egitim_Eski] PRIMARY KEY CLUSTERED 
----(
----	[ID] ASC
----)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
----) ON [PRIMARY]
----GO

----ALTER TABLE [dbo].[Egitim_Eski]  WITH CHECK ADD  CONSTRAINT [FK_Egitim_Eski_Dersler] FOREIGN KEY([Ders_ID])
----REFERENCES [dbo].[Dersler] ([ID])
----GO

----ALTER TABLE [dbo].[Egitim_Eski] CHECK CONSTRAINT [FK_Egitim_Eski_Dersler]
----GO

----ALTER TABLE [dbo].[Egitim_Eski]  WITH CHECK ADD  CONSTRAINT [FK_Egitim_Eski_Ogretmenler] FOREIGN KEY([Ogretmen_ID])
----REFERENCES [dbo].[Ogretmenler] ([ID])
----GO

----ALTER TABLE [dbo].[Egitim_Eski] CHECK CONSTRAINT [FK_Egitim_Eski_Ogretmenler]
----GO

----ALTER TABLE [dbo].[Egitim_Eski]  WITH CHECK ADD  CONSTRAINT [FK_Egitim_Eski_Siniflar] FOREIGN KEY([Sinif_ID])
----REFERENCES [dbo].[Siniflar] ([ID])
----GO

----ALTER TABLE [dbo].[Egitim_Eski] CHECK CONSTRAINT [FK_Egitim_Eski_Siniflar]
----GO


---- Egitim tablosundan silme SP'sini yazýn. Silme için gönderilen ID 'ye ait bilgileri önce Egitim_Eski tablosuna kaydetsin.
---- Sonra egitim tablosundan silme iþlemini yapsýn.

--ALTER PROC SP_EgitimSil
--(@id int)
--AS
--BEGIN
--	--DECLARE @ders_id TINYINT;
--	--DECLARE @ogretmen_id SMALLINT; 
--	--DECLARE @sinif_id TINYINT;
--	--DECLARE @tarih DATE;
--	--DECLARE @saat_aralik NVARCHAR(15);
	 
--	--SELECT @ders_id=Egitim.Ders_ID,@ogretmen_id=Egitim.Ogretmen_ID,@sinif_id=Egitim.Sinif_ID,@tarih=Egitim.Tarih,@saat_aralik=Egitim.SaatAralik
--	--FROM Egitim WHERE ID = @id;

--	--INSERT INTO Egitim_Eski VALUES(@ders_id,@ogretmen_id,@sinif_id,@tarih,@saat_aralik);
--	INSERT INTO Egitim_Eski (Ders_ID,Ogretmen_ID,Sinif_ID,Tarih,SaatAralik) 
--	( SELECT Ders_ID, Ogretmen_ID, Sinif_ID,Tarih,SaatAralik FROM Egitim WHERE ID=@id);

--	DELETE FROM Egitim WHERE ID=@id;
--END

--EXECUTE SP_EgitimSil 3;
--EXECUTE SP_EgitimSil 1;

--DELETE FROM OgrenciEgitim;

--SELECT * FROM Egitim;
--SELECT * FROM Egitim_Eski;

---- Danismanlar tablosundaki verileri güncelleme SP'sini yazýn.

--ALTER PROCEDURE SP_Danisman_Guncelle
--(
--@id INT,
--@ad NVARCHAR(100) = NULL,
--@soyad NVARCHAR(100)
--)
--AS
--BEGIN
--	DECLARE @eski_ad NVARCHAR(100);
--	DECLARE @eski_soyad NVARCHAR(100);
--	SELECT @eski_ad=Ad,@eski_soyad=Soyad FROM Danismanlar WHERE ID=@id;
--	IF(@ad='' OR @ad IS NULL)
--	BEGIN
--		SET @ad=@eski_ad;
--	END
--	IF(@soyad='' OR @soyad IS NULL)
--	BEGIN
--		SET @soyad=@eski_soyad;
--	END
--	UPDATE Danismanlar SET Ad=@ad, Soyad=@soyad WHERE ID=@id;
--	SELECT * FROM Danismanlar;
--	--HACKERRANK
--END

--SELECT * FROM Danismanlar;

--EXEC SP_Danisman_Guncelle 3,'Talip','Karabora';
--EXEC SP_Danisman_Guncelle @id=3,@ad='Salih',@soyad='Karabora';

--EXEC SP_Danisman_Guncelle 1,'AD','Soyad';


-- Dersler tablosundaki derse ait Update SP'sini yazýnýz. (ID,Ad,Saat)
SELECT * FROM Dersler;

INSERT INTO Dersler VALUES('3DS Max',148);
INSERT INTO Dersler VALUES('Photoshop',148);