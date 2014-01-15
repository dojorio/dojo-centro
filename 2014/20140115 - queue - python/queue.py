def salim(grid):
    if grid[0][0] == '#':
        return 0
        
    if any('#' in line for line in grid):
        return max(max(line.find('#') for line in grid), 1)
    else:
        return len(grid[0]) * len(grid)
