import unittest
from light import americusto, conta

#custo(consumo) -> conta(custo(a+b), (custo(a)-custo(b))), custo(a)

class TestAmericusto(unittest.TestCase):
    def teste_consumo_0(self):
        self.assertEqual(americusto(0), 0)

    def teste_consumo_1(self):
        self.assertEqual(americusto(1), 2)

    def teste_consumo_101(self):
        self.assertEqual(americusto(100+1), 200+3)

    def teste_consumo_10001(self):
        self.assertEqual(americusto(100 + 9900 + 1), 100*2 + 9900*3 + 5)

    def teste_consumo_1000001(self):
        self.assertEqual(americusto(100 + 9900 + 990000 + 1), 100*2 + 9900*3 + 990000*5 + 7)

class TestConta(unittest.TestCase):
    def teste_consumo_0(self):
        self.assertEqual(conta(0, 0), 0)

    def teste_consumo_1_vizinho_2(self):
        self.assertEqual(conta(6, 2), 2)

    def teste_consumo_0_vizinho_1(self):
        self.assertEqual(conta(2, 2), 0)
        
    def teste_consumo_50_vizinho_52(self):
        self.assertEqual(conta(206, 4), 100)
        
    def teste_consumo_51_vizinho_52(self):
        self.assertEqual(conta(209, 2), 102)
        
unittest.main()
