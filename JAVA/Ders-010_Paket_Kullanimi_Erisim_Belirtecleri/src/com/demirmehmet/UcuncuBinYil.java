package com.demirmehmet;

public class UcuncuBinYil {
	public String DersAdi;
	public byte DersSaati;
	public String DersOgretmeni;
	
	public void BilgiYazdir()
	{
		System.out.println("Dersin Ad�: "+this.DersAdi); // this. S�n�fa ait �zelli�e eri�memizi sa�lar.
		System.out.println("Dersin Saati: "+this.DersSaati);
		System.out.println("Dersin ��retmeni: "+this.DersOgretmeni);
		ErisimKontrol ek = new ErisimKontrol();
		System.out.println(ek.isim1); // default: eri�imim var.
	}
}

/* Proje:Matematik. Matematik isimli bir paket i�inde DortIslem.java dosyas�n� olu�turun.
 * void ToplaYaz(int s1,int s2): Heryerden eri�ilsin.
 * void CikarYaz(int s1, int s2): Sadece paket i�inden eri�ilebilsin.
 * CarpYaz : Sadece s�n�f i�inden eri�ilsin.
 * BolYaz: Paket i�inden ve t�m alt s�n�flardan eri�ilsin.
 * Bu metotlar nesne tan�mlamadan kullan�labilsin.
 * Bu paketi Ders11_Ornekler isimli projedeki class dosyas�ndan �ap�r�p kullan�n.
 * */