def salim(grid):
    desconto = max(line.rfind('#') for line in grid)+1
    return len(grid[0]) * len(grid) - desconto
