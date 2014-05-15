import copy


POSITIONS = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1),           (0, 1),
             (1, -1),  (1, 0),  (1, 1)]

def neighbors(board, x, y):
    neighbors = 0

    for x_offset, y_offset in POSITIONS:
        try:
            neighbors += board[x + x_offset][y + y_offset]
        except IndexError:
            pass
    return neighbors

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
