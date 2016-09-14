import unittest
from game_of_life import game_of_life

class TestGameOfLife(unittest.TestCase):
	def test_0(self):
		table_of_life_now = [
			[0]
		]
		table_of_life_later = [
			[0]
		]
		self.assertEquals(game_of_life(table_of_life_now), 
			table_of_life_later)

	def test_0_0(self):
		table_of_life_now = [
			[1, 0]
		]
		table_of_life_later = [
			[0, 0]
		]
		self.assertEquals(game_of_life(table_of_life_now), 
			table_of_life_later)
	
	def test_0_1(self):
		table_of_life_now = [
			[1, 0, 1]
		]
		table_of_life_later = [
			[0, 0, 0]
		]
		self.assertEquals(game_of_life(table_of_life_now), 
			table_of_life_later)
	
	def test_0_2(self):
		table_of_life_now = [
			[1, 1, 1]
		]
		table_of_life_later = [
			[0, 1, 0]
		]
		self.assertEquals(game_of_life(table_of_life_now), 
			table_of_life_later)
				

unittest.main()