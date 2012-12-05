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

    def test_2_casais_e_1_relacionamento_extra_invertido(self):
        resultado = bridezilla(2, (('H1', 'H0'),))
        self.assertEqual(['M0', 'H1'], resultado)
    
    def test_2_casais_e_deu_barraco(self):
        self.assertRaises(
            BarracoException, 
            lambda: bridezilla(2, (('H0', 'H1'), ('H0', 'M1')))
        )

    def test_3_casais_caretas(self):
        resultado = bridezilla(3, ())
        self.assertEqual(['M0', 'M1', 'M2'], resultado)

    def test_3_casais_e_1_relacionamento_extra(self):
        resultado = bridezilla(3, (('H1', 'M2'),))
        self.assertEqual(['M0', 'M1', 'M2'], resultado)

    def test_3_casais_e_1_relacionamento_gay(self):
        resultado = bridezilla(3, (('H1', 'H2'),))
        self.assertEqual(['M0', 'M1', 'H2'], resultado)

    def test_3_casais_e_1_relacionamento_gay2(self):
        resultado = bridezilla(3, (('H0', 'H2'),))
        self.assertEqual(['M0', 'M1', 'H2'], resultado)

    def test_3_casais_e_2_relacionamento_gay(self):
        resultado = bridezilla(3, (('H0', 'H2'), ('H1', 'H2')))
        self.assertEqual(['M0', 'M1', 'H2'], resultado)

    def test_3_casais_e_2_relacionamento_gay2(self):
        resultado = bridezilla(3, (('H0', 'H2'), ('H0', 'H1')))
        self.assertEqual(['M0', 'H1', 'H2'], resultado)

    def test_3_casais_e_2_relacionamentos(self):
        resultado = bridezilla(3, (('H0', 'H1'), ('H2', 'M1')))
        self.assertEqual(['M0', 'H1', 'H2'], resultado)

unittest.main()
