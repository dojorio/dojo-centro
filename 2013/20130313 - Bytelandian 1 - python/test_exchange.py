import unittest
from exchange import exchange

class TestExchange(unittest.TestCase):
    def test_coin_0(self):
        self.assertEqual(exchange(0), 1)

    def test_coin_1(self):
        self.assertEqual(exchange(1), 3)

    def test_coin_2(self):
        self.assertEqual(exchange(2), 5)

    def test_coin_3(self):
        self.assertEqual(exchange(3), 7)

    def test_coin_4(self):
        self.assertEqual(exchange(4), 11)

    def test_coin_5(self):
        self.assertEqual(exchange(5), 11)

    def test_coin_6(self):
        self.assertEqual(exchange(6), 15)

    def test_coin_7(self):
        self.assertEqual(exchange(7), 15)

    def test_coin_12(self):
        self.assertEqual(exchange(12), )


unittest.main()
