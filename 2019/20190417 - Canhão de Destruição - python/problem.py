#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mission_accomplished(bombs, cannon, castle):
    if bombs[0][0] >= castle and bombs[0][1] <= cannon:
        return True

    if len(bombs) == 2:
        total_power  = bombs[0][0] + bombs[1][0]
        total_weight = bombs[0][1] + bombs[1][1]
        return total_power >= castle and total_weight <= cannon

    return False