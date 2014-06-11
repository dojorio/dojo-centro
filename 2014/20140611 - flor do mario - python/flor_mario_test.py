import unittest
from flor_mario import demarcar

class Test (unittest.TestCase):
	def test_parametros_iguais(self):
		circulo_cacador = (1,(1,1))
		circulo_flor = (1,(1,1))
		self.assertTrue(demarcar(circulo_cacador,circulo_flor))


if __name__ == "__main__":
	unittest.main()
