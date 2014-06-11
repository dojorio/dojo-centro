import unittest
from flor_mario import demarcar

class Test (unittest.TestCase):
	def test_se_os_circulos_forem_iguais(self):
		flor = (1, (1, 1))
		demarcacao = (1, (1, 1))
		self.assertTrue(demarcar(flor, demarcacao))

	def test_centros_iguais_demarcacao_maior(self):
		demarcacao = (2, (1, 1))
		flor = (1, (1, 1))
		self.assertTrue(demarcar(flor, demarcacao))

	def test_centros_iguais_demarcacao_menor(self):
		demarcacao = (1, (1, 1))
		flor = (2, (1, 1))
		self.assertFalse(demarcar(flor, demarcacao))

	def test_circulos_afastados(self):
		demarcacao = (1, (2, 2))
		flor = (1, (-2, -2))
		self.assertFalse(demarcar(flor, demarcacao))

	def test_circulos_inscritos(self):
		demarcacao = (2, (2, 0))
		flor = (1, (1, 0))
		self.assertTrue(demarcar(flor, demarcacao))

	def test_circulos_inscritos(self):
		demarcacao = (3, (3, 0))
		flor = (1, (2, 0))
		self.assertTrue(demarcar(flor, demarcacao))

if __name__ == "__main__":
	unittest.main()
