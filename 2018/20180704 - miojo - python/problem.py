#!/usr/bin/env python
# -*- coding: utf-8 -*-

IMPOSSIVEL = None

def miojo(amp1, amp2):

	# checando se eh par
	if amp1 % 2 == 0 and amp2 % 2 == 0:
		return IMPOSSIVEL

	if 3 in (amp1, amp2) or 1 in (amp1, amp2):
		return 3

	min_amp, max_amp = sorted([amp1, amp2])

	if max_amp - min_amp == 3:
		return max_amp

	if 2 * min_amp - max_amp == 3:
		return 2 * min_amp

	if 3 * min_amp - max_amp == 3:
		return 3 * min_amp

	if 4 * min_amp - max_amp == 3:
		return 4 * min_amp

	return max_amp