import math

def onde_está(tempo):
    raiz = int(math.sqrt(tempo))

    if raiz % 2 == 1:
        if tempo < raiz * (raiz + 1):
            x = tempo - raiz * raiz
            y = raiz
        else:
            x = raiz
            y = (raiz + 1)**2 - tempo - 1
    else:
        if tempo < raiz * (raiz + 1):
            x = raiz
            y = tempo - raiz * raiz
        else:
            x = (raiz + 1)**2 - tempo - 1
            y = raiz
    
    return (x, y)