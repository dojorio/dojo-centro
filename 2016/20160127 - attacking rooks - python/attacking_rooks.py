from functools import reduce 

def transpose_board(board):
    output = []
    for i in range(0,len(board)):
        new_row = []
        for j in range(0,len(board)):
            new_row.append(board[j][i])
        output.append(new_row)

    return output


def attacking_rooks(board):
    f = lambda memo, row: memo + 1 if row.count('x') != len(board) else memo    
    return reduce(f , board, 0)
