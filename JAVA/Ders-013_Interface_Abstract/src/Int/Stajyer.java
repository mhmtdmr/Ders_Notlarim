package Int;

public class Stajyer implements IPersonel,Isgk{
// IPersonel interface'inde bu metot belirtildiði için tanýmlamak zorundayýz.
	@Override
	public void BilgiYazdir() {
		System.out.println("Stajyer bilgileri:");
	}
	
	@Override
	public void SigortaOde()
	{
		System.out.println("Personel sigortasý ödendi.");
	}
}
