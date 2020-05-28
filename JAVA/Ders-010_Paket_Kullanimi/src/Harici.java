// farklı projedeki sınıfları kullanmak için. görsele bakın.
import com.demirmehmet.*;

public class Harici {
	public static void main(String[] args) {

		UcuncuBinYil u1 = new UcuncuBinYil();
		u1.DersAdi = "Python";
		u1.DersSaati = 72;
		u1.DersOgretmeni = "Utku Sabahaddin Ko�lar";
		u1.BilgiYazdir();
		// hackerrank.com dan �al�� F�rat.
		// API: �gda�-Akbank
		ErisimKontrol ek = new ErisimKontrol();
		// ek.isim1 Bu �zelli�e eri�emiyorum!!! Default-friedly oldu�u i�in.
		ek.isim2 = "Serhat"; // Bu �zelli�e eri�ebiliyorum!!! public oldu�u i�in.
		ek.setHesap("IG5874633216");
		System.out.println(ek.getHesap());
	}
}
