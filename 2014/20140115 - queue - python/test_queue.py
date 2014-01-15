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

unittest.main()