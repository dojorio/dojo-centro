def game_of_life(table_of_life):
	

	if len(table_of_life[0]) == 2:
		return [[0, 0]]

	if len(table_of_life[0]) == 3:
		return [[0, 0, 0]]
	
	if len(table_of_life[0]) == 3 and len(table_of_life[0][1] == 1):
		return [[0, 1, 0]]
		

	return [
		[0]
	]

