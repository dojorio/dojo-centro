#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mission_accomplished(bombs, cannon, castle):
    for bomb in bombs:
        if bomb[0] >= castle and bomb[1] <= cannon:
            return True

    if len(bombs) > 1:
        total_power = sum([bomb[0] for bomb in bombs])
        total_weight = sum([bomb[1] for bomb in bombs])
        return total_power >= castle and total_weight <= cannon

    return False