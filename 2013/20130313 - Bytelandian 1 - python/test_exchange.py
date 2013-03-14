import unittest
from exchange import n_zeroes, max_value

class TestMaxValue(unittest.TestCase):
    def test_coin_0(self):
        self.assertEqual(max_value(0), 0)

    def test_useless_coins(self):
        for i in range(1, 12):
             self.assertEqual(max_value(i), i)

    def test_coin_12(self):
        self.assertEqual(max_value(12), 13)

    def test_coin_13(self):
        self.assertEqual(max_value(13), 13)

    def test_coin_16(self):
        self.assertEqual(max_value(16), 17)

    def test_coin_20(self):
        self.assertEqual(max_value(20), 21)

    def test_coin_24(self):
        self.assertEqual(max_value(24), 27)

    def test_coin_27(self):
        self.assertEqual(max_value(27), 28)

    def test_coin_1000(self):
        self.assertEqual(max_value(1000), 1370)

class TestNZeroes(unittest.TestCase):
    def test_coin_0(self):
        self.assertEqual(n_zeroes(0), 1)

    def test_coin_1(self):
        self.assertEqual(n_zeroes(1), 3)

    def test_coin_2(self):
        self.assertEqual(n_zeroes(2), 5)

    def test_coin_3(self):
        self.assertEqual(n_zeroes(3), 7)

    def test_coin_4(self):
        self.assertEqual(n_zeroes(4), 11)

    def test_coin_5(self):
        self.assertEqual(n_zeroes(5), 11)

    def test_coin_6(self):
        self.assertEqual(n_zeroes(6), 15)

    def test_coin_7(self):
        self.assertEqual(n_zeroes(7), 15)

    def test_coin_8(self):
        self.assertEqual(n_zeroes(8), 21)

    def test_coin_9(self):
        self.assertEqual(n_zeroes(9), 23)

    def test_coin_12(self):
        self.assertEqual(n_zeroes(12), 33)

    def test_coin_18(self):
        self.assertEqual(n_zeroes(18), 49)

    def test_coin_24(self):
        self.assertEqual(n_zeroes(24), 69)

    def test_coin_36(self):
        self.assertEqual(n_zeroes(36), 105)

    def test_coin_25(self):
        self.assertEqual(n_zeroes(25), 69)

    def test_coin_50(self):
        self.assertEqual(n_zeroes(50), 69+43+33)






unittest.main()
