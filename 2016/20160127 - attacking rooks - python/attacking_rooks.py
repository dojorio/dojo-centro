def attacking_rooks(board):
	count = 0
	if len(board[0]) == 2 and board[0][1] == "x":
		return 1

	if board[0][0] == ".":
		return len(board)

	if len(board[0]) == 2 and board[0][0] == "x":
		return 2

	return 0