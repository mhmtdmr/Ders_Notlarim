--CREATE PROC EGetir
--(
--	@eid int,
--	@fname nvarchar(max) OUTPUT
--)
--AS
--BEGIN
--SELECT @fname = Employees.FirstName FROM Employees WHERE EmployeeID = @eid;
--END

--DECLARE @fname NVARCHAR(MAX);
--EXEC EGetir 3, @fname OUTPUT;
--SELECT @fname AS EAdı;

-- OUTPUT Kullanımı

--CREATE TRIGGER TR_Emp_Del
--ON Employees
--INSTEAD OF DELETE
--AS
--BEGIN
--	RollBack Tran -- İşlemi Geri Al.
--END

--DELETE FROM Employees;

--ALTER TRIGGER TR_Shi_Del
--ON Shippers
--AFTER DELETE
--AS
--DECLARE @id int;
--SELECT @id = ShipperID FROM DELETED;
--IF (@id>=5)
--BEGIN
--	ROLLBACK TRAN
--END

DELETE FROM Shippers WHERE ShipperID=4;

SELECT * FROM Shippers;

DISABLE TRIGGER TR_Shi_Del ON Shippers;
ENABLE TRIGGER TR_Shi_Del ON Shippers;



