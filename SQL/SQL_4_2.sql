-- View: Sanal tablolar veritaban�nda toplu olarak tutulmas. �a��r�ld�klar�nda veri anl�k olarak olu�turulur.
--CREATE VIEW AllCustomersOrders AS
--	SELECT Customers.CompanyName, Orders.OrderID
--	FROM Customers
--	RIGHT JOIN Orders
--	ON Customers.CustomerID=Orders.CustomerID;

--SELECT * FROM AllCustomersOrders;

--SELECT * FROM Orders;

--CREATE VIEW Siparis1996 AS
--SELECT * FROM Orders WHERE OrderDate LIKE '%1996%';

--SELECT * FROM Siparis1996;


--SELECT OrderID,CustomerID FROM Orders WHERE ShipCountry ='Germany';

--SELECT * FROM Orders

--Orders tablosunda USA'a g�nderilen sipari�lerin IrderID,CustomerID ve Employee Name ve Surname
-- Yukar�daki verileri VIEW olusturarak ��kar�n�z.

--CREATE VIEW OrdersUSA AS
--SELECT Employees.FirstName,Employees.LastName,Orders.OrderID,Orders.CustomerID,Orders.ShipCountry FROM Orders
--INNER JOIN Employees ON Employees.EmployeeID = Orders.EmployeeID
--WHERE ShipCountry='USA';

--Select * From OrdersUSA;


-- GROUP BY --

-- Hangi �lkeden ka� m��terim var?

--SELECT CAST((COUNT(*)/((SELECT COUNT(*) FROM Customers)*1.0)) AS FLOAT) AS YUZDE Country FROM Customers GROUP BY Country ORDER BY Country;

SELECT COUNT(*) FROM Customers;

-- Toplam m��teri say�s� 5'ten fazla olan �lkeleri, m��teri say�lar� ile birlikte listele

SELECT COUNT(CustomerID), Country FROM  Customers GROUP BY Country HAVING COUNT(CustomerID)>5;

SELECT COUNT(*) FROM Customers;
SELECT COUNT(Region) FROM Customers; -- NULL h�cre COUNT'ta say�lm�yor.

-- Products : Hangi kategoriden ka� �r�n var?
SELECT * FROM Products;
SELECT COUNT(ProductID) AS Miktar, CategoryID FROM Products GROUP BY CategoryID;

SELECT COUNT(*) FROM Products WHERE CategoryID IS NULL;

-----------------

SELECT COUNT(*) FROM Customers;

SELECT (CAST(13 AS FLOAT)/CAST(91 AS FLOAT))*100;

-- H�seyin'in sordu�u soru.
SELECT CAST((CAST(COUNT(*) AS FLOAT)/CAST((SELECT COUNT(*) FROM Customers)AS FLOAT))*100 AS FLOAT) AS Oran
, Country FROM Customers GROUP BY Country ORDER BY Country;

-- Hangi kategoride toplam ne kadar stok var? (Products)
-- 
SELECT SUM(Products.UnitsInStock),Categories.CategoryName FROM Categories INNER JOIN Products ON Products.CategoryID = Categories.CategoryID
Group By Categories.CategoryName;

-- Her kategorideki �r�nlerin toplam mal de�eri nedir?
SELECT SUM(Products.UnitsInStock*Products.UnitPrice),Categories.CategoryName FROM Categories INNER JOIN Products ON Products.CategoryID = Categories.CategoryID
Group By Categories.CategoryName;

 SELECT * FROM Categories;
 SELECT * FROM Products;





