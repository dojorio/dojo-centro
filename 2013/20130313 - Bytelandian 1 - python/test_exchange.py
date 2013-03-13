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

    def test_coin_8(self):
        self.assertEqual(exchange(8), 21)

    def test_coin_9(self):
        self.assertEqual(exchange(9), 23)

    def test_coin_12(self):
        self.assertEqual(exchange(12), 33)

    def test_coin_18(self):
        self.assertEqual(exchange(18), 49)

    def test_coin_24(self):
        self.assertEqual(exchange(24), 69)

    def test_coin_36(self):
        self.assertEqual(exchange(36), 105)

	def test_coin_25(self):
		self.assertEqual(exchange(25), 69)

	def test_coin_50(self):
		self.assertEqual(exchange(50), 69+43+33)






unittest.main()
