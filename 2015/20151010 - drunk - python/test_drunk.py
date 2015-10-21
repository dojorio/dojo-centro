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

	def test_one_house_homeless_drunk(self):
		probabilities = [
			[1],
		]
		result_fail = fail(initial_house=0,
		 				   drunks_house=None, 
		 				   tries=1,
		 				   probabilities=probabilities)
		self.assertEqual(result_fail, 1)


	def test_two_houses_1(self):
		probabilities = [
			[.5, .5], 
			[.5, .5]
		]
		result_fail = fail(initial_house=0,
		 				   drunks_house=1, 
		 				   tries=1,
		 				   probabilities=probabilities)
		self.assertEqual(result_fail, 0.5)

	def test_two_houses_2(self):
		probabilities = [
			[.3, .7], 
			[.3, .7]
		]
		result_fail = fail(initial_house=1,
		 				   drunks_house=0, 
		 				   tries=1,
		 				   probabilities=probabilities)
		self.assertEqual(result_fail, 0.7)

	def test_two_houses_3(self):
		probabilities = [
			[.5, .5], 
			[.5, .5]
		]
		result_fail = fail(initial_house=0,
		 				   drunks_house=1, 
		 				   tries=2,
		 				   probabilities=probabilities)
		self.assertEqual(result_fail, 0.25)

	def test_three_houses(self):
		probabilities = [
			[.25, .25, .5], 
			[.25, .5, .25],
			[.5, .25, .25],  
		]
		result_fail = fail(initial_house=0,
		 				   drunks_house=1, 
		 				   tries=2,
		 				   probabilities=probabilities)
		self.assertEqual(result_fail, 0.5625)

unittest.main()