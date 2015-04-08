import unittest
from knight import knight_escape

class TestKnight(unittest.TestCase):
    def test_cavalo_solo(self):
        cavalo = '4c'
        peoes = []
        self.assertEqual(knight_escape(cavalo, peoes), 8)

unittest.main()