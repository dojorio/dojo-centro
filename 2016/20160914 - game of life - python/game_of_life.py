def game_of_life(table_of_life):
	

	if len(table_of_life[0]) == 2:
		return [[0, 0]]

	if len(table_of_life[0]) >= 3:
		result = []
		size = len(table_of_life[0])
		for idx in range(size):
			previous = table_of_life[0][idx-1] if idx > 0 else 0
			next = table_of_life[0][idx+1] if idx < size - 1 else 0
			if previous == 1 and next == 1:
				result.append(1)
			else:
				result.append(0)

		return [result]

	return [[0]]

