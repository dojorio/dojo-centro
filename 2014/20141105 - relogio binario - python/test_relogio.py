import unittest
from relogio import hora_binaria

class TestRelogio(unittest.TestCase):
    def test_1_1(self):
        self.assertEquals(hora_binaria(1,1), ('0001', '000001'))

    def test_1_0(self):
        self.assertEquals(hora_binaria(1,0), ('0001', '000000'))

    def test_1_2(self):
        self.assertEquals(hora_binaria(1,2), ('0001', '000010'))

    def test_1_3(self):
        self.assertEquals(hora_binaria(1,3), ('0001', '000011'))

    def test_1_4(self):
        self.assertEquals(hora_binaria(1,4), ('0001', '000100'))

unittest.main()