import unittest
from pulga import pulga

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
