import unittest
from exchange import exchange

class TestExchange(unittest.TestCase):
    def test_coin_1(self):
        self.assertEqual(exchange(1), 3)

    def test_coin_2(self):
        self.assertEqual(exchange(2), 5)

unittest.main()
