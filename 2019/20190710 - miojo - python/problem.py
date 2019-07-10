#!/usr/bin/env python
# -*- coding: utf-8 -*-

def eh_par(amp):
    return not amp % 2


def miojo(amp1, amp2):
    if 3 in (amp1, amp2):
        return 3

    if eh_par(amp1) and eh_par(amp2):
        return None

    if abs(amp1 - amp2) == 3:
        return max((amp1, amp2))

    # if amp1 == 2 or amp2 == 2:
    #     return 5

    l_amp1 = [amp1*i for i in range(0, 10)]
    l_amp2 = [amp2*i for i in range(0, 10)]

    for tempo1 in l_amp1:
        for tempo2 in l_amp2:
            if abs(tempo1 - tempo2) == 3:
                return max(tempo1,tempo2)



    return 3