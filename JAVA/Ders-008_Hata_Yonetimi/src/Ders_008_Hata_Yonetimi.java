import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.IOException;

public class Ders_008_Hata_Yonetimi {

	public static void main(String[] args) {

		// Programımızda hata alma olsalığı olan bir kod bloğumuz var ise;
		// bu hata ihtimaline karşı bir tedbir almamız icap eder.
		// try-catch blokları sayesinde hata olma olasılığı olan kod hata üretirse
		// catch bloğunda yazdığımız kod çalıştırılır.
		// Örnek: banka para transferi, eşzamanlı 2 hesapta işlem gerektirir.

		int num1, num2;
		try {
			/* 0'a bölme hatası olabileceğinden try bloğu kullandık. */

			num1 = 0;
			num2 = 62 / num1; // bu kısımda hata alır. buradan sonraki 2 satır çalıştırılmadan catch bloğu
								// çalıştırılır.
			System.out.println(num2);
			System.out.println("Burası ekrana yazıldıysa kod sorunsuz olarak çalıştırılmış demektir.");
		} catch (Exception e) {
			/* Exception sınıfı üst hata sınıfıdır. Tüm hata türlerini kapsar ve yakalar. */
			System.out.println("Hata oluştu." + e.toString()); // hata detayını yazdırdık.
		}
		System.out.println("try-catch bloğu sonlandı.");

		// Birden fazla catch kullanımı:
		try {
			/* 0'a bölme hatası olabileceğinden try bloğu kullandık. */

			num1 = 0;
			num2 = 62 / num1; // bu kısımda hata alır. buradan sonraki 2 satır çalıştırılmadan catch bloğu
								// çalıştırılır.
			System.out.println(num2);
			System.out.println("Hey I'm at the end of try block");
		} catch (ArithmeticException e) {
			/*
			 * ArithmeticException sınıfı aritmetiksel hataları kapsayan bir sınıftır. Bu
			 * blok sadece aritmetik hataları yakalar.
			 */
			System.out.println("Bölünen 0 olamaz.");
		} catch (Exception e) {
			/* Exception sınıfı üst hata sınıfıdır. Tüm hata türlerini kapsar ve yakalar. */
			System.out.println("Hata oluştu." + e.toString()); // hata detayını yazdırdık.
		}

		System.out.println("----------------------------------------");

		try {
			int a[] = new int[7];
			a[7] = 30 / 5;
			System.out.println("First print statement in try block");
		} catch (ArithmeticException e) {
			System.out.println("Warning: ArithmeticException");
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("Warning: ArrayIndexOutOfBoundsException");
		} catch (Exception e) {
			System.out.println("Warning: Some Other exception");
		} finally {
			// Buraya hata veya başarı durumu farketmeksizin çalışmasını istediğimiz kodları
			// yazabiliriz.
			// örnek: Veritabanı bağlantısı kapatma.
			System.out.println("Her durumda çalışsın!");
		}

		// Hiyeraşik try-catch kulllanımı:

		// main try-block
		try {
			// try-block2
			try {
				// try-block3
				try {
					int arr[] = { 1, 2, 3, 4 };
					/*
					 * I'm trying to display the value of an element which doesn't exist. The code
					 * should throw an exception
					 */
					System.out.println(arr[10]);
				} catch (ArithmeticException e) {
					System.out.print("Arithmetic Exception");
					System.out.println(" handled in try-block3");
				}
			} catch (ArithmeticException e) {
				System.out.print("Arithmetic Exception");
				System.out.println(" handled in try-block2");
			}
		} catch (ArithmeticException e3) {
			System.out.print("Arithmetic Exception");
			System.out.println(" handled in main try-block");
		} catch (ArrayIndexOutOfBoundsException e4) {
			System.out.print("ArrayIndexOutOfBoundsException");
			System.out.println(" handled in main try-block"); // Diğer catch'ler hata türünü karşılamadığından burada
																// yakalandı.
		} catch (Exception e5) {
			System.out.print("Exception");
			System.out.println(" handled in main try-block");
		}

		// el ile hata fırlatmak:
		System.out.println("Welcome to the Registration process!!");
		checkEligibilty(10, 39);
		System.out.println("Have a nice day..");

		// throws
		try {
			ThrowExample obj = new ThrowExample();
			obj.myMethod(1);
		} catch (Exception ex) {
			System.out.println(ex);
		}
		
		// throws ile aynı zamanda unchecked yapı sağlanmış olur.
		// Aşağıda örneği var.
		
		
		
		// Kendi hatamızı tanımlama
		try{
			System.out.println("Starting of try block");
			// I'm throwing the custom exception using throw
			throw new MyException("This is My error Message");
		}
		catch(MyException exp){
			System.out.println("Catch Block") ;
			System.out.println(exp) ;
		}

	}

	static void checkEligibilty(int stuage, int stuweight) {
		if (stuage < 12 && stuweight < 40) {
			throw new ArithmeticException("Student is not eligible for registration");
		} else {
			System.out.println("Student Entry is Valid!!");
		}
	}

}

// throws
class ThrowExample {

	// Metodumuz hata fırlatacaksa throws ile bunu belirttik. Belirtmeden hata
	// fırlatma durumunda derleme hatası alacaktık.
	void myMethod(int num) throws IOException, ClassNotFoundException {
		if (num == 1)
			throw new IOException("IOException Occurred");
		else
			throw new ClassNotFoundException("ClassNotFoundException");
	}
}

// Kendi hatamızı tanımlama
class MyException extends Exception {
	String str1;

	/*
	 * Constructor of custom exception class here I am copying the message that we
	 * are passing while throwing the exception to a string and then displaying that
	 * string along with the message.
	 */
	MyException(String str2) {
		str1 = str2;
	}

	public String toString() {
		return ("MyException Occurred: " + str1);
	}
}


// throws unchecked
class Main { 
    public static void main(String[] args) throws IOException{   // throws IOException: sayesinde aşağıdaki kod unchecked olur. 
    															 // Derleme sırasında IOException hata kontrolü yapılmaz.
    															 // Eklemezsek FileNotFoundException ihtimali olduğu için hata üretir.
        FileReader file = new FileReader("C:\\test\\a.txt"); 
        BufferedReader fileInput = new BufferedReader(file); 
          
        // Print first 3 lines of file "C:\test\a.txt" 
        for (int counter = 0; counter < 3; counter++)  
            System.out.println(fileInput.readLine()); 
          
        fileInput.close(); 
    } 
} 

/*
Bazı Hata Türleri

1- Error Sınıfı:
VirtualMachineError: JVM’nin çalışmasını etkileyen durumları inceler.
AWTError: Grafik arayüze ait hataları inceler.
OutOfMemoryError: Bellek yetersizliği durumlarını inceler.

2- Exception Sınıfı:
ClassNotFoundException: Olmayan bir dosyaya erişme istediği durumlarını inceler.
IOException: Giriş çıkış işlemlerindeki istenmeyen durumları inceler.
RunTimeException: Çalışma zamanı hatalarını inceler.
AritmeticException: Aritmetik hataları inceler.
NullPointerException: Herhangi bir nesneye null referanslı bir değişken ile ulaşılmaya çalışılan durumlarda fırlatılır.
IllegalArgumentException: Metotlara geçersiz argüman atamalarında fırlatılır.

İstisna Metotlar

getMessage() metodu: İstisna nesnesi içersindeki mesajı döner.
toString(): istisna mesajını istisna adını ili nokta ve arada bir boşluk ile döner.
printStackTrace(): oluşan istisnanın bilgilerini aşama aşama ekrana yazdırır.
getStackTrace(): oluşan istisnanın bilgilerini aşama aşama stacktrace tipinde bir dizi olarak döner.
 */

// Kaynaklar
/*
https://medium.com/gokhanyavas/javada-i%CC%87stisnalar-f7ec3838a623
https://www.geeksforgeeks.org/checked-vs-unchecked-exceptions-in-java/
https://beginnersbook.com/2013/04/java-checked-unchecked-exceptions-with-examples/

Ayrıca bakabilirsiniz: http://javayaz.com/?page_id=100
*/