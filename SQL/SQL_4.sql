-- LEFT JOIN (FROM'dan sonra ve ON'dan sonra yazd���m�z tablo ad� SOLDAK�'dir.)
-- Soldakinin tamam�n� listele sa�dakinde null'lar olabilir.
	SELECT Customers.CompanyName, Orders.OrderID
	FROM Customers
	LEFT JOIN Orders
	ON Customers.CustomerID=Orders.CustomerID
	ORDER BY Customers.CompanyName;
-- Sa�dakinin tamam�n� listele Soldakinde null'lar olabilir.

	SELECT Customers.CompanyName, Orders.OrderID
	FROM Customers
	RIGHT JOIN Orders
	ON Customers.CustomerID=Orders.CustomerID
	ORDER BY Customers.CompanyName;


-- RIGHT JOIN : (FROM'dan sonra ve ON'dan sonra yazd���m�z tablo ad� SOLDAK�'dir. Di�erleri SA�DAK�.)
--T�m employee/�al��anlar� getir. �li�kili olduklar� sipari� ID'sini de getir.
SELECT Orders.OrderID,Employees.LastName,Employees.FirstName FROM Orders
RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
Order BY Orders.OrderID;


-- FULL OUTER JOIN: �ki tablonun tamam�n� listele. �li�kilileri ayn� sat�rda g�ster.
-- Hem sa�da hem solda NULL kay�tlar olabilir.

SELECT Customers.CompanyName, Orders.OrderID
FROM Customers
FULL OUTER JOIN Orders
ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CompanyName;



