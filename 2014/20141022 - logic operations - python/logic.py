#proibido usar + - * /

def add(a, b):
    carry0 = (a & b)
    add0 = xor(a, b)
    add1 = xor(xor(a >> 1, b >> 1), carry0)

    return add1 << 1 | add0

def xor(a, b):
    return (a | b) & (not(a & b))