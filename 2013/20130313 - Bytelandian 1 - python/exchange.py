import functools

def memoize(f):
    cache = {}

    @functools.wraps(f)
    def new_func(coin):
        cache[coin] = cache.get(coin) or f(coin)
        return cache[coin]

    return new_func

@memoize
def max_value(coin):
    if coin == 0:
        return 0

    maximum_exchange_value = max_value(coin/2)+max_value(coin/3)+max_value(coin/4)
    return max(maximum_exchange_value, coin)

#max_value = memoize(max_value)

@memoize
def n_zeroes(coin):
    if coin == 0:
        return 1

    return n_zeroes(coin/2) + n_zeroes(coin/3) + n_zeroes(coin/4)
