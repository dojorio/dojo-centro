import unittest
from tennis import *

class Teste(unittest.TestCase):
    
    def test_jogador1_marcando_1o_ponto_do_game(self):
        game = Game()
        game.pontua(game.JOGADOR1)

        self.assertEquals((15, 0), game.placar)
    
    def test_jogador1_marcando_3o_ponto_do_game(self):
        game = Game(30,0)
        game.pontua(game.JOGADOR1)
        self.assertEquals((40,0), game.placar)
    
    def test_jogador2_marcando_1o_ponto_no_game(self):
        game = Game()
        game.pontua(game.JOGADOR2)
        self.assertEquals((0,15), game.placar)
 


if __name__ == '__main__':
    unittest.main()