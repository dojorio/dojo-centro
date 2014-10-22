#proibido usar + - * /

def add(a, b):
    carry = xor(a, b) << 1
    return carry | (a | b)

def xor(a, b):
    return (a | b) & ((not a) | (not b))