#!/usr/bin/env python
# -*- coding: utf-8 -*-

IMPOSSIVEL = None

def miojo(amp1, amp2):

	if 3 in (amp1, amp2) or 1 in (amp1, amp2):
		return 3

	min_amp, max_amp = sorted([amp1, amp2])

	if (max_amp - 3) % min_amp == 0:
		return max_amp

	if (max_amp + 3) % min_amp == 0:
		return max_amp + 3

	if max_amp % 3 == 0:
		return 3 * min_amp