import unittest
from huffman import *

class TestTabelaCompactacao(unittest.TestCase):

    def test_arvore_vazia(self):
        self.assertEqual(tabela_compactacao(()), {})
    
    def test_arvore_com_um_elemento(self):
        arvore = (1, 'a')
        tabela = { 'a': '0' }
        self.assertEqual(tabela_compactacao(arvore), tabela)

    def test_arvore_com_dois_elementos(self):
        arvore = (2, None, (1, 'a'), (1, 'b'))
        tabela = { 'a': '0', 'b': '1' }
        self.assertEqual(tabela_compactacao(arvore), tabela)

    def test_arvore_com_tres_elementos(self):
        arvore = (4, None, 
                    (2, 'a'), 
                    (2, None, 
                        (1, 'b'),
                        (1, 'c')
                    ))
        tabela = { 'a': '0', 'b': '10', 'c': '11' }
        self.assertEqual(tabela_compactacao(arvore), tabela)

    def test_arvore_com_tres_elementos(self):
        arvore = (7, None, 
                    (3, 'a'), 
                    (4, None, 
                        (2, 'b'),
                        (2, None,
                            (1, 'c'),
                            (1, 'i'))))
        tabela = { 'a': '0', 'b': '10', 'c': '110', 'i': '111' }
        self.assertEqual(tabela_compactacao(arvore), tabela)

class TestCompactador(unittest.TestCase):
    def setUp(self):
        self.tabela = { 'a': '0', 'b': '10', 'c': '110', 'i': '111' }
    
    def test_string_vazia(self):
        cadeia = ''
        esperado = ''
        self.assertEqual(compactar(self.tabela, cadeia), esperado)

    def test_string_com_um_caractere_a(self):
        cadeia = 'a'
        esperado = '0'
        self.assertEqual(compactar(self.tabela, cadeia), esperado)

    def test_string_com_um_caractere_b(self):
        cadeia = 'b'
        esperado = '10'
        self.assertEqual(compactar(self.tabela, cadeia), esperado)    
    
    def test_string_com_um_caractere_c(self):
        cadeia = 'c'
        esperado = '110'
        self.assertEqual(compactar(self.tabela, cadeia), esperado)    

    def test_string_com_dois_caracteres_ab(self):
        cadeia = 'ab'
        esperado = '010'
        self.assertEqual(compactar(self.tabela, cadeia), esperado) 
     
    def test_string_com_caractere_nao_indexado(self):
        cadeia = 'ax'
        self.assertRaises(CaractereNaoIndiciadoError, compactar, self.tabela, cadeia) 

class TestDescompactador(unittest.TestCase):

    def setUp(self):
        self.arvore = (7, None, 
                    (3, 'a'), 
                    (4, None, 
                        (2, 'b'),
                        (2, None,
                            (1, 'c'),
                            (1, 'i'))))
                            
    def test_string_vazia(self):
        cadeia = ''
        esperado = ''
        self.assertEqual(descompactar(self.arvore, cadeia), esperado)
    
    def test_string_um_caracter(self):
        cadeia = '0'
        esperado = 'a'
        self.assertEqual(descompactar(self.arvore, cadeia), esperado)
    
    def test_string_dois_caracteres(self):
        cadeia = '010'
        esperado = 'ab'
        self.assertEqual(descompactar(self.arvore, cadeia), esperado)
    
    def test_string_tres_caracteres(self):
        cadeia = '010110'
        esperado = 'abc'
        self.assertEqual(descompactar(self.arvore, cadeia), esperado)
        
unittest.main()
