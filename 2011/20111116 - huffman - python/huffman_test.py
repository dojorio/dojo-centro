import unittest
from huffman import *

class TestTabelaFrequencia(unittest.TestCase):
    def test_palavra_vazia(self):
        palavra = ''
        self.assertEqual(frequencia(palavra), {})
    
    def test_palavra_com_1_letra(self):
        palavra = 'a'
        self.assertEqual(frequencia(palavra), {'a': 1})
    
    def test_palavra_com_2_letras_b(self):
        palavra = 'bb'
        self.assertEqual(frequencia(palavra), {'b': 2})
        
    def test_palavra_com_letras_diferentes(self):
        palavra = 'ab'
        self.assertEqual(frequencia(palavra), {'a': 1, 'b':1})

    def test_abacabi(self):
        palavra = 'abacabi'
        self.assertEqual(frequencia(palavra), {'a': 3, 'b': 2, 'c': 1, 'i': 1})


class TestArvoreDePrefixos(unittest.TestCase):
    def test_tabela_com_um_elemento_a(self):
        tabela = {'a': 1}
        self.assertEqual(prefixos(tabela), (1, 'a'))
        
    def test_tabela_com_um_elemento_b(self):
        tabela = {'b': 1}
        self.assertEqual(prefixos(tabela), (1, 'b'))
    
    def test_tabela_com_elementos_diferentes_ab(self):
        tabela = {'a': 1, 'b':1}
        arvore = (2, None, (1, 'a'), (1, 'b'))
        self.assertEqual(prefixos(tabela), arvore)
    
    def test_tabela_com_elementos_diferentes_ac(self):
        tabela = {'a': 1, 'c': 1}
        arvore = (2, None, (1, 'a'), (1, 'c'))
        self.assertEqual(prefixos(tabela), arvore)
    
    def test_tabela_abacabi(self):
        tabela = {'i': 1, 'a': 3, 'b': 2, 'c':1}
        arvore = (7, None, 
                    (3, 'a'),
                    (4, None, 
                        (2, None, 
                            (1, 'c'), 
                            (1, 'i')),
                        (2, 'b'))
                    )
        self.assertEqual(prefixos(tabela), arvore)

unittest.main()
