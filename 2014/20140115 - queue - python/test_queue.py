import unittest
from queue import salim

class TestQueue(unittest.TestCase):
    def test_1x1(self):
        estacionamento = ['.']
        self.assertEquals(salim(estacionamento), 1)

    def test_1x2(self):
        estacionamento = ['..']
        self.assertEquals(salim(estacionamento), 2)

    def test_2x1(self):
        estacionamento = ['.',
                          '.']
        self.assertEquals(salim(estacionamento), 2)

    def test_1x2_com_obstaculo(self):
        estacionamento = ['.#']
        self.assertEquals(salim(estacionamento), 1)

    def test_2x1_com_obstaculo(self):
        estacionamento = ['.',
                          '#']
        self.assertEquals(salim(estacionamento), 1)

    def test_1x3_com_obstaculo(self):
        estacionamento = ['.#.']
        self.assertEquals(salim(estacionamento), 1)

    def test_1x3_com_obstaculo_longe(self):
        estacionamento = ['..#']
        self.assertEquals(salim(estacionamento), 2)

    def test_1x3_com_obstaculo_na_porta(self):
        estacionamento = ['#..']
        self.assertEquals(salim(estacionamento), 0)

    def test_2x2_sem_obstaculo(self):
        estacionamento = ['..',
                          '..']
        self.assertEquals(salim(estacionamento), 4)

    def test_2x2_com_um_obstaculo(self):
        estacionamento = ['.#',
                          '..']
        self.assertEquals(salim(estacionamento), 3)

    def test_3x2_sem_obstaculo(self):
        estacionamento = ['..',
                          '..',
                          '..']
        self.assertEquals(salim(estacionamento), 6)

    def test_3x2_com_obstaculo(self):
        estacionamento = ['..',
                          '#.',
                          '..']
        self.assertEquals(salim(estacionamento), 5)
    
unittest.main()