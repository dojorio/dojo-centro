#proibido usar + - * /

def add(a, b):
    carry = (a ^ b)<<1
    return (a | b)

def xor(a, b):
    return a | b