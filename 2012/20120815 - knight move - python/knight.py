def move(from_x, from_y, to_x, to_y):
    var_x = abs(from_x - to_x)
    var_y = abs(from_y - to_y)

    is_not_aligned = var_x > 0 and var_y > 0
    distance = var_x + var_y

    if distance == 1:
        return 3
    if distance == 4:
        return 2
    if distance == 2:
        if is_not_aligned:
            return 4
        else:
            return 2


    return distance / 3
