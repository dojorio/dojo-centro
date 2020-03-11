#!/usr/bin/env python
# -*- coding: utf-8 -*-

def hand_value(hand):
    return 'carta-alta'

def sort_hand(hand):
    splited = []
    values = {
      'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    for card in hand:
        splited.append(list(card))

    for card in splited:
        value = card[0]

        if value in values:
            card[0] = values[value]
        else:
            card[0] = int(value)

    splited.sort()

    for card in splited:
        value = card[0]
        if value == 10:
            card[0] = 'T'
        elif value == 11:
            card[0] = 'J'
        elif value == 12:
            card[0] = 'Q'
        elif value == 13:
            card[0] = 'K'
        elif value == 14:
            card[0] = 'A'    
        else:
            card[0] = str(value)

    result = []

    for card in splited:
        result.append(card[0]+card[1])

    return result[::-1]