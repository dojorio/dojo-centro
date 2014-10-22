#proibido usar + - * /

def add(a, b):
    carry = (a & b) << 1
    return carry | xor(a, b)

def xor(a, b):
    return (a | b) & (not(a & b))