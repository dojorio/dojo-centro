import unittest
from doces import menor_diferenca

class DocesTest(unittest.TestCase):
    def test_2kg(self):
        doces = [2]
        self.assertEqual(menor_diferenca(doces), 2)

    def test_5kg(self):
        doces = [5]
        self.assertEqual(menor_diferenca(doces), 5)

    def test_2kg_5kg(self):
        doces = [2, 5]
        self.assertEqual(menor_diferenca(doces), 3)

    def test_2kg_2kg(self):
        doces = [2, 2]
        self.assertEqual(menor_diferenca(doces), 0)

    def test_2kg_2kg_2kg(self):
        doces = [2, 2, 2]
        self.assertEqual(menor_diferenca(doces), 2)

    def test_2kg_3kg_2kg(self):
        doces = [2, 3, 2]
        self.assertEqual(menor_diferenca(doces), 1)

    def test_3kg_2kg_2kg(self):
        doces = [3, 2, 2]
        self.assertEqual(menor_diferenca(doces), 1)

    def test_5kg_2kg_2kg(self):
        doces = [5, 2, 2]
        self.assertEqual(menor_diferenca(doces), 1)

    def test_2kg_2kg_2kg_2kg(self):
        doces = [2, 2, 2, 2]
        self.assertEqual(menor_diferenca(doces), 0)

    def test_2kg_2kg_2kg_3kg(self):
        doces = [2, 2, 2, 3]
        self.assertEqual(menor_diferenca(doces), 1)

    def test_1kg_2kg_3kg_4kg(self):
        doces = [1, 2, 3, 4]
        self.assertEqual(menor_diferenca(doces), 0)

    def test_1kg_2kg_4kg_3kg(self):
        doces = [1, 2, 4, 3]
        self.assertEqual(menor_diferenca(doces), 0)

    def test_5kg_1kg_1kg_1kg(self):
        doces = [5, 1, 1, 1]
        self.assertEqual(menor_diferenca(doces), 2)

    def test_6kg_1kg_1kg_1kg(self):
        doces = [6, 1, 1, 1]
        self.assertEqual(menor_diferenca(doces), 3)

    def test_6kg_3kg_2kg_1kg(self):
        doces = [6, 3, 2, 1]
        self.assertEqual(menor_diferenca(doces), 0)

    def test_6kg_3kg_2kg_1kg(self):
        doces = [6, 3, 2, 1]
        self.assertEqual(menor_diferenca(doces), 0)

    def test_1_2_3_4_5(self):
        doces = [1, 2, 3, 4, 5]
        self.assertEqual(menor_diferenca(doces), 1)

    def test_1_2_3_4_6(self):
        doces = [1, 2, 3, 4, 6]
        self.assertEqual(menor_diferenca(doces), 0)

    def test_3_criancas(self):
        doces = [3, 3, 3, 3, 3, 3, 5, 5]
        self.assertEqual(menor_diferenca(doces, 3), 1)



unittest.main()