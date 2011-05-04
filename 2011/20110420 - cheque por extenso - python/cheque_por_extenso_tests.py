# coding:utf-8

import unittest
from cheque_por_extenso import cheque_por_extenso

class ChequePorExtensoTests(unittest.TestCase):
    def test_numeros_de_1_a_9(self):
        self.assertEqual(cheque_por_extenso(1), "um real")
        self.assertEqual(cheque_por_extenso(2), "dois reais") 
        self.assertEqual(cheque_por_extenso(3), "três reais")
        self.assertEqual(cheque_por_extenso(4), "quatro reais")
        self.assertEqual(cheque_por_extenso(5), "cinco reais")
        self.assertEqual(cheque_por_extenso(6), "seis reais")
        self.assertEqual(cheque_por_extenso(7), "sete reais")
        self.assertEqual(cheque_por_extenso(8), "oito reais")
        self.assertEqual(cheque_por_extenso(9), "nove reais")

        
    def test_numeros_de_11_a_19(self):
        self.assertEqual(cheque_por_extenso(11), "onze reais")
        self.assertEqual(cheque_por_extenso(12), "doze reais")
        self.assertEqual(cheque_por_extenso(13), "treze reais")
        self.assertEqual(cheque_por_extenso(14), "quatorze reais")
        self.assertEqual(cheque_por_extenso(15), "quinze reais")
        self.assertEqual(cheque_por_extenso(16), "dezesseis reais")
        self.assertEqual(cheque_por_extenso(17), "dezessete reais")
        self.assertEqual(cheque_por_extenso(18), "dezoito reais")
        self.assertEqual(cheque_por_extenso(19), "dezenove reais")
        
    def test_numeros_de_21(self):
        self.assertEqual(cheque_por_extenso(21), "vinte e um reais")
        
    def test_numeros_de_22(self):
        self.assertEqual(cheque_por_extenso(22), "vinte e dois reais")
    
    def test_numero_30(self):
        self.assertEqual(cheque_por_extenso(30), "trinta reais")
    
    def test_numeros_na_casa_dos_31(self):
        self.assertEqual(cheque_por_extenso(31), "trinta e um reais")
        
    def test_numero_40(self):
        self.assertEqual(cheque_por_extenso(40), "quarenta reais")

    def test_numero_55(self):
        
        self.assertEqual(cheque_por_extenso(55), "cinquenta e cinco reais")
    def test_numero_100(self):
        self.assertEqual(cheque_por_extenso(100), "cem reais")
    
    def test_numero_110(self):
        self.assertEqual(cheque_por_extenso(110), "cento e dez reais")
    
    def test_dezenas(self):
        self.assertEqual(cheque_por_extenso(10), "dez reais")
        self.assertEqual(cheque_por_extenso(20), "vinte reais")
        self.assertEqual(cheque_por_extenso(30), "trinta reais")
        self.assertEqual(cheque_por_extenso(40), "quarenta reais")
        self.assertEqual(cheque_por_extenso(50), "cinquenta reais")
        self.assertEqual(cheque_por_extenso(60), "sessenta reais")
        self.assertEqual(cheque_por_extenso(70), "setenta reais")
        self.assertEqual(cheque_por_extenso(80), "oitenta reais")
        self.assertEqual(cheque_por_extenso(90), "noventa reais")
    
unittest.main()