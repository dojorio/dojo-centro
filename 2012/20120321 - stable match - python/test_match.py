import unittest
from match import match

class TestMatch(unittest.TestCase):
    def test_two_people_make_one_couple(self):
        preferences =   {'A': ('1',)}
        self.assertEqual(match(preferences), 1)

    def test_two_people_make_no_couple(self):
        preferences =   {'A': ()}
        self.assertEqual(match(preferences), 0)

    def test_four_people_make_two_couples(self):
        preferences =   {
            'A': ('1',),
            'B': ('2',),
        }
        self.assertEqual(match(preferences), 2)
        
    def test_three_people_make_one_couple(self):
        preferences =   {
            'A': ('1',),
            'B': ('1',),
        }
        self.assertEqual(match(preferences), 1)
    
    def test_four_people_make_two_couples_when_there_is_a_conflict(self):
        preferences =   {
            'A': ('1',),
            'B': ('1', '2'),
        }
        self.assertEqual(match(preferences), 2)

    def test_four_people_make_two_couples_when_there_is_a_conflict_2(self):
        preferences =   {
            'A': ('1', '2'),
            'B': ('1',),
        }
        self.assertEqual(match(preferences), 2)

unittest.main()
