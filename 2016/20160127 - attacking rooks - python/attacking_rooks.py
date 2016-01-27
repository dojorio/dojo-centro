from functools import reduce 

def transpose_board(board):
    output = []
    for row in board:
        new_row = []
        for col in row:
            new_row.append(col)
        output.append(new_row)

    return output


def attacking_rooks(board):
    f = lambda memo, row: memo + 1 if row.count('x') != len(board) else memo    
    return reduce(f , board, 0)
