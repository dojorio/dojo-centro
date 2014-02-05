import unittest
from formiga import onde_está

class TestFormiga(unittest.TestCase):
    def test_0(self):
        self.assertEqual(onde_está(0), (0, 0))

    def test_1(self):
        self.assertEqual(onde_está(1), (0, 1))

    def test_2(self):
        self.assertEqual(onde_está(2), (1, 1))

    def test_3(self):
        self.assertEqual(onde_está(3), (1, 0))

    def test_4(self):
        self.assertEqual(onde_está(4), (2, 0))

    def test_5(self):
        self.assertEqual(onde_está(5), (2, 1))

    def test_6(self):
        self.assertEqual(onde_está(6), (2, 2))

    def test_7(self):
        self.assertEqual(onde_está(7), (1, 2))

    def test_8(self):
        self.assertEqual(onde_está(8), (0, 2))

    def test_9(self):
        self.assertEqual(onde_está(9), (0, 3))

    def test_10(self):
        self.assertEqual(onde_está(10), (1, 3))

    def test_13(self):
        self.assertEqual(onde_está(13), (3, 2))

    def test_25(self):
        self.assertEqual(onde_está(25), (0, 5))

unittest.main()
