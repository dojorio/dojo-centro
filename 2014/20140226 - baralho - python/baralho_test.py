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

    def test_dez_cartas(self):
        self.assertEqual(baralho(19), ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 4, 8, 12, 16, 2, 10, 18, 14], 6))
#Discarded cards: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 4, 8, 12, 16, 2, 10, 18, 14
#Remaining card: 6
unittest.main()
