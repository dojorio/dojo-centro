#!/usr/bin/env python
# -*- coding: utf-8 -*-

def hand_value(hand):
    return 'carta-alta'

def sort_hand(hand):
    splited = []

    for card in hand:
        splited.append(list(card))
    print(splited)

    return hand[::-1]