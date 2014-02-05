import unittest
from campominado import campominado

class TestCampominado(unittest.TestCase):
    def test_campo1x1_sem_bomba(self):
        campo = [['.']]
        self.assertEquals(campominado(campo), [['0']])

    def test_campo1x1_com_bomba(self):
        campo = [['*']]
        self.assertEquals(campominado(campo), [['*']])

    def test_campo1x2_com_bomba(self):
        campo = [['*','.']]
        self.assertEquals(campominado(campo), [['*', '1']])

    def test_campo1x2_com_bomba_direita(self):
        campo = [['.','*']]
        self.assertEquals(campominado(campo), [['1', '*']])

    def test_campo1x2_sem_bomba(self):
        campo = [['.', '.']]
        self.assertEquals(campominado(campo), [['0', '0']])

    def test_campo1x3_com_bomba_a_esquerda(self):
        campo = [['*', '.', '.']]
        self.assertEquals(campominado(campo), [['*', '1', '0']])

unittest.main()
