def game_of_life(table_of_life):

	if len(table_of_life) > 1:
		result = []
		size = len(table_of_life)

		for idx in range(len(table_of_life)):
			current = table_of_life[idx][0]
			previous = table_of_life[idx-1][0] if idx > 0 else 0
			next = table_of_life[idx+1][0] if idx < size - 1 else 0

			if previous and next:
				result.append([current])
			else:
				result.append([0])

		return result

	if len(table_of_life[0]) >= 2:
		result = []
		size = len(table_of_life[0])
		
		for idx in range(size):
			current = table_of_life[0][idx]
			previous = table_of_life[0][idx-1] if idx > 0 else 0
			next = table_of_life[0][idx+1] if idx < size - 1 else 0
			
			if previous and next:
				result.append(current)
			else:
				result.append(0)

		return [result]

	return [[0]]

