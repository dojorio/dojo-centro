using System;
using NUnit.Framework;

public class ErdosTest
{
	[Test]
	public void DistanciaDeErdos()
	{
		var erdômetro = new Erdômetro();
		Assert.AreEqual(0, erdômetro.Distância("Erdos"));
	}
	
	[Test]
	public void DistanciaDeLopes()
	{
		var erdômetro = new Erdômetro();
		erdômetro.AdicionaLivro("Erdos", "Lopes");
		Assert.AreEqual(1, erdômetro.Distância("Lopes"));
	}
	
	[Test]
	public void DistanciaDeLopesComCarvalho()
	{
		var erdômetro = new Erdômetro();
		erdômetro.AdicionaLivro("Erdos", "Lopes");
		erdômetro.AdicionaLivro("Lopes", "Carvalho");
		Assert.AreEqual(1, erdômetro.Distância("Lopes"));
	}
	
	[Test]
	public void DistanciaDeCarvalho()
	{
		var erdômetro = new Erdômetro();
		erdômetro.AdicionaLivro("Erdos", "Lopes");
		erdômetro.AdicionaLivro("Lopes", "Carvalho");
		Assert.AreEqual(2, erdômetro.Distância("Carvalho"));
	}
	[Test]
	public void DistanciaDeAbreu()
	{
		var erdômetro = new Erdômetro();
		erdômetro.AdicionaLivro("Erdos", "Lopes");
		erdômetro.AdicionaLivro("Lopes", "Carvalho");
		erdômetro.AdicionaLivro("Carvalho", "Abreu");
		Assert.AreEqual(3, erdômetro.Distância("Abreu"));
	}
	[Test]
	public void DistanciaDeThimoteo()
	{
		var erdômetro = new Erdômetro();
		erdômetro.AdicionaLivro("Erdos", "Lopes");
		erdômetro.AdicionaLivro("Lopes", "Carvalho");
		erdômetro.AdicionaLivro("Carvalho", "Abreu");
		erdômetro.AdicionaLivro("Abreu", "Thimóteo");
		erdômetro.AdicionaLivro("Thimóteo", "Erdos");
		Assert.AreEqual(1, erdômetro.Distância("Thimóteo"));
	}
	[Test]
	public void DistanciaDeBernardes()
	{
		var erdômetro = new Erdômetro();
		erdômetro.AdicionaLivro("Erdos", "Lopes");
		erdômetro.AdicionaLivro("Bernardes", "Carvalho");
		Assert.AreEqual(int.MaxValue, erdômetro.Distância("Bernardes"));
	}
}


