cache = {0: 1}

def max_value(coin):
    if coin < 24:
        return max(coin/2 + coin/3 + coin/4, coin)
    else:
        return max_value(coin/2)+max_value(coin/3)+max_value(coin/4)


def n_zeroes(coin):
    cache[coin] = cache.get(coin) or \
                        n_zeroes(coin/2) + \
                        n_zeroes(coin/3) + \
                        n_zeroes(coin/4)
    return cache[coin]

