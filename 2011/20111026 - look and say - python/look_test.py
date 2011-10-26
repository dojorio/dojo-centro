import unittest
from look import *

class TestLookAndSay(unittest.TestCase):
    def test_numero_1(self):
        self.assertEqual(11, look_and_say(1))

    def test_numero_2(self):
        self.assertEqual(12, look_and_say(2))

    def test_numero_11(self):
        self.assertEqual(21, look_and_say(11))

    def test_numero_22(self):
        self.assertEqual(22, look_and_say(22))

    def test_numero_33(self):
        self.assertEqual(23, look_and_say(33))

    def test_numero_44(self):
        self.assertEqual(24, look_and_say(44))
        
    def test_numero_111(self):
        self.assertEqual(31, look_and_say(111))

    def test_numero_222(self):
        self.assertEqual(32, look_and_say(222))
        
    def test_numero_1111(self):
        self.assertEqual(41, look_and_say(1111))

    def test_numero_11111(self):
        self.assertEqual(51, look_and_say(11111))
        
    def test_numero_12(self):
        self.assertEqual(1112, look_and_say(12))   

    def test_numero_13(self):
        self.assertEqual(1113, look_and_say(13))  
    
    def test_numero_14(self):
        self.assertEqual(1114, look_and_say(14))  
        
    def test_numero_17(self):
        self.assertEqual(1117, look_and_say(17))
    
    def test_numero_1211(self):
        self.assertEqual(111221, look_and_say(1211))
        
    def test_numero_111221(self):
        self.assertEqual(312211, look_and_say(111221))

    def test_numero_111221(self):
        self.assertEqual(312211, look_and_say(111221))
    
    def test_encontrar_2o_sequencia(self):
        self.assertEqual(11,look_say_then_find(1,2))
    
    def test_encontrar_4o_sequencia(self):
        self.assertEqual(1211,look_say_then_find(1,4))
    
    def test_encontrar_6o_sequencia(self):
        self.assertEqual(312211,look_say_then_find(1,6))
    
    def test_soma_digitos_11(self):
        self.assertEqual(2, sum_digits(11))

    def test_soma_digitos_12(self):
        self.assertEqual(3, sum_digits(12))
        
unittest.main()