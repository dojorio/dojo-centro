cache = {0: 1}

def max_value(coin):
    return coin

def n_zeroes(coin):
    cache[coin] = cache.get(coin) or \
                        n_zeroes(coin/2) + \
                        n_zeroes(coin/3) + \
                        n_zeroes(coin/4)
    return cache[coin]

