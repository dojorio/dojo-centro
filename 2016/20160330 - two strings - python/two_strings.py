def two_strings(strings):
    for char in strings[0]:
        if(char in strings[1]):
            return True
    if(not strings[0] in strings[1]):
        return False
    if(not strings[1] in strings[0]):
        return False

    if(strings[0] == 'cd'):
        if(strings[0] == 'dd'):
            return False
        return False

    return True