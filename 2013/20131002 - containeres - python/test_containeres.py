import unittest
from skyline import skyline

class TestSkyline(unittest.TestCase):
    def test_nenhum_predio(self):
        predios = []
        self.assertEqual([], skyline(predios))    

    def test_um_predio(self):
        predios = [(5, 20, 10)]
        self.assertEqual([5, 20, 10, 0], skyline(predios))

    def test_dois_predios_separados(self):
        predios = [(5, 30, 10), (15, 30, 20)]
        self.assertEqual([5, 30, 10, 0, 15, 30, 20, 0], skyline(predios))
    
    def test_tres_predios_separados(self):
        predios = [(5, 30, 10), (15, 30, 20), (21, 5, 23)]
        self.assertEqual([5, 30, 10, 0, 15, 30, 20, 0, 21, 5, 23, 0], skyline(predios))

    def test_dois_predios_colados(self):
        predios = [(5, 30, 10), (10, 30, 20)]
        self.assertEqual([5, 30, 20, 0], skyline(predios))
          
if __name__ == '__main__':
    unittest.main()
