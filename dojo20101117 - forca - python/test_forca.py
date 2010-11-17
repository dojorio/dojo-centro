import unittest
import jogo_da_forca


class TesteJogoDaForcaComAPalavraa(unittest.TestCase):
    def setUp(self):
        self.novo_jogo = jogo_da_forca.JogoDaForca('a', 99)

    def teste_tentativa_a_ganha_com_0_erros(self):
        resposta = self.novo_jogo.tentativa('a')
        self.assertEqual(resposta.ganhou, True)
        self.assertEqual(resposta.erros, 0)

    def teste_tentativa_b_nao_ganha_com_1_erro(self):
        resposta = self.novo_jogo.tentativa('b')
        self.assertEqual(resposta.ganhou, False)
        self.assertEqual(resposta.erros, 1)

    def teste_tentativas_w_z_nao_ganha_com_2_erros(self):
        resposta = self.novo_jogo.tentativa('w').tentativa('z')
        self.assertEqual(resposta.ganhou, False)
        self.assertEqual(resposta.erros, 2)


unittest.main()

