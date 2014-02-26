import unittest
from baralho import baralho

class TestBaralho(unittest.TestCase):
    def test_uma_carta(self):
        self.assertEqual(baralho(1), ([], 1))

    def test_duas_cartas(self):
        self.assertEqual(baralho(2), ([1], 2))

    def test_três_cartas(self):
        self.assertEqual(baralho(3), ([1, 3], 2))

unittest.main()
