#!/usr/bin/python

import unittest

from fizzbuzz import fizzbuzz


class Test(unittest.TestCase):
    def test_numero_primo(self):
        self.assertEqual(fizzbuzz(41), 41)
    
    def test_multiplo_de_3(self):
        self.assertEqual(fizzbuzz(6), "fizz")
    
    def test_multiplo_de_5(self):
        self.assertEqual(fizzbuzz(10), "buzz")
        
    def test_multiplo_de_3_e_5(self):
        self.assertEqual(fizzbuzz(15), "fizzbuzz")
        
    def test_numero_0(self):
        self.assertEqual(fizzbuzz(0), "fizzbuzz")
    
    def test_numero_negativo(self):
        self.assertEqual(fizzbuzz(-2), 6)
    
    
unittest.main()
