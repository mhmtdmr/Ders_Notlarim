
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

	}

}
