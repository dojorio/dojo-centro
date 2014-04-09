import unittest, hurry

class TestHurry(unittest.TestCase):
    def test_um_jogador_andando_na_vertical(self):
        jogadores = [(0, 0, 1)] #x, y, velocidade
        chegadas = [(0, 1)]
        self.assertEqual(1, hurry.hurry(jogadores, chegadas))

    def test_um_jogador_andando_na_vertical_mais(self):
        jogadores = [(0, 0, 1)] #x, y, velocidade
        chegadas = [(0, 2)]
        self.assertEqual(2, hurry.hurry(jogadores, chegadas))

    def test_um_jogador_andando_na_horizontal(self):
        jogadores = [(0, 0, 1)] #x, y, velocidade
        chegadas = [(1, 0)]
        self.assertEqual(1, hurry.hurry(jogadores, chegadas))

    def test_um_jogador_andando_na_horizontal_pra_trás(self):
        jogadores = [(1, 0, 1)] #x, y, velocidade
        chegadas = [(0, 0)]
        self.assertEqual(1, hurry.hurry(jogadores, chegadas))

    def test_um_jogador_andando_na_diagonal(self):
        jogadores = [(0, 0, 1)] #x, y, velocidade
        chegadas = [(1, 1)]
        self.assertEqual(2**.5, hurry.hurry(jogadores, chegadas))

unittest.main()
