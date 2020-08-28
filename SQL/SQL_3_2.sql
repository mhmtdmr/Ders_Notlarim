INSERT INTO Dersler (Ad,ToplamSaat) VALUES('Muhasebe',48);
INSERT INTO Dersler (Ad,ToplamSaat) VALUES('Excel',48);
INSERT INTO Dersler (Ad,ToplamSaat) VALUES('Adobe Photoshop',75);
INSERT INTO Dersler (Ad,ToplamSaat) VALUES('Ýleri Excel',48);

INSERT INTO Siniflar (Ad,Kapasite,Kat) VALUES ('105',16,1);
INSERT INTO Siniflar (Ad,Kapasite,Kat) VALUES ('104',20,1);
INSERT INTO Siniflar (Ad,Kapasite,Kat) VALUES ('106',24,1);

INSERT INTO Ogretmenler (Ad,Soyad,TC,Telefon,Eposta) 
VALUES ('Ahmet','Necip','98765432155','+905467891233','anecip@necip.com');
INSERT INTO Ogretmenler (Ad,Soyad,TC,Telefon,Eposta) 
VALUES ('Mehmet','Necip','98765542155','+905467822233','mnecip@necip.com');

INSERT INTO Ogretmenler (Ad,Soyad,TC,Telefon,Eposta) 
VALUES ('Necla','SARI','98365542155','+905467832233','necala@gmail.com');




INSERT INTO Danismanlar (Ad,Soyad) VALUES('Gözde','Karaca');
INSERT INTO Danismanlar (Ad,Soyad) VALUES('Selvi','Merdan');
INSERT INTO Danismanlar (Ad,Soyad) VALUES('Talha','Akbora');

INSERT INTO Ogrenciler (Ad,Soyad) Values ('Sercan','YILMAZ');
INSERT INTO Ogrenciler (Ad,Soyad) Values ('Celil','Tiryaki');
INSERT INTO Ogrenciler (Ad,Soyad) Values ('Sýdýka','Karaca');

INSERT INTO Egitim (Ders_ID,Ogretmen_ID,Sinif_ID,Tarih,SaatAralik)
VALUES(2,1,2,'2019-12-30','10:00-13:00');

INSERT INTO Egitim (Ders_ID,Ogretmen_ID,Sinif_ID,Tarih,SaatAralik)
VALUES(2,1,1,'2019-12-23','16:00-19:00');

INSERT INTO Egitim (Ders_ID,Ogretmen_ID,Sinif_ID,Tarih,SaatAralik)
VALUES(1,2,3,'2019-12-30','10:00-13:00');

INSERT INTO OgrenciEgitim (Ogrenci_ID,Egitim_ID,Danisman_ID)
VALUES (3,1,1);

INSERT INTO OgrenciEgitim (Ogrenci_ID,Egitim_ID,Danisman_ID)
VALUES (2,2,2);



SELECT * FROM OgrenciEgitim;
SELECT * FROM Egitim;
-- (OgrenciEgitim tablosu ile Ogrenciler tablosu arasýndaki kesiþim bilgilerini getirir.)Eðitim Alan Öðrenciler.
SELECT Ogrenciler.Ad, Ogrenciler.Soyad FROM OgrenciEgitim
INNER JOIN Ogrenciler ON OgrenciEgitim.Ogrenci_ID = Ogrenciler.ID;

-- (OgrenciEgitim tablosu ile Ogrenciler tablosu arasýndaki kesiþim bilgilerini getirir.)
-- Eðitim Alan Öðrenciler ve Danýþmanlarýnýn Bilgilerini Getir.
SELECT Ogrenciler.Ad, Ogrenciler.Soyad, Danismanlar.Ad AS 'Danýþman Adý',Danismanlar.Soyad AS 'Danýþman Soyadý'
FROM OgrenciEgitim
INNER JOIN Ogrenciler ON OgrenciEgitim.Ogrenci_ID = Ogrenciler.ID
INNER JOIN Danismanlar ON OgrenciEgitim.Danisman_ID = Danismanlar.ID;

--  Egitim tablosundaki kayýtlara ait Öðretmen Ad,Soyad ve Sýnýf Ad bilgilerini Egitim Tarih bilgisi
--  ile birlikte listeleyin. (Sorudaki kýsmý yapanlar Ders Ad ý bilgisini listeleyebilir.)

--  Devamýnda 30.12.2019 tarihindeki eðitimlere ait yukarýdaki bilgileri listeleyin


SELECT Ogretmenler.Ad,Ogretmenler.Soyad ,Siniflar.Ad AS 'Sýnýf Adý',Egitim.Tarih FROM Egitim
INNER JOIN Ogretmenler ON Egitim.Ogretmen_ID = Ogretmenler.ID
INNER JOIN Siniflar ON Egitim.Sinif_ID = Siniflar.ID
WHERE Egitim.Tarih = '2019-12-30';

SELECT * FROM Ogrenciler;
SELECT * FROM Ogretmenler;
SELECT * FROM Dersler;
SELECT * FROM Danismanlar;
select * from Siniflar;
SELECT * FROM Egitim;
SELECT * FROM OgrenciEgitim;

-- SORU: Eðitim tablosundaki verilerin Ogretmenlerini listeleyen sorgu: 
-- Aktif olarak egitim veren öðretmen Ad ve Soyadlarý

SELECT Ogretmenler.Ad,Ogretmenler.Soyad, Egitim.Tarih FROM Egitim
INNER JOIN Ogretmenler ON Ogretmenler.ID = Egitim.Ogretmen_ID;

SELECT Ogretmenler.Ad,Ogretmenler.Soyad, Egitim.Tarih FROM Egitim
,Ogretmenler WHERE Ogretmenler.ID = Egitim.Ogretmen_ID;

SELECT * FROM Egitim;
SELECT * FROM Ogretmenler;

-- LEFT JOIN (FROM'dan sonra ve ON'dan sonra yazdýðýmýz tablo adý SOLDAKÝ'dir.)
-- Tüm eðitimleri listele. Ve eðitim tablosunda bulunan öðretmenleri listeleyen sorgu.
SELECT Egitim.ID AS EgitimNumarasý,Ogretmenler.Ad,Ogretmenler.Soyad,Egitim.Tarih FROM Egitim
LEFT JOIN Ogretmenler ON Egitim.Ogretmen_ID = Ogretmenler.ID;
















-- SORU: 2 ID'li öðrencilerin aldýðý eðitimlere ait. Öðretmen, Sýnýf ve SaatAralik bilgisini listeleyin.

SELECT Ogretmenler.Ad AS 'Öðretmen Adý', Ogretmenler.Soyad AS 'Ogretmen SOyadý', Siniflar.Ad, Egitim.SaatAralik FROM Egitim
INNER JOIN Ogretmenler ON Egitim.Ogretmen_ID = Ogretmenler.ID
INNER JOIN Siniflar ON Egitim.Sinif_ID = Siniflar.ID
INNER JOIN OgrenciEgitim ON Egitim.ID = OgrenciEgitim.Egitim_ID
WHERE OgrenciEgitim.Ogrenci_ID = 2;