import unittest
from tictactoeT import verifica

class TesteTicTacToeT(unittest.TestCase):
	def test_vazio(self):
		entrada = \
		['T...',
		 '....',
		 '....',
		 '....']
		saida = 'Rolando'
		self.assertEqual( verifica(entrada) , saida)

	def test_x_venceu_com_primeira_linha_completa_com_T(self):
		entrada = \
		['Txxx',
		 '....',
		 '....',
		 '....']
		saida = 'x Ganhou'
		self.assertEqual( verifica(entrada) , saida)

	def test_o_venceu_com_primeira_linha_completa_com_T(self):
		entrada = \
		['Tooo',
		 '....',
		 '....',
		 '....']
		saida = 'o Ganhou'
		self.assertEqual( verifica(entrada) , saida)



unittest.main()


