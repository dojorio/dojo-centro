def salim(grid):
    if any('#' in line for line in grid):
        return max(line.index('#') for line in grid if '#' in line)
    else:
        return len(grid[0]) * len(grid)
