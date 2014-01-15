def salim(grid):
    if grid[0][-1] == '#' or grid[-1][0] == '#':
        return 1
    else:
        return len(grid[0]) * len(grid)
