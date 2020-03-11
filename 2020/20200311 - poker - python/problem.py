#!/usr/bin/env python
# -*- coding: utf-8 -*-

def hand_value(hand):
	return 'carta-alta'

def sort_hand(hand):
	for card in enumerate(hand):
		print card
	return hand[::-1]