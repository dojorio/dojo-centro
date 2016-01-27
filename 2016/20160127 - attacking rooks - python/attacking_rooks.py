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
    transboard = transpose_board(board)
    
    f = lambda memo, row: memo + 1 if row.count('x') != len(board) else memo    

    transboard_count = reduce(f , transboard, 0)
    board_count = reduce(f , board, 0)

    if(transboard_count < board_count):
        return transboard_count
    return board_count
