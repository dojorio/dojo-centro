#coding: utf-8
import unittest
from bridezilla import bridezilla

class BridezillaTestCase(unittest.TestCase):
    def test_dois_casais_caretas(self):
        resultado = bridezilla(2, tuple())
        self.assertEqual(['M0', 'M1'], resultado)

        

unittest.main()