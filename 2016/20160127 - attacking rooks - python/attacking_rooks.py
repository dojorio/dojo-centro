from functools import reduce 
def attacking_rooks(board):
    f = lambda memo, row: memo + 1 if row.count('x') != len(board) else memo
    return reduce(f , board, 0)

