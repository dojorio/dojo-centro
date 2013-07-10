import unittest
from skyline import skyline

class TestSkyline(unittest.TestCase):
	def test_caso_vazio(self):
		entrada = []
		saida = []
		self.assertEqual(saida, skyline(entrada))

	def test_caso_com_um_predio(self):
		entrada = [(1,10,2)]
		saida = [(1, 10), (2, 0)]
		self.assertEqual(saida, skyline(entrada))

	def test_caso_com_outro_predio(self):
		entrada = [(1,5,3)]
		saida = [(1, 5), (3, 0)]
		self.assertEqual(saida, skyline(entrada))

	def test_caso_com_dois_predios(self):
		entrada = [(1,10,2),(3,5,4)]
		saida = [(1, 10), (2, 0), (3, 5), (4, 0)]
		self.assertEqual(saida, skyline(entrada))

	def test_caso_com_tres_predios(self):
		entrada = [(1,10,2),(3,5,4), (5,2,7)]
		saida = [(1, 10), (2, 0), (3, 5), (4, 0), (5, 2), (7, 0)]
		self.assertEqual(saida, skyline(entrada))

	def test_caso_com_dois_predios_juntinhos(self):
		entrada = [(1,10,2),(2,10,3)]
		saida = [(1, 10), (3, 0)]
		self.assertEqual(saida, skyline(entrada))

	def test_caso_com_dois_predios_juntinhos_mas_diferentes(self):
		entrada = [(1,10,2),(2,12,3)]
		saida = [(1, 10), (2, 12), (3, 0)]
		self.assertEqual(saida, skyline(entrada))

	def test_caso_com_dois_predios_nao_juntinhos_e_nao_diferentes(self):
		entrada = [(1,10,2),(3,10,4)]
		saida = [(1, 10), (2, 0), (3, 10), (4, 0)]
		self.assertEqual(saida, skyline(entrada))

	def test_caso_com_dois_predios_na_terceira_base(self):
		entrada = [(1,10,3),(2,10,4)]
		saida = [(1, 10), (4, 0)]
		self.assertEqual(saida, skyline(entrada))

	def test_caso_com_dois_predios_na_terceira_base(self):
		entrada = [(1,10,3),(1,10,4)]
		saida = [(1, 10), (4, 0)]
		self.assertEqual(saida, skyline(entrada))

unittest.main()


