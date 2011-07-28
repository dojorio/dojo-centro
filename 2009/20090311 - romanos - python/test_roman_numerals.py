import unittest
from roman_numerals import *

class TestRomanNumerals(unittest.TestCase):
    
    def test_1(self):
        input = 1
        output = "I"
        
        self.assertEqual(decimal_to_roman(input), output)
    
    def test_2(self):
        input = 2
        output = "II"
        
        self.assertEqual(decimal_to_roman(input), output)
    
    def test_4(self):
        input = 4
        output = "IV"
        
        self.assertEqual(decimal_to_roman(input), output)
        
    def test_5(self):
        input = 5
        output = "V"
        
        self.assertEqual(decimal_to_roman(input), output)
        
    def test_6_8(self):
        input = {6:'VI', 7:'VII', 8:'VIII'}
        
        for i, o in input.items():
            self.assertEqual(decimal_to_roman(i), o)
            
    def test_9(self):
        input = 9
        output = "IX"
        
        self.assertEqual(decimal_to_roman(input), output)
    
    def test_10_13(self):
        
        input = {10:'X', 11:'XI', 12:'XII', 13:'XIII'}
        
        for i, o in input.items():
            self.assertEqual(decimal_to_roman(i), o)
            
        
        
if __name__ == "__main__":
    unittest.main()