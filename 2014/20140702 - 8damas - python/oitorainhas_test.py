import unittest
from oitorainhas import oitorainhas

class OitoRainhas(unittest.TestCase):
    def test_tabuleiro_sem_nenhuma(self):
        tabuleiro = [ 
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0], 
        ]
        self.assertEquals(oitorainhas(tabuleiro), False)

    def test_tabuleiro_com_uma(self):
        tabuleiro = [ 
            [1,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(oitorainhas(tabuleiro), False)


    def test_tabuleiro_com_duas_na_primeira_linha(self):
        tabuleiro = [ 
            [1,0,0,1],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(oitorainhas(tabuleiro), True)


    def test_tabuleiro_com_duas_na_primeira_linha_em_posicoes_(self):
        tabuleiro = [ 
            [1,0,1,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(oitorainhas(tabuleiro), True)


unittest.main() 