
def skyline(predios):
    if predios:
        output = []
        for predio in predios:
            if output and output[-2] == predio[0]:
                output.pop()
                output.pop()
                output += [predio[-1], 0]
            else:
                output += list(predio) + [0]
        return output
    return []