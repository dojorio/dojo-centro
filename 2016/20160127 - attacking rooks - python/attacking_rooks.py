def attacking_rooks(board):
    count = 0
    for row in board:
        if row.count('x') != len(board):
            count = count  + 1

    return count