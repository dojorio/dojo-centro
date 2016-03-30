def two_strings(strings):
    for char in strings[0]:
        if(char in strings[1]):
            return True
    for char in strings[1]:
        if(char in strings[0]):
            return True

    return False