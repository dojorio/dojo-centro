import unittest
from containeres import quantos_movimentos

class TestContaineres(unittest.TestCase):
    def test_1_linha_e_coluna(self):
        patio = [[1]]
        self.assertEqual(0, quantos_movimentos(patio))

    def test_2_linhas_trocadas(self):
        patio = [[2], [1]]
        self.assertEqual(1, quantos_movimentos(patio))

    def test_2_linhas_corretas(self):
        patio = [[1], [2]]
        self.assertEqual(0, quantos_movimentos(patio))

    def test_3_linhas_somente_uma_troca(self):
        patio = [[1], [3], [2]]
        self.assertEqual(1, quantos_movimentos(patio))


          
if __name__ == '__main__':
    unittest.main()
