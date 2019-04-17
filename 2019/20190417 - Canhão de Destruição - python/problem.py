#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mission_accomplished(bombs, cannon, castle):
    bag = [None]*(cannon+1)
    bag[0] = 0

    for bomb in bombs:
        power, weight = bomb
        ind = cannon
        while ind >= 0:
            if bag[ind] is not None:
                check = ind + weight
                if check <= cannon:
                    if bag[check] is None or bag[check] < bag[ind] + power:
                        bag[check] = bag[ind] + power
            ind -= 1
    
    new_bag = [item for item in bag if item is not None]
    return max(new_bag) >= castle
