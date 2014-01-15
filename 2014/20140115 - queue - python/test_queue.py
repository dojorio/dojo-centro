import unittest
from queue import salim

class TestQueue(unittest.TestCase):
    
    def test_1x1(self):
        estacionamento = ['.']
        self.assertEquals(salim(estacionamento), 1)

unittest.main()