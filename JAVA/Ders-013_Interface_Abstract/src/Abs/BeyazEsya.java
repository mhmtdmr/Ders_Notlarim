package Abs;
public class BeyazEsya extends Veritabani {
	String Marka;
	String Model;
	double Fiyat;
	
	@Override
	public void Kaydet(String sorgu) {
		System.out.println("V.T. Sorgusu: "+sorgu);
	}
}
