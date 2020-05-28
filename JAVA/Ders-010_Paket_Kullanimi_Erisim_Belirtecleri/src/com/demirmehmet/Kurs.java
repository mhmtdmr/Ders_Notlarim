package com.demirmehmet;

public class Kurs {

	public static void main(String[] args) 
	{
		// S�n�flara ayn� package i�indeki ba�ka bir java dosyas�ndan do�rudan eri�im var.
		UcuncuBinYil u1 = new UcuncuBinYil();
		u1.DersAdi = "Java";
		u1.DersSaati = 72;
		u1.DersOgretmeni = "F�rat Ko�";
		u1.BilgiYazdir();
	}
}
