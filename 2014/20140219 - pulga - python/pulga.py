
def casa_branca(s, x, y):
    metadinha = x%s == 0 or y%s == 0
    branco = (x//s + y//s) % 2 == 1

    return branco and not metadinha

def pulga(s, x, y, dx, dy):
    pulos = 0
    while not casa_branca(s, x, y):
        x += dx
        y += dy
        pulos += 1

    return pulos