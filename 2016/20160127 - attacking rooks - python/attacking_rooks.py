def attacking_rooks(board): 
    if board[0].count('.') == len(board):
        return len(board) - 1

    if board[0].count('x') == len(board):
        return len(board) - 1

    return len(board)
