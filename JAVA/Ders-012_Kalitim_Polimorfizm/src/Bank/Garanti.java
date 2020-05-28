package Bank;

public class Garanti extends Banka {
	// Learn more, fear less
	public void EFT(String iban,double miktar)
	{
		double ucret = 15;
		if(this.Bakiye>=(miktar+ucret))
		{
			System.out.println("Para transferi gerçekleşti.\nGönderen IBAN:"+this.IBAN+"\nAlıcı IBAN:"+iban+"\nMiktar:"+miktar);
			this.Bakiye -= (miktar+ucret);
			System.out.println("İşlem Ücreti:"+ucret+"₺");
			System.out.println("Garanti Bankası İyi Günler Diler...");
			// Garanti bankasına özgü ekstra işlemler...
		}
		else 
		{
			System.out.println("Para transferi için yeterli bakiye mevcut değildir!!!");
		}
	}
}
