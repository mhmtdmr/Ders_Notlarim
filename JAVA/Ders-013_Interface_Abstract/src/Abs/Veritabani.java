package Abs;

public abstract class Veritabani {
	/* ABSTRACT:
	 * Nesne türetilemez.
	 * Sýnýflardan miras alabilir.
	 * Interface'leri implemente edebilir.
	 * Ýçerisinde abstract veya gövdeli metotlar olabilir.
	 * 
	 */
	public void BaglantiAc()
	{
		System.out.println("Veritabaný baðlantýsý açýldý...");
	}
	
	// abstract: alt sýnýfta implemente edilmek zorunda.
	public abstract void Kaydet(String sorgu);
	
	
	public void BaglantiKapat()
	{
		System.out.println("Veritabaný baðlantýsý kapatýldý...");
	}
}
