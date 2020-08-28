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
--SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country;

--SELECT * FROM Customers;

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
SELECT SUM(Products.UnitsInStock*Products.UnitPrice),Categories.CategoryName FROM Categories 
INNER JOIN Products ON Products.CategoryID = Categories.CategoryID
Group By Categories.CategoryName;

-- T�m �r�nlerin toplam mal de�eri.
SELECT SUM(Products.UnitsInStock*Products.UnitPrice) AS TOPLAMTUTAR FROM Products;

 SELECT * FROM Categories;
 SELECT * FROM Products;

 -- Hangi m��teri ka� adet sipari� verdi?(Her m��teri i�in sipari� adedi.)  -- Bu sorguya CompanyName ve City bilgileri eklenin.
 SELECT COUNT(Orders.OrderID) as [Sipari� Adedi],Orders.CustomerID,Customers.CompanyName,Customers.City FROM Orders
 INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID
 GROUP BY Orders.CustomerID,Customers.CompanyName,Customers.City;

 -- London'daki hangi m��teri ne kadar sipari� verdi?
  SELECT COUNT(Orders.OrderID) as [Sipari� Adedi],Orders.CustomerID,Customers.CompanyName,Customers.City FROM Orders
 INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID
 GROUP BY Orders.CustomerID,Customers.CompanyName,Customers.City
 HAVING Customers.City='London';

 -- Her sipari�e ait a�a��daki bilgileri �eken sorgu.
 -- (OrderID, CustomerID,City)
 -- C1: Hangi bilgi hangi tabloda.
 --  	(Orders.OrderID,Orders.CustomerID,Customers.City)
 -- C2: Bu iki tablo hangi kolonlar� ile ili�kili.?
 --     (Orders.CustomerID = Customers.CustomerID)
 SELECT Orders.OrderID,Orders.CustomerID,Customers.City FROM Orders
 INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;


 -- Hangi �ehirden ka� sipari� gelmi�.
  SELECT COUNT(Orders.OrderID),Customers.City FROM Orders
 INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
 GROUP BY Customers.City;

 -- Her sipari�in toplam tutar�n� hesaplay�n?
 -- C1: Benden istenen bilgileri hangi tablolarda?
 --     (OD.OrderID, OD.UnitPrice*OD.Quantity)
 SELECT OD.OrderID, OD.UnitPrice,OD.Quantity FROM [Order Details] OD; -- Ad�m1
 SELECT OD.OrderID,OD.ProductID, (OD.UnitPrice*OD.Quantity) AS UrunToplam FROM [Order Details] OD; -- Ad�m2
 
 
 SELECT OD.OrderID, SUM(OD.UnitPrice*OD.Quantity) AS UrunToplam FROM [Order Details] OD 
 GROUP BY OD.OrderID;								-- Ad�m3
 -- Her m��terinin toplam sipari� tutar�.

 ALTER VIEW MusteriTutar AS -- Ad�m 4
 SELECT OD.OrderID, SUM(OD.UnitPrice*OD.Quantity) AS UrunTutar,O.CustomerID FROM [Order Details] OD
 INNER JOIN Orders O ON OD.OrderID = O.OrderID
 GROUP BY OD.OrderID,O.CustomerID;

 SELECT SUM(UrunTutar), CustomerID FROM MusteriTutar GROUP BY CustomerID; -- Ad�m 5



 -- Hangi sipari�te ka� farkl� �r�n var?
   SELECT * FROM [Order Details];
   SELECT COUNT(*) AS Farkl�UrunAdedi,OrderID FROM [Order Details]
   GROUP BY OrderID;

 -- Her sipari�teki toplam urun adedi hesaplayan sorgu?
    --C1: istenilen bilgiler neler(OrderID ve Quantity)_> Order Details
	--C2: Her OrderID i�in SUM(Quantity)
	SELECT OD.OrderID, SUM(OD.Quantity) FROM [Order Details] OD
	GROUP BY OD.OrderID;

-- Her bir �r�nden ka� adet sipari� verilmi�?
-- C1: ProductID/ProdudctName Order.Quantity -> Urune g�re toplam�.
	SELECT OD.ProductID,SUM(OD.Quantity) AS SiparisMiktari FROM [Order Details] OD
	GROUP BY OD.ProductID;
	-- isim ile.
	SELECT P.ProductName,SUM(OD.Quantity) AS SiparisMiktari FROM [Order Details] OD
	INNER JOIN Products P ON OD.ProductID = P.ProductID 
	GROUP BY P.ProductName;

	-- Bir sipari�teki ortalama kalem say�s�
	-- Her m��terinin sipari�teki ortalama �r�n adedi.



	SELECT AVG(OD.Quantity),OD.OrderID FROM [Order Details] OD
	GROUP BY OD.OrderID; -- T�m�n�n ortalamas�.
	SELECT * FROM [Order Details];

	-- 


	--M��teri ba��na 10 dan fazla sipari�i olan m��teriler(CompanyName) ve sipari� adetleri; 

	SELECT COUNT(Orders.OrderID) AS Adet,Customers.CompanyName FROM Orders
	INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
	GROUP BY Customers.CompanyName
	HAVING COUNT(Orders.OrderID)>10 ORDER BY Adet;

	SELECT * FROM ORders;
	-- ShipVia'ya g�re hangisinin ne kadar �cret toplam� oldu�unu bulun. (ShipVia 3'teki toplam Freight XX'tir.)
	SELECT SUM(Orders.Freight) AS ToplamUcret FROM Orders
	GROUP BY Orders.ShipVia;


















 SELECT TOP 10 * FROM [Order Details];
 SELECT * FROM Orders ORDER BY CustomerID;

 SELECT * FROM Orders;

 SELECT * FROM Products;

 SELECT * FROM Orders;
 SELECT * FROM Customers;




