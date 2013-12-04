memory = {0:1, 1:1}

def how_many_ways(tile, rows=2):
	if rows == 3:
		return tile - 1
	if tile not in memory:
		memory[tile] = how_many_ways(tile-2) + how_many_ways(tile-1)
	return memory[tile]
	
	
	
	
