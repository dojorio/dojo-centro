import unittest
from heap import *

class TestHeap(unittest.TestCase):
    def test_insercao_heap_vazia(self):
        heap = Heap()
        heap.push(1)
        self.assertEqual(heap.get_state(), [1])
        
    def test_insercao_numero_maior_que_raiz(self):
        heap = Heap()
        heap.push(5)
        heap.push(6)
        self.assertEqual(heap.get_state(), [5, 6])
       
    def test_insercao_numero_menor_que_raiz(self):
        heap = Heap()
        heap.push(5)
        heap.push(4)
        self.assertEqual(heap.get_state(), [4, 5])
        
    def test_insercao_3_numeros_em_ordem_decrescente(self):
        heap = Heap()
        heap.push(5)
        heap.push(4)
        heap.push(3)
        self.assertEqual(heap.get_state(), [3, 5, 4])

    def test_insercao_4_numeros_em_ordem_decrescente(self):
        heap = Heap()
        heap.push(6)
        heap.push(5)
        heap.push(4)
        heap.push(3)
        self.assertEqual(heap.get_state(), [3, 4, 5, 6])
        
    def test_insercao_4_numeros_em_ordem_crescente(self):
        heap = Heap()
        heap.push(3)
        heap.push(4)
        heap.push(5)
        heap.push(6)
        self.assertEqual(heap.get_state(), [3, 4, 5, 6])
        
    def test_insercao_6_numeros_desordenadamente(self):
        heap = Heap([0, 4, 7, 9, 8])
        heap.push(0)
        heap.push(4)
        heap.push(7)
        heap.push(9)
        heap.push(8)
        heap.push (5)
        self.assertEqual(heap.get_state(), [0, 4, 5, 9, 8, 7])
unittest.main()
