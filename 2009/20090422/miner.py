def start_matrix(col, row):
    matrix = list()
    for c in range(col):
        matrix.append(list())
        for r in range(row):
            matrix[c].append(0) 
            
    return matrix
    
def coloca_bomba(matriz, lin, col):
    matriz[lin][col]=-1
    return matriz 
    
def compute_field(field):
		
    return field

def compute_cell(field, col, row):
	bombs = 0
	if field[col][row]==-1: return -1
	for row in field:
		for cell in row:
			if cell == -1:
				bombs += 1
	return bombs