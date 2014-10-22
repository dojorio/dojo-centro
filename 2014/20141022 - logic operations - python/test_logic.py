import unittest
from logic import add

class TestLogic(unittest.TestCase):
    def test_add_0_0(self):
        self.assertEqual(add(0, 0), 0)

    def test_add_0_1(self):
        self.assertEqual(add(0, 1), 1)

    def test_add_1_1(self):
        self.assertEqual(add(1, 1), 2)

unittest.main()