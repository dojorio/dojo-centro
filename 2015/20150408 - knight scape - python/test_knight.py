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

    def teste_cavalo_solo_h8(self):
        cavalo = 'h7'
        peoes = []
        self.assertEqual(knight_escape(cavalo, peoes), 3)

    def teste_cavalo_solo_b3(self):
        cavalo = 'b3'
        peoes = []
        self.assertEqual(knight_escape(cavalo, peoes), 6)
    
    def teste_cavalo_solo_g1(self):
        cavalo = 'g1'
        peoes = []
        self.assertEqual(knight_escape(cavalo, peoes), 3)

    def teste_cavalo_solo_b2(self):
        cavalo = 'b2'
        peoes = []
        self.assertEqual(knight_escape(cavalo, peoes), 4)

    def teste_cavalo_solo_e1(self):
        cavalo = 'e1'
        peoes = []
        self.assertEqual(knight_escape(cavalo, peoes), 4)

    def teste_cavalo_solo_e2(self):
        cavalo = 'e2'
        peoes = []
        self.assertEqual(knight_escape(cavalo, peoes), 6)

    def teste_cavalo_solo_d7(self):
        cavalo = 'd7'
        peoes = []
        self.assertEqual(knight_escape(cavalo, peoes), 6)

    def teste_cavalo_solo_f8(self):
        cavalo = 'f8'
        peoes = []
        self.assertEqual(knight_escape(cavalo, peoes), 4)

    def teste_cavalo_solo_c2(self):
        cavalo = 'c2'
        peoes = []
        self.assertEqual(knight_escape(cavalo, peoes), 6)

    def teste_cavalo_c2_peao_b2(self):
        cavalo = 'c2'
        peoes = 'b2'
        self.assertEqual(knight_escape(cavalo, peoes), 5)

unittest.main()