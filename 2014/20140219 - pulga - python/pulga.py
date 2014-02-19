def pulga(s, x, y, dx, dy):
    if 0 in (x%s, y%s):
        return 1
    return 0