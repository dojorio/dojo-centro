def onde_está(tempo):
    if tempo == 6:
        return (2, 2)
    x = tempo // 2     
    y = (tempo + 1) //2 % 2 
    return (x  , y)