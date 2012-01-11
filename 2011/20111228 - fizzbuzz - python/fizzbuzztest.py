#!/usr/bin/python

import unittest
from fizzbuzz import fizzbuzz


class Test(unittest.TestCase):
    def test_passa_um_retorna_um(self):
        self.assertEqual(1, fizzbuzz(1))
        
    def test_passa_dois_retorna_dois(self):
        self.assertEqual(2, fizzbuzz(2))
        
    def test_passa_tres_retorna_fizz(self):
        self.assertEqual("Fizz", fizzbuzz(3))
        
    def test_passa_quatro_retorna_quatro(self):
        self.assertEqual(4, fizzbuzz(4))
    
    def test_passa_seis_retorna_fizz(self):
        self.assertEqual("Fizz", fizzbuzz(6))
        
    def test_passa_cinco_retorna_buzz(self):
        self.assertEqual("Buzz", fizzbuzz(5))
        
    def test_passa_dez_retorna_buzz(self):
        self.assertEqual("Buzz", fizzbuzz(10))
        
    def test_passa_vinte_retorna_buzz(self):
        self.assertEqual("Buzz", fizzbuzz(20))
        
    def test_passa_quinze_retorna_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizzbuzz(15))
    
    def test_passa_30_retorna_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizzbuzz(30))
    
    def test_passa_45_retorna_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizzbuzz(45))
    
    
unittest.main()
