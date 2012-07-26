#coding:utf-8
import unittest
from dependencias import *

class TestDependencias(unittest.TestCase):    
    def teste_uma_dependencia(self):
        entrada = {'a':['b']}
        saida = {'a' :['b']}
        self.assertEqual(saida, dependencias(entrada))
   
    def teste_2_dependencia(self):
        entrada = {'a':['b', 'c']}
        saida = {'a' :['b', 'c']}
        self.assertEqual(saida, dependencias(entrada))   

    def teste_1_dependencia_transitiva(self):
        entrada = {'a':['b'], 'b': ['c']}
        saida = {'a' :['b', 'c'], 'b': ['c']}
        self.assertEqual(saida, dependencias(entrada))

    def teste_1_dependencia_transitiva_outro_nome(self):
        entrada = {'e':['f'], 'f': ['g']}
        saida = {'e' :['f', 'g'], 'f': ['g']}
        self.assertEqual(saida, dependencias(entrada))

    def teste_2_dependencias_transitivas(self):
        entrada = {'a':['b'], 'b': ['c'], 'c':['d']}
        saida = {'a' :['b', 'c', 'd'], 'b': ['c', 'd'], 'c':['d']}
        self.assertEqual(saida, dependencias(entrada))
        
    def teste_2_dependencias_transitivas_redundantes(self):
        entrada = {'a':['b'], 'b': ['c','d'], 'c':['d']}
        saida = {'a' :['b', 'c', 'd'], 'b': ['c', 'd'], 'c':['d']}
        self.assertEqual(saida, dependencias(entrada))

    def teste_ciclo(self):
        entrada = {'a':['b'], 'b': ['a']}
        saida = {'a' :['b'], 'b': ['a']}
        self.assertEqual(saida, dependencias(entrada))

    def teste_2_ciclos(self):
        entrada = {'a':['b'], 'b': ['a', 'c'], 'c': ['b']}
        saida = {'a' :['b', 'c'], 'b': ['a', 'c'], 'c':['a','b']}
        self.assertEqual(saida, dependencias(entrada))

    def teste_2_ciclos_com_mais_dependencias(self):
        entrada = {'a':['b'], 'b': ['a', 'c'], 'c': ['b', 'f']}
        saida = {'a' :['b', 'c'], 'b': ['a', 'c'], 'c':['a','b']}
        self.assertEqual(saida, dependencias(entrada))


unittest.main()
