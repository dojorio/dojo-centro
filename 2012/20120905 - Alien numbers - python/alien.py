#coding: utf-8
def translate(text, source_base, dest_base):
    return to_base(to_decimal(text, source_base), dest_base)

def to_decimal(text, base):
    result = 0
    for c in text:
        # Multiplicar um número pela base de numeração que ele está
        # representado é o mesmo que adicionar zero ao final
        result *= len(base)
        result += base.find(c)
    
    return result    
    
def to_base(number, base):
    result = ''
    while number:
        result = base[number % len(base)] + result
        number /= len(base)

    return result or base[0]
