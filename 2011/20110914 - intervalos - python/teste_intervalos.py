import unittest
from intervalos import intervalos

class TestIntervalos(unittest.TestCase):
    def test_um_numero(self):
        self.assertEqual(intervalos([100]), [(100,)])

    def test_dois_numeros_avulsos(self):
        self.assertEqual(intervalos([100, 110]), 
                                   [(100,), (110,)])
                                   
    def test_dois_numeros_consecutivos(self):
        self.assertEqual(intervalos([100, 101]), [(100, 101)])
        
    def test_tres_numeros_consecutivos(self):
        self.assertEqual(intervalos([100, 101, 102]), 
                                   [(100, 102)])
                                   
    # def test_tres_numeros_consecutivos_e_um_numero_avulso(self):
        # self.assertEqual(intervalos([100, 101, 102, 110]), 
                                   # [(100, 102), (110,)])

unittest.main()