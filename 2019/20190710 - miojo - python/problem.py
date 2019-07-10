#!/usr/bin/env python
# -*- coding: utf-8 -*-

def miojo(amp1, amp2):
    if amp1 in (1, 3) or amp2 in (1, 3):
        return 3

    if not amp1 % 2 and not amp2 % 2 or amp1 == amp2:
        return None

    maior = max(amp1, amp2)

    for tempo1 in (amp1*i for i in range(0, maior)):
        for tempo2 in (amp2*i for i in range(0, maior)):
            diff = abs(tempo1 - tempo2)
            if diff == 3:
                return max(tempo1, tempo2)
            if diff > 3 and tempo2 > tempo1:
                break
