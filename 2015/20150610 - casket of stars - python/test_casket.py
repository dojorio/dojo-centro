import unittest
from casket import destroy


class TestCasketOfStars(unittest.TestCase):
    def test_com_tres_estrelas(self):
        self.assertEqual(3, destroy([1, 2, 3]))

    def test_com_tres_estrelas_iguais(self):
        self.assertEqual(1, destroy([1, 1, 1]))

    def test_com_tres_estrelas_duas_iguais(self):
        self.assertEqual(2, destroy([2, 1, 1]))

    def test_com_quatro_estrelas(self):
        self.assertEqual(4, destroy([2, 1, 1, 1])) 

    def test_com_quatro_estrelas_b(self):
        self.assertEqual(8, destroy([2, 1, 3, 1]))  

    def test_com_quatro_estrelas_c(self):
        self.assertEqual(8, destroy([1, 3, 1, 2]))       

    def test_com_quatro_estrelas_d(self):
        self.assertEqual(20, destroy([3, 2, 2, 4]))

    def test_com_quatro_estrelas_e(self):
        self.assertEqual(34, destroy([2, 1, 8, 9]))

    def test_com_quatro_estrelas_f(self):
        self.assertEqual(2937051, destroy([477,744,474,777,447,747,777,474]))
        self.assertEqual(10400, destroy([100,2,1,3,100]))



unittest.main()