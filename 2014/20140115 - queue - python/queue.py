
def encontra(line):
    walked = line.find('#')
    if walked < 0:
        return len(line)
    return walked

def salim(grid):
    andou = encontra(grid[0])

    for i, line in enumerate(grid):
        if len(grid) == 1:
            andou += encontra(grid[1][::-1])
        else:
            andou += encontra(grid[i])
        


    return andou
