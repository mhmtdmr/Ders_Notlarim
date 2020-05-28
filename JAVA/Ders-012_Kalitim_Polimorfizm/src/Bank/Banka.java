package Bank;

public class Banka {
	String AdSoyad;
	String IBAN;
	double Bakiye;
	public void EFT(String iban,double miktar)
	{
		double ucret = 5;
		if(this.Bakiye>=(miktar+ucret))
		{
			System.out.println("Para transferi gerçekleşti.\nGönderen IBAN:"+this.IBAN+"\nAlıcı IBAN:"+iban+"\nMiktar:"+miktar);
			this.Bakiye -= (miktar+ucret);
			System.out.println("İşlem Ücreti:"+ucret+"₺");
		}
		else 
		{
			System.out.println("Para transferi için yeterli bakiye mevcut değildir!!!");
		}
	}
}
