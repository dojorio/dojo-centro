#proibido usar + - * /

def add(a, b):
    carry0, add0 = ma_bit(a, b, 0, 0)
    carry1, add1 = ma_bit(a, b, carry0, 1)
    carry2, add2 = ma_bit(a, b, carry1, 2)

    return carry2 << 3 | add2 << 2 | add1 << 1 | add0

def ma_bit(a, b, carry, bit):
    a0 = (a >> bit) & 1
    b0 = (b >> bit) & 1
    carry0, add0 = carry_add(a0, b0)
    return carry_add(add0, carry, carry0)

def carry_add(a, b, carry = 0):
    return (a & b) | carry, xor(a, b)

def xor(a, b):
    return (a | b) & (not(a & b))