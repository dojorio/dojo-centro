import unittest
from gauss_jordan import *

class TestGaussJordan(unittest.TestCase):
    def test_2x_igual_4(self):
        matrix = [[2, 4]]
        self.assertEqual(gauss_jordan(matrix), [2])

    def test_2x_igual_6(self):
        matrix = [[2, 6]]
        self.assertEqual(gauss_jordan(matrix), [3])
        
    def test_3x_igual_6(self):
        matrix = [[3, 6]]
        self.assertEqual(gauss_jordan(matrix), [2])

    def test_3x_igual_10(self):
        matrix = [[3, 10]]
        self.assertEqual(gauss_jordan(matrix), [10.0/3])
        
    def test_identidade(self):
        matrix = [[1,0, 8],
                  [0,1, 7]]
        self.assertEqual(gauss_jordan(matrix), [8, 7])

    def test_2x_identidade(self):
        matrix = [[2,0, 10],
                  [0,2, 8]]
        self.assertEqual(gauss_jordan(matrix), [5, 4])
        
    def test_matriz_triangular_superior(self):
        matrix = [[2,1, 6],
                  [0,3, 12]]
        self.assertEqual(gauss_jordan(matrix), [1, 4])

        
class TestOperacoesBasicas(unittest.TestCase):
    def test_trocar_2_linhas_de_lugar(self):
        matrix = [[1, 2],
                  [3, 4]]
        trocar_linha(matrix, 0, 1)
        self.assertEqual(matrix,[[3, 4],
                                 [1, 2]])

    def test_multiplicar_linha_por_constante(self):
        linha = [1, 2]
        esperado = [-2 * 1, -2 * 2] 
        self.assertEqual(multiplicar_linha(linha, -2), esperado)
                                 
                                 
    def test_somar_duas_linhas(self):
        self.assertEqual(somar_linhas([1, 2], [3, 4]), [4, 6])
        
        

        

unittest.main()
