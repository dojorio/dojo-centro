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

    def test_3_linhas_2_3_1(self):
        patio = [[2], [3], [1]]
        self.assertEqual(2, quantos_movimentos(patio))

    def test_3_linhas_3_2_1(self):
        patio = [[3], [2], [1]]
        self.assertEqual(1, quantos_movimentos(patio))

    def test_4_linhas_4_1_2_3(self):
        patio = [[4], [1], [2], [3]]
        self.assertEqual(3, quantos_movimentos(patio))
          
    def test_4_colunas_4_1_2_3(self):
        patio = [[4, 1, 2, 3]]
        self.assertEqual(3, quantos_movimentos(patio))

    def test_2_linhas_2_colunas_com_colunas_invertidas(self):
        patio = [[2, 1], 
                 [4, 3]]
        self.assertEqual(1, quantos_movimentos(patio))

          
if __name__ == '__main__':
    unittest.main()
