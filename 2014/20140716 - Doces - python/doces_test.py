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

unittest.main()