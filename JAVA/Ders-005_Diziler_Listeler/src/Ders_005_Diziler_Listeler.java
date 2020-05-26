import java.util.Scanner;
import java.util.Random;
import java.util.ArrayList;
import java.util.Arrays;

public class Ders_005_Diziler_Listeler {

	public static void main(String[] args) {

		// DİZİLER
				int[] rakamlar = {0,1,2,3,4,5,6,7,8,9};// Dolu idiz tanımlama
				 
				int[] sayilar = new int[5]; // 5 elemanlı boş bir dizi tanıladık.
				// int 'in varsayılan değeri 0 olduğundan aslında ilk değerleri 0'dır.
				
				sayilar[3] = 40;
				sayilar[4] = 10;
				*/
				//System.out.println(sayilar[3]);
				
				/*
				for (int i : sayilar) {
					System.out.println(i);
				}
				*/
				/*
				for(int i=0;i<sayilar.length;i++)
				{
					System.out.println(sayilar[i]);
				}
				*/
				// Rastgele üretilen 10 sayıyı sayilar ismindeki bir diziye atayın.
				// (0-100 aralığı)
				// daha sonra bu dizideki elemanları okuyup her birini f(x) = 3x+2 formülüne
				// koyup bu formül sonucunu formul isimli başka bir diziye atayın.
				
				// Son olarak dizileri ekrana yazdırın.
			
				int[] sayilar = new int[10];
				int[] formul = new int[10];
				Random rnd = new Random();
				
				for(int i=0;i<10;i++)
				{
					sayilar[i]= rnd.nextInt(100);	
					formul[i] = 3*(sayilar[i])+2;
					
					System.out.print(sayilar[i]+"  ==>  "+formul[i]);
					System.out.println();
				}
				
				
				/*
				 int[] sayiListe = new int[5];
				 
				 
				 sayiListe[0] = 15;
				 
				 
				 String[] isimler = new String[3];
				 
				 
				 for (String i : isimler) {
					System.out.println("Dizi eleman�:"+i);
				 }
				 */
					
					
					
				/*	
				 int[][] ikiBoyutlu = new int[3][3];
				 
				 for (int i=0; i<3;i++)
				 {
					 for(int j=0;j<3;j++)
					 {
						 ikiBoyutlu[i][j] = 1; 
						 System.out.print(ikiBoyutlu[i][j]+" ");
					 }
					 System.out.println();
				 }
				 */
				/*
					int[] rastgeleDizi = new int[10];
					Random r = new Random();
				 
					for(int i=0;i<rastgeleDizi.length;i++)
					{
						rastgeleDizi[i]= r.nextInt(16);
						System.out.println(rastgeleDizi[i]);
					}
					
					Arrays.sort(rastgeleDizi);
					
					for(int i=0;i<rastgeleDizi.length;i++)
					{
						System.out.println(rastgeleDizi[i]);
					}
					int indis = Arrays.binarySearch(rastgeleDizi, 15);
					System.out.println("--------------------");
					System.out.println("Aranan de�erin indisi:"+indis);
					*/
					/*
					String[] IcAnadolu = {"Kayseri","Nev�ehir","Yozgat","Sivas"};
					String[] Karadeniz = {"Ordu","Giresun","Tokat","Trabzon","D�zce"};
					String[] Turkiye = new String[81];
					
					System.arraycopy(IcAnadolu, 0, Turkiye, 0, 4);
					System.arraycopy(Karadeniz, 0, Turkiye, 4, 2);
					
					for (String sehir : Turkiye) {
						System.out.println(sehir);
					}
					*/
					/*SORU: Rastgele �retilen 20 say�dan tekleri bir diziye �iftleri bir diziye toplay�n�z.
					 * Son olarak dizileri ekrana yazd�r�n�z.
					 */
					/*
					
				 int[] tekler = new int[20];
				 int[] ciftler = new int[20];
				 Random r = new Random();
				 
				 int itek=0;
				 int icift=0;
				 for(int i=1;i<=20;i++)
				 {
					 int sayi = (r.nextInt(100))+1;
					 if(sayi%2==0)
					 {
						 ciftler[icift] = sayi;
						 icift++;
					 }else
					 {
						 tekler[itek] = sayi;
						 itek++;
					 }
						 
				 }
				 
				 System.out.println("Tek Dizi:");
				 for(int i=0; i<20;i++)
				 {
					 System.out.print(tekler[i] + " - ");
				 }
				 
				 System.out.println("�ift Dizi:");
				 for(int i=0; i<20;i++)
				 {
					 System.out.print(ciftler[i] + " - ");
				 }
				 */
			
				
			
			//  ***************************  ARRAYLIST KULLANIMI   ******************************
				/*
				ArrayList<Integer> sayilar = new ArrayList<Integer>();
				sayilar.add(15);
				sayilar.add(1);
				sayilar.add(11);
				sayilar.add(12);
				sayilar.add(13);
				sayilar.add(17);
				sayilar.add(18);
				
				System.out.println(sayilar);
				sayilar.remove(0);     // indis ile silme
				System.out.println(sayilar);
				sayilar.remove((Object)18);   // Objeyi silme.
				System.out.println(sayilar);
				
				sayilar.set(0, 99); //0. eleman� 99 yap.
				
				ArrayList<Integer> rakamlar = new ArrayList<Integer>();
				rakamlar.add(0);
				rakamlar.add(2);
				rakamlar.add(3);
				rakamlar.add(4);
				
				sayilar.addAll(rakamlar);
				System.out.println(sayilar);
				
				System.out.println(rakamlar.get(3));
				
				
				System.out.println("sayilar dizisinde 12 de�erinin indisi"+sayilar.indexOf(12));
				System.out.println("sayilar dizisinin 2. ve 5 . de�eri aras�"+sayilar.subList(2, 5)); // 5 hari�
			 	*/
				/*
				ArrayList<String> isimler = new ArrayList<String>();
				isimler.add("Harun");
				isimler.add("Kenan");
				isimler.add("Selda");
				isimler.add("Kamer");
				isimler.add("Kenan");
				
				ArrayList<String> baskaisimler = new ArrayList<String>();
				baskaisimler = (ArrayList<String>)isimler.clone();
				System.out.println(baskaisimler);
			 
			 
				System.out.println("isimler listesinde Kenan var m�?"+isimler.contains("Kenan"));
				
			 
			 int i1 = isimler.indexOf("Kenan");
			 System.out.println(i1);
			 
			 System.out.println("isimler listesinin boyutu: "+isimler.size());
			 */
			 // 3 Kullan�c�dan adSoyad,dogumYili,telefon bilgisi al�p bu bilgileri bir ArrayList'de 
			 // tutunuz. 
			 // 2. eleman�n bilgilerini listelemek istedi�imde listeleyebilece�im kod blo�u.
			 
				/*
				Scanner in = new Scanner(System.in);
				ArrayList<Object> personel = new ArrayList<Object>();
				
				
				for(int i=0;i<9;i=i+3)
				{
					System.out.print("adSoyad: ");
					String adSoyad = in.nextLine();
					System.out.print("dogumYili: ");
					int dogumYili = in.nextInt();
					System.out.print("telefon:");
					String telefon = in.nextLine();
					telefon = in.nextLine();
					
					
					personel.add(adSoyad);
					personel.add(dogumYili);
					personel.add(telefon);
				}
				
				
				//2. personelin bilgilerini getiren b�l�m.
				int indis = ((2-1)*3);
				System.out.println("Ad Soyad: "+personel.get(indis));
				System.out.println("Dogumyili: "+personel.get(indis+1));
				System.out.println("Telefon: "+personel.get(indis+2));
			 */
				
				
				ArrayList<Integer> sayilar = new ArrayList<Integer>();
				sayilar.add(123);
				sayilar.add(321);
				sayilar.add(222);
				sayilar.add(444);
				System.out.println(sayilar);
				System.out.println(sayilar.get(1));
				System.out.println("ArrayList'in boyutu: "+sayilar.size());
				System.out.println("ArrayList'in i�ince 222 var m�?:"+sayilar.contains(222));
				System.out.println("ArrayList'in i�ince 555 var m�?:"+sayilar.contains(555));
				
				Integer[] sayiDizisi = new Integer[5];
				sayiDizisi=	sayilar.toArray(sayiDizisi);
				
				/*SORU: Klavyeden girilen 5 say�y� bir listeye at�p say�lar�n ortalamas�n�
				 * ekrana yazd�ran program� yaz�n�z.
				 */
				
				int ortalama=0;
				int toplam=0;
				ArrayList<Integer> sayilar2 = new ArrayList<Integer>();
				Scanner input = new Scanner(System.in);
				for (int i = 1; i <=5 ; i++) { // indis �nemli de�il 1 den ba�lad�k.
					System.out.print(i+". say�y� giriniz:");
					int sayi = input.nextInt();
					sayilar2.add(sayi);
				}
				System.out.println(sayilar);// indis �nemli 0'dan ba�lad�k.
				for(int i =0; i<5; i++)
				{
					toplam+= sayilar2.get(i);
				}
				ortalama = toplam/sayilar2.size();
				System.out.println("Ortalama: "+ortalama);
				
				
				// clear();
				// size();
				// contains();
				// toArray();

	}

}
