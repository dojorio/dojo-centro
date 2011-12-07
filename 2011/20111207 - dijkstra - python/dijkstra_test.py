import unittest
from dijkstra import *

class TestDijkstra(unittest.TestCase):
    def test_grafo_unitario(self):
        grafo = { 'A': ()}
        no = 'A'
        menores_distancias = {'A': 0 }
        self.assertEqual(dijkstra(grafo, no), menores_distancias)
        
    def test_grafo_unitario_de_no_com_nome_B(self):
        grafo = { 'B': ()}
        no = 'B'
        menores_distancias = {'B': 0}
        self.assertEqual(dijkstra(grafo, no), menores_distancias)

    def test_grafo_com_dois_nos(self):
        grafo = { 'A': ((42, 'B'),), 'B': () }
        no = 'A'
        menores_distancias = {'A': 0, 'B': 42}
        self.assertEqual(dijkstra(grafo, no), menores_distancias)

    def test_grafo_dois_nos_de_B_para_A(self):
        grafo = { 'A': (), 'B': ((42, 'A'),) }
        no = 'B'
        menores_distancias = {'A': 42, 'B': 0}
        self.assertEqual(dijkstra(grafo, no), menores_distancias)

    def test_grafo_com_tres_nos_indo_pra_C_direto(self):
        grafo = { 
            'A': ((42,'B'),(20,'C')), 
            'B': ((10,'C'),),
            'C': (),
            }
        no = 'A'
        menores_distancias = {'A': 0, 'B': 42, 'C': 20}
        self.assertEqual(dijkstra(grafo, no), menores_distancias)
    
    def test_grafo_com_tres_nos_indo_pra_C_por_B(self):
        grafo = {
            'A': ((42, 'B'), (100, 'C')),
            'B': ((10, 'C'),),
            'C': (),
            }
        no = 'A'
        menores_distancias = {'A': 0, 'B': 42, 'C': 52}
        self.assertEqual(dijkstra(grafo, no), menores_distancias)

    def test_grafo_com_quatro_nos(self):
        grafo = { 
            'A': ((42,'B'),(20,'C'),), 
            'B': ((10,'C'),),
            'C': ((120,'D'),),
            'D': ((24,'C'),),
            }
        no = 'A'
        menores_distancias = {'A': 0, 'B': 42, 'C': 20, 'D': 140}
        self.assertEqual(dijkstra(grafo, no), menores_distancias)
        
    def test_grafo_com_quatro_nos_sequenciais(self):
        grafo = { 
            'A': ((42,'B'),), 
            'B': ((10,'C'),),
            'C': ((120,'D'),),
            'D': (),
            }
        no = 'A'
        menores_distancias = {'A': 0, 'B': 42, 'C': 52, 'D': 172}
        self.assertEqual(dijkstra(grafo, no), menores_distancias)
    
    
    
    
unittest.main()
