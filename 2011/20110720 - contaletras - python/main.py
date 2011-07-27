from unittest import TestCase, main

def contaLetrasEmUmNumero(numero):
    mapa = {
        1:len("um"),
        2:len("dois"),
        3:len("tres"),
        4:len("quatro"),
        5:len("cinco"),
        6:len("seis"),
        7:len("sete"),
        8:len("oito"),
        9:len("nove"),
        10:len("dez"),
        11:len("onze"),
        12:len("doze"),
        13:len("treze"),
        14:len("catorze"),
        15:len("quinze"),
        16:len("dezesseis"),
        17:len("dezessete"),
        18:len("dezoito"),
        19:len("dezenove"),
        20:len("vinte"),
        30:len("trinta"),
    }
    
    if numero > 20:
        dezenas = numero / 10 # 2
        retorno = mapa[dezenas * 10] # mapa[20]
        unidades = numero % 10
        if unidades:
            retorno += len("e")
            retorno += mapa[unidades]
        
        return retorno
         
    return mapa[numero]

def somaTodasAsPalavras(numero):
    numeros = range(1, numero+1)
    totalLetras = map(contaLetrasEmUmNumero, numeros)
    return sum(totalLetras)
    
class ContaLetraTeste(TestCase):
    def test_entrada_1_retorno_2(self):
        self.assertEquals(contaLetrasEmUmNumero(1), len("um"))
        
    def test_entrada_2_retorno_4(self):
        self.assertEquals(contaLetrasEmUmNumero(2), len("dois"))
        
    def test_entrada_3_retorno_4(self):
        self.assertEquals(contaLetrasEmUmNumero(3), len("tres"))

    def test_entrada_4_retorno_6(self):
        self.assertEquals(contaLetrasEmUmNumero(4), len("quatro"))
        
    def test_entrada_5_retorno_5(self):
        self.assertEquals(contaLetrasEmUmNumero(5), len("cinco"))

    def test_entrada_10_retorno_3(self):
        self.assertEquals(contaLetrasEmUmNumero(10), len("dez"))

    def test_entrada_21_retorno_8(self):
        self.assertEquals(contaLetrasEmUmNumero(21), len("vinteeum"))

    def test_entrada_22_retorno_10(self):
        self.assertEquals(contaLetrasEmUmNumero(22), len("vinteedois"))

    def test_entrada_30_retorno_10(self):
        self.assertEquals(contaLetrasEmUmNumero(30), len("trinta"))
        
class SomaLetrasTeste(TestCase):
    def test_total_de_caracteres_dos_numeros_de_1_ate_2(self):
        self.assertEquals(somaTodasAsPalavras(2), len("umdois"))

    def test_total_de_caracteres_dos_numeros_de_1_ate_5(self):
        self.assertEquals(somaTodasAsPalavras(5), len("umdoistresquatrocinco"))
        
    def test_total_de_caracteres_dos_numeros_de_1_ate_10(self):
        self.assertEquals(somaTodasAsPalavras(10), 
            len("umdoistresquatrocincoseisseteoitonovedez"))

    def test_total_de_caracteres_dos_numeros_de_1_ate_20(self):
        self.assertEquals(somaTodasAsPalavras(20), 
            len("umdoistresquatrocincoseisseteoitonovedez"
                + "onzedozetrezecatorzequinzedezesseisdezessetedezoitodezenovevinte"))
                    
        
        
if __name__ == "__main__":
    main()

