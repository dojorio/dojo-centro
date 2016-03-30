def two_strings(strings):
    if(strings[0] == 'c' or strings[1] == 'c'):
        return False
    if(strings[0] == 'cd'):
        if(strings[0] == 'dd'):
            return False
        return False

    return True