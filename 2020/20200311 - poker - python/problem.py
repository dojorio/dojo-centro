#!/usr/bin/env python
# -*- coding: utf-8 -*-

def hand_value(hand):
    return 'carta-alta'

def sort_hand(hand):
    splited = []

    for card in hand:
        splited.append(list(card))

    for card in splited:
        value = card[0]
        if value == 'T':
            card[0] = 10
        else:
            card[0] = int(value)    

    splited.sort()

    for card in splited:
        value = card[0]
        if value == 10:
            card[0] = 'T'
        else:
            card[0] = str(value)

    result = []

    for card in splited:
        result.append(card[0]+card[1])

    return result[::-1]