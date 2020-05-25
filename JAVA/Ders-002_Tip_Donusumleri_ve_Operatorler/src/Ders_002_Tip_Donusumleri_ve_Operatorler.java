import java.util.Scanner;
public class Ders_002_Tip_Donusumleri_ve_Operatorler {

	public static void main(String[] args) {
		/*
		System.out.println("Test");

		// Küçük türler büyük türlere otomatik dönüştürülür.
		byte byteSayi1 = 45;
		int intSayi1 = byteSayi1;
		short shortSayi1 = byteSayi1;
		long longSayi1 = byteSayi1;

		float fSayi1 = 45.44f;
		double dSayi1 = fSayi1;

		// Büyük türden küçük türe dönüşüm yaparken casting yapılması zorunludur.
		// Veri kaybı ihtimali vardır.

		fSayi1 = (float)dSayi1;

		int iSayi2 = 83574;
		short sSayi2 = (short)iSayi2;
		System.out.println("iSayi2 : "+iSayi2);
		System.out.println("sSayi2: "+sSayi2);

		// intSayi1 değişkenin tipini yazdırma
		System.out.println(((Object)intSayi1).getClass().getName());
		System.out.println(intSayi1);
		System.out.println(((Object)byteSayi1).getClass().getName());



		int i = 224;
		byte b = (byte)i;
		System.out.println("i :"+i);
		System.out.println("b :"+b);
		short s = (short)i;
		long l = 789456;
		i = (int)l;
		 */
		/*

		byte b2 = 65;
		char h2 = (char)b2;
		System.out.println(h2);
		 */


		// byte: -128 <-> 127

		/*	Aritmetiksel Operatörler
		 * 
		 *  + : toplama
		 *  - : çıkarma
		 *  / : bölme
		 *  * : çarpma
		 *  % : mod alma
		 *  ++: 1 artırma
		 *  --: 1 eksiltme
		 */

		/* Karşılaştırma Operatörleri
		 * 
		 *  == : Eşit Mi?
		 *  != : Değerler Farklı Mı?
		 *  >  : Soldaki Sayı Büyük Mü?
		 *  <  : Soldaki Sayı Küçük Mü?
		 *  >= : Soldaki Sayı Büyük veya Eşit Mi?
		 *  <= : Soldaki Sayı Küçük veya Eşit Mi?
		 */

		/* Bitsel Düzey Operatörleri
		 * & : VE
		 * | : VEYA
		 * ^ : Özel VEYA
		 * <<: SOla 1 bit kaydır
		 * >>: Sağa 1 bit kaydır
		 */

		/* Mantıksal Operatörler
		 * 
		 * &&: Mantıksal VE Operatörü
		 * ||: Mantıksal VEYA Operatörü
		 * ! : Mantıksal DEĞİL Operatörü
		 */

		/* Atama Operatörleri
		 * =  : atama op.
		 * += : sağdaki değeri soldaki(eşittirin solu) değere ekleme
		 * -= : sağdaki değeri soldaki(eşittirin solu) değerden çıkar
		 * *= : sağdaki değeri soldaki değer ile çarp ve sonucu soldaki değişkene ata.
		 * /= : sağdaki değeri soldaki değere böl. SOnucu soldaki değişkene ata
		 * %= : Soldaki değeri sağdakine böl Kalanı soldaki değişkene ata.
		 * Bitsel Düzeyde: <<= , >>= , &=, |= , ^= 
		 * 
		 */

		/*
		byte b1 = 1;
		byte b22 = 2;

		byte s = (byte) (b1 | b22); 
		System.out.println(s);

		String cevap = (8>5)?"Doğru":"Yanlış";	// Koşullu Atama Operatörü
		System.out.println(cevap); 
		 */

		/*
		int bolunen = 25;
		int bolen = 4;
		int kalan = bolunen % bolen;
		System.out.println(kalan);
		 */
		/*
		// Scanner sınıfından ece isminde bir nesne türettik.

		Scanner ece = new Scanner(System.in);

		System.out.print("Sayı1'i giriniz:");
		// Scanner sınıfının nextInt() metodunu kullandık.
		int sayi = ece.nextInt();

		System.out.println("Klavyeden girilen Sayı: "+sayi);
		*/
		
		
		
		Scanner input = new Scanner(System.in);
		/*
		System.out.print("isim giriniz:"); // print ile yazdık imleç alt satıra geçmesin diye.
		String isim = input.next(); // Konsoldan String tipinde veri okumamızı sağlar.
		System.out.println("Hoşgeldin "+isim);
		*/
		/*
		System.out.print("Sayı giriniz:");
		int sayi = input.nextInt(); // Konsoldan int tipinde veri okumamızı sağlar.
		System.out.println("Girilen Sayı: "+sayi);
		*/
		// Klavyeden al�nan 2 Sayıyı toplayıp toplamı ekrana yazdıran programı yazınız.
		/*
		System.out.print("s1:");
		int s1 = input.nextInt();
		System.out.print("s2:");
		int s2 = input.nextInt();
		System.out.println("s1 + s2 : "+(s1+s2));
		*/
		// Klavyeden string olarak okunan Sayısal veriyi int'e çevirip karesini ekrana yazdıran program
		
		System.out.print("Sayı giriniz:");
		String string_sayi = input.next();
		int int_sayi = Integer.valueOf(string_sayi);  // String'den int'e çevirme.
		System.out.println("Sayın�n Karesi: "+(int_sayi*int_sayi));
		
		
	}

}
