-- TRANSACTION: Bir sorgu blo�unun �al��mas�n� geri sarmada kullan�l�r.
--�RNEK: CategoryID'si 10 olan silinmek istedi�inde i�lemi geri sar.
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

-- SilinmeyecekKategoriler isminde bir tablo olu�turun.
-- Bu tabloda silinmesini istemedei�imiz kategorilerin ID'sini tutun.
-- Categories tablosundan bir kay�t silinmek istedi�inde bu tabloya bak�n. Bu tabloda varsa silme i�lemini geri sard�r�n.

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
--DELETE FROM Categories WHERE CategoryID=12; -- silinme hatas� verecek.
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
--	PRINT 'De�er Var'
--END


-- TRANSACTION

BEGIN TRAN
	BEGIN TRY
		UPDATE Hesap SET Bakiye-=100 WHERE ID=1;
		UPDATE Hesap SET Bakiye+=100 WHERE ID=2;
		COMMIT TRAN  -- ��lemi onaylar ve Transsaction'� kapat
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN -- Geri sar ve Transaction � kapat.
	END CATCH
SELECT * FROM Hesap;

-- SP_ParaTransfer: GonderenID,Al�c�ID,Miktar
	--Paray� g�ndermeden �nce bakiye kontrol� yap. Sonra da transaction i�inde transferi ger�ekle�tir.

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
			COMMIT TRAN  -- ��lemi onaylar ve Transsaction'� kapat
		END TRY
		BEGIN CATCH
			PRINT '��lem ger�ekle�medi.'
			ROLLBACK TRAN -- Geri sar ve Transaction � kapat.
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