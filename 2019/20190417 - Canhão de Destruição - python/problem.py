#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mission_accomplished(bombs, cannon, castle):
    bag = [None]*(cannon+1)
    bag[0] = 0

    for bomb in bombs:
        power, weight = bomb

        for ind in range(cannon, -1, -1):
            check = ind + weight

            if bag[ind] is not None and check <= cannon:
                if bag[check] is None or bag[check] < bag[ind] + power:
                    bag[check] = bag[ind] + power
    
    new_bag = [item for item in bag if item is not None]
    return max(new_bag) >= castle
