#coding: utf-8
import unittest
from bridezilla import *

class BridezillaTestCase(unittest.TestCase):
    def test_2_casais_caretas(self):
        resultado = bridezilla(2, ())
        self.assertEqual(['M0', 'M1'], resultado)

    def test_2_casais_e_1_relacionamento_extra(self):
        resultado = bridezilla(2, (('H0', 'H1'),))
        self.assertEqual(['M0', 'H1'], resultado)
    
    def test_2_casais_e_noiva_mansa(self):
        self.assertRaises(
            BarracoException, 
            lambda: bridezilla(2, (('H0', 'H1'), ('H0', 'M1')))
        )

    def test_3_casais_caretas(self):
        resultado = bridezilla(2, ())
        self.assertEqual(['M0', 'M1'], resultado)


unittest.main()