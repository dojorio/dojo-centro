import copy


def neighbors(board, x, y):
    neighbors = []
    if y > 0:
        neighbors.append(board[x][y-1])
    if y < len(board[x]) - 1:
        neighbors.append(board[x][y+1])

    return sum(neighbors)

ALIVE = 1
DEAD = 0

def game_of_life(board):
    result = copy.deepcopy(board)
    for y, element in enumerate(board[0]):
        living_neighbors = neighbors(board, 0, y)
        if element is ALIVE:
            if living_neighbors < 2: #or living_neighbors > 3:
                result[0][y] = DEAD
            else:
                result[0][y] = ALIVE
        else:
            pass
    return result
