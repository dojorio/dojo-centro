cache = {0: 1}

def exchange(coin):
    if coin not in cache:
        cache[coin] = exchange(coin/2) + \
                      exchange(coin/3) + \
                      exchange(coin/4)

    return cache[coin]

