import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class Ders_006_Metotlar {
	public static void main(String[] args) {

		/* Metot: Bir programda belirli bir görevi yerine 
		 * getiren (örnek: iki sayıdan büyük olanın ekrana yazdırılması),
		 * kodların tekrar kullanılması durumunda baştan yazılmaması için
		 * 1 defa yazılarak belirli bir isimleçağırılmasıdır.
		 * Ayrıca kodların derli toplu olmasını da sağlar.
		 * Metotlar parametre'ler alarak bu parametreleriişlemlerinde
		 * kullanabilir.
		 * işlem sonucunda bir değer döndürebilir.
		 */

		// static olmayan metodun kullanımı: ileriki derslerde daha iyi anlaşılacak.	
		// Ders7_Metotlar d1 = new Ders7_Metotlar();
		// d1.MerhabaYaz();
		
		
		// Değer döndürmeyen, parametresiz metot.
		
		MerhabaYaz(); // static metoda sınıf içinden erişim.
		//Ders7_Metotlar.MerhabaYaz(); // static metoda sınıf dışından erişim
		
		//Math.min(3, 4); // static metoda bir örnek.
		//Math.max(4, 5); // Değer döndürür.

		
		// Değer döndürmeyen, 1 parametreli metot.
		MerhabaIsim("Mehmet");
		
		ASCII('C');
		
		Katimi7nin(77);
		
		Katimi7nin(88);
		
		// Değer döndürmeyen, 2 parametreli metot.
		Topla(15,25);

		SayiKatiMi(70,6);
		
		// Değer döndürmeyen, parametre olarak liste alan metot.
		ArrayList<Integer> sayilistesi = new ArrayList<Integer>();
		sayilistesi.add(78);
		sayilistesi.add(77);
		sayilistesi.add(79);
		ListeOrtalama(sayilistesi);
		
		// Değer döndürmeyen, 3 parametreli metot.
		Sirala(15,64,12);
		
		
		// Çeşitli Örnekler
		
		/* Kendisine gönderilen sayının rakamlarının toplamını ekrana yazdıran metodu yazınız.
		125/10 = 12   125 %10 = 5
		12/10 = 1  12%10 = 2
		1/10 = 0 1%10 = 1
		n=n/10 
		 */
		// Cevaplanacak
		
		
		/* Kullanıcıdan alınan 3 sayının ortalamasını ekrana yazdıran metot.*/
		
		/*
		Scanner input = new Scanner(System.in);
		System.out.print("sayı 1: ");
		int s1 = input.nextInt();
		System.out.print("sayı 2: ");
		int s2 = input.nextInt();
		System.out.print("sayı 3: ");
		int s3 = input.nextInt();
		
		ortalama(s1,s2,s3);
		*/
		
		/*
		 * 1SORU: Para kısatlma metodu:
		 * 
		 * TL cinsinden aldığı parayı: milyon, milyar,trilyon TL cinsinden 
		 * yazdıran metot.
		 * ÖRNEK: 47 000			 => 47 000 TL
		 * ÖRNEK: 47 000 000         => 47 Milyon TL 
		 * ÖRNEK: 47 000 000 000     => 47 Milyar TL 
		 * ÖRNEK: 47 000 000 000 000 => 47 Trilyon TL 
		 * 
		 */
		/*
		milyonmilyar(47000000L
		milyonmilyar(47000000000L);
		milyonmilyar(47000000000000L);
		*/
		
		// Sayiiste(int adet): Bu metoda 3 gönderirseniz. 3 tane sayı isteyip.
		// aldığı sayıları ArrayList'e eklesin.
		// Başka bir metot da kendisine gönderilen ArrayList'i ekrana yazdırsın.
		
		Sayiiste(4);
		
		
		
		
		
		
		// Değer Döndüren Metotlar
		
		/*
		System.out.println(ToplaDondur(45,96));
		
		int sonuc = ToplaDondur(77,13);
		System.out.println(sonuc*sonuc);
		
		System.out.println("45 100'den büyük mü?:"+BuyukMu100den(45));
		*/
		// Parametre olarak aldığı sayının tek olup olmadmadığını kontrol edip true/false döndüren metot.
		// Ornek: TekMi(99) => true
		
		/*
		 * sayıUret(byte ilk,byte son,byte adet)
		 * ilk sayı ile son sayı arasında adet kadar sayı �retip bir ArrayListe atarak döndür�n.
		 * dönüş tipi ArrayList<Byte> olacak. 
		 */
/*
		Listele(SayiUret(3, 8, 5));
		
		ArrayList<Integer> asd = new ArrayList<Integer>();
		asd= SayiUret(45, 245, 20);
		Listele(asd);
	*/	
		
		/*
		Random r = new Random();
		int s = r.nextInt(5+1) +(10); // 10-15 arası
		System.out.println(s);
		*/
		
		//int sa = (min+(int)Math.random()*max-min);
		// SORU: Klavyeden sayı isteme metodu: intGir(); geriye klavyeden alınan int sayıyı döndürs�n.
		

		
		int sayi1 = intGir();
		int sayi2 = intGir();
		System.out.println();
		
		
		/* SORU: ListeOrtalama isminde bir metot tanımlayın. Integer tipinde bir
		 * ArrayList alacak. ve Bu ArrayList in ortalamasını bulup döndürecek. */
		
		ArrayList<Integer> listem = new ArrayList<Integer>();
		listem.add(5);
		listem.add(15);
		listem.add(25);
		
		//System.out.println(ListeOrtalama(listem));
		
		
		// Parametre olarak aldığı ArrayList'teki sayıların karelerini başka bir
		// listeye atıp bu listeyi döndüren fonksiyon
		System.out.println(KareListe(listem));
		
		/*SORU: Kendisine gönderilen sayının Asal olup olmadığını bulan fonksiyon*/

		/*
		System.out.println("1 Asal mı?:"+AsalKontrol(1));
		System.out.println("2 Asal mı?:"+AsalKontrol(2));
		System.out.println("6 Asal mı?:"+AsalKontrol(6));
		System.out.println("5 Asal mı?:"+AsalKontrol(5));
		*/
		
		// SORU: Klavyeden sayı girişi için kısa bir fonksiyon yazınız.
		/*
		Scanner in = new Scanner(System.in);
		System.out.print("Sayi gir:");
		int sayi = in.nextInt();
		*/
		int sayi = input("sayı giriniz:");	
		System.out.println("Girilen sayı: "+sayi);
		
	
		
		
		
	}
	// Değer Döndürmeyen Metotlar
	
	// Static metotlar nesne tanımlanmadan kullanılabilr. void: geriye değer döndürmeyeceğini gösterir.
	public static void MerhabaYaz()
	{
		System.out.println("Metot'dan merhabalar...");
		int a = 111;
		int b = 888;
		System.out.println("111 ve 888'in toplamü:"+(a+b));
	}
	
	public static void MerhabaIsim(String isim)
	{
		System.out.println("Merhaba "+isim);
	}
	
	// Parametre olarak aldığı 2 tane int tipinde sayıyı toplay�p ekrana yazdıran program.
	public static void Topla(int sayi1,int sayi2)
	{
		System.out.println("sayıların toplamü: "+(sayi1+sayi2));
	}
	
	// Parametre olarak aldığı char değerin ASCII karşılığını ekrana yazdıran metot.
	public static void ASCII(char karakter)
	{
		System.out.println("Karakterin ASCII tablosundaki karşılığı: "+(short)karakter);
	}
	
	// Kendisine gönderilen sayının 7'nin katı olup olmadmadığını ekrana yazdıran metot.
	public static void Katimi7nin(int sayi)
	{
		String cevap = (sayi%7==0)?"katıdır":"katı değildir.";
		System.out.println(sayi+ " 7 nin "+cevap);
	}
	
	// Kendisine gönderilen 2 sayıdan 1. sayının 2.sinin katı olup olmadmadığını ekrana yazdıran metot.
	public static void SayiKatiMi(int bolunen,int bolen)
	{
		if(bolunen%bolen==0)
			System.out.println(bolunen+" "+bolen+"'in katıdır.");
		else
			System.out.println(bolunen+" "+bolen+"'in katı değildir.");
	}
	
	// 1'den kendisine gönderilen sayıya kadar olan tek sayıların toplamını hesaplayıp ekrana yazdıran metot.

	// Klavyeden 10 sayı alıp Integer tipinde bir ArrayList'e atın, ekrana listi yazdırsın.
	// ListeOrtalama isminde bir metot tanımlayın. Parametre olarak iInteger tipinde 1 ArrayList als�n.
	// Bu metot parametre olarak aldığı ArrayList'in elemanlarının aritmetik ortalamasını alıp ekrana yazdırsın.
	// ilk başta olulturduğumuz diziyi ListeOrtalama isimli metoda parametre olarak gönderin.
	
	public static void ListeOrtalama(ArrayList<Integer> liste)
	{
		int toplam = 0 ;
		for (int i = 0; i <liste.size(); i++) {
			toplam += liste.get(i);
		}
		System.out.println("Ortalama: "+(toplam/liste.size()));
	}
	
	// SORU: Kendisine gönderilen 3 sayıyı küçükten büyüğe sıralayıp yazdıran metot.
	public static void Sirala(int a,int b,int c)
	{
		int kucuk = Math.min(Math.min(a,b),c);
		int buyuk = Math.max(Math.max(a,b),c);
		int orta;
		if(kucuk==a)
		{
			orta = Math.min(b,c);
		}else if(kucuk==b)
		{
			orta = Math.min(a,c);
		}else
		{
			orta = Math.min(a,b);
		}
		System.out.println("sayılar sırasıyla: "+kucuk+" "+orta+" "+buyuk);
	}

	
	public static void Sayiiste(int adet)
	{
		ArrayList<Integer> istenenSayilar = new ArrayList<Integer>();
		Scanner input = new Scanner(System.in);
		int s;
		for (int i = 0; i < adet; i++) {
			System.out.print((i+1)+". sayıyı giriniz:");
			s = input.nextInt();
			istenenSayilar.add(s);
		}
		Listele(istenenSayilar);
		
	}

	public static void Listele(ArrayList<Integer> liste)
	{
		for (int i = 0; i < liste.size(); i++) 
		{
			System.out.println((i+1)+". eleman: "+liste.get(i));
		}
	}

	public static void milyonmilyar(long para)
	{
		if((para>1000000) && (para<1000000000))
		{
			long sayi = para/1000000;
			String metin = "Milyon TL";
			System.out.println(sayi+" "+metin);			
		}
		
		if((para>1000000000L) && (para<1000000000000L))
		{
			long sayi = para/1000000000;
			String metin = "Milyar TL";
			System.out.println(sayi+" "+metin);			
		}
		
		if((para>1000000000000L) && (para<1000000000000000L))
		{
			long sayi = para/1000000000000L;
			String metin = "Trilyon TL";
			System.out.println(sayi+" "+metin);			
		}
	}

	public static void ortalama(int sayi1,int sayi2, int sayi3)
	{
		System.out.println("sayıların ortalamas�:"+((sayi1+sayi2+sayi3))/3);
	}
	
	
	// Değer döndüren metotlar.
	
	public static int intGir()
	{
		Scanner input = new Scanner(System.in);
		System.out.print("sayı Giriniz:");
		return input.nextInt();
	}
	
	
	public static ArrayList<Integer> SayiUret(int ilk,int son,int adet)
	{
		ArrayList<Integer> rastgeleSayilar = new ArrayList<Integer>();
		Random rast = new Random();
		int s;
		for (int i = 1; i <= adet; i++) 
		{
			s = rast.nextInt((son-ilk)+1)+(ilk);
			rastgeleSayilar.add(s);
		}
		return rastgeleSayilar;
	}
	
	public static int ToplaDondur(int a,int b)
	{
		return (a+b);
		//System.out.println("Bu komutçalışmaz.Return'den sonra yazdığımız ,için.");
	}
	public static boolean BuyukMu100den(int sayi)
	{
		if(sayi>100)
			return true;
		else
			return false;
	}
	
	
	public static ArrayList<Integer> ListeDondur()

	{
		ArrayList<Integer> sayiListesi = new ArrayList<Integer>();
		sayiListesi.add(10);
		sayiListesi.add(20);
		sayiListesi.add(36);
		
		for (Integer sayi : sayiListesi) {
			
		}
		
		return sayiListesi;
	}
	
	public static int ListeOrtalama(ArrayList<Integer> listem)
	{
		int toplam =0;
		for (Integer sayi : listem) {
			toplam += sayi;
		}
		return (toplam/listem.size());
				
	}
	
	public static ArrayList<Integer> KareListe(ArrayList<Integer> sayilar)
	{
		ArrayList<Integer> kareler = new ArrayList<Integer>();
		for (Integer sayi : sayilar) {
			kareler.add(sayi*sayi);
		}
		return kareler;
	}
	
	
	public static boolean AsalKontrol(int sayi)
	{
		if(sayi==1)
			return false;
		else
		{
			for(int i=2; i<sayi;i++)
			{
				if(sayi%i==0)
					return false;
			}
			return true;
		}
	}
	
}
