#!/usr/bin/env python
# -*- coding: utf-8 -*-

def hand_value(hand):
    hand = sort_hand(hand)

    if hand[4][0] == hand[3][0]:
        return 'par'

    if hand[3][0] == hand[2][0]:
        return 'par'

    if hand[2][0] == hand[1][0]:
        return 'par'    

    return 'carta-alta'

def sort_hand(hand):
    values = {
      'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    splited = [list(card) for card in hand]

    for card in splited:
        value = card[0]

        if value in values:
            card[0] = values[value]
        else:
            card[0] = int(value)

    splited.sort()
    values = {v:k for k, v in values.items()}

    for card in splited:
        value = card[0]

        if value in values:
            card[0] = values[value]
        else:
            card[0] = str(value)

    return [''.join(card) for card in splited[::-1]]
