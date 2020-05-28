package Polimorfizm;

public class Polimorfizm {

	public static void main(String[] args) {
		/*
		 * AltSinif test = new AltSinif(); test.MerhabaDunya();
		 * 
		 * int i1 = 15; int i2 = 17; test.Topla(i1, i2); double d1 = 45.4D; double d2 =
		 * 15; test.Topla(d1, d2);
		 */
		AltSinif altsinif = new AltSinif();
		AnaSinif anasinif = new AnaSinif();
		Merhaba(altsinif);
		Merhaba(anasinif);

	}

	// Polimorfizm: Tek bir isimle her nesne kendi sýnýfýna ait metodu çalýþtýrýr.
	// Çok biçimlilik.
	public static void Merhaba(AnaSinif nesne) {
		nesne.MerhabaDunya();
	}

}
