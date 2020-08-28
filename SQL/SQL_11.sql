-- TRANSACTION: Bir sorgu bloðunun çalýþmasýný geri sarmada kullanýlýr.
--ÖRNEK: CategoryID'si 10 olan silinmek istediðinde iþlemi geri sar.
--CREATE TRIGGER TR_Kosullu_Engelle
--ON Categories
--AFTER DELETE 
--AS
--BEGIN
--	DECLARE @silinenid INT;
--	SELECT @silinenid=CategoryID FROM DELETED;
--	IF(@silinenid = 10)
--	BEGIN
--		ROLLBACK TRANSACTION
--	END

--END

--DELETE FROM Categories WHERE CategoryID=10;
--	SELECT * FROM Categories;

-- SilinmeyecekKategoriler isminde bir tablo oluþturun.
-- Bu tabloda silinmesini istemedeiðimiz kategorilerin ID'sini tutun.
-- Categories tablosundan bir kayýt silinmek istediðinde bu tabloya bakýn. Bu tabloda varsa silme iþlemini geri sardýrýn.

--ALTER TRIGGER TR_CAT_Kontrol_Sil
--ON Categories
--AFTER DELETE
--AS
--BEGIN
--	DECLARE @SilinenID INT;
--	SELECT @SilinenID = CategoryID FROM DELETED;
--	DECLARE @varMi INT 
--	SELECT @varMi =  CatID FROM SilinmeyecekKategoriler WHERE CatID=@SilinenID;
--	IF(@varMi IS NOT NULL)
--	BEGIN
--		ROLLBACK TRANSACTION
--		PRINT 'Bu kategori silinemez!'
--	END
--END
--DELETE FROM Categories WHERE CategoryID=12; -- silinme hatasý verecek.
--DELETE FROM Categories WHERE CategoryID IN (10,12) -- 10 yoktu 12 silinmedi
--DELETE FROM Categories WHERE CategoryID IN (13,14) -- 2 side silinmedi.
--DELETE FROM Categories WHERE CategoryID IN (15,13) -- 2 side silinmedi.


--SELECT * FROM Categories;

--DECLARE @varMi INT 
--SELECT @varMi =  CatID FROM SilinmeyecekKategoriler WHERE CatID=10;
--PRINT @varMi

--IF(@varMi IS NULL)
--BEGIN
--	PRINT 'Null'
--END
--ELSE
--BEGIN
--	PRINT 'Deðer Var'
--END


-- TRANSACTION

BEGIN TRAN
	BEGIN TRY
		UPDATE Hesap SET Bakiye-=100 WHERE ID=1;
		UPDATE Hesap SET Bakiye+=100 WHERE ID=2;
		COMMIT TRAN  -- Ýþlemi onaylar ve Transsaction'ý kapat
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN -- Geri sar ve Transaction ý kapat.
	END CATCH
SELECT * FROM Hesap;

-- SP_ParaTransfer: GonderenID,AlýcýID,Miktar
	--Parayý göndermeden önce bakiye kontrolü yap. Sonra da transaction içinde transferi gerçekleþtir.

ALTER PROC SP_ParaTransfer
(@gonderenid INT,@aliciid INT, @miktar INT)
AS
BEGIN
	DECLARE @gonderenbakiye INT;
	SELECT @gonderenbakiye = Bakiye FROM Hesap WHERE ID=@gonderenid;
	IF (@gonderenbakiye>=@miktar)
	BEGIN
	BEGIN TRAN
		BEGIN TRY
			UPDATE Hesap SET Bakiye-=@miktar WHERE ID=@gonderenid;
			UPDATE Hesap SET Bakiye+=@miktar WHERE ID=@aliciid;
			COMMIT TRAN  -- Ýþlemi onaylar ve Transsaction'ý kapat
		END TRY
		BEGIN CATCH
			PRINT 'Ýþlem gerçekleþmedi.'
			ROLLBACK TRAN -- Geri sar ve Transaction ý kapat.
		END CATCH
	END
	ELSE
	BEGIN
		PRINT 'Hesapta yeterince para yok.'
	END
END

EXEC SP_ParaTransfer 2,1,400;

-- TRANSACTION KAYDETME

BEGIN TRANSACTION
INSERT INTO Hesap (Bakiye) VALUES(15000);
SAVE TRANSACTION HesapEkle;
ROLLBACK TRANSACTION HesapEkle;
ROLLBACK TRAN;

BEGIN TRANSACTION
INSERT INTO Hesap (Bakiye) VALUES(77000);
SAVE TRANSACTION HesapEklee;
COMMIT TRANSACTION HesapEklee;
COMMIT TRAN;

SELECT * FROM Hesap