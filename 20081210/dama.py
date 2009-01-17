def dama(x1, y1, x2, y2):


    if x1 == 0 or y1 == 0 or x2 ==0 or y2 == 0:
        raise IndexError
    
    elif (x1, y1) == (x2, y2):
        return 0
    elif (y1 - y2) == (x1 - x2):
        return 1
    elif x1 == x2 or y1 == y2:
        return 1
    else:
        return 2
