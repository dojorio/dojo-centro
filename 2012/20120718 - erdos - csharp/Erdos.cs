using System;
using System.Collections.Generic;

public class Erdômetro
{
	Dictionary<string, List<string>> autores = 
		new Dictionary<string, List<string>>();
	
	public int Distância(string nome) {
		var lista = new List<List<string>>();
		lista.Add(new List<string> { nome });
		
		for(int nivel=0;;nivel++) {
			if (lista[nivel].Contains("Erdos"))
				return nivel;
			
			lista.Add(new List<string>());
			
			foreach(var autor in lista[nivel]) {
				foreach(var coautor in autores[autor]) {
					lista[nivel+1].Add(coautor);	
				}
			}
		}
	}
	
	public void AdicionaLivro(params string[] livro) {
		foreach(var autor in livro) {
			if (!autores.ContainsKey(autor)) {
				autores[autor] = new List<string>();
			}
			foreach(var coautor in livro) {
				autores[autor].Add(coautor);
			}
		}
	}
}