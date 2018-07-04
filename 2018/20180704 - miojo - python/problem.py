#!/usr/bin/env python
# -*- coding: utf-8 -*-

IMPOSSIVEL = None

def miojo(amp1, amp2):
	if amp1 % 2 == 0 and amp2 % 2 == 0:
		return IMPOSSIVEL

	if 3 in (amp1, amp2) or 1 in (amp1, amp2):
		return 3

	min_amp, max_amp = sorted([amp1, amp2])

	menor, maior = min_amp, max_amp

	while abs(maior - menor) != 3:
		if menor > maior:
			maior += max_amp
		else:
			menor += min_amp

	return max(menor, maior)