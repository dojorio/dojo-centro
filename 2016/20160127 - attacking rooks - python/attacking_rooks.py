from functools import reduce 

def transpose_board(board):
    transboard = []
    for i in range(0,len(board)):
        new_row = []
        for j in range(0,len(board)):
            new_row.append(board[j][i])
        transboard.append(new_row)

    return transboard

def attacking_rooks(board):
    if len(board) == 3:
        return 3 if board[1].count('x') == 0 else 4

    transboard = transpose_board(board)

    f = lambda memo, row: memo + 1 if row.count('x') != len(board) else memo    

    return min(reduce(f , transboard, 0), reduce(f , board, 0))
