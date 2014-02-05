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
        if tempo >= 9:
            return (tempo-9, 3)
        elif tempo >= 6:
            return (8-tempo, 2)
        x = tempo // 2     
        y = (tempo + 1) //2 % 2 
    
    return (x  , y)