import unittest
from pulga import pulga, casa_branca

class TestCasaBranca(unittest.TestCase):
    def test_10_11_1_branco(self):
        self.assertEqual(True, casa_branca(10, 11, 1));

    def test_10_1_1_preto(self):
        self.assertEqual(False, casa_branca(10, 1, 1));

    def test_10_21_1_preto(self):
        self.assertEqual(False, casa_branca(10, 21, 1));

    def test_10_10_1_indefinido(self):
        self.assertEqual(False, casa_branca(10, 10, 1));

    def test_10_21_11_branco(self):
        self.assertEqual(True, casa_branca(10, 21, 11));
    
    def test_10_11_11_preto(self):
        self.assertEqual(False, casa_branca(10,11, 11));

class TestPulga(unittest.TestCase):
    def test_ja_esta_na_casa_branca(self):
        s = 10
        x, y = 11, 1
        dx, dy = 1, 1
        self.assertEqual(0, pulga(s, x, y, dx, dy))

    def test_falta_1mm_para_chegar_na_casa_branca(self):
        s = 10
        x, y = 10, 0
        dx, dy = 1, 1
        self.assertEqual(1, pulga(s, x, y, dx, dy))

    def test_falta_1mm_no_x_para_chegar_na_casa_branca(self):
        s = 10
        x, y = 10, 5
        dx, dy = 1, 1
        self.assertEqual(1, pulga(s, x, y, dx, dy))

    def test_falta_1mm_no_y_para_chegar_na_casa_branca(self):
        s = 10
        x, y = 5, 10
        dx, dy = 1, 1
        self.assertEqual(1, pulga(s, x, y, dx, dy))

    def test_falta_1mm_em_x_com_x_30_para_chegar_na_casa_branca(self):
        s = 10
        x, y = 30, 5
        dx, dy = 1, 1
        self.assertEqual(1, pulga(s, x, y, dx, dy))

unittest.main()
