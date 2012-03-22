def match(preferences):
    return len(reduce(lambda x, y: x.union(set(y)), preferences.values(), set()))
