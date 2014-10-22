#proibido usar + - * /

def add(a, b, carry = 0):
    carry = (a & b) << 1

    return carry | xor(a, b) | (b << 1)

def xor(a, b):
    return (a | b) & (not(a & b))