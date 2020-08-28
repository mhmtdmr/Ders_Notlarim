-- LEFT JOIN (FROM'dan sonra ve ON'dan sonra yazdýðýmýz tablo adý SOLDAKÝ'dir.)
-- Soldakinin tamamýný listele saðdakinde null'lar olabilir.
	SELECT Customers.CompanyName, Orders.OrderID
	FROM Customers
	LEFT JOIN Orders
	ON Customers.CustomerID=Orders.CustomerID
	ORDER BY Customers.CompanyName;
-- Saðdakinin tamamýný listele Soldakinde null'lar olabilir.

	SELECT Customers.CompanyName, Orders.OrderID
	FROM Customers
	RIGHT JOIN Orders
	ON Customers.CustomerID=Orders.CustomerID
	ORDER BY Customers.CompanyName;


-- RIGHT JOIN : (FROM'dan sonra ve ON'dan sonra yazdýðýmýz tablo adý SOLDAKÝ'dir. Diðerleri SAÐDAKÝ.)
--Tüm employee/çalýþanlarý getir. Ýliþkili olduklarý sipariþ ID'sini de getir.
SELECT Orders.OrderID,Employees.LastName,Employees.FirstName FROM Orders
RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
Order BY Orders.OrderID;


-- FULL OUTER JOIN: Ýki tablonun tamamýný listele. Ýliþkilileri ayný satýrda göster.
-- Hem saðda hem solda NULL kayýtlar olabilir.

SELECT Customers.CompanyName, Orders.OrderID
FROM Customers
FULL OUTER JOIN Orders
ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CompanyName;



