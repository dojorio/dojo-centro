def neighbors(board, x, y):
    neighbors = []
    if y > 0:
        neighbors.append(board[x][y-1])
    if y < len(board[x]) - 1:
        neighbors.append(board[x][y+1])

    return sum(neighbors)


def game_of_life(board):
    resultado = [[1] * len(board[0])]

    for idx, cell in enumerate(board[0]):
        if idx == 0:
            previous = 0
        else:
            previous = board[0][idx - 1]

        if idx == len(board[0]) - 1:
            next = 0
        else:
            next = board[0][idx + 1]

        if cell == 1:
            if previous + next < 2:
                resultado[0][idx] = 0
        else:
            resultado[0][idx] = 0

    return resultado
