def look_and_say(n):
    sequence = str(n)
    last = sequence[0]
    counter = 0
    result = ''
    
    for number in sequence:
        if number == last:
            counter += 1
        else:
            result += str(counter) + last
            counter = 1
        last = number
        
    result += str(counter) + last
    return int(result)

def look_say_then_find(firstDigit,nth):
    result = firstDigit
    for c in range(nth-1):
        result = look_and_say(result)
    return result
    
def sum_digits(number):
    return reduce(sum_single_digit, digits(number))
    
def sum_single_digit(a, b):
    return a+b
    
def digits(number):
    while(number):
        yield number%10
        number = number/10
