
def salim(grid):
    if grid[0][0] == '#':
        return 0

    for line in grid :
        if any('#' in line ):
            return max(max(line.find('#') for line in grid), 1)
        else:
            return len(grid[0]) * len(grid)
