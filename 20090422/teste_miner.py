import unittest

import miner

class TestMiner(unittest.TestCase):
	def test_col_only_field(self):
		col = 7
		row = 1
		field = miner.start_matrix(col, row)
		cells = 0
		for i in field:
			cells += 1
				
		self.assertEqual(cells, col)

	
	def test_row_only_field(self):
		col = 1
		row = 8
		field = miner.start_matrix(col, row)
		cells = 0
		for i in field[0]:
			cells += 1
				
		self.assertEqual(cells, row)
	
	def test_empty_field(self):
		col = 9
		row = 8
		field = miner.start_matrix(col, row)
		soma = 0
		for linha in field:
			for celula in linha:
				soma += celula
				
		self.assertEqual(soma, 0)
		
	def test_assert_bomb(self):
		col = 12
		row = 8
		field = miner.start_matrix(col, row)
		miner.coloca_bomba(field, 3,7)
		
		self.assertEqual(field[3][7], -1) 
		
	def test_assert_near_bomb(self):
		col = 1
		row = 1
		field = miner.start_matrix(col, row)
		field = miner.coloca_bomba(field, 0, 0)
		
		computed_field = miner.compute_field(field)
		self.assertEqual(computed_field, field)
		
	def test_2x2_field_with_1_bomb(self):
		col = 2
		row = 2
		field = miner.start_matrix(col, row)
		field = miner.coloca_bomba(field, 0, 0)
		
		computed_field = miner.compute_field(field)
		self.assertEqual(computed_field, [[-1, 1], [1, 1]])
		
	def test_2x2_field_with_1_bomb(self):
		col = 2
		row = 2
		field = miner.start_matrix(col, row)
		field = miner.coloca_bomba(field, 0, 0)

		computed_cell = miner.compute_cell(field, 0, 1)
		self.assertEqual(computed_cell, 1)

	def test_2x2_field_with_2_bombs(self):
		col = 2
		row = 2
		field = miner.start_matrix(col, row)
		field = miner.coloca_bomba(field, 0, 0)
		field = miner.coloca_bomba(field, 1, 1)

		computed_cell = miner.compute_cell(field, 0, 1)
		self.assertEqual(computed_cell, 2)
		
	def test_2x2_field_with_3_bombs(self):
		col = 2
		row = 2
		field = miner.start_matrix(col, row)
		field = miner.coloca_bomba(field, 0, 0)
		field = miner.coloca_bomba(field, 1, 1)
		field = miner.coloca_bomba(field, 1, 0)

		computed_cell = miner.compute_cell(field, 0, 1)
		self.assertEqual(computed_cell, 3)

	def test_3x3_field_with_4_bombs(self):
		col = row = 3
		field = miner.start_matrix(col, row)
		field = miner.coloca_bomba(field, 0, 0)
		field = miner.coloca_bomba(field, 0, 1)
		field = miner.coloca_bomba(field, 0, 2)
		field = miner.coloca_bomba(field, 2, 0)

		computed_cell = miner.compute_cell(field, 1, 1)
		self.assertEqual(computed_cell, 4)

	def test_3x3_field_with_5_bombs(self):
		col = row = 3
		field = miner.start_matrix(col, row)
		field = miner.coloca_bomba(field, 0, 0)
		field = miner.coloca_bomba(field, 0, 1)
		field = miner.coloca_bomba(field, 0, 2)
		field = miner.coloca_bomba(field, 2, 0)
		field = miner.coloca_bomba(field, 2, 1)

		computed_cell = miner.compute_cell(field, 1, 1)
		self.assertEqual(computed_cell, 5)
		
	def test_3x3_field_with_8_bombs(self):
		col = row = 3
		field = miner.start_matrix(col, row)
		field = miner.coloca_bomba(field, 0, 0)
		field = miner.coloca_bomba(field, 0, 1)
		field = miner.coloca_bomba(field, 0, 2)
		field = miner.coloca_bomba(field, 1, 0)
		field = miner.coloca_bomba(field, 1, 2)
		field = miner.coloca_bomba(field, 2, 0)
		field = miner.coloca_bomba(field, 2, 1)
		field = miner.coloca_bomba(field, 2, 2)

		computed_cell = miner.compute_cell(field, 1, 1)
		self.assertEqual(computed_cell, 8)

	def test_3x3_field_with_8_bombs_(self):
		col = row = 3
		field = miner.start_matrix(col, row)
		field = miner.coloca_bomba(field, 0, 0)
		field = miner.coloca_bomba(field, 0, 1)
		field = miner.coloca_bomba(field, 0, 2)
		field = miner.coloca_bomba(field, 1, 0)
		field = miner.coloca_bomba(field, 1, 2)
		field = miner.coloca_bomba(field, 2, 0)
		field = miner.coloca_bomba(field, 2, 1)
		field = miner.coloca_bomba(field, 2, 2)

		computed_cell = miner.compute_cell(field, 0, 0)
		self.assertEqual(computed_cell, -1)
		
	def test_3x3_field_with_8_bombs_the_right_way(self):
		field = [[-1,-1,-1],[-1,0,-1],[-1,-1,-1]]
		#computed_field = miner.compute_fieldl(field,1,1)
		computed_field = field
		mapa = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
		self.assertEqual(computed_field, mapa)
unittest.main()		   
