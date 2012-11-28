#coding: utf-8
import unittest
from laser import laser

class TestLaser(unittest.TestCase):
    def test_nenhum_soldado(self):
        soldados = []
        self.assertEqual(0, laser(soldados))

    def test_um_soldado(self):
        soldados = [(1,1)]
        self.assertEqual(1, laser(soldados))

    def test_dois_soldados_em_fila(self):
        soldados = [(1,1), (1,2)]
        self.assertEqual(1, laser(soldados))

    def test_dois_soldados_em_diagonal(self):
        soldados = [(1,1), (2,2)]
        self.assertEqual(2, laser(soldados))

    def test_dois_soldados_em_coluna(self):
        soldados = [(1,1), (2,1)]
        self.assertEqual(1, laser(soldados))

    def test_tres_soldados_em_coluna(self):
        soldados = [(1,1), (2,1), (3,1)]
        self.assertEqual(1, laser(soldados))

    def test_tres_soldados_em_linha(self):
        soldados = [(1,2), (1,1), (1,3)]
        self.assertEqual(1, laser(soldados))
    
    def test_tres_soldados_em_L(self):
        soldados = [(1,2), (1,1), (2,1)]
        self.assertEqual(2, laser(soldados))

    def test_cinco_soldados_em_L(self):
        soldados = [(0,0), (0,1), (0,2), (1,0), (2,0)]
        '''
        #....
        #....
        ###..
        '''
        self.assertEqual(2, laser(soldados))

unittest.main()