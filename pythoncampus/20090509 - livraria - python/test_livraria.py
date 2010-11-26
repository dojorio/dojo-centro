import unittest
from livraria import calcular_preco

class LivrariaTest(unittest.TestCase):
       
    def teste_com_um_livro(self):
        lista_livros = [0, 1, 0, 0, 0] 
        self.assertEqual(calcular_preco(lista_livros), 42)

    def teste_dois_livros_iguais(self):
        lista_livros = [0, 2, 0, 0, 0] 
        self.assertEqual(calcular_preco(lista_livros), 84)

    def teste_100_livros_iguais(self):
        lista_livros = [0, 100, 0, 0, 0] 
        self.assertEqual(calcular_preco(lista_livros), 4200)
        
    def teste_n_livros(self):
        lista_livros = [0, 0, 100, 0, 0] 
        self.assertEqual(calcular_preco(lista_livros), 4200)        

    def teste_2_livros_diferentes(self):
        lista_livros = [0, 1, 1, 0, 0] 
        self.assertAlmostEqual(calcular_preco(lista_livros), 84*0.95)

    def teste_2_livros_diferentes_2(self):
        lista_livros = [0, 0, 1, 1, 0] 
        self.assertAlmostEqual(calcular_preco(lista_livros), 84*0.95)

    def teste_2_livros_diferentes_3(self):
        lista_livros = [1, 0, 0, 0, 1] 
        self.assertAlmostEqual(calcular_preco(lista_livros), 84*0.95)

    def teste_2_livros_com_quantidade_diferentes(self):
        lista_livros = [7, 0, 0, 0, 5] 
        self.assertAlmostEqual(calcular_preco(lista_livros), 42 * 12 * 0.95)


unittest.main()
