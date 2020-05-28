package Abs;
public class Run {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		BeyazEsya beyazEsya = new BeyazEsya();
		beyazEsya.Marka = "Beko";
		beyazEsya.Model = "B490";
		beyazEsya.Fiyat = 2000;
		
		beyazEsya.BaglantiAc();
		
		String sorgu = "INSERT INTO BeyazEsyalar (Marka,Model,Fiyat)"
				+ "VALUES("+beyazEsya.Marka+","+beyazEsya.Model+","+beyazEsya.Fiyat+")";
		beyazEsya.Kaydet(sorgu);
		
		beyazEsya.BaglantiKapat();
	}
	
	/*
	 * ÖDEV: Temel Abstract Sýnýf: Marka,CPU,RAM,Fiyat
	 * Metotlar: Abs Kaydet(); Abs BilgiListele();
	 * 
	 * Dizustu: EkranBoyut,Kaydet(),BilgiListele()
	 * 
	 * Masaustu: KasaTipi, GucKaynagi, FanSayisi, Kaydet(), BilgiListele()
	 * 
	 * */

}
