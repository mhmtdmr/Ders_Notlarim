
public class Ders_007_Hazir_Metotlar {

	public static void main(String[] args) {
		
		// Metinsel İşlem Fonksiyonları
		
		// n. karakteri döndüren fonk.
		String myStr = "Hello";
		char result = myStr.charAt(0);
		System.out.println(result);  // H
		
		// n. karakterin Unicode değerini döndüren fonk.
		String myStr2 = "Hello";
		int result2 = myStr.codePointAt(0);
		System.out.println(result2);
		
		// metinsel eşitlik-fark döndüren fonk. (Büyük küçük harf duyarlı)
		String myStr11 = "Hello";
		String myStr22= "hello";
		System.out.println(myStr11.compareTo(myStr22));
		// Eşitse 0 döner, değilse ASCII karakterleri farkını döner.
		
		// metinsel eşitlik-fark döndüren fonk. (Büyük küçük harf duyarsız)
		String myStr111 = "HELLO";
		String myStr222 = "hello";
		System.out.println(myStr111.compareToIgnoreCase(myStr222));
		// Eşitse 0 döner, değilse karakter sayısı farkını döner.
		
		// metinsel birleştirme
		String firstName = "John ";
		String lastName = "Doe";
		System.out.println(firstName.concat(lastName));
		
		// metin başka bir metini içeriyior mu? kontrol fonk.
		String myStr12 = "Hello";
		System.out.println(myStr12.contains("Hel"));   // true
		System.out.println(myStr12.contains("e"));     // true
		System.out.println(myStr12.contains("Hi"));    // false
		
		// Metinsel değer eşitmi konrolü
		String myStr13 = "Hello";
		System.out.println(myStr13.contentEquals("Hello"));  // true
		System.out.println(myStr13.contentEquals("hello"));  // false
		System.out.println(myStr13.contentEquals("e"));      // false
		System.out.println(myStr13.contentEquals("Hi"));     // false
		
		// Bir metindeki karakterlerin belirli bir kısmını alma
	    char[] myStr14 = {'H', 'e', 'l', 'l', 'o'};
	    String myStr24 = "";
	    myStr24 = myStr24.copyValueOf(myStr14, 0, 2);
	    System.out.println("Returned String: " + myStr24);   // He
	    
	    
	    // bir metinin belirli bir metin ile bitip bitmediğini bulan fonk.
	    String myStr33 = "Hello";
	    System.out.println(myStr33.endsWith("Hel"));   // false
	    System.out.println(myStr33.endsWith("llo"));   // true
	    System.out.println(myStr33.endsWith("o"));     // true
	    
	 // bir metinin belirli bir metin ile başlayıp başlamadığını bulan fonk.
	    String myStr44 = "Hello";
	    System.out.println(myStr44.startsWith("Hel"));   // true
	    System.out.println(myStr44.startsWith("llo"));   // false
	    System.out.println(myStr44.startsWith("o"));     // false
	    
	    
	    // Metinsel eşitlik kontrolü(Büyük küçük duyarlı)
	    
	    String myStr1111 = "Hello";
	    String myStr2222 = "Hello";
	    String myStr3333 = "Another String";
	    System.out.println(myStr1111.equals(myStr2222)); // Returns true because they are equal
	    System.out.println(myStr1111.equals(myStr3333)); // false
	    
	    // Metinsel eşitlik kontrolü(Büyük küçük duyarsız)
	    String myStr01 = "Hello";
	    String myStr02 = "HELLO";
	    String myStr03 = "Another String";
	    System.out.println(myStr01.equalsIgnoreCase(myStr02)); // true
	    System.out.println(myStr01.equalsIgnoreCase(myStr03)); // false
	    
	    
	    // format()
	    

	    
	    
	    // formatlayıcılar
	    /*
	    %a : 	floating point (except BigDecimal) 	 : Returns Hex output of floating point number.
	    %b :  	Any type 	 : "true" if non-null, "false" if null
	    %c :  	character 	 : Unicode character
	    %d :  	integer (incl. byte, short, int, long, bigint) 	 : Decimal Integer
	    %e :  	floating point 	 : decimal number in scientific notation
	    %f :  	floating point 	 : decimal number
	    %g :  	floating point 	 : decimal number, possibly in scientific notation depending on the precision and value.
	    %h :  	any type 	 	 : Hex String of value from hashCode() method.
	    %n :  	none 			 : Platform-specific line separator.
	    %o :  	integer (incl. byte, short, int, long, bigint) 	 : Octal number
	    %s :  	any type 		 : String value
	    %t :  	Date/Time (incl. long, Calendar, Date and TemporalAccessor) 	 : %t is the prefix for Date/Time conversions. More formatting flags are needed after this. See Date/Time conversion below.
	    %x :  	integer (incl. byte, short, int, long, bigint) 	 : 	    Hex string.
	    */
	    
	    
        String str1 = String.format("%d", 101);          // Integer value  
        String str2 = String.format("%s", "Amar Singh"); // String value  
        String str3 = String.format("%f", 101.00);       // Float value  
        String str4 = String.format("%x", 101);          // Hexadecimal value  
        String str5 = String.format("%c", 'c');          // Char value  
        System.out.println(str1);  
        System.out.println(str2);  
        System.out.println(str3);  
        System.out.println(str4);  
        System.out.println(str5); 	    
        /*
        String str1 = String.format("%d", 101);  
        String str2 = String.format("|%10d|", 101);  // Specifying length of integer  
        String str3 = String.format("|%-10d|", 101); // Left-justifying within the specified width  
        String str4 = String.format("|% d|", 101);   
        String str5 = String.format("|%010d|", 101); // Filling with zeroes  
        System.out.println(str1);  
        System.out.println(str2);  
        System.out.println(str3);  
        System.out.println(str4);  
        System.out.println(str5);  
	    */
	    
	    
	    String name="sonoo";  
	    String sf1=String.format("name is %s",name);  
	    String sf2=String.format("value is %f",32.33434);  
	    String sf3=String.format("value is %32.12f",32.33434);//returns 12 char fractional part filling with 0  
	      
	    System.out.println(sf1);  
	    System.out.println(sf2);  
	    System.out.println(sf3);
	    
	    
	    
	    
	    // Metinde bir karakterin veya alt karakter dizisinin ilk görüldüğü indis
	    
	    String myStr41 = "Hello planet earth, you are a great planet.";
	    System.out.println(myStr41.indexOf("planet"));
	    System.out.println(myStr41.indexOf("planet",7)); // 7. indisden itibaren bakar.
	    
	    /*
	        public int indexOf(int char) // ASCII'deki kodu ile arama yapmak için.
			public int indexOf(int char, int fromIndex)
	     */
		
		
		// Metin boş mu
	    
	    String myStr10 = "Hello";
	    String myStr20 = "";
	    System.out.println(myStr10.isEmpty()); // false
	    System.out.println(myStr20.isEmpty()); // true
	    
	    // metinsel değişiklik.
	    
	    // karakteri değiştirme
	    String myStr5 = "Hello";
	    System.out.println(myStr5.replace('l', 'p')); // Heppo
	    
	    // metin değiştirme
	    
	    // replaceFirst(String regex, String replacement) // sadece bulunan ilk değeri değiştirir.
	    // replaceAll(String regex, String replacement)   // bulunan tüm değerleri değiştirir.
	    
	    
	    
	    
	    
	    // metinsel parçalama: metin dizisine / işaretlerinden parçalayıp atar.
	    
		String str = new String("28/12/2013");

		String array1[]= str.split("/");
		for (String temp: array1){
		      System.out.println(temp);
		}
		
		// limit:2 olduğu için ilk / den 2 parçaya böler,bırakır
		String array2[]= str.split("/", 2);
		for (String temp: array2){
		      System.out.println(temp);
		}

		// limit sonsuz:0
		String array3[]= str.split("/", 0);
		for (String temp: array3){
		      System.out.println(temp);
		}
		
		
		// Büyük veya küçüğe dönüştürme
		
		String txt = "Hello World";
		System.out.println(txt.toUpperCase());
		System.out.println(txt.toLowerCase());
		
	    // Kenar boşluklarını silme.
		
		String myStr21 = "       Hello World!       ";
		System.out.println(myStr21);
		System.out.println(myStr21.trim());
		
	    
	    
		// Aynı değerde bir değişken varsa yenisi oluşturulmadan eskisi referans gösterilerek  yeni isme atanır.
		
		String str113 = "beginnersbook";    
		
		/* The Java String intern() method searches the string "beginnersbook"  
		 * in the memory pool and returns the reference of it.
		 */
		String str213 = new String("beginnersbook").intern(); 
		//prints true 
		System.out.println("str1==str2: "+(str1==str2));
		
		
		
		
		
		// Kaynaklar
		
		/* https://www.w3schools.com/java/
		 * https://www.programiz.com/java-programming/
		 * https://beginnersbook.com/java-tutorial-for-beginners-with-examples/
		 */
		
		
		
		
		
		

	}

}
