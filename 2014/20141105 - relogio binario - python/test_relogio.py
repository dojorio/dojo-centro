import unittest
from relogio import hora_binaria

class TestRelogio(unittest.TestCase):
    def test_1_1(self):
        self.assertEquals(hora_binaria(1, 1), ('0001', '000001'))

    def test_1_0(self):
        self.assertEquals(hora_binaria(1, 0), ('0001', '000000'))

    def test_1_2(self):
        self.assertEquals(hora_binaria(1, 2), ('0001', '000010'))

    def test_1_3(self):
        self.assertEquals(hora_binaria(1, 3), ('0001', '000011'))

    def test_1_4(self):
        self.assertEquals(hora_binaria(1, 4), ('0001', '000100'))

    def test_1_8(self):
        self.assertEquals(hora_binaria(1, 8), ('0001', '001000'))

    def test_1_16(self):
        self.assertEquals(hora_binaria(1, 16), ('0001', '010000'))

    def test_1_32(self):
        self.assertEquals(hora_binaria(1, 32), ('0001', '100000'))

    def test_1_17(self):
        self.assertEquals(hora_binaria(1, 17), ('0001', '010001'))

    def test_2_0(self):
        self.assertEquals(hora_binaria(2, 0), ('0010', '000000'))

unittest.main()