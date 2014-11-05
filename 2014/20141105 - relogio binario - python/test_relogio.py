import unittest
from relogio import hora_binaria

class TestRelogio(unittest.TestCase):
    def test_1_1(self):
        self.assertEquals(hora_binaria(1,1),('0001','000001'))

    def test_1_0(self):
        self.assertEquals(hora_binaria(1,0),('0001','000000'))

unittest.main()