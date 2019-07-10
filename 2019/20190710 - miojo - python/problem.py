#!/usr/bin/env python
# -*- coding: utf-8 -*-

def miojo(amp1, amp2):
    l_amp1 = [amp1*i for i in range(0, 1000000)]
    l_amp2 = [amp2*i for i in range(0, 1000000)]

    for tempo1 in l_amp1:
        for tempo2 in l_amp2:
            if abs(tempo1 - tempo2) == 3:
                return max(tempo1,tempo2)
