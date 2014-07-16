import unittest

class DocesTest(unittest.TestCase):
    def test_um_doce_2kg(self):
        doces = [2]

        self.assertEqual(divisao(doces), 2)

unittest.main()