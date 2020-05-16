def explode(board):
    for j in range(0, 8):
        for i in range(0, 6):
            a, b, c = board[j][i: i + 3]
            if a == b == c:
                return True
    for j in range(6):
        for i in range(8):
            a, b, c = board[i][j: j + 3]
            if a == b == c:
                return True


    return False