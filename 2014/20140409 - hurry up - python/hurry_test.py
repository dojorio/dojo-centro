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

    def test_um_jogador_andando_na_diagonal_2x_mais_rápido(self):
        jogadores = [(0, 0, 2)] #x, y, velocidade
        chegadas = [(1, 1)]
        self.assertEqual(2**.5/2, hurry.hurry(jogadores, chegadas))

    def test_um_jogador_várias_chegadas(self):
        jogadores = [(0, 0, 1)] #x, y, velocidade
        chegadas = [(2, 2), (1, 1)]
        self.assertEqual(2**.5, hurry.hurry(jogadores, chegadas))

    def test_2_jogadores_2_saídas_uma_dimensao(self):
        jogadores = [(0, 0, 1), (3, 0, 1)] #x, y, velocidade
        chegadas = [(2, 0), (4, 0)]
        self.assertEqual(2, hurry.hurry(jogadores, chegadas))

    def test_2_jogadores_2_saídas_diagonal(self):
        jogadores = [(0, 0, 1), (3, 3, 1)] #x, y, velocidade
        chegadas = [(2, 2), (1.5, 1.5)]
        self.assertAlmostEqual((3*2**.5)/2, hurry.hurry(jogadores, chegadas))

    def test_2_jogadores_2_saídas_rápido_perto_lento_longe(self):
        jogadores = [(0, 0, 3), (0, 2, 1)] #x, y, velocidade
        chegadas = [(0, 1), (0, 4)]
        self.assertAlmostEqual((3*2**.5)/2, hurry.hurry(jogadores, chegadas))



unittest.main()
