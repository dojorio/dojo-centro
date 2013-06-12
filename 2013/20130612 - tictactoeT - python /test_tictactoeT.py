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

	def test_primeira_linha_completa_com_x_e_o_entao_ta_rolando(self):
		entrada = \
		['Toxo',
		 '....',
		 '....',
		 '....']
		saida = 'Rolando'
		self.assertEqual( verifica(entrada) , saida)

	def test_primeira_linha_completa_com_x_e_o_com_T_fora_ta_rolando(self):
		entrada = \
		['xxxo',
		 'T...',
		 '....',
		 '....']
		saida = 'Rolando'
		self.assertEqual( verifica(entrada) , saida)

	def test_x_venceu_com_segunda_linha_completa_com_T(self):
		entrada = \
		['....',
		 'Txxx',
		 '....',
		 '....']
		saida = 'x Ganhou'
		self.assertEqual( verifica(entrada) , saida)

	def test_x_venceu_com_terceira_linha_completa_com_T(self):
		entrada = \
		['....',
		 '....',
		 'Txxx',
		 '....']
		saida = 'x Ganhou'
		self.assertEqual( verifica(entrada) , saida)

	def test_x_venceu_com_primeira_coluna_completa_com_T(self):
		entrada = \
		['T...',
		 'x...',
		 'x...',
		 'x...']
		saida = 'x Ganhou'
		self.assertEqual( verifica(entrada) , saida)

	def test_x_venceu_com_primeira_coluna_completa_com_T(self):
		entrada = \
		['T...',
		 'x...',
		 'x...',
		 'x...']
		saida = 'x Ganhou'
		self.assertEqual( verifica(entrada) , saida)

unittest.main()


