package Polimorfizm;


public class AltSinif extends AnaSinif{
	
	String AltOzellik1;
	String AltOzellik2;
	
	@Override   //�st s�n�ftaki ayn� isimli metodu ezdi�imizi belirtik.
	public void MerhabaDunya()
	{
		System.out.println("Alt s�n�ftan merhaba d�nya..");
	}
	
	/*
	public void Topla(int a, int b)
	{
		System.out.println("Toplama sonucu:"+(a+b));
	}
	*/
	public void Topla(Object a, Object b)
	{		
		double s1 = ((Number)a).doubleValue();
		double s2 = ((Number)b).doubleValue();
		System.out.println("Toplama sonucu:"+(s1+s2));
	}
}
