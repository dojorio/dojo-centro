#!/usr/bin/python

import unittest
from embratel import distancias, comprimento_fibra_minimo
from math import sqrt

class TestArvoreMinima(unittest.TestCase):
    def test_1_cliente(self):
        clientes = ((1,1),)
        self.assertEqual(0, comprimento_fibra_minimo(clientes))

    def test_2_clientes_distantes_1_kilometro(self):
        clientes = ((1,1),(1,2))
        self.assertEqual(1, comprimento_fibra_minimo(clientes))

    def test_3_clientes_distantes_2_kilometros(self):
        clientes = ((1,1),(1,2),(1,3))
        self.assertEqual(2, comprimento_fibra_minimo(clientes))

    def test_3_clientes_distantes_irracional_kilometros(self):
        clientes = ((1,1),(1,2),(2,2))
        self.assertEqual(2, comprimento_fibra_minimo(clientes))

        
class TestDistancias(unittest.TestCase):
    def test_1_cliente(self):
        clientes = ((1,1),)
        distancias_esperadas = ((0,),)
        self.assertEqual(distancias_esperadas, distancias(clientes))

    def test_2_clientes_distantes_1_kilometro(self):
        clientes = ((1,1),(1,2))
        distancias_esperadas = ((0,1),
                                (1,0))
        self.assertEqual(distancias_esperadas, distancias(clientes))
        
    def test_2_clientes_distantes_2_kilometros(self):
        clientes = ((1,1),(1,3))
        distancias_esperadas = ((0,2),
                                (2,0))
        self.assertEqual(distancias_esperadas, distancias(clientes))

    def test_2_clientes_distantes_2_kilometros_para_direita(self):
        clientes = ((1,1),(3,1))
        distancias_esperadas = ((0,2),
                                (2,0))
        self.assertEqual(distancias_esperadas, distancias(clientes))
        
    def test_3_clientes_distantes_2_kilometros(self):
        clientes = ((1,1),(1,2),(1,3))
        distancias_esperadas = ((0,1,2),
                                (1,0,1),
                                (2,1,0))
        self.assertEqual(distancias_esperadas, distancias(clientes))
    
    def test_3_clientes_distantes_irracionais_kilometros(self):
        clientes = ((1,1),(1,2),(2,2))
        distancias_esperadas = ((0,1,sqrt(2)),
                                (1,0,1),
                                (sqrt(2),1,0))
        self.assertEqual(distancias_esperadas, distancias(clientes))
    
    
unittest.main()
