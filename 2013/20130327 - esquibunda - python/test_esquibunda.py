#-*- coding: utf-8 -*-
import unittest
from esquibunda import esquibunda

class EsquibundaTestCase(unittest.TestCase):
    def test_planicie(self):
        montanha = []
        self.assertEquals(0, esquibunda(montanha))

    def test_lombada(self):
        montanha = [
            [1]
        ]
        self.assertEquals(1, esquibunda(montanha))

    def test_lombada_dupla(self):
        montanha = [
            [1, 2]
        ]
        self.assertEquals(2, esquibunda(montanha))

    def test_lombada_tripla(self):
        montanha = [
            [1, 2, 3]
        ]
        self.assertEquals(3, esquibunda(montanha))


    def test_lombada_tripla_com_pico_central(self):
        montanha = [
            [1, 3, 2]
        ]
        self.assertEquals(2, esquibunda(montanha))

    def test_lombada_dupla_invertida(self):
        montanha = [
            [2, 1]
        ]
        self.assertEquals(2, esquibunda(montanha))

    def test_lombada_tripla_com_vale_central(self):
        montanha = [
            [2, 1, 3]
        ]
        self.assertEquals(2, esquibunda(montanha))

    def test_1_1_1(self):
        montanha = [
            [1, 1, 1]
        ]
        self.assertEquals(1, esquibunda(montanha))


    def test_triplo_twist_carpado(self):
        montanha = [
            [2, 2, 3]
        ]
        self.assertEquals(2, esquibunda(montanha))


unittest.main()
