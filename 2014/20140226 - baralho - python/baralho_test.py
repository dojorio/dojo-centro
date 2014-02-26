import unittest
from baralho import baralho

class TestBaralho(unittest.TestCase):
    def test_uma_carta(self):
        self.assertEqual(baralho(1), ([], 1))

    def test_duas_cartas(self):
        self.assertEqual(baralho(2), ([1], 2))

    def test_três_cartas(self):
        self.assertEqual(baralho(3), ([1, 3], 2))

    def test_quarto_cartas(self):
        self.assertEqual(baralho(4), ([1, 3, 2], 4))

    def test_cinco_cartas(self):
        self.assertEqual(baralho(5), ([1, 3, 5, 4], 2))

unittest.main()
