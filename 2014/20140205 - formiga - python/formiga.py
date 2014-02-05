import math

def onde_está(tempo):
    raiz = int(math.sqrt(tempo))

    if tempo < raiz * (raiz + 1):
        a = tempo - raiz * raiz
        b = raiz
    else:
        a = raiz
        b = (raiz + 1)**2 - tempo - 1

    return (a, b) if raiz % 2 == 1 else (b, a)