using System;
using NUnit.Framework;

class QuebraDeLinha {
    public static string Quebrar(string input, int columns) {
        return "";
    }
}

class QuebraDeLinhaTestes {
    [Test]
    public void ao_quebrar_string_vazia_retorna_uma_string_vazia() {
        var esperado = "";
        var encontrado = QuebraDeLinha.Quebrar("", 80);
        Assert.AreEqual(esperado, encontrado);
    }
}