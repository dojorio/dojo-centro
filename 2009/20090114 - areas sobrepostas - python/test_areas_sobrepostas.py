import unittest
from areas_sobrepostas import *

class TestAreasSobrepostas(unittest.TestCase):

    def testAreaUmRetangulo(self):
        
        self.assertEquals(area_retangulo(0, 0, 1, 2), 2)

    def testNaoIntercecao(self):
        retangulo1 = (0, 0, 1, 2)
        retangulo2 = (3, 5, 2, 1)
        result = intersecao(retangulo1, retangulo2)
        self.assertEqual(result, None)

    def testIntercecao(self):
        retangulo1 = (0, 0, 1, 2)
        retangulo2 = (0, 0, 1, 1)
        result = intersecao(retangulo1, retangulo2)
        self.assertEqual(result, (0, 0, 1, 1))

    def testNaoIntercecao2(self):        
        retangulo1 = (0, 0, 1, 2)
        retangulo2 = (3, 5, 2, 2)
        result = intersecao(retangulo1, retangulo2)
        self.assertEqual(result, None)

unittest.main()
    

