import java.sql.*;
import java.util.ArrayList;
import java.util.List;

import javax.naming.spi.DirStateFactory.Result;
public class Kategori {
	private int _ID;
	private String _Ad;
	private int _Sayac;
	
	public String getAd()
	{
		return this._Ad;
	}
	public void setAd(String ad)
	{
		this._Ad = ad;
	}
	public int getSayac()
	{
		return this._Sayac;
	}
	public void setSayac(int sayac)
	{
		this._Sayac = sayac;
	}
	public int getID()
	{
		return this._ID;
	}
	public boolean Kaydet()
	{
		Veritabani vt = new Veritabani();
		Connection con = vt.Baglan();
		
		try
		{
			String sorgu = String.format("INSERT INTO Kategori (Ad) VALUES('%s');", this._Ad);
			//Statement durum = con.createStatement();
			
			PreparedStatement durum = con.prepareStatement(sorgu,Statement.RETURN_GENERATED_KEYS);
			// vt'de otomatik olarak olu�turulan kolonlar�n listesini getirir.
			
			//durum.execute(sorgu);
			durum.execute();
			
			ResultSet rs = durum.getGeneratedKeys();
			// Sorgu i�lendikten sonra otomatik olarak ol�turulan ID de�erini listede d�nd�r�r.
			
			if(rs.next())
			{
				this._ID = rs.getInt(1);
			}		
			
			System.out.println("Kay�t ba�ar�l�.");
			vt.Kapat(con);
			return true;
		}
		catch(Exception e)
		{
			System.out.println("Kay�t ba�ar�s�z !!!");
			vt.Kapat(con);
			return false;
		}
		
			
	}
	
	public static Kategori getKategori(int id)
	{
		Veritabani vt = new Veritabani();
		Connection con = vt.Baglan();
		Kategori bulunan = new Kategori();
		
		String sorgu = String.format("SELECT ID,Ad,Sayac FROM Kategori WHERE ID='%s';",id);
		try {
			Statement durum = con.createStatement();
			ResultSet tablo = durum.executeQuery(sorgu);
			while(tablo.next())
			{
				bulunan._ID = tablo.getInt("ID");
				bulunan._Ad = tablo.getString("Ad");
				bulunan._Sayac = tablo.getInt("Sayac");
			}
			vt.Kapat(con);
			return bulunan;
		}
		catch(Exception e)
		{
			vt.Kapat(con);
			System.out.println("Arama yap�lamad�!!"+e.getMessage());
			//e.getMessage() hatan�n detay�n� ekrana yazd�r�r.
			return bulunan;
		}
		
		
		
	}

	public boolean Guncelle()
	{
		Veritabani vt = new Veritabani();
		Connection con = vt.Baglan();
		try
		{
			String sorgu = String.format("UPDATE Kategori SET Ad='%s' WHERE ID='%s' ; ", this._Ad,this._ID);
			Statement durum = con.createStatement();
			durum.execute(sorgu);
			System.out.println("G�ncelleme ba�ar�l�");
			vt.Kapat(con);
			return true;
		}
		catch(Exception e)
		{
			System.out.println("G�ncelleme ba�ar�s�z !!"+e.getMessage());
			vt.Kapat(con);
			return false;
		}
	}

	public boolean Sil()
	{
		Veritabani vt = new Veritabani();
		Connection con = vt.Baglan();
		try
		{
			String sorgu = String.format("DELETE FROM Kategori WHERE ID=%s ; ",this._ID);
			Statement durum = con.createStatement();
			durum.execute(sorgu);
			System.out.println("Silme ba�ar�l�");
			vt.Kapat(con);
			return true;
		}
		catch(Exception e)
		{
			System.out.println("Silme ba�ar�s�z !!"+e.getMessage());
			vt.Kapat(con);
			return false;
		}
	}

	public static List<Kategori> getKategoriListe()
	{
		List<Kategori> kategoriler = new ArrayList<Kategori>();
		Veritabani vt = new Veritabani();
		Connection con = vt.Baglan();
		String sorgu = String.format("SELECT * FROM Kategori;");
		try 
		{
			Statement durum = con.createStatement();
			ResultSet tablo = durum.executeQuery(sorgu);
			while(tablo.next())
			{
				Kategori gecici = new Kategori();
				gecici._ID = tablo.getInt("ID");
				gecici._Ad = tablo.getString("Ad");
				gecici._Sayac = tablo.getInt("Sayac");
				kategoriler.add(gecici);
			}
			vt.Kapat(con);
			return kategoriler;
		}
		catch(Exception e)
		{
			vt.Kapat(con);
			System.out.println("Liste getirilemedi!!"+e.getMessage());
			return kategoriler;
		}
	}
}
