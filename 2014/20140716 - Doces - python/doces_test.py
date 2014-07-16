import unittest
from doces import menor_diferenca

class DocesTest(unittest.TestCase):
    def test_um_doce_2kg(self):
        doces = [2]
        self.assertEqual(menor_diferenca(doces), 2)

    def test_um_doce_5kg(self):
        doces = [5]
        self.assertEqual(menor_diferenca(doces), 5)

    def test_dois_doces_2kg_5kg(self):
        doces = [2, 5]
        self.assertEqual(menor_diferenca(doces), 3)

    def test_dois_doces_2kg_2kg(self):
        doces = [2, 2]
        self.assertEqual(menor_diferenca(doces), 0)

    def test_dois_doces_2kg_2kg_2kg(self):
        doces = [2, 2, 2]
        self.assertEqual(menor_diferenca(doces), 0)

unittest.main()