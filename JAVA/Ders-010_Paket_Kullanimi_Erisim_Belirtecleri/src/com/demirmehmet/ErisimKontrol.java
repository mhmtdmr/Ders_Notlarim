package com.demirmehmet;


public class ErisimKontrol {
	// ER���M BEL�RTE�LER�:
	// Bo�sa:(public-private-protected yaz�lmam��sa) 
	// Default-friendly: S�n�f i�inden ve paket i�indeki di�er s�n�flardan eri�ilebilir.
	// Paket i�indeki farkl� dosyadan da eri�ilir.Farkl� paketten ve alt s�n�flardan eri�ilemez!
	
	
	// public: her yerden her ko�ulda eri�ilebilir.
	
	// private: Sadece tan�ml� oldu�u s�n�f i�erisinden eri�ilebilir.
	
	// protected: Paket i�erisinden ve t�m alt s�n�flardan eri�ilebilir.
	String isim1;
	public String isim2;
	private String isim3;
	protected String isim4;
	
	private String _K_HesapN;
	
	// Getter: private bir �zelli�in verisine d��ar�dan eri�memizi sa�lar. Gizlilik sa�lar.
	// E�er bu �zelli�in sadece okunur olmas�n� de�i�mesini istemiyorsak. setter metodunuz yazmazsak olur.
	public String getHesap()
	{
		return this._K_HesapN;
	}
	// Setter: private bir �zelli�e d��ar�dan eri�im. Gizlilik sa�lar. Atan�lan de�eri kontrol etmemizi
	// sa�lar. 
	public void setHesap(String hesapno)
	{
		this._K_HesapN = hesapno;
	}
	
	
	void Topla(int a, int b)
	{
		System.out.println("isim1 'e eri�iyorum: "+this.isim1);
		System.out.println("isim3 'e eri�iyorum: "+this.isim3);
	}
	private void gizliTopla(int a, int b)
	{
		System.out.println("gizliMetot: "+this.isim1);
		System.out.println("gizliMetot: "+this.isim3);
	}

	public static void main(String[] args) {
		
	}

}
class ErisimTesti{
	void test()
	{
		ErisimKontrol ek = new ErisimKontrol();
		System.out.println(ek.isim1); // Ayn� dosyadaki ba�ka s�n�ftan eri�ebilirim.
		System.out.println(ek.isim2); // Ayn� dosyadaki ba�ka s�n�ftan eri�ebilirim.
		// System.out.println(ek.isim3); // Sadece kendi s�n�f�ndan eri�ilebilir.
		System.out.println(ek.isim4); // Protected sorun yok.
	}
}
