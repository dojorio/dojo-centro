import unittest
from indiana import indiana

class TestIndiana(unittest.TestCase):
    def test_uma_rampa(self):
        rampas = [(5, 1, 4)]
        largura = 2
        altura = 5
        self.assertEqual(1, indiana(rampas, largura, altura))

    def test_uma_rampa_com_mais_espaco(self):
        rampas = [(5, 1, 4)]
        largura = 3
        altura = 5
        self.assertEqual(2, indiana(rampas, largura, altura))


unittest.main()
