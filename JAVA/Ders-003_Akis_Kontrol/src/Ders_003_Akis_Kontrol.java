
public class Ders_003_Akis_Kontrol {

	public static void main(String[] args) {
		// IF-ELSE IF -ELSE

		int s =100;
		if(s<100) 
		{
			// Koşul sağlandığında çalışacak blok
			System.out.println("Girilen Sayı 100'den küçüktür.");
		}
		else if(s>100)
		{
			// 2. Koşul sağlanırsa çalışacak Koşul
			System.out.println("Girilen Sayı 100'den büyüktür.");
		}		
		else
		{
			// Koşul sağlanmadığında çalışacak blok.
			System.out.println("Girilen Sayı 100'dür.");
			int a =5;int b= 6; 
			String sonuc= String.format("İki Sayının toplamı %d %s %b",(a+b),"Metin",1);
			System.out.println(sonuc);
			sonuc= "İki Sayının toplamı "+(a+b)+" Metin "+true;
			System.out.println(sonuc);
		}
		System.out.println("Program Sonu");
		
		/*SORU: 
		 * 1: Klavyeden girilen 2 Sayıdan büyük olanı ekrana yazdıran program.
		 * 2: Klavyeden girilen Sayı tek ise küpünü çift ise karesini ekrana yazdıran program.
		 * 3: Klavyeden girilen 1 karakter alın, ASCII tablsoundaki Sayısal değeri 125'ten küçükse ve 10dan büyükse. Sayısal değerinden 5 çıkardığımızda oluşan karakteri ekrana yazdır.
		 * 		char a = 'A';
				a++;
				boolean b = 'A'>66;
				System.out.println(b);
		 * 
		
		Scanner input = new Scanner(System.in);
		System.out.print("1. Sayıyı Gir:");
		int s1 = input.nextInt();
		System.out.print("\n2. Sayıyı Gir:");
		int s2 = input.nextInt();
		
		if(s1>s2)
		{
			System.out.println("1. Sayı büyük: "+s1);
		}
		else if (s2>s1)
		{
			System.out.println("2. Sayı büyük: "+s2);
		}
		else
		{
			System.out.println("Sayılar Eşit "+s1);
		}
		*/
		// CEVAP2
		Scanner input = new Scanner(System.in);
		System.out.print("1. Sayıyı Gir:");
		int s1 = input.nextInt();
		
		if(s1%2==0)
		{
			System.out.println(s1*s1);
		}
		else
		{
			System.out.println(s1*s1*s1);
		}
		
		
		
		// Switch Case:
		
		Scanner input = new Scanner(System.in);

		/*
		 * int i = 2; String mesaj; switch (i) { case 1: mesaj = "i'nin değeri 1'dir";
		 * break; case 2: mesaj = "i'nin değeri 2'dir"; break; case 3: mesaj =
		 * "i'nin değeri 3'tür"; break; default: mesaj = "i 1 2 3 değildir."; break; }
		 * System.out.println(mesaj);
		 * 
		 */
		System.out.print("Gün Numarası:");
		int gunSayi = input.nextInt();
		String gunAdi;
		switch (gunSayi) {
			case 1:
				gunAdi = "Pazartesi";
				break;
			case 2:
				gunAdi = "Sal�";
				break;
			case 3:
				gunAdi = "�ar�amba";
				break;
			case 4:
				gunAdi = "Per�embe";
				break;
			case 5:
				gunAdi = "Cuma";
				break;
			case 6:
				gunAdi = "Cumartesi";
				break;
			case 7:
				gunAdi = "Pazar";
				break;
			default:
				gunAdi = "Hatal� Gün Numarası!";
				break;
		}
		System.out.println(gunAdi);

		// Soru: klavyeden haftanın Gün Numarasını (1-7) alın. Ve karşısındaki günün
		// adını yazdırın(switch-case ile)

		/*
		 * Ödev:
		 * 
		 * Klavyeden girilen karakterin ASCII değeri: 10dan büyük 125'ten
		 * küçükse:sayının değerinden 5 çıkardığımızda oluşan değeri ekrana yazdırın.
		 * 
		 * 
		 * Scanner input = new Scanner(System.in);
		 * System.out.print("Karakter giriniz:"); char karakter =
		 * input.next().charAt(0);
		 * 
		 * if (karakter<125 && karakter>70) { karakter = (char)(karakter - 5); }
		 * System.out.println("Karakterin Sayısal değeri: " + (int)karakter);
		 * System.out.println("Karakter: "+karakter);
		 * 
		 * 
		 * 
		 * String il = "Kayseri"; String ilce = "Erciyes";
		 * 
		 * 
		 * if (il=="Yozgat") { System.out.println("İl Yozgat"); } else if(il=="Manisa")
		 * { System.out.println("İl Manisa"); } else if(il == "Kayseri") {
		 * System.out.println("İl Kayseri"); if (ilce=="Talas") {
		 * System.out.println("İlçe Talas"); } else if(ilce=="Develi") {
		 * System.out.println("İlçe Develi"); } else if(ilce=="Erciyes") {
		 * System.out.println("İlçe Erciyes"); } }
		 */

	}

}
