import unittest
from rsa import *

class TesteGerarPhi(unittest.TestCase):
    def test_quando_os_primos_sao_2_e_3(self):
        resultado = phi(2,3)
        self.assertEqual(resultado, 1*2)

    def test_quando_os_primos_sao_3_e_5(self):
        resultado = phi(3,5)
        self.assertEqual(resultado, 2*4)

class TesteGerarE(unittest.TestCase):
    def test_que_e_de_4_eh_3(self):
        resultado = e(4)
        self.assertEqual(resultado, 3)
        
class TesteGerarD(unittest.TestCase):
    def test_quando_f_eh_4_e_eh_3(self):
        resultado = d(4, 3)
        self.assertEqual(resultado, 3)

    def test_quando_f_eh_10_e_eh_3(self):
        resultado = d(10, 3)
        self.assertEqual(resultado, 7) 

    def test_quando_f_eh_20_e_eh_3(self):
        resultado = d(20, 3)
        self.assertEqual(resultado, 7) 


    def test_quando_f_eh_9999999999_e_eh_100000(self):
        resultado = d(9999999999, 100000)
        self.assertEqual(resultado, 100000) 

        
        
          

unittest.main()
