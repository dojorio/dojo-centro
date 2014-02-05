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


unittest.main()
