import unittest
from cards import cards

class TestCards(unittest.TestCase):
    def test_duas_cartas_iguais(self):
        cartas = [1, 1]
        self.assertEqual(1, cards(cartas))

    def test_duas_cartas_diferentes(self):
        cartas = [1, 2]
        self.assertEqual(2, cards(cartas))

    def test_duas_cartas_diferentes_2_1(self):
        cartas = [2, 1]
        self.assertEqual(2, cards(cartas))

    def test_quatro_cartas_iguais(self):
        cartas = [1, 1, 1, 1]
        self.assertEqual(2, cards(cartas))

    def test_quatro_cartas_iguais_2(self):
        cartas = [2, 2, 2, 2]
        self.assertEqual(4, cards(cartas))

    def test_quatro_cartas_diferentes(self):
        cartas = [1, 2, 2, 1]
        self.assertEqual(3, cards(cartas))

    def test_quatro_cartas_diferentes1234(self):
        cartas = [1, 2, 3, 4]
        self.assertEqual(6, cards(cartas))

    def test_quatro_cartas_diferentes_onde_o_melhor_eh_ser_esperto(self):
        cartas = [47, 50, -3, 7]
        self.assertEqual(57, cards(cartas))

    def test_quatro_cartas_diferentes_onde_o_melhor_eh_ser_esperto2(self):
        cartas = [7, -3, 50, 47]
        self.assertEqual(57, cards(cartas))

    def test_quatro_cartas_diferentes_onde_o_melhor_eh_ser_meio_burro(self):
        cartas = [7, -3, 47, 50]
        self.assertEqual(57, cards(cartas))

    def test_seis_cartas_diferentes(self):
        cartas = [811605199,89864465,877809956,930012974,283791902,907039700]
        self.assertEqual(2068641558, cards(cartas))

    def test_10(self):
        cartas = [1]*30
        self.assertEqual(len(cartas)/2, cards(cartas))
    
    

unittest.main()
