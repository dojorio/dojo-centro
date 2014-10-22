import unittest
from logic import add, xor

class TestLogic(unittest.TestCase):
    def test_add_0_0(self):
        self.assertEqual(add(0, 0), 0)

    def test_add_0_1(self):
        self.assertEqual(add(0, 1), 1)

    def test_add_1_1(self):
        self.assertEqual(add(1, 1), 2)

class TestXor(unittest.TestCase):
    def test_xor_False_False(self):
        self.assertEqual(xor(False, False), False)

    def test_xor_True_False(self):
        self.assertEqual(xor(True, False), True)

    def test_xor_False_True(self):
        self.assertEqual(xor(False, True), True)

    def test_xor_True_True(self):
        self.assertEqual(xor(True, True), False)

unittest.main()