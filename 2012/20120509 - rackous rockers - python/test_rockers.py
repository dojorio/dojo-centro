#!/usr/bin/python
import unittest
from rockers import rock

class TestRockers(unittest.TestCase):
    def test_one_1min_cd_with_one_1m_song(self):
        result = rock(cds=1, size=1, songs=[1])
        self.assertEqual(result, 1)

    def test_one_2min_cd_with_two_1m_song(self):
        result = rock(cds=1, size=2, songs=[1, 1])
        self.assertEqual(result, 2)
        
    def test_one_2min_cd_with_one_2min_song(self):
        result = rock(cds=1, size=2, songs=[2])
        self.assertEqual(result, 1)
        
    def test_one_2min_cd_with_one_5min_song(self):
        result = rock(cds=1, size=2, songs=[5])
        self.assertEqual(result, 0)
        
    def test_one_2min_cd_with_one_5min_and_one_1min_song(self):
        result = rock(cds=1, size=2, songs=[5,1])
        self.assertEqual(result, 1)

    def test_one_2min_cd_with_three_1min_song(self):
        result = rock(cds=1, size=2, songs=[1,1,1])
        self.assertEqual(result, 2)

    def test_one_2min_cd_with_one_2min_and_two_1min_songs(self):
        result = rock(cds=1, size=2, songs=[2,1,1])
        self.assertEqual(result, 2)

    def test_cds2_size2_songs121(self):
        result = rock(cds=2, size=2, songs=[1,2,1])
        self.assertEqual(result, 2)

    def test_cds2_size4_songs1421(self):
        result = rock(cds=2, size=4, songs=[1,4,2,1])
        self.assertEqual(result, 3)

    def test_cds2_size2_songs1111(self):
        result = rock(cds=2, size=2, songs=[1,1,1,1])
        self.assertEqual(result, 4)


unittest.main()
