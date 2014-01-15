
def encontra(line):
    walked = line.find('#')
    if walked < 0:
        return len(line)
    return walked

def salim(grid):
    andou = 0
    for i, line in enumerate(grid):
        if i == 1:
            andou += encontra(line[::-1])
        else:
            andou += encontra(line)
        
    return andou
