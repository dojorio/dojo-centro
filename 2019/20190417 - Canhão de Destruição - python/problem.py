#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mission_accomplished(bombs, cannon, castle):
    for bomb in bombs:
        if bomb[0] >= castle and bomb[1] <= cannon:
            return True

    if len(bombs) > 1:
        total_power  = 0
        total_weight = 0

        for bomb in bombs:
            total_power  += bomb[0]
            total_weight += bomb[1]

            if total_power >= castle and total_weight <= cannon:
                return True

            if total_weight == cannon:
                total_power  -= bomb[0]
                total_weight -= bomb[1]


    return False