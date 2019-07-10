#!/usr/bin/env python
# -*- coding: utf-8 -*-

def miojo(amp1, amp2):
    menor = min(amp1,amp2)
    maior = max(amp1,amp2)

    if not amp1 % 2 and not amp2 % 2:
        return None
    if amp1 == amp2 and amp1 not in (1, 3) and amp2 not in (1, 3):
        return None

    for tempo1 in (amp1*i for i in range(0, maior)):
        for tempo2 in (amp2*i for i in range(0, maior)):
            diff = abs(tempo1 - tempo2)
            if diff == 3:
                return max(tempo1, tempo2)
            if diff > 3 and tempo2 > tempo1:
                break
