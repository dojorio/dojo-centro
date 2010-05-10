import unittest
from romanos import romanos

class RomanosTestCase(unittest.TestCase):
    def test_passando_I_retorna_1(self):
        self.assertEqual(1, romanos('I'))
    
    
    def test_passando_II_retorna_2(self):
        self.assertEqual(2, romanos('II'))
    
    
    def test_passando_III_retorna_3(self):
        self.assertEqual(3, romanos('III'))
    
    def test_passando_IV_retorna_4(self):
        self.assertEqual(4, romanos('IV'))
    
    def test_passando_V_retorna_5(self):
        self.assertEqual(5, romanos('V'))
 
    def teste_passando_VI_retorna_6(self):
        self.assertEqual(6, romanos('VI'))
        
    def teste_passando_VII_retorna_7(self):
        self.assertEqual(7, romanos('VII'))
        
    def teste_passando_VIII_retorna_8(self):
        self.assertEqual(8, romanos('VIII'))

    def teste_passando_IX_retorna_9(self):
        self.assertEqual(9, romanos('IX'))
        
if __name__ == '__main__':
    unittest.main()
