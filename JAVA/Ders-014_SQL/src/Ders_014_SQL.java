import java.sql.*;
import java.util.Scanner;
public class Ders_014_SQL{
	static Connection con = null;

	public static void main(String[] args) {

		VeriTabaniBaglantiAc();
		//OgrenciEkle();
		//OgrenciGuncelle("Utku Sabahaddin","Koçlar",4);
		//OgrenciSil(3);
		OgrenciListele();
		VeriTabaniBaglantiKapat();
	}
	private static void OgrenciListele() {
		String sorgu = "SELECT * FROM Ogrenci;";
		try {
			Statement durum = con.createStatement();
			ResultSet tablo = durum.executeQuery(sorgu);
			while (tablo.next())
			{
				System.out.println(tablo.getString("ad")+" - "+tablo.getString("soyad"));
			}
		} catch (SQLException e) {
			System.out.println("Sorgu çalýþtýrýlýrke bir hata oluþtu.");
		}
		
	}
	private static void OgrenciSil(int id) {
		String sorgu = String.format("DELETE FROM Ogrenci WHERE ID=%s", id);
		Statement durum;
		try {
			durum = con.createStatement();
			durum.execute(sorgu);
		} catch (SQLException e) {
			System.out.println("Silme sýrasýnda bir hata oluþtu.");
			System.out.println(e.getMessage());
		}
		System.out.println("Kayýt baþarý ile silindi.");
	}
	private static void OgrenciGuncelle(String guncelad, String guncelsoyad, int id) {
		String sorgu = String.format("UPDATE Ogrenci SET ad='%s', soyad='%s' WHERE ID=%s;",guncelad,guncelsoyad,id);
		Statement durum;
		try {
			durum = con.createStatement();
			durum.execute(sorgu);
		} catch (SQLException e) {
			System.out.println("Güncelleme sýrasýnda bir hata oluþtu.");
			System.out.println(e.getMessage());
		}
		System.out.println("Kayýt baþarý ile güncellendi.");
	}
	private static void VeriTabaniBaglantiKapat() {
		try {
			if(con != null && !con.isClosed())
				con.close();
		} catch (SQLException e) {
			System.out.println("Baðlantý kapatýlýrken bir hata oluþtu.");
		}
	}
	public static void VeriTabaniBaglantiAc()
	{

		String dburl = "jdbc:sqlserver://127.0.0.1;database=Kurs;";
		String user = "sa";
		String pass = "1234";
		try {
			con = DriverManager.getConnection(dburl,user,pass);
		} catch (SQLException e) {
			System.out.println("Veri tabaný baðlantýsý saðlanamadý!!!");
			System.out.println(e.getMessage());
		}
	}
	public static void OgrenciEkle()
	{

		Scanner input = new Scanner(System.in);
		//String sorgu = "INSERT INTO Ogrenci (ad,soyad,dogumtarihi) VALUES('Özkan','YILMAZ','1980.01.01');";
		try 
		{   // SORU: Klavyeden alýnan ad soyad doðum tarihi bilgisini veritabanýna kaydediniz.
			System.out.print("Ad:");
			String ad = input.next();
			System.out.print("Soyad:");
			String soyad = input.next();
			System.out.print("Doðum Tarihi:");
			String dogumtarihi = input.next();
			//String sorgu = "INSERT INTO Ogrenci (ad,soyad,dogumtarihi) VALUES('"+ad+"','"+soyad+"','"+dogumtarihi+"');";
			String sorgu = String.format("INSERT INTO Ogrenci (ad,soyad,dogumtarihi) VALUES('%s','%s','%s');",ad,soyad,dogumtarihi); 
			Statement durum = con.createStatement();
			durum.execute(sorgu);
			System.out.println("Kayýt baþarý ile gerçekleþti.");
		}
		catch(Exception e)
		{
			System.out.println(e.getMessage());
			System.out.println("Hata Oluþtu");
		}
		finally
		{
			System.out.println("finally Her durumda çalýþýr");
		}
	}

}
