import unittest
from beverages import beverage_sort

class TestBeverages(unittest.TestCase):
    def test_nenhuma_bebida(self):
        bebidas = ()
        relacoes = ()
        self.assertEqual((), beverage_sort(bebidas, relacoes))
        
    def test_uma_bebida(self):
        bebidas = ("vinho",)
        relacoes = ()
        self.assertEqual(("vinho",), beverage_sort(bebidas, relacoes))

    def test_duas_bebidas_com_relacao(self):
        bebidas = ("rum", "vinho")
        relacoes = (("vinho", "rum"),)
        self.assertEqual(("vinho", "rum"), beverage_sort(bebidas, relacoes))

    def test_tres_bebidas_com_relacao(self):
        bebidas = ("rum", "vinho", "cerveja")
        relacoes = (
                    ("cerveja", "vinho"),
                    ("vinho", "rum"),
                   )
        self.assertEqual(("cerveja", "vinho", "rum"), beverage_sort(bebidas, relacoes))

    def test_tres_bebidas_com_relacao_so_pela_primeira(self):
        bebidas = ("rum", "cerveja", "vinho")
        relacoes = (
                    ("vinho", "rum"),
                   )
        self.assertEqual(("cerveja", "vinho", "rum"), beverage_sort(bebidas, relacoes))

       
unittest.main()
