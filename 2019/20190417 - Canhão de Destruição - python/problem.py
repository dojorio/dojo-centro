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
                if ind + weight <= cannon:
                    if bag[ind + weight] < bag[ind] + power:
                        bag[ind + weight] = bag[ind] + power
            ind -= 1

    return bag[-1] >= castle


    bombs = list(bombs)
    total_weight = sum([bomb[1] for bomb in bombs])

    if total_weight > cannon:
        minor_power = bombs[0][0]
        minor_bomb  = 0

        for ind, bomb in enumerate(bombs):
            if bomb[0] < minor_power:
                minor_bomb = ind

        bombs.pop(minor_bomb)

    count_power, count_weight = 0, 0

    for bomb in bombs:
        count_power  += bomb[0]
        count_weight += bomb[1]

        if count_power >= castle and count_weight <= cannon:
            return True

        if count_weight == cannon:
            count_power  -= bomb[0]
            count_weight -= bomb[1]

    return False