def attacking_rooks(board):
	count = 0
	if len(board[0]) == 2:
		if board[1] != ['x', 'x']:
			count = count + 1  
		return count

	if board[0][0] == ".":
		return len(board[0])

	return 0