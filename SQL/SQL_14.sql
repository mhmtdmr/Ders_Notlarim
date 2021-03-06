-- XML ve JSON formatında export işlemi için sorgunun sonuna aşağıdaki 
-- eklemeler yapılarak çıkan dosya linkine tıklanır.
-- Açılan formatlı dosya aktarımın türüne göre .xml veya .json uzantısı
-- ile kaydedilir.s

SELECT * FROM Ders
--FOR JSON AUTO;
--FOR XML PATH('Ders')
--FOR XML PATH
--FOR XML AUTO



--> ANLIK OLARAK OLUŞTURULUR VE SORGU BU Sanal Tablodan Çekilebilir.
WITH AzKalanUrunler AS(
  SELECT Products.ProductName,Products.UnitsInStock, Products.CategoryID
  FROM Products WHERE UnitsInStock<50)
SELECT ProductName,UnitsInStock FROM AzKalanUrunler WHERE CategoryID=2;

-- Orders tablosundaki Fransa siparişlerinin içinde
-- 3 numaralı taşıma şirketi ile taşınacak olan siparişleri listeleyin.
-- WITH kullanarak.
WITH FransaSiparis AS
(SELECT * FROM Orders Where Orders.ShipCountry='France')
SELECT * FROM FransaSiparis WHERE ShipVia=3
-- Arkaplanda çalışılan veriyi kilitlemez. Başka çalışmaları engellemez.
SELECT * FROM Orders WITH (NOLOCK);


-- Hangi Siparişin Toplam Kaç para olduğunu Siparis,Tutar isimli
-- geçici tabloda tutunuz.
-- Daha sonra bunları artan sıralama ile geçici tablodan çekiniz.
-- WITH ile...
DECLARE @WithDenGelen INT;
WITH SiparisTutar AS
(
SELECT OD.OrderID,SUM(OD.UnitPrice * OD.Quantity) as ToplamTutar FROM [Order Details] OD
GROUP BY OD.OrderID
)
SELECT @WithDenGelen = COUNT(*) FROM SiparisTutar;
DECLARE @ODdenGelen INT;
SELECT @ODdenGelen = COUNT(DISTINCT(OrderID)) FROM [Order Details]

IF (@WithDenGelen=@ODdenGelen)
BEGIN
	PRINT('Değerler Aynı')
END
ELSE
BEGIN
	PRINT('Değerler Farklı')
END




