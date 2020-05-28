public class Emlak 
{
	String ID;
	short MetreKare;
	String IlanTipi;
	short BinaYasi;
	String OdaSayisi;
	boolean EsyaliMi;
	double Fiyat;
	double Aidat;
	
	Kullanici kullanici; // Emlak nesnelerinin bir kullan�c� nesnesi olmal�d�r.
	
	// Yap�c�(Constructor) Metot: Runtime'da otomatik olu�turulur. Ve otomatik �al��t�r�l�r.
	// public Emlak(){....}   : G�revi: S�n�f niteliklerinin varsay�lan de�erlerini atamak.
	// S�n�f niteliklerine belirli de�erleri otomatik atama yapt�rabiliriz.
	// Parametresiz Yap�c� Metot
	public Emlak()
	{
		EsyaliMi = false;
		Aidat = 0;
		System.out.println("Yap�c� metot otomatik �al���r.");
	}
	// Parametreli Yap�c� Metot
	public Emlak(String ID,short metrekare, String ilanTipi,short binaYasi,String odaSayisi,boolean esyaliMi,double fiyat, double aidat)
	{
		this.ID = ID;
		this.MetreKare = metrekare;
		this.IlanTipi = ilanTipi;
		this.BinaYasi = binaYasi;
		this.OdaSayisi = odaSayisi;
		this.EsyaliMi = esyaliMi;
		this.Fiyat = fiyat;
		this.Aidat = aidat;
		System.out.println("Parametreli yap�c� metot �al��t�.");
	}
	
	
	void Yayinla()
	{
		System.out.println("Ilan yay�nland�...");
	}
}
