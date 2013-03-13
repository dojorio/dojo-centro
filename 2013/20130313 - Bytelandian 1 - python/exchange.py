def exchange(coin):
    if coin == 0:
        return 1
    return exchange(coin/2) + \
           exchange(coin/3) + \
           exchange(coin/4)
