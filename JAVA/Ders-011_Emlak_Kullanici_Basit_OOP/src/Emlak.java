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
	
	Kullanici kullanici; // Emlak nesnelerinin bir kullanýcý nesnesi olmalýdýr.
	
	// Yapýcý(Constructor) Metot: Runtime'da otomatik oluþturulur. Ve otomatik çalýþtýrýlýr.
	// public Emlak(){....}   : Görevi: Sýnýf niteliklerinin varsayýlan deðerlerini atamak.
	// Sýnýf niteliklerine belirli deðerleri otomatik atama yaptýrabiliriz.
	// Parametresiz Yapýcý Metot
	public Emlak()
	{
		EsyaliMi = false;
		Aidat = 0;
		System.out.println("Yapýcý metot otomatik çalýþýr.");
	}
	// Parametreli Yapýcý Metot
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
		System.out.println("Parametreli yapýcý metot çalýþtý.");
	}
	
	
	void Yayinla()
	{
		System.out.println("Ilan yayýnlandý...");
	}
}
