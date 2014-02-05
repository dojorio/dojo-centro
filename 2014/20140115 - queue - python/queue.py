
def encontra(line):
    walked = line.find('#')
    if walked < 0:
        return len(line)
    return walked

def salim(grid):
    andou, pos = 0, 0
    for i, line in enumerate(grid):
        if i == 1:
            andou += encontra(line[len(line)-pos])
        else:
            andou += encontra(line[pos])

        pos = encontra(line)

    return andou
