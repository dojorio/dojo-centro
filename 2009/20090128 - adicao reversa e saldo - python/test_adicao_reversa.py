import unittest
from adicao_reversa import *

class TestAdicaoReversa(unittest.TestCase):
    def teste_inverte_digito(self): 
        for i in range(10):
            self.assertEquals(i, inverter(i))
            
    def teste_inverte_dois_digitos(self):
        self.assertEquals(42, inverter(24))
        
    def teste_soma (self):
        self.assertEquals(59, adicao_reversa(12, 47))
        
    def teste_soma_tres_parcelas(self):
        self.assertEquals(811, adicao_reversa(12, 47, 32))
        
unittest.main()
