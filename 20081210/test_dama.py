import unittest
from dama import dama


class damaTest(unittest.TestCase):
    def testMesmaCasa(self):
        self.assertEquals(dama(3, 3, 3, 3), 0)

    def testUmaCasaParaBaixo(self):
        self.assertEquals(dama(3, 3, 3, 4), 1)

    def testUmaCasaEmDiagonal(self):
        self.assertEquals(dama(3, 3, 4, 4), 1)

    def testEmL(self):
        self.assertEquals(dama(3, 3, 4, 5), 2)

    def testDuasCasasEmDiagonal(self):
        self.assertEquals(dama(1, 1, 3, 3), 1)

    def testForaDoTabuleiro(self):
        self.assertRaises(IndexError, dama, 0, 0, 3, 4)

    def testForaDoTabuleiroDoisParametros(self):
        self.assertRaises(IndexError, dama, 0, 0, 0, 0)
        
unittest.main()
