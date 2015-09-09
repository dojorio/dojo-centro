import unittest
from linhas_cruzadas import linhas_cruzadas

class TestLinhasCruzadas(unittest.TestCase):
	def test_2_linhas_com_mesmo_ponto_se_cruzam(self):
		linha1 = ((0,0), (0,1))
		linha2 = ((0,0), (1,0))
		self.assertTrue(linhas_cruzadas(linha1, linha2))

	def test_2_linhas_que_não_se_cruzam(self):
		linha1 = ((0,0), (1,0))
		linha2 = ((2,0), (3,0))
		self.assertFalse(linhas_cruzadas(linha1, linha2))

	def test_2_linhas_com_mesmo_ponto_se_cruzam_2(self):
		linha1 = ((0,0), (0,2))
		linha2 = ((0,1), (0,2))
		self.assertTrue(linhas_cruzadas(linha1, linha2))

	def test_2_linhas_com_mesmo_ponto_se_cruzam_3(self):
		linha1 = ((0,1), (0,3))
		linha2 = ((0,0), (0,1))
		self.assertTrue(linhas_cruzadas(linha1, linha2))

	def test_2_linhas_com_mesmo_ponto_se_cruzam_4(self):
		linha1 = ((0,0), (0,1))
		linha2 = ((0,1), (0,3))
		self.assertTrue(linhas_cruzadas(linha1, linha2))

	def test_linha_com_ponto_no_meio_da_outra_linha(self):
		linha1 = ((0,0), (0,2))
		linha2 = ((0,1), (0,3))
		self.assertTrue(linhas_cruzadas(linha1, linha2))


unittest.main()