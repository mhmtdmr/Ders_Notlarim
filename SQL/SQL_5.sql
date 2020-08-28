-- View: Sanal tablolar veritabanýnda toplu olarak tutulmas. Çaðýrýldýklarýnda veri anlýk olarak oluþturulur.
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

--Orders tablosunda USA'a gönderilen sipariþlerin IrderID,CustomerID ve Employee Name ve Surname
-- Yukarýdaki verileri VIEW olusturarak çýkarýnýz.

--CREATE VIEW OrdersUSA AS
--SELECT Employees.FirstName,Employees.LastName,Orders.OrderID,Orders.CustomerID,Orders.ShipCountry FROM Orders
--INNER JOIN Employees ON Employees.EmployeeID = Orders.EmployeeID
--WHERE ShipCountry='USA';

--Select * From OrdersUSA;


-- GROUP BY --

-- Hangi ülkeden kaç müþterim var?
--SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country;

--SELECT * FROM Customers;

SELECT COUNT(*) FROM Customers;

-- Toplam müþteri sayýsý 5'ten fazla olan ülkeleri, müþteri sayýlarý ile birlikte listele

SELECT COUNT(CustomerID), Country FROM  Customers GROUP BY Country HAVING COUNT(CustomerID)>5;

SELECT COUNT(*) FROM Customers;
SELECT COUNT(Region) FROM Customers; -- NULL hücre COUNT'ta sayýlmýyor.

-- Products : Hangi kategoriden kaç ürün var?
SELECT * FROM Products;
SELECT COUNT(ProductID) AS Miktar, CategoryID FROM Products GROUP BY CategoryID;

SELECT COUNT(*) FROM Products WHERE CategoryID IS NULL;

-----------------

SELECT COUNT(*) FROM Customers;

SELECT (CAST(13 AS FLOAT)/CAST(91 AS FLOAT))*100;

-- Hüseyin'in sorduðu soru.
SELECT CAST((CAST(COUNT(*) AS FLOAT)/CAST((SELECT COUNT(*) FROM Customers)AS FLOAT))*100 AS FLOAT) AS Oran
, Country FROM Customers GROUP BY Country ORDER BY Country;

-- Hangi kategoride toplam ne kadar stok var? (Products)
-- 
SELECT SUM(Products.UnitsInStock),Categories.CategoryName FROM Categories INNER JOIN Products ON Products.CategoryID = Categories.CategoryID
Group By Categories.CategoryName;

-- Her kategorideki ürünlerin toplam mal deðeri nedir?
SELECT SUM(Products.UnitsInStock*Products.UnitPrice),Categories.CategoryName FROM Categories 
INNER JOIN Products ON Products.CategoryID = Categories.CategoryID
Group By Categories.CategoryName;

-- Tüm ürünlerin toplam mal deðeri.
SELECT SUM(Products.UnitsInStock*Products.UnitPrice) AS TOPLAMTUTAR FROM Products;

 SELECT * FROM Categories;
 SELECT * FROM Products;

 -- Hangi müþteri kaç adet sipariþ verdi?(Her müþteri için sipariþ adedi.)  -- Bu sorguya CompanyName ve City bilgileri eklenin.
 SELECT COUNT(Orders.OrderID) as [Sipariþ Adedi],Orders.CustomerID,Customers.CompanyName,Customers.City FROM Orders
 INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID
 GROUP BY Orders.CustomerID,Customers.CompanyName,Customers.City;

 -- London'daki hangi müþteri ne kadar sipariþ verdi?
  SELECT COUNT(Orders.OrderID) as [Sipariþ Adedi],Orders.CustomerID,Customers.CompanyName,Customers.City FROM Orders
 INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID
 GROUP BY Orders.CustomerID,Customers.CompanyName,Customers.City
 HAVING Customers.City='London';

 -- Her sipariþe ait aþaðýdaki bilgileri çeken sorgu.
 -- (OrderID, CustomerID,City)
 -- C1: Hangi bilgi hangi tabloda.
 --  	(Orders.OrderID,Orders.CustomerID,Customers.City)
 -- C2: Bu iki tablo hangi kolonlarý ile iliþkili.?
 --     (Orders.CustomerID = Customers.CustomerID)
 SELECT Orders.OrderID,Orders.CustomerID,Customers.City FROM Orders
 INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;


 -- Hangi þehirden kaç sipariþ gelmiþ.
  SELECT COUNT(Orders.OrderID),Customers.City FROM Orders
 INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
 GROUP BY Customers.City;

 -- Her sipariþin toplam tutarýný hesaplayýn?
 -- C1: Benden istenen bilgileri hangi tablolarda?
 --     (OD.OrderID, OD.UnitPrice*OD.Quantity)
 SELECT OD.OrderID, OD.UnitPrice,OD.Quantity FROM [Order Details] OD; -- Adým1
 SELECT OD.OrderID,OD.ProductID, (OD.UnitPrice*OD.Quantity) AS UrunToplam FROM [Order Details] OD; -- Adým2
 
 
 SELECT OD.OrderID, SUM(OD.UnitPrice*OD.Quantity) AS UrunToplam FROM [Order Details] OD 
 GROUP BY OD.OrderID;								-- Adým3
 -- Her müþterinin toplam sipariþ tutarý.

 ALTER VIEW MusteriTutar AS -- Adým 4
 SELECT OD.OrderID, SUM(OD.UnitPrice*OD.Quantity) AS UrunTutar,O.CustomerID FROM [Order Details] OD
 INNER JOIN Orders O ON OD.OrderID = O.OrderID
 GROUP BY OD.OrderID,O.CustomerID;

 SELECT SUM(UrunTutar), CustomerID FROM MusteriTutar GROUP BY CustomerID; -- Adým 5



 -- Hangi sipariþte kaç farklý ürün var?
   SELECT * FROM [Order Details];
   SELECT COUNT(*) AS FarklýUrunAdedi,OrderID FROM [Order Details]
   GROUP BY OrderID;

 -- Her sipariþteki toplam urun adedi hesaplayan sorgu?
    --C1: istenilen bilgiler neler(OrderID ve Quantity)_> Order Details
	--C2: Her OrderID için SUM(Quantity)
	SELECT OD.OrderID, SUM(OD.Quantity) FROM [Order Details] OD
	GROUP BY OD.OrderID;

-- Her bir üründen kaç adet sipariþ verilmiþ?
-- C1: ProductID/ProdudctName Order.Quantity -> Urune göre toplamý.
	SELECT OD.ProductID,SUM(OD.Quantity) AS SiparisMiktari FROM [Order Details] OD
	GROUP BY OD.ProductID;
	-- isim ile.
	SELECT P.ProductName,SUM(OD.Quantity) AS SiparisMiktari FROM [Order Details] OD
	INNER JOIN Products P ON OD.ProductID = P.ProductID 
	GROUP BY P.ProductName;

	-- Bir sipariþteki ortalama kalem sayýsý
	-- Her müþterinin sipariþteki ortalama ürün adedi.



	SELECT AVG(OD.Quantity),OD.OrderID FROM [Order Details] OD
	GROUP BY OD.OrderID; -- Tümünün ortalamasý.
	SELECT * FROM [Order Details];

	-- 


	--Müþteri baþýna 10 dan fazla sipariþi olan müþteriler(CompanyName) ve sipariþ adetleri; 

	SELECT COUNT(Orders.OrderID) AS Adet,Customers.CompanyName FROM Orders
	INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
	GROUP BY Customers.CompanyName
	HAVING COUNT(Orders.OrderID)>10 ORDER BY Adet;

	SELECT * FROM ORders;
	-- ShipVia'ya göre hangisinin ne kadar ücret toplamý olduðunu bulun. (ShipVia 3'teki toplam Freight XX'tir.)
	SELECT SUM(Orders.Freight) AS ToplamUcret FROM Orders
	GROUP BY Orders.ShipVia;


















 SELECT TOP 10 * FROM [Order Details];
 SELECT * FROM Orders ORDER BY CustomerID;

 SELECT * FROM Orders;

 SELECT * FROM Products;

 SELECT * FROM Orders;
 SELECT * FROM Customers;




