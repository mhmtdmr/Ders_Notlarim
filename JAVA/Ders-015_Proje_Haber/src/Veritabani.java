import java.sql.*;

public class Veritabani {
	public Connection baglanti = null;
	private String _dburl;
	private String _dbuser;
	private String _dbpass;
	
	// Yapýcý metot ile ilk deðer atamasý.
	public Veritabani()
	{
		this._dburl = "jdbc:sqlserver://127.0.0.1;database=HABER";
		this._dbuser = "sa";
		this._dbpass = "1234";
	}
	public Connection Baglan()
	{
		try {
			this.baglanti = DriverManager.getConnection(this._dburl,this._dbuser,this._dbpass);
			System.out.println("Baðlantý baþarýlý :) ");
			return baglanti;
		}
		catch(Exception e)
		{
			System.out.println("Baðlantý baþarýsýz !!!");
			return baglanti;
		}
	}
	
	public void Kapat(Connection con)
	{
		try {
			if(con != null && !con.isClosed())
			{
				System.out.println("Baðlantý kapatýldý.");
				con.close();
			}
		}
		catch(Exception e)
		{
			System.out.println("Baðlantý kapatýlamadý !");
		}
	}
	
}
