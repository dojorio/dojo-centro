import unittest
from cabos import metros_de_cabo

class TestCabos(unittest.TestCase):
	def test_uma_aresta(self):
		grafo = [(('a', 'b'), 1)]
		self.assertEqual(metros_de_cabo(grafo), 1)

	def test_uma_aresta_mais_robusta(self):
		grafo = [(('a', 'b'), 2)]
		self.assertEqual(metros_de_cabo(grafo), 2)

	def test_duas_arestas(self):
		grafo = [(('a', 'b'), 1),
				 (('b', 'c'), 1)]
		self.assertEqual(metros_de_cabo(grafo), 2)

	def test_tres_arestas_sem_ciclo(self):
		grafo = [(('a', 'b'), 1),
				 (('b', 'c'), 1),
				 (('c', 'd'), 1)]
		self.assertEqual(metros_de_cabo(grafo), 3)

	def test_duas_arestas_com_ciclo(self):
		grafo = [(('a', 'b'), 1),
				 (('b', 'a'), 2)]
		self.assertEqual(metros_de_cabo(grafo), 1)

	def test_três_arestas_com_dois_ciclos(self):
		grafo = [(('a', 'b'), 1),
				 (('b', 'a'), 2),
				 (('a', 'b'), 3)]
		self.assertEqual(metros_de_cabo(grafo), 1)

	def test_quatro_arestas_maior_peso_desconecta(self):
		grafo = [(('a', 'b'), 3),
				 (('b', 'c'), 1),
				 (('b', 'd'), 1),
				 (('c', 'd'), 1)]
		self.assertEqual(metros_de_cabo(grafo), 5)

	def test_quatro_arestas_maior_peso_desconecta_2(self):
		grafo = [(('a', 'b'), 3),
				 (('b', 'c'), 2),
				 (('b', 'd'), 2),
				 (('c', 'd'), 2)]
		self.assertEqual(metros_de_cabo(grafo), 7)

unittest.main()