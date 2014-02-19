
def casa_branca (s, x, y):
    metadinha = x%s == 0
    branco = ((x//s) % 2 == 1) and ((y//s) % 2 == 0)

    return (branco and not metadinha)

def pulga(s, x, y, dx, dy):
    if 0 in (x%s, y%s):
        return 1
    return 0