#!/usr/bin/env python
# -*- coding: utf-8 -*-

def miojo(amp1, amp2):
	if 8 in (amp1, amp2):
		return 8
	if min(amp1, amp2) == 5:
		return 10
	if 3 in (amp1, amp2):
		return 3