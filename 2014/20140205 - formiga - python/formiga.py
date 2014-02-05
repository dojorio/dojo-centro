def onde_está(tempo):
    x = tempo // 2 if tempo < 6 else 2
    y = 1 if (tempo-1)//2 % 2 == 0 else 0
    return (x  , y)