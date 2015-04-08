import unittest
from knight import knight_escape

class TestKnight(unittest.TestCase):
    def test_cavalo_solo(self):
        cavalo = 'c4'
        peoes = []
        self.assertEqual(knight_escape(cavalo, peoes), 8)

    def test_cavalo_solo_a1(self):
        cavalo = 'a1'
        peoes = []
        self.assertEqual(knight_escape(cavalo, peoes), 2)

    def test_cavalo_solo_a2(self):
        cavalo = 'a2'
        peoes = []
        self.assertEqual(knight_escape(cavalo, peoes), 3)

    def teste_cavalo_solo_a4(self):
        cavalo = 'a4'
        peoes = []
        self.assertEqual(knight_escape(cavalo, peoes), 4)

    def teste_cavalo_solo_a5(self):
        cavalo = 'a5'
        peoes = []
        self.assertEqual(knight_escape(cavalo, peoes), 4)

    def teste_cavalo_solo_a8(self):
        cavalo = 'a8'
        peoes = []
        self.assertEqual(knight_escape(cavalo, peoes), 2)

unittest.main()