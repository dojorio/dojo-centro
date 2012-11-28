#coding: utf-8
import unittest
from laser import laser

class TestLaser(unittest.TestCase):
    def test_nenhum_soldado(self):
        soldados = []
        self.assertEqual(0, laser(soldados))

    def test_um_soldado(self):
        soldados = [(1,1)]
        self.assertEqual(1, laser(soldados))

    def test_dois_soldados_em_fila(self):
        soldados = [(1,1), (1,2)]
        self.assertEqual(1, laser(soldados))


unittest.main()