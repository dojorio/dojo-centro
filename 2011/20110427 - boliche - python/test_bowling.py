import unittest
from bowling import bowling


class BowlingTest(unittest.TestCase):
    def test_derrubou_0_pino(self):
        game = ((0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0))
        self.assertEqual(0, bowling(game))

    def test_derrubou_1_pino_na_primeira_rodada(self):
        game = ((1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0))
        self.assertEqual(1, bowling(game))
    
    def test_derrubou_2_pinos_na_primeira_rodada(self):
        game = ((2,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0))
        self.assertEqual(2, bowling(game))

    def test_derrubou_2_pinos_na_primeira_rodada_em_tentativas_diferentes(self):
        game = ((1,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0))
        self.assertEqual(2, bowling(game))

    def test_derrubou_3_pinos_na_primeira_rodada_em_tentativas_diferentes(self):
        game = ((2,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0))
        self.assertEqual(3, bowling(game))
        
    def test_derrubou_3_pinos_em_rodadas_e_tentativas_diferentes(self):
        game = ((1,1),(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0))
        self.assertEqual(3, bowling(game))
        
    def test_derrubou_4_pinos_em_rodadas_e_tentativas_diferentes(self):
        game = ((1,1),(1,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0))
        self.assertEqual(4, bowling(game))    
        
    def test_derrubou_5_pinos_em_rodadas_e_tentativas_diferentes(self):
        game = ((1,1),(1,1),(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0))
        self.assertEqual(5, bowling(game))    
        
    def test_spare_na_primeira_rodada(self):
        game = ((5,5),(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0))
        self.assertEqual(12, bowling(game))
        
    def test_spare_na_segunda_rodada(self):
        game = ((5,4),(6,4),(0,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0))
        self.assertEqual(21, bowling(game))

    def test_spare_na_segunda_rodada_com_proximo_dif_de_1(self):
        game = ((5,4),(6,4),(4,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0))
        self.assertEqual(29, bowling(game))
    
    def test_strike_na_primeira_rodada(self):
        game = ((10,0),(1,0),(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0))
        self.assertEqual(14, bowling(game))  

    def test_dois_spares(self):
        game = ((4,6),(5,5),(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0))
        self.assertEqual(32, bowling(game))            
        
unittest.main()