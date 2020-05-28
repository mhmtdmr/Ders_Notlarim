import java.sql.*;
import java.util.Scanner;
public class Ders_014_SQL{
	static Connection con = null;

	public static void main(String[] args) {

		VeriTabaniBaglantiAc();
		//OgrenciEkle();
		//OgrenciGuncelle("Utku Sabahaddin","Ko�lar",4);
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
			System.out.println("Sorgu �al��t�r�l�rke bir hata olu�tu.");
		}
		
	}
	private static void OgrenciSil(int id) {
		String sorgu = String.format("DELETE FROM Ogrenci WHERE ID=%s", id);
		Statement durum;
		try {
			durum = con.createStatement();
			durum.execute(sorgu);
		} catch (SQLException e) {
			System.out.println("Silme s�ras�nda bir hata olu�tu.");
			System.out.println(e.getMessage());
		}
		System.out.println("Kay�t ba�ar� ile silindi.");
	}
	private static void OgrenciGuncelle(String guncelad, String guncelsoyad, int id) {
		String sorgu = String.format("UPDATE Ogrenci SET ad='%s', soyad='%s' WHERE ID=%s;",guncelad,guncelsoyad,id);
		Statement durum;
		try {
			durum = con.createStatement();
			durum.execute(sorgu);
		} catch (SQLException e) {
			System.out.println("G�ncelleme s�ras�nda bir hata olu�tu.");
			System.out.println(e.getMessage());
		}
		System.out.println("Kay�t ba�ar� ile g�ncellendi.");
	}
	private static void VeriTabaniBaglantiKapat() {
		try {
			if(con != null && !con.isClosed())
				con.close();
		} catch (SQLException e) {
			System.out.println("Ba�lant� kapat�l�rken bir hata olu�tu.");
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
			System.out.println("Veri taban� ba�lant�s� sa�lanamad�!!!");
			System.out.println(e.getMessage());
		}
	}
	public static void OgrenciEkle()
	{

		Scanner input = new Scanner(System.in);
		//String sorgu = "INSERT INTO Ogrenci (ad,soyad,dogumtarihi) VALUES('�zkan','YILMAZ','1980.01.01');";
		try 
		{   // SORU: Klavyeden al�nan ad soyad do�um tarihi bilgisini veritaban�na kaydediniz.
			System.out.print("Ad:");
			String ad = input.next();
			System.out.print("Soyad:");
			String soyad = input.next();
			System.out.print("Do�um Tarihi:");
			String dogumtarihi = input.next();
			//String sorgu = "INSERT INTO Ogrenci (ad,soyad,dogumtarihi) VALUES('"+ad+"','"+soyad+"','"+dogumtarihi+"');";
			String sorgu = String.format("INSERT INTO Ogrenci (ad,soyad,dogumtarihi) VALUES('%s','%s','%s');",ad,soyad,dogumtarihi); 
			Statement durum = con.createStatement();
			durum.execute(sorgu);
			System.out.println("Kay�t ba�ar� ile ger�ekle�ti.");
		}
		catch(Exception e)
		{
			System.out.println(e.getMessage());
			System.out.println("Hata Olu�tu");
		}
		finally
		{
			System.out.println("finally Her durumda �al���r");
		}
	}

}
