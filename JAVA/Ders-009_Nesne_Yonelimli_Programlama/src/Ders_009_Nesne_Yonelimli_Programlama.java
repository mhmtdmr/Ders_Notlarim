
public class Ders_009_Nesne_Yonelimli_Programlama {

	public static void main(String[] args) {

		// Monitor sınıfından bir nesne tanımladık.
		/*
		 * Monitor m1 = new Monitor(); m1.Marka = "Toshiba"; m1.Model = "TM450";
		 * m1.Fiyat = 750.50D; m1.Boyut = 20;
		 */

		// Monitor sınıfından bir nesne tanımladık.
		/*
		 * Monitor m2 = new Monitor(); m2.Boyut = 19; m2.Fiyat = 600D; m2.Marka =
		 * "Samsung"; m2.Model = "SM3412";
		 */

		// Nesneler için Monitor sınıfının metodunu çağırdık.
		// metot static olmadığı için nesne üzerinden çağırıdk.(m1.)
		// m1.BilgiListele();
		// m2.BilgiListele();
		// m2.KDVliFiyatYaz();

		// static olarak tanımladığımız için nesnesiz çağırabildik.
		// (Monitor)
		// Monitor.BilgiListele(m1);

		// Hiç nesne tanımlamamış olsak bile static olan aşağıdaki metoda ulaşabiliriz.
		// Monitor.KDVOranYaz();

		// Bilgisayar Sınıfı
		/*
		 * Bilgisayar Pc1 = new Bilgisayar(); Pc1.Fiyat = 4500D; double indirimliFİyat =
		 * Pc1.IndirimHesapla(10); System.out.println(indirimliFİyat);
		 */
		Bilgisayar Pc2 = new Bilgisayar(7000D, 3.6D, (byte) 32);
		System.out.println(Pc2.Fiyat);
		System.out.println(Pc2.IndirimHesapla(25));

		Pc2.FiyatKarsilastir(7000D);

	}

}

//Aşağıdaki Monitor sınıfına KDVliFiyatYaz() isimli metotu tanımlayın. Fiyata %18 KDV ekleyip ekrana yazdıracak.
//Monitor sınıfını tanımladık.
class Monitor {
	String Marka; // ""
	String Model; // ""
	double Fiyat; // 1.0D
	int Boyut; // 1

	void BilgiListele() {
		System.out.println("Monitörün markası: " + Marka);
		System.out.println("Monitörün modeli: " + Model);
		System.out.println("Monitörün fiyatı: " + Fiyat);
		System.out.println("Monitörün boyutu: " + Boyut);
	}

	// Kafanız karışmasın nesnesiz kullanıma örnek olarak bu metodu static
	// tanımladık.
	static void BilgiListele(Monitor monitorNesnesi) {
		System.out.println("Monitörün markası: " + monitorNesnesi.Marka);
		System.out.println("Monitörün modeli: " + monitorNesnesi.Model);
		System.out.println("Monitörün fiyatı: " + monitorNesnesi.Fiyat);
		System.out.println("Monitörün boyutu: " + monitorNesnesi.Boyut);
	}

	static void KDVOranYaz() {
		System.out.println("Monitörlerde KDV %18'dir.");
	}

	void KDVliFiyatYaz() {
		double KDVliFiyat = ((Fiyat * 18) / 100) + Fiyat;
		System.out.println("Ürünün KDV'li Fiyatı: " + KDVliFiyat);
	}
}

//Bilgisayar isminde bir sınıf tanımlayın.
/*
 * Özellikleri:
 * CPUModel,CPUHiz,RAM,HDDKapasite,SSDKapasite,GPUModel,GPUBellek,Renk,
 * BluetoothVarMi, WifiVarMi,Fiyat Metotları: KDVHesapla(),
 * IndirimHesapla(double oran): Parametre olarak gönderilen oranda indirim yapıp
 * indirimli fiyatı döndürsün.
 * 
 */
class Bilgisayar {
	String CPUModel;
	double CPUHiz;
	byte RAM;
	int SSDKapasite;
	String GPUModel;
	byte GPUBellek;
	String Renk;
	boolean BluetoothVarMi;
	boolean WifiVarMi;
	double Fiyat;

	// Constructor - Yapıcı metodun dönüş tipi olmaz.! Sınıf ile aynı isimde
	// olmalıdır!!!
	Bilgisayar() {
		System.out.println("Bilgisayar sınıfından bir nesne oluşturuldu.\nParametresiz yapıcı metot çalıştı.");
	}

	Bilgisayar(double fiyat, double cpuHiz, byte ram) {
		this.Fiyat = fiyat;
		CPUHiz = cpuHiz;
		RAM = ram;
		System.out.println("Parametreli yapıcı metot çalıştı. 3 niteliğe değer atanarak nesne oluşturuldu.");
	}

	void KDVHesapla() {
		double KDVliFiyat = ((Fiyat * 18) / 100) + Fiyat;
		System.out.println("Ürünün KDV'li Fiyatı: " + KDVliFiyat);
	}

	double IndirimHesapla(double indirimOrani) {
		double indirimliFiyat = Fiyat - ((Fiyat * indirimOrani) / 100);
		return indirimliFiyat;
	}

	void FiyatKarsilastir(double Fiyat) {
		// this ile sınıfa ait niteliğe ulaştık.
		if (this.Fiyat > Fiyat)
			System.out.println("Gönderdiğiniz fiyatdan pahalı.");
		else if (this.Fiyat < Fiyat)
			System.out.println("Gönderdiğiniz fiyatdan ucuz.");
		else
			System.out.println("Gönderdiğiniz fiyat ile aynı.");
	}
}

/*
 * SORU: Otomobil sınıfı: Özellikleri:
 * Marka,Model,MotorHacmi,VitesTipi,KasaTipi,Renk,UretimYili,Klima,KM,Fiyat Tüm
 * parametrelerin verilerek nesne oluşturulabilmesi için yapıcı metodu
 * tanımlayınız.
 * 
 */
