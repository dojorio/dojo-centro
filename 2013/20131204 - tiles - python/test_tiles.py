import unittest
from tiles import how_many_ways

class TestTiles(unittest.TestCase):
    def test_1_tile(self):
        self.assertEqual(1, how_many_ways(1))

    def test_2_tiles(self):
        self.assertEqual(2, how_many_ways(2))
    
    def test_4_tiles(self):
        self.assertEqual(5, how_many_ways(4))

    def test_5_tiles(self):
        self.assertEqual(8, how_many_ways(5))

    def test_34_tiles(self):
        self.assertEqual(9227465, how_many_ways(34))

    def test_2_tiles_3_rows(self):
        self.assertEqual(1, how_many_ways(2, 3))

    def test_3_tiles_3_rows(self):
        self.assertEqual(2, how_many_ways(3, 3))

    def test_4_tiles_3_rows(self):
        self.assertEqual(4, how_many_ways(4, 3))


unittest.main()
