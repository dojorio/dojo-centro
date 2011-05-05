import unittest
from bowling import placar


#Pinos:     (10,) (10,) (10,) (1, 0) (0, 1)
#Pontuacao:  30     21    11    1     1

class BowlingTest(unittest.TestCase):
    def test_errou_tudo_entao_pontuacao_eh_0(self):
        jogo = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
        self.assertEqual(placar(jogo), 0)
        
    def test_acertou_um_entao_pontuacao_eh_um(self):
        jogo = ((1, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
        self.assertEqual(placar(jogo), 1)

    def test_pontuacao_eh_tres(self):
        jogo = ((1, 2), (0, 0), (0, 0), (0, 0), (0, 0),
                (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
        self.assertEqual(placar(jogo), 3)

    def test_pontuacao_das_duas_primeiras_rodadas(self):
        jogo = ((1, 2), (2, 1), (0, 0), (0, 0), (0, 0),
                (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
        self.assertEqual(placar(jogo), 6)

    def test_pontuacao_de_todas_as_rodadas_simples(self):
        jogo = ((1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                (1, 1), (1, 1), (1, 1), (1, 1), (1, 1))
        self.assertEqual(placar(jogo), 20)

    def test_pontuacao_de_todas_as_rodadas_com_1_spare(self):
        jogo = ((1, 9), (1, 0), (0, 0), (0, 0), (0, 0),
                (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
        self.assertEqual(placar(jogo), 10+1+1)

    def test_pontuacao_de_todas_as_rodadas_com_1_spare_na_2_rodada(self):
        jogo = ((0, 0), (1, 9), (1, 0), (0, 0), (0, 0),
                (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
        self.assertEqual(placar(jogo), 10+1+1)

    def test_pontuacao_de_todas_as_rodadas_com_2_spares_rodada(self):
        jogo = ((0, 0), (1, 9), (1, 0), (2, 8), (3, 0),
                (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
        self.assertEqual(placar(jogo), 10+1+1 + 10+3+3)

    def test_pontuacao_de_todas_as_rodadas_com_3_spares_rodada(self):
        jogo = ((0, 0), (1, 9), (1, 0), (2, 8), (3, 0),
                (0, 0), (5, 5), (3, 0), (0, 0), (0, 0))
        self.assertEqual(placar(jogo), 10+1+1 + 10+3+3 + 10+3 +3)

    def test_pontuacao_de_todas_as_rodadas_com_1_spares_na_10a_jogada(self):
        jogo = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                (0, 0), (0, 0), (0, 0), (0, 0), (5, 5), (1,))
                
        self.assertEqual(placar(jogo), 10+1)

    def test_pontuacao_de_strike(self):
        jogo = ((0, 0), (0, 0), (10,), (0, 0), (0, 0),
                (0, 0), (0, 0), (0, 0), (0, 0), (5, 5), (1,))
                
        self.assertEqual(placar(jogo), 10 + 10+1)
        
unittest.main()