import math

def onde_está(tempo):
    raiz = math.sqrt(tempo)
    if raiz == int(raiz):
        if tempo % 2 == 0:
            y = 0
            x = raiz
        else:
            x = 0
            y = raiz
    else:
        raiz = int(raiz)
        if raiz % 2:
            if raiz * (raiz + 1) > tempo:
                y = raiz
                x = tempo - raiz * raiz
            else:
                x = raiz
                y = (raiz + 1)**2 - tempo
        if tempo >= 9:
            return (tempo-9, 3)
        elif tempo >= 6:
            return (8-tempo, 2)
        x = tempo // 2     
        y = (tempo + 1) //2 % 2 
    
    return (x  , y)