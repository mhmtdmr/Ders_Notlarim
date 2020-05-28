public class Ders_011 {

	public static void main(String[] args) {
		//Emlak ev = new Emlak();
		//ev.Aidat = 100;
		//System.out.println(ev.BinaYasi);
		//System.out.println(ev.Aidat);
		//System.out.println(ev.EsyaliMi);
		
		Emlak ev2 = new Emlak("EV002",(short)120,"Kiralýk",(short)5,"2+1",false,1700,50);
		System.out.println(ev2.ID);
		System.out.println(ev2.IlanTipi);
		
		/*
		Kullanici kln1 = new Kullanici();
		kln1.ID  ="KU001";
		kln1.Eposta = "test@test.com";
		kln1.Parola = "zxcaasdQWEs.987!!";
		ev2.kullanici = kln1;
		*/
		//Kullanici.Foto kf = kln1.new Foto(); // Inner Class Kullanma.
		
		ev2.kullanici = new Kullanici(); // Bu satýrý yazmazsak ram'de yer açýlmadýðýndan NullPointerException verecek.
		ev2.kullanici.Eposta = "asd@asd.com";
		
		System.out.println(ev2.kullanici.Eposta);
	}

}
