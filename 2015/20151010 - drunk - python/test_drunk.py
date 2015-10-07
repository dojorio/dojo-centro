import unittest
from drunk import fail


class TestDrunk(unittest.TestCase):
	def test_one_house(self):
		initial_house = 0
		drunks_house = 0
		tries = 1
		probabilities = [
			[1],
		]

		self.assertEqual(fail(initial_house,
		 					   drunks_house, 
		 					   tries), 0)

unittest.main()