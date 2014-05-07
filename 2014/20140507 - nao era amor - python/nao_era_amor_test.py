import unittest
from nao_era_amor import cilada

class TestNãoEraAmor(unittest.TestCase):
    # def test_vida(self):
    #     self.assertEqual('cilada', 'amor')

    def test_1x1_com_1_padrão(self):
        tabuleiro = ((1,),)
        padrões = ('+',)
        self.assertEqual(cilada(tabuleiro, padrões), 1)

    def test_1x1_com_1_padrão_tabuleiro_diferente(self):
        tabuleiro = ((2,),)
        padrões = ('+',)
        self.assertEqual(cilada(tabuleiro, padrões), 2)

    def test_1x1_com_1_padrão_negativo(self):
        tabuleiro = ((2,),)
        padrões = ('-',)
        self.assertEqual(cilada(tabuleiro, padrões), -2)

    def test_1x1_com_1_padrão_ponto(self):
        tabuleiro = ((2,),)
        padrões = ('.',)
        self.assertEqual(cilada(tabuleiro, padrões), 0)

    def test_1x1_com_padrões_ponto_mais(self):
        tabuleiro = ((2,),)
        padrões = ('.','+')
        self.assertEqual(cilada(tabuleiro, padrões), 2)

    def test_1x2_com_padrões_maismais(self):
        tabuleiro = ((2,1),)
        padrões = ('++',)
        self.assertEqual(cilada(tabuleiro, padrões), 3)

    def test_1x2_com_padrões_menosmais(self):
        tabuleiro = ((2,1),)
        padrões = ('-+',)
        self.assertEqual(cilada(tabuleiro, padrões), -1)

    def test_1x2_com_padrões_maismais_outro_tabuleiro(self):
        tabuleiro = ((3,1),)
        padrões = ('++',)
        self.assertEqual(cilada(tabuleiro, padrões), 4)

    def test_1x2_com_padrões_maismais_e_pontomenos(self):
        tabuleiro = ((3,1),)
        padrões = ('++','.-')
        self.assertEqual(cilada(tabuleiro, padrões), 4)

    def test_1x2_com_padrões_maismenos_e_menosmais(self):
        tabuleiro = ((3,1),)
        padrões = ('+-','-+')
        self.assertEqual(cilada(tabuleiro, padrões), 2)

    def test_2x1_com_padrões_ponto_mais(self):
        tabuleiro = ((1,), (2,))
        padrões = ('+', '.')
        self.assertEqual(cilada(tabuleiro, padrões), 2)

    def test_2x1_com_padrões_menos_mais(self):
        tabuleiro = ((1,), (2,))
        padrões = ('-', '+')
        self.assertEqual(cilada(tabuleiro, padrões), 1)

unittest.main()
