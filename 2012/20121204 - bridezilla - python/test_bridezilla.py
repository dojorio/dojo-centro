#coding: utf-8
import unittest
from bridezilla import bridezilla

class BridezillaTestCase(unittest.TestCase):
    def test_dois_casais_caretas(self):
        resultado = bridezilla(2, ())
        self.assertEqual(['M0', 'M1'], resultado)

    def test_dois_casais_e_um_relacionamento_extra(self):
        resultado = bridezilla(2, (('H0', 'H1'),))
        self.assertEqual(['M0', 'H1'], resultado)
        

unittest.main()