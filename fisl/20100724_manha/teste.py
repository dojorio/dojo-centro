import unittest
from codigo import *

class TestTriangulosInvalidos(unittest.TestCase):

    def test_um_triangulo_com_lados_negativos(self):
        self.assertEquals("invalido", triangulo(-5, 1, -1))

    def test_um_triangulo_0_0_0(self):
        self.assertEquals("invalido", triangulo(0, 0, 0))

    def test_um_triangulo_5_670_5(self):
        self.assertEquals("invalido", triangulo(5, 670, 5))
    
    def test_um_triangulo_670_5_5(self):
        self.assertEquals("invalido", triangulo(670, 5, 5))
    
    def test_um_triangulo_500_50_5(self):
        self.assertEquals("invalido", triangulo(500, 50, 5))


class TestTrianguloEquilatero(unittest.TestCase):

    def test_um_triangulo_5_5_5(self):
        self.assertEquals("equilatero", triangulo(5, 5, 5))
        
    def test_um_triangulo_5_4_5(self):
        self.assertNotEquals("equilatero", triangulo(5, 4, 5))


class TestTrianguloIsosceles(unittest.TestCase):

    def test_um_triangulo_5_5_4(self):
        self.assertEquals("isosceles", triangulo(5, 5, 4))

    def test_um_triangulo_5_4_5(self):
        self.assertEquals("isosceles", triangulo(5, 4, 5))
        
    def test_um_triangulo_4_5_5(self):
        self.assertEquals("isosceles", triangulo(4, 5, 5))


unittest.main()
