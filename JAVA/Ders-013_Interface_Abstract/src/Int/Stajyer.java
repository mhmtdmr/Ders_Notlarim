package Int;

public class Stajyer implements IPersonel,Isgk{
// IPersonel interface'inde bu metot belirtildi�i i�in tan�mlamak zorunday�z.
	@Override
	public void BilgiYazdir() {
		System.out.println("Stajyer bilgileri:");
	}
	
	@Override
	public void SigortaOde()
	{
		System.out.println("Personel sigortas� �dendi.");
	}
}
