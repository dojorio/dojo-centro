using System;
using System.Linq;
using NUnit.Framework;

class QuebraDeLinha {
    public static string Quebrar(string input, int columns) {
        if(columns == 1){
            string resultado = "";
            for (int i = 0; i < input.Length; i++) {
                resultado += input[i] + "\n";
            }
            return resultado.Trim('\n');
        }
        return input;
    }
}

class QuebraDeLinhaTestes {
    [Test]
    public void ao_quebrar_string_vazia_retorna_uma_string_vazia() {
        var encontrado = QuebraDeLinha.Quebrar("", 80);
        var esperado = "";
        Assert.AreEqual(esperado, encontrado);
    }
    
    [Test]
    public void ao_quebrar_uma_letra_retorna_uma_letra(){
        var encontrado = QuebraDeLinha.Quebrar("A", 80);
        var esperado = "A";
        Assert.AreEqual(esperado, encontrado);
    }
    
    
    [Test]
    public void ao_quebrar_duas_letras_com_uma_coluna_retorna_em_duas_linhas(){
        var encontrado = QuebraDeLinha.Quebrar("AB", 1);
        var esperado = "A\nB";
        Assert.AreEqual(esperado, encontrado);

        encontrado = QuebraDeLinha.Quebrar("BW", 1);
        esperado = "B\nW";
        Assert.AreEqual(esperado, encontrado);
    }
    
    [Test]
    public void ao_quebrar_tres_letras_com_uma_coluna_retorna_em_tres_linhas(){
        var encontrado = QuebraDeLinha.Quebrar("ABC", 1);
        var esperado = "A\nB\nC";
        Assert.AreEqual(esperado, encontrado);

    }
   
    
    
}