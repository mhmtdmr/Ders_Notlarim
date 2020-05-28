package Abs;

public abstract class Veritabani {
	/* ABSTRACT:
	 * Nesne t�retilemez.
	 * S�n�flardan miras alabilir.
	 * Interface'leri implemente edebilir.
	 * ��erisinde abstract veya g�vdeli metotlar olabilir.
	 * 
	 */
	public void BaglantiAc()
	{
		System.out.println("Veritaban� ba�lant�s� a��ld�...");
	}
	
	// abstract: alt s�n�fta implemente edilmek zorunda.
	public abstract void Kaydet(String sorgu);
	
	
	public void BaglantiKapat()
	{
		System.out.println("Veritaban� ba�lant�s� kapat�ld�...");
	}
}
