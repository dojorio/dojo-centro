import unittest
from oitorainhas import pode_atacar

class OitoRainhas(unittest.TestCase):
    def test_tabuleiro_sem_nenhuma(self):
        tabuleiro = [ 
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0], 
        ]
        self.assertEquals(pode_atacar(tabuleiro), False)

    def test_tabuleiro_com_uma(self):
        tabuleiro = [ 
            [1,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), False)


    def test_tabuleiro_com_duas_na_primeira_linha(self):
        tabuleiro = [ 
            [1,0,0,1],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)


    def test_tabuleiro_com_duas_na_primeira_linha_em_posicoes_(self):
        tabuleiro = [ 
            [1,0,1,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)

    def test_tabuleiro_com_tres_na_primeira_linha_em_posicoes_(self):
        tabuleiro = [ 
            [1,1,1,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)

    def test_tabuleiro_com_duas_na_segunda_linha(self):
        tabuleiro = [ 
            [0,0,0,0],
            [1,0,1,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)

    def test_tabuleiro_com_um_na_segunda_linha(self):
        tabuleiro = [ 
            [0,0,0,0],
            [0,0,1,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), False)

    def test_tabuleiro_com_tres_na_segunda_linha(self):
        tabuleiro = [ 
            [0,0,0,0],
            [1,1,1,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)

    def test_tabuleiro_com_dois_na_terceira_linha(self):
        tabuleiro = [ 
            [0,0,0,0],
            [0,0,0,0],
            [1,1,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)

unittest.main() 