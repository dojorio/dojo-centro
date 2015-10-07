import unittest
from drunk import fail


class TestDrunk(unittest.TestCase):
	def test_one_house(self):
		probabilities = [
			[1],
		]
		result_fail = fail(initial_house=0,
		 				   drunks_house=0, 
		 				   tries=1,
		 				   probabilitie=probabilities)
		self.assertEqual(result_fail, 0)

unittest.main()