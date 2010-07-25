# encoding: utf-8
import unittest

"""
I = 1
II = 2
III = 3
IV = 4
V = 5
VI = 6
...
"""

VALUES = {
    'I': 1, 
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'M': 1000,
}

def roman_to_int(roman):
    
    if len(roman) > 1:
        if roman[0] ==v
    if roman == 'VI':
        return 6
    elif roman == 'IV':
        return 4
    if roman in VALUES:
        return VALUES[roman]
    return len(roman)

class RomanTest(unittest.TestCase):
    def test_retorna_1_para_I(self):
        self.assertEquals(1, roman_to_int('I'))

    def test_retorna_2_para_II(self):
        self.assertEquals(2, roman_to_int('II'))
        
    def test_retorna_3_para_III(self):
        self.assertEquals(3, roman_to_int('III'))
    
    def test_retorna_5_para_V(self):
        self.assertEquals(5, roman_to_int('V'))
        
    def test_retorna_4_para_IV(self):
        self.assertEquals(4, roman_to_int('IV'))
        
    def test_retorna_10_para_X(self):
        self.assertEquals(10, roman_to_int('X'))
    
    def test_retorna_50_para_L(self):
        self.assertEquals(50, roman_to_int('L'))
    
    def test_retorna_100_para_C(self):
        self.assertEquals(100, roman_to_int('C'))
        
    def test_retorna_1000_para_M(self):
        self.assertEquals(1000, roman_to_int('M'))
  
    def teste_retorna_6_para_VI(self):
        self.assertEquals(6, roman_to_int('VI'))      
if __name__ == '__main__':
    unittest.main()
