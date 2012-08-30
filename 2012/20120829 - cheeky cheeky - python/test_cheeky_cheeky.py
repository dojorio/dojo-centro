import unittest
from cheeky_cheeky import *

class TestCheekyCheeky(unittest.TestCase):
    def test_padrao123(self):
        self.assertEquals("123", identifica_padrao("123123"))

    def test_padrao1234(self):
        self.assertEquals("1234", identifica_padrao("12341234"))

    def test_padrao124123(self):
        self.assertEquals("124123", identifica_padrao("124123124123"))

    def test_padrao1234_12(self):
        self.assertEquals("1234", identifica_padrao("1234123412"))

    def test_padrao3412_34(self):
        self.assertEquals("3412", identifica_padrao("3412341234"))

    def test_padrao1(self):
        self.assertEquals("1", identifica_padrao("11"))
    
    def test_padrao_gigante(self):
        padrao = ''.join(str(x) for x in range(10000))
        self.assertEquals(padrao, identifica_padrao(padrao*2))

class TestNextSteps(unittest.TestCase):
    def test_proximos_8_123(self):
        self.assertEquals("12312312", proximos_n("123123"))

    def test_proximos_8_312(self):
        self.assertEquals("31231231", proximos_n("12312312"))

    def test_proximos_8_1(self):
        self.assertEquals("11111111", proximos_n("11"))
        
    def test_proximos_6_123(self):
        self.assertEquals("123123", proximos_n("123123", 6))

    def test_proximos_12_312(self):
        self.assertEquals("312312312312", proximos_n("12312312", 12))
        
    def test_proximos_80_1234(self):
        esperado = "1234" * 20
        self.assertEquals(esperado, proximos_n("12341234", 80))
    
    def test_proximos_80_1234(self):
        padrao = ''.join(str(x) for x in range(10000))
        esperado = padrao[:10000]
        self.assertEquals(esperado, proximos_n(padrao*2, 10000))
   
unittest.main()
