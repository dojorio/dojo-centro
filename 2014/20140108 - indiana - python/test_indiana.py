import unittest
from indiana import indiana

class TestIndiana(unittest.TestCase):
    def test_uma_rampa(self):
        rampas = [(5, 1, 4)]
        largura = 2
        altura = 5
        self.assertEqual(1, indiana(rampas, largura, altura))

    def test_uma_rampa_com_mais_espaco(self):
        rampas = [(5, 1, 4)]
        largura = 3
        altura = 5
        self.assertEqual(2, indiana(rampas, largura, altura))

    def test_duas_rampas(self):
        rampas = [(5,1,4), (3, 1, 1)]
        largura = 3
        altura = 5
        self.assertEqual(1, indiana(rampas, largura, altura))

    def test_duas_rampas_com_mais_espaco(self):
        rampas = [(5,1,4), (3, 2, 1)]
        largura = 3
        altura = 5
        self.assertEqual(2, indiana(rampas, largura, altura))

    def test_duas_rampas_com_a_primeira_maior(self):
        rampas = [(5,2,4), (3, 2, 1)]
        largura = 3
        altura = 5
        self.assertEqual(1, indiana(rampas, largura, altura))

    def test_tres_rampas_distantes(self):
        rampas = [(50,1,49), (30, 2, 29), (10,2,9)]
        largura = 3
        altura = 50
        self.assertEqual(1, indiana(rampas, largura, altura))

    def test_tres_rampas_distantes_com_o_segundo_menor(self):
        rampas = [(50,1,49), (30, 1, 29), (10,1,9)]
        largura = 3
        altura = 50
        self.assertEqual(1, indiana(rampas, largura, altura))

    def test_duas_rampas_distantes_com_(self):
        rampas = [(10,1,9), (9, 1, 8)]
        largura = 2
        altura = 11
        self.assertEqual(2**0.5/2, indiana(rampas, largura, altura))

unittest.main()
