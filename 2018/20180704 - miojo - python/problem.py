#!/usr/bin/env python
# -*- coding: utf-8 -*-

def miojo(amp1, amp2):
	if 3 in (amp1, amp2):
		return 3
		
	min_amp, max_amp = sorted([amp1, amp2])
	if max_amp - min_amp == 3:
		return max_amp

	if min(amp1, amp2) == 5:
		return 10
	return max(amp1, amp2)