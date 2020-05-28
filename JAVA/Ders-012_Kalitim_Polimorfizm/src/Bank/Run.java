package Bank;

public class Run {

	public static void main(String[] args) {
		// Ana sınıf: Banka: AdSoyad,IBAN,Bakiye  EFT(): Bu metot gönderim ücreti olarak 5₺ alsın.
		// Alt sınıf: Garanti: EFT(): Bu metot gönderim ücreti olarak 15₺ alsın.
		// Alt sınıf: Halk: EFT(): Bu metot gönderim ücreti olarak 0₺ alsın:(bunu siz ekleyiniz.)
		// Alt sınıf: CHB: Varsayılan metotları kullanır.
		
		Banka b_musteri = new Banka();
		b_musteri.AdSoyad = "Mehmet DEMİR";
		b_musteri.IBAN = "TR07856468912300";
		b_musteri.Bakiye = 500;
		EFT(b_musteri,"TR2134234001254",(double)200);
		System.out.println("Bakiyeniz: "+b_musteri.Bakiye);

		System.out.println();
		
		CHB c_musteri = new CHB();
		c_musteri.AdSoyad = "Yutangu Yumatu";
		c_musteri.IBAN = "TR78965432133";
		c_musteri.Bakiye = 7500;
		EFT(c_musteri,"TR654321987",1000);
		
		System.out.println();
		
		Garanti g_musteri = new Garanti();
		g_musteri.AdSoyad="Ahmet AKYÜREK";
		g_musteri.IBAN = "TR125487963524";
		g_musteri.Bakiye = 9870;
		EFT(g_musteri,"TR07856468912300",5000);
		System.out.println("Bakiyeniz: "+g_musteri.Bakiye);
		
	}
	public static void EFT(Banka banka,String hedefIban, double miktar)
	{
		banka.EFT(hedefIban,miktar);
	}

}
