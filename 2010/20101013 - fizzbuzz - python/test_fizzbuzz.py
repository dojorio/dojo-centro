import unittest
from fizzbuzz import *

class FizzbuzzTests(unittest.TestCase):

    def test_retorna_1_ao_receber_1(self):
        self.assertEqual(fizzbuzz(1), '1')

    def test_retorna_2_ao_receber_2(self):
        self.assertEqual(fizzbuzz(2), '2')

    def test_retorna_fizz_ao_receber_3(self):
        self.assertEqual(fizzbuzz(3), 'fizz')

    def test_retorna_4_ao_receber_4(self):
        self.assertEqual(fizzbuzz(4), '4')

    def test_retorna_buzz_ao_receber_5(self):
        self.assertEqual(fizzbuzz(5), 'buzz')

    def test_retorna_fizz_ao_receber_6(self):
        self.assertEqual(fizzbuzz(6), 'fizz')

    def test_retorna_fizz_ao_receber_9(self):
        self.assertEqual(fizzbuzz(9), 'fizz')

    def test_retorna_fizz_ao_receber_10(self):
        self.assertEqual(fizzbuzz(10), 'buzz')

    def test_retorna_fizzbuzz_ao_receber_15(self):
        self.assertEqual(fizzbuzz(15), 'fizzbuzz')
unittest.main()

