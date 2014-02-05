def onde_está(tempo):
    if tempo >= 9:
        return (tempo-9, 3)
    elif tempo >= 6:
        return (8-tempo, 2)
    x = tempo // 2     
    y = (tempo + 1) //2 % 2 
    return (x  , y)