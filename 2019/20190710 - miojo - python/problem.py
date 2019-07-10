#!/usr/bin/env python
# -*- coding: utf-8 -*-

def eh_par(amp):
    return not amp % 2


def miojo(amp1, amp2):
    if eh_par(amp1) and eh_par(amp2):
        return None

    if 3 in (amp1, amp2):
        return 3

    if amp1 == 2 or amp2 == 2:
        return 5

    return 3