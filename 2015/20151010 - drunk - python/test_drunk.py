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
		 				   probabilities=probabilities)
		self.assertEqual(result_fail, 0)

	def test_two_houses(self):
		probabilities = [
			[.5, .5], 
			[.5, .5]
		]
		result_fail = fail(initial_house=1,
		 				   drunks_house=0, 
		 				   tries=1,
		 				   probabilities=probabilities)
		self.assertEqual(result_fail, 0)
unittest.main()