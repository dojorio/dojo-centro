import unittest
from oitorainhas import pode_atacar

class OitoRainhas(unittest.TestCase):
    def test_sem_nenhuma(self):
        tabuleiro = [ 
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0], 
        ]
        self.assertEquals(pode_atacar(tabuleiro), False)

    def test_uma(self):
        tabuleiro = [ 
            [1,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), False)


    def test_duas_na_primeira_linha(self):
        tabuleiro = [ 
            [1,0,0,1],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)


    def test_duas_na_primeira_linha_em_posicoes_(self):
        tabuleiro = [ 
            [1,0,1,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)

    def test_3_na_primeira_linha_em_posicoes_(self):
        tabuleiro = [ 
            [1,1,1,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)

    def test_duas_na_segunda_linha(self):
        tabuleiro = [ 
            [0,0,0,0],
            [1,0,1,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)

    def test_um_na_segunda_linha(self):
        tabuleiro = [ 
            [0,0,0,0],
            [0,0,1,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), False)

    def test_3_na_segunda_linha(self):
        tabuleiro = [ 
            [0,0,0,0],
            [1,1,1,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)

    def test_2_na_terceira_linha(self):
        tabuleiro = [ 
            [0,0,0,0],
            [0,0,0,0],
            [1,1,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)

    def test_3_na_terceira_linha(self):
        tabuleiro = [ 
            [0,0,0,0],
            [0,0,0,0],
            [1,1,1,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)

    def test_um_na_quarta_linha(self):
        tabuleiro = [ 
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,1,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), False)

    def test_2_na_quarta_linha(self):
        tabuleiro = [ 
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,1,1,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)

    def test_2_na_primeira_coluna(self):
        tabuleiro = [ 
            [1,0,0,0],
            [1,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)

    def test_2_na_primeira_coluna_em_posicoes_diferentes(self):
        tabuleiro = [ 
            [1,0,0,0],
            [0,0,0,0],
            [1,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)

    def test_2_na_primeira_coluna_em_posicoes_diferentes_2(self):
        tabuleiro = [ 
            [1,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [1,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)

    def test_2_na_segunda_coluna(self):
        tabuleiro = [ 
            [0,1,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,1,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)

    def test_2_na_terceira_coluna(self):
        tabuleiro = [ 
            [0,0,1,0],
            [0,0,0,0],
            [0,0,1,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)

    def test_2_na_diagonal_linha1_linha2(self):
        tabuleiro = [ 
            [1,0,0,0],
            [0,1,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)


    def test_2_na_diagonal_linha1_linha2_linha3(self):
        tabuleiro = [ 
            [1,0,0,0],
            [0,0,0,0],
            [0,0,1,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)

    def test_2_na_diagonal_linha1_linha2_linha3_oposta(self):
        tabuleiro = [ 
            [0,0,0,1],
            [0,0,1,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)


    def test_2_na_diagonal_linha1_linha2_linha3_oposta_2(self):
        tabuleiro = [ 
            [0,0,0,1],
            [0,0,0,0],
            [0,1,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)


    def test_2_na_diagonal_linha1_linha2_linha3_oposta_3(self):
        tabuleiro = [ 
            [0,0,0,1],
            [0,0,0,0],
            [0,0,0,0],
            [1,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)


    def test_2_na_diagonal_shiftada_pra_direita(self):
        tabuleiro = [ 
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.assertEquals(pode_atacar(tabuleiro), True)

unittest.main() 