cache = {0: 1}


def memoize(f, cache):
    def new_func(coin):

    return new_func

def max_value(coin):

    if coin == 0:
        return 0
    else:
        maximum_exchange_value = max_value(coin/2)+max_value(coin/3)+max_value(coin/4)
        return max(maximum_exchange_value, coin)


def n_zeroes(coin):
    cache[coin] = cache.get(coin) or \
                        n_zeroes(coin/2) + \
                        n_zeroes(coin/3) + \
                        n_zeroes(coin/4)
    return cache[coin]

