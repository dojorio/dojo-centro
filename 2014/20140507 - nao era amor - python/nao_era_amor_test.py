import unittest
from nao_era_amor import cilada

class TestNãoEraAmor(unittest.TestCase):
    def test_1x1_com_1_padrão(self):
        tabuleiro = ((1,),)
        padrões = ('+',)
        self.assertEqual(cilada(tabuleiro, padrões), 1)

    def test_1x1_com_1_padrão_tabuleiro_diferente(self):
        tabuleiro = ((2,),)
        padrões = ('+',)
        self.assertEqual(cilada(tabuleiro, padrões), 2)

    def test_1x1_com_1_padrão_diferente(self):
        tabuleiro = ((2,),)
        padrões = ('-',)
        self.assertEqual(cilada(tabuleiro, padrões), -2)

unittest.main()
