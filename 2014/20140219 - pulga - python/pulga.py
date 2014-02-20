
def casa_branca(s, x, y):
    metadinha = x%s == 0 or y%s == 0
    branco = (x//s + y//s) % 2 == 1

    return branco and not metadinha

def pulga(s, x, y, dx, dy):
    for i in range(100):
        if casa_branca(s, x, y):
            return i
        
        x += dx
        y += dy


    return None