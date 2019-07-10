#!/usr/bin/env python
# -*- coding: utf-8 -*-

def miojo(amp1, amp2):
    if not amp1 % 2 and not amp2 % 2:
        return None
    if amp1 == amp2 and amp1 not in (1, 3) and amp2 not in (1, 3):
        return None

    l_amp1 = (amp1*i for i in range(0, 1000000))
    l_amp2 = [amp2*i for i in range(0, 999999)]

    for tempo1 in l_amp1:
        for tempo2 in l_amp2:
            diff = abs(tempo1 - tempo2)
            if diff == 3:
                return max(tempo1, tempo2)
            if diff > 3 and tempo2 > tempo1:
                break
