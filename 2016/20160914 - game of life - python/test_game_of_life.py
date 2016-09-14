import unittest
from game_of_life import game_of_life

class TestGameOfLife(unittest.TestCase):
	def test_empty(self):
		table_of_life_now = [
			[0]
		]
		table_of_life_later = [
			[0]
		]
		self.assertEquals(game_of_life(table_of_life_now), 
			table_of_life_later)

	def test_empty(self):
		table_of_life_now = [
			[1, 0]
		]
		table_of_life_later = [
			[0, 0]
		]
		self.assertEquals(game_of_life(table_of_life_now), 
			table_of_life_later)
	
unittest.main()