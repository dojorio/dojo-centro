def inverter(numero):
    numero = str(numero)
    numero = numero[::-1] #inverte a string formada
    return int(numero)

def adicao_reversa(*args):
    #return inverter(inverter(num1) + inverter(num2))
    return inverter(sum(map(inverter, args)))
