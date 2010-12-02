import unittest
from espiral import Espiral



class TestEspiral(unittest.TestCase):
    def test_1x1(self):
        espiral = Espiral(1, 1)
        self.assertEqual([1], espiral.linha(0))

    def test_1x2(self):
        espiral = Espiral(1, 2)
        self.assertEqual([1, 2], espiral.linha(0))

    def test_1x3(self):
        espiral = Espiral(1, 3)
        self.assertEqual([1, 2, 3], espiral.linha(0))

    def test_2x1(self):
        espiral = Espiral(2, 1)
        self.assertEqual([1], espiral.linha(0))
        self.assertEqual([2], espiral.linha(1))

    def test_3x1(self):
        espiral = Espiral(3, 1)
        self.assertEqual([1, 2, 3], espiral.coluna(0))

    def test_2x2(self):
        espiral = Espiral(2, 2)
        self.assertEqual([1, 2], espiral.linha(0))
        self.assertEqual([4, 3], espiral.linha(1))

    def test_3x2(self):
        espiral = Espiral(3, 2)
        self.assertEqual([1, 6, 5], espiral.coluna(0))
        self.assertEqual([2, 3, 4], espiral.coluna(1))

unittest.main()

