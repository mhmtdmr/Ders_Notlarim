import java.util.List;

public class Run {

	public static void main(String[] args) {
		/*
		// Kategori ekleme
		Kategori ktg = new Kategori();
		ktg.setAd("Siyaset");
		ktg.Kaydet();
		System.out.println("ktg _ID: "+ktg.getID());
		*/
		
		
		//Kategori arama, nesnesye atama
		//Kategori gelen = Kategori.getKategori(3);
		//System.out.println(gelen.getID()+ " --> " +gelen.getAd());
		
		
		// Kay�t G�ncelleme
		//gelen.setAd("Test");
		//gelen.Guncelle();
		
		//Kay�t Silme
		//gelen.Sil();
		
		
		// Kay�tlar� Listeleme
		/*
		List<Kategori> kategoriler = Kategori.getKategoriListe();
		
		for (Kategori kategori : kategoriler) {
			System.out.println("Kategori Ad�: "+kategori.getAd()+"  Kategori ID: "+kategori.getID());
		}
		*/
		
		
		Haber hbr = new Haber();
		hbr.yazar = new Yazar();
		hbr.yazar.Ad = "Mehmet";
		
	}

}
