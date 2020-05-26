import java.util.Scanner;
import java.util.Random;
public class Ders_004_Donguler {

	public static void main(String[] args) {

		// Döngüler

				// While Döngüsü : Koşul sağlandığı sürece çalışan Döngü.
				/*
				 * while (koşul) { //Koşul sağlandığında çalışacak //kodlar }
				 */

				// Sonsuz Döngü
				/*
				 * while (true) { System.out.println("Sonsuz kez çalışacağım"); }
				 * 
				 * int sayac=1; while (sayac<=10) { System.out.println("Sayı: "+sayac); sayac++;
				 * // sayac'ı 1 artır. }
				 * 
				 */
				// Klavyeden girilen değeri ekrana 20 defa yazdıran program(while)
				/*
				 * Scanner input = new Scanner(System.in); System.out.print("Birşeyler yazın:");
				 * String girilen = input.next(); int sayac=1; while(sayac<=20) {
				 * System.out.println(girilen); sayac++; }
				 */
				// Klavyeden girilen Sayının faktöriyelini bulan program.

				// sayi carpim
				/*
				 * System.out.print("Sayı giriniz:"); int sayi = input.nextInt(); int carpim =1;
				 * while(sayi>=1) { carpim = carpim * sayi; sayi--; }
				 * System.out.println("Faktöriyeli: " +carpim);
				 */

				// 1'den Klavyeden girilen Sayıya kadar olan �ift Sayıları toplayan
				// program.(while Döngüsü ile)
				/*
				 * System.out.print("Sayı giriniz:"); int sayi = input.nextInt();
				 * 
				 * int ciftToplam=0; int sayac = 1; while (sayac<=sayi) { if(sayac%2==0) {
				 * //System.out.println(sayac); ciftToplam += sayac; // ciftToplam = ciftToplam
				 * + sayac; } sayac++; }
				 * System.out.println("�ift Sayıların toplamı: "+ciftToplam);
				 * 
				 * 
				 * // 1 ile girilen Sayıya kadar olan Sayılardan: // 9'a ve 2'ye tam b�l�nenleri
				 * toplayıp ekrana yazdıran
				 * 
				 * int i=1; while(i<=5) { if(i==3) { i++; continue; // buraya gelince Döngün�n
				 * ileriki kısmı çalışmaz ve Döngü bir sondaki aşamaya geçer.
				 * 
				 * } if(i==4) break; System.out.println(i); i++; }
				 * 
				 * 
				 * // Kullanıcıdan Sayı istiyoruz. Ve kullanıcı çıkmak istermisiniz sorusuna
				 * evet yazana kadar tekrar Sayı istiyoruz. // En son girilen Sayılardan tek
				 * olanları toplayıp ekrana yazdırın.
				 * 
				 * int tekToplam = 0;
				 * 
				 * while(true) { System.out.print("Sayı:"); int sayi = input.nextInt();
				 * if(sayi%2==1) { tekToplam = tekToplam + sayi; }
				 * System.out.print("çıkmak istiyor musunuz? (e/h) :"); char cevap =
				 * input.next().charAt(0); if(cevap=='e') break;
				 * 
				 * } System.out.println("Tek Toplam: "+tekToplam);
				 * 
				 */
		
		
		
		
		
		
		
		
		
		
		/* do-while: koşula bakılmadan önce döngü 1 kez çalışır. Yani döngü en az 1 kez çalışır.
		do {
			//Çalışacak kodlar
		}while(true);
		*/
	
		
		
		// kullanici 0 girene kadar girilen sayıları yoplayıp ekrana yazdıran program.
		Scanner input = new Scanner(System.in);
		/*
		int sayi;
		int toplam = 0;
	
		
		do {
			System.out.print("Bir sayı giriniz:(çıkmak için 0)");
			sayi = input.nextInt();
			toplam += sayi;
		} while (sayi!=0);
		System.out.println("Girilen sayıların toplamı: " + toplam);
		*/
		
		
		
		// == ram'deki adresi karşılaştırıken; equals() içindeki veriyi karşılaştırır.
		/*
		String email="ali@gmail.com";
		System.out.println(email.contentEquals("ali@gmail.com"));
		System.out.println(email.equals("ali@gmail.com"));
		
		System.out.print("eposta gir:");
		String ep = input.next();

		//if (ep==email) {
		if (ep.equals(email)) {
			System.out.println("Veriler eşit");
		}else
		{
			System.out.println("Veriler eşit değil.");
		}
		
		System.out.println("email ram'deki adresi: "+System.identityHashCode(email));
		System.out.println("ep  ram'deki   adresi: "+System.identityHashCode(ep));
*/
		// Soru: eposta = "ali@gmail.com" parola = "aLi.1221" 
		// yukarıdaki eposta ve parolayı kontrol eden do-while döngüsünü yazınız.
		// Kullanıcıdan eposta ve parola alıp doğru mu kontrolü yapılacak.
		// Yanlış girişte tekrar denemesi sağlanacak. 3 hakkı
		/*
		String eposta = "ali@gmail.com";
		String parola = "aLi.1221";
		String keposta,kparola;
		int sayac=1;
		do {
			
			System.out.print("Eposta adresiniz :");
			keposta = input.nextLine();
			System.out.print("Parolanız :");
			kparola = input.nextLine();
			if(keposta.equals(eposta) && kparola.equals(parola) )
			{
				System.out.println("Başarılı Giriş.");
				break;
			}else if (sayac<=3) {
				System.out.println("Başarısız giriş tekrar deneyin! Kalan hakkınız:"+(3-sayac));
			}else {
				System.out.println("Başarısız giriş. Başka hakkınız kalmadı.");
			}
			sayac++;
		} while (sayac<=3);
		*/
		
		/*
		 * Klavyeden girilen sayı 100'den küçük olduğu sürece yarısını alıp toplayacak programı yazınız.
		 * 100'den büyükse döngüden çıkılıp toplam ekrana yazdırılacak. 
		 */
		/*
		int toplam=0;
		int sayi;
		
		do {
			System.out.print("Sayı Giriniz:");
			sayi = input.nextInt();
			if(sayi<100)
			{
				toplam += (sayi/2);
			}
		} while (sayi<100);
		System.out.println("Toplam :"+toplam);
		*/
		
		
		/*
		
		// FOR Döngüsü:
		
		for(int i=1;i<=3;i++)
		{
			System.out.println("Döngü sayısı : "+i);
		}
		
		// Sırayla charları yazdırma.
		for(char i=0;i<=255;i++)
		{
			System.out.println(i);
		}
		
		// SORU: 10-1 arasındaki sayıları ekrana yazdırınız. Azalan
		
		for (int i = 10; i > 0; i--) {
			System.out.println();
		}
		*/
		// 1'den klavyeden alınan değere kadar olan sayıları toplayıp
		// ekrana yazdıran program.
		/*
		int toplam = 0;
		int sayi;
		
		System.out.print("Sayı gir:");
		sayi = input.nextInt();
		
		for(int i=1;i<=sayi;i++)
		{
			toplam+=i;
		}
		System.out.println("Toplam:"+toplam);
		*/
		
		// Klavyeden alınan 2 sayı arasındaki tek sayıları toplayan program.
		// En son toplamı ekrana yazdırsın.
		/*
		System.out.println(Math.min(3, 5));
		System.out.println(Math.max(3, 5));
		
		int s1,s2;
		int toplam =0;
		System.out.print("s1 :");
		s1 = input.nextInt();
		
		System.out.print("s2 :");
		s2 = input.nextInt();
		
		int kucuk = Math.min(s1, s2);
		int buyuk = Math.max(s1, s2);
		
		for(int i=kucuk;i<=buyuk;i++)
		{
			toplam += i;
		}
			*/	
		/*Ekrana aşağıdaki çıktıyı veren programı yazınız.
		 * 
		 
		    * 
		   ***
		  ***** 
		 *******
		********* 
		  
		 */
		/*
		for (int i = 1; i <= 5; i++) {
			for (int j = 1; j <= i; j++) {
				
				System.out.print("*");
			}
			
			System.out.println();
		}
		*/
		/*Ekrana aşağıdaki çıktıyı veren programı yazınız.
		 * 
		 
		    * 
		   ***
		  ***** 
		 *******
		********* 
		  
		
		for (int i = 1; i <= 5; i++) {
			for (int j = 1; j <= 5-i; j++) { // Boşluk yazmak için.
				System.out.print(" ");
			}
			for (int j = 1; j <=i; j++) {
				System.out.print("*"); // Boşluktan sonraki yıldızı yazmak için Boşluğu dikdörtgene tamamladık.
				// Boşluktan sonraki karakter sayısı 5 olana kadar yıldız yazdık.
			}
			for (int j = 2; j <= i; j++) {
				System.out.print("*"); // 5. karakterden sonraki yıldızları basmak için.
			}
			System.out.println();
		}
		
		 */
		// Klavyeden kisakenar ve uzun kenar bilgisi girilen dikdörtgeni yıldızlar ile çiziniz.
		// 
		
		
		/*
		 
		 ***********
		 ***********
		 ***********
		 ***********
		 
		 ÖDEV: 5X10 dörtgen çizme.
		 **********
		 *        *
		 * 		  *
		 *        *
		 **********
		 
		 */
		System.out.println("kk:");
		int kk = input.nextInt();
		System.out.println("uk:");
		int uk = input.nextInt();
		
		for (int i = 1; i <= kk; i++) {
			for (int j = 1; j <= uk; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
		
		
		
		/* Aşağıdaki şekli for döngüsü ile çıkarınız. HackerRank 5X10
		 
		 **********
		 *        *
		 *        *
		 *        *
		 **********
		 
		 */
		/*
		for(int i=1;i<=5;i++)
		{
			System.out.print("*");
			
			if(i==1 || i==5)
			{
				System.out.print("********");
			}else
			{
				System.out.print("        ");
			}
			
			System.out.print("*");
			System.out.println();
		}
		
		*/
		// kullanıcıdan karakter,yükseklik ve genişlik değerlerini alarak. Bunlaragöre ekrana dikdörtgen
		//çizdirin.
		/*
		Scanner input = new Scanner(System.in);
		System.out.print("Karakter:");
		char k = input.next().charAt(0);
		
		System.out.print("yükseklik:");
		byte yukseklik = input.nextByte();
		
		System.out.print("genişlik:");
		byte genislik = input.nextByte();
		
		for (int i=1;i<=yukseklik;i++)
		{
			System.out.print(k);
			if(i==1 || i==yukseklik)
			{
				for(int j =0;j<=(genislik-2);j++)
				{
					System.out.print(k);
				}
			}else
			{
				for(int j =0;j<=(genislik-2);j++)
				{
					System.out.print(" ");
				}
			}
			System.out.print(k);
			System.out.println();
		}
		
		
		
		
		*/
		

	}

}
