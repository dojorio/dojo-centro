def exchange(coin):
    return exchange(coin/2) + \
           exchange(coin/3) + \
           exchange(coin/4) if coin else 1
