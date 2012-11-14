#coding: utf-8
import unittest
from gattaca import gattaca

class TestGattaca(unittest.TestCase):
    def test_2_dominantes(self):
        # 0 -> 100%
        # 1 -> 0%
        self.assertEqual([1.0, 0.0], gattaca("AA", "AA"))

    def test_1_dominante_1_recessivo(self):
        self.assertEqual([1.0, 0.0], gattaca("AA", "aa"))

    def test_2_heterozigotos(self):
        self.assertEqual([0.75, 0.25], gattaca("Aa", "Aa"))

    def test_1_heterozigoto_1_recessivo(self):
        self.assertEqual([0.5, 0.5], gattaca("Aa", "aa"))

    def test_1_recessivo_1_heterozigoto(self):
        self.assertEqual([0.5, 0.5], gattaca("aa", "Aa"))

    def test_2_recessivos(self):
        self.assertEqual([0.0, 1.0], gattaca("aa", "aa"))

    def test_2_dominantes_e_2_dominantes(self):
        self.assertEqual([1.0, 0.0, 0.0], gattaca("AAAA", "AAAA"))

    def test_2_recessivos_e_2_heterozigotos(self):
        self.assertEqual([0.25, 0.5, 0.25], gattaca("aaaa", "AaAa"))

    def test_2_recessivos_e_2_recessivos(self):
        self.assertEqual([0.0, 0.0, 1.00], gattaca("aaaa", "aaaa"))


unittest.main()