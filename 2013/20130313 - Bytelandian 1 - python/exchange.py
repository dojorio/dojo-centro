cache = {0: 1}

def exchange(coin):
    cache[coin] = cache.get(coin) or \
                        exchange(coin/2) + \
                        exchange(coin/3) + \
                        exchange(coin/4)
    return cache[coin]

