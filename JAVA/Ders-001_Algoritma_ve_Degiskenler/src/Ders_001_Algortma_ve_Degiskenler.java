// Algoritma
/*

Algoritma: Bir sorunu çözmek veya belirlenmiş bir amaca ulaşmak için tasarlanan yola,
takip edilen işlem basamaklarına denir. Algoritmalar açıkça belirtilmiş bir başlangıcı
ve sonu olan işlemler kümesidir.

Amaca ulaşmak için işlenecek çözüm yolları ve sıralamaları belirlenir ve algoritma bu sırayı takip ederek en mantıklı
çözüme ulaşır.


    Giriş/Çıkış Bilgisi: Algoritmalarda giriş ve çıkış bilgileri olmalıdır. Dışarıdan gelen verilere giriş bilgisi denir.
        Bu veriler algoritmada işlenir ve çıkış bilgisini oluşturur. Çıkış bilgisi her algoritmada mutlaka vardır.
        Algoritmaların temel amacı giriş bilgisini işleyerek çıkış bilgisi oluşturmaktır.

    Sonluluk: Her türlü olasılık için algoritma sonlu adımda bitmelidir. Algoritma sonsuz döngüye girmemelidir.
        Başı ve sonu belli olmalıdır.
    Kesinlik: Her komut kişinin kalem ve kağıt ile yürütebileceği kadar basit olmalıdır. Algoritmanın her adımı anlaşılır,
        basit ve kesin bir biçimde ifade edilmiş olmalıdır. Kesinlikle yorum gerektirmemeli ve belirsiz ifadelere sahip
        olmamalıdır.
    Etkinlik: Yazılan algoritmalar etkin ve dolayısıyla gereksiz tekrarlardan uzak oluşturulmalıdır.
        Bu algoritmanın temel özelliklerinden birisidir. Ayrıca algoritmalar genel amaçlı yazılıp yapısal bir ana
        algoritma ve alt algoritmalardan oluşturulmalıdır.
        Böylece daha önce yazılmış bir algoritma daha sonra başka işlemler için de kullanılabilir.
        Buna örnek vermek gerekirse eğer elimizde, verilen n adet sayının ortalamasını bulmakta kullandığımız algoritma
        varsa bu algoritma, bir sınıfta öğrencilerin yaş ortalamasını bulan bir algoritma için de kullanılabilmelidir.
    Başarım ve Performans: Amaç donanım gereksinimi (bellek kullanımı gibi), çalışma süresi gibi performans kriterlerini
        dikkate alarak yüksek başarımlı programlar yazmak olmalıdır. Gereksiz tekrarlar ortadan kaldırılmalıdır.
        Bir algoritmanın performans değerlendirmesinde aşağıdaki temel kriterler göz önünde bulundurulur.
            Birim İşlem Zamanı
            Veri Arama ve Getirme Zamanı
            Kıyaslama Zamanı
            Aktarma Zamanı

İlk algoritma, El-Harezmi’nin ‘Hisab-el Cebir ve El Mukabala’ kitabında sunulmuştur
ve algoritma kelimesi de El-Harezmi’nin isminden gelmiştir.

Örnek 1: Kullanıcı tarafından belirlenen 3 farklı sayının ortalamasını alalım.

Bu algoritmadaki değişkenlerimiz : x,y,z,sonuc

İ0: Başla.
İ1: x sayısını gir.
İ2: y sayısını gir.
İ3: z sayısını gir.
İ4: sonuc = (x+y+z)/3 işlemini yap.
İ5: sonuc değişkenini göster.
İ6: Dur.

Akış Diyagramları: algoritmanın okunması ve takibi karıştırmaya müsait bir yapı olmasından dolayı
    algoritmanın görselleştirilmiş halidir.

ÖDEV: Görsellere bak!

*/

// Değişkenler

public class Ders_001_Algortma_ve_Degiskenler {

	public static void main(String[] args) {
		//Programımızın Çalışma Kapsamı Başlangıcı
		
		//Açıklama Satırı: Bu satırlar derleyici tarafından dikkate alınmaz.
		
		/* Çoklu Açıklama Satırı
		 * Mehmet DEMİR
		 * Bu Programı Java Kursunda Yazıyporum
		 * Bu satırları dikkate almayın
		 * 
		 */
		/**
		 * @author Mehmet DEMİR
		 * @version 2.1
		 * @since 1865
		 */
		System.out.println("Merhaba Mecidiyeköy");
		
		Test();
		
		// İlkel Veri Tipleri: Stack'te tutulur.
		//*******************
		//*******************
		
		// boolean: 1 bitlik veri tutar. true/false : Mantıksal veri tutar.
		
		
		// değişkenTipi Adı = Değeri;
		boolean boolDegisken1 = true;
		boolean boolDegisken2;
		boolDegisken2 = false;
		boolDegisken2 = 8<9;
		
		System.out.println(boolDegisken2);
		
		// byte: 8 bitlik veri tutar. -128 ile +127 arasındaki değüerleri tutar.
		
		byte byteDegisken1 = 27;
		
		//byte 4Sayi = 45; // Yanlış
		byte Sayi4 = 45; // Doğru
		
		//byte kucuk Sayi = 3; // Yanlış
		byte kucukSayi = 3; // Doğru: camelCase
		byte BuyukSayi = 5; // Doğru: PascalCase
		byte orta_sayi = 4; // Doğru: SnakeCase
		//byte leziz-sayi =90;// Yanlış: kebab-case
		
		
		// short: 16 bitlik veri tutar.
		
		short shortDegisken1 = 32000;
//		short shortDegisken2 = 33000; // Kapasitesinden büyük veri atadığımız için hata veriyor.
		
		// int: 32 bitlik veri tutar.
		
		int intDegisken1 = 33000;
		
		// long: 64 bitlik veri tutar.
		
		long longDegisken1 = 789456123;
		
		// float: 32 bitlik ondalıklı sayı tutar.
		
		float floatDegisken1 = 3.14F;
		float floatDegisken2 = 45.9f;
		
		// double: 64 bitlik ondalıklı sayı.
		
		double doubleDegisken1 = 3.14;
		double doubleDegisken2 = 45.9D;
		double doubleDegisken3 = 78.3d;
		
		// char: 16 bitlik veri tutar. Tek bir karakter/harf veya ASCII tablsoundaki sayısal değeri tutar.
		
		char charDegisken1 = 'A';
		char charDegisken2 = 65; // A harfinin ASCII tablosundaki sayısal değerinin atadık.
		
		System.out.println(charDegisken2);
				
				
		// İlkel Olmayan (Non-Primitif) Veri Tipleri : Heap'te tutulur. (Sınıf nesneleri ve Diziler de burada tutulur.)
		
				
		String cumle = "Bu c�mle k�sa veya uzun olaca��ndan boyutu sabit bir veri tipinde saklanamaz.";
			   //cumle = 1948; // int tipi String'e atanamayaca��ndan TypeMismatch hatas� verir.
				
		Object nesne = "Be�ikta�"; // Object s�n�f� t�m tiplerin �st s�n�f� oldu�u i�in her t�rden veri saklayabilir.
		nesne = 1948; //int
		nesne = 15.9D;//double
		nesne = 'D';  //char
		
		// ÖRNEKLER:
		/*
		int a = 77;
		int b = 33;
		// Ekrana birşeyler yazdırmada kullanılır.
		System.out.println("a ve b sayılarının toplamı:"+(a+b));
		*/
		
		// isimlendirme �ekilleri: Notasyonlar.
		/*
		byte camelCase = 45;
		byte PascalCase = 45;
		byte Snake_Case = 45;
		
		//byte kebab-case = 45  // Java'da kullanılamaz.
		*/
		
		String isim = "Alican";
		String soyisim = "AKYILDIZ";		
		boolean ornegiMi = isim instanceof String;
		System.out.println(ornegiMi);
		

	}

}



























