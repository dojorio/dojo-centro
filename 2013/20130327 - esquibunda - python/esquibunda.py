#-*- coding: utf-8 -*-

def esquibunda(montanha):
    if not montanha:
        return 0

    index = montanha[0].index(max(montanha[0]))
    return max(index + 1, len(montanha[0]) - index)
