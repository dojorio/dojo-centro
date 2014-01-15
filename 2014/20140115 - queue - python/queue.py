
def encontra(line, how):
    walked = how(line, '#')
    if walked < 0:
        return len(line)
    return walked

def salim(grid):
    andou = encontra(grid[0], str.find)

    if len(grid) > 1:
        andou += encontra(grid[1], str.rfind)

    return andou
