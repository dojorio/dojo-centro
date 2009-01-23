import junit.framework.*;

public class TesteConversao extends TestCase {

	public void test1() {
		ConversorInteiroParaRomano c = new ConversorInteiroParaRomano();
		String romano = c.converte(1);
		assertEquals("I", romano);
	}
	
	public void test2 ()
	{
		ConversorInteiroParaRomano c = new ConversorInteiroParaRomano();
		String romano = c.converte(2);
		assertEquals("II", romano);
	}
	
	public void test4 ()
	{
		ConversorInteiroParaRomano c = new ConversorInteiroParaRomano();
		String romano = c.converte(4);
		assertEquals("IV", romano);
	}
	
	public void test7 ()
	{
		ConversorInteiroParaRomano c = new ConversorInteiroParaRomano();
		String romano = c.converte(7);
		assertEquals("VII", romano);
	}
	
	public void test9 ()
	{
		ConversorInteiroParaRomano c = new ConversorInteiroParaRomano();
		String romano = c.converte(9);
		assertEquals("IX", romano);
	}
	
	public void test12 ()
	{
		ConversorInteiroParaRomano c = new ConversorInteiroParaRomano();
		String romano = c.converte(12);
		assertEquals("XII", romano);
	}
	
	public void test15 ()
	{
		ConversorInteiroParaRomano c = new ConversorInteiroParaRomano();
		String romano = c.converte(15);
		assertEquals("XV", romano);
	}
	public void test17 ()
	{
		ConversorInteiroParaRomano c = new ConversorInteiroParaRomano();
		String romano = c.converte(17);
		assertEquals("XVII", romano);
	}
	public void test18 ()
	{
		ConversorInteiroParaRomano c = new ConversorInteiroParaRomano();
		String romano = c.converte(18);
		assertEquals("XVIII", romano);
	}
	public void test20 ()
	{
		ConversorInteiroParaRomano c = new ConversorInteiroParaRomano();
		String romano = c.converte(20);
		assertEquals("XX", romano);
	}
	public void test40 ()
	{
		ConversorInteiroParaRomano c = new ConversorInteiroParaRomano();
		String romano = c.converte(40);
		assertEquals("XL", romano);
	}
	public void test50 ()
	{
		ConversorInteiroParaRomano c = new ConversorInteiroParaRomano();
		String romano = c.converte(50);
		assertEquals("L", romano);
	}
	public void test999 ()
	{
		ConversorInteiroParaRomano c = new ConversorInteiroParaRomano();
		String romano = c.converte(999);
		assertEquals("CMXCIX", romano);
	}
	public void teste1975 ()
	{
		ConversorInteiroParaRomano c = new ConversorInteiroParaRomano();
		String romano = c.converte(1975);
		assertEquals("MCMLXXV", romano);
	}
	public void teste3000 ()
	{
		ConversorInteiroParaRomano c = new ConversorInteiroParaRomano();
		String romano = c.converte(3000);
		assertEquals("MMM", romano);
	}
	public void teste4000 ()
	{
		ConversorInteiroParaRomano c = new ConversorInteiroParaRomano();
		String romano = c.converte(4000);
		assertNull(romano);
	}
}
