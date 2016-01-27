def attacking_rooks(board):
	if len(board[0]) == 2:
		return 2 - board[0].count('x')

	if board[0][0] == ".":
		return len(board[0])

	return 0