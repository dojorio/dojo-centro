#!/usr/bin/env python
# -*- coding: utf-8 -*-

def letter_range(str):
    str = str.replace(' ', '')
    resposta = []

    if str == '':
        return []

    str = sorted(set(str))

    if len(str) == 2:       
        if (ord(str[1]) - ord(str[0]) == 1):
            return [str[0]+":"+str[1]]

        else:
            return [str[0]+":"+str[0], str[1]+":"+str[1]]

    # if len(str) == 3:
    #     if (ord(str[1]) - ord(str[0]) == 1):
    #         if (ord(str[2]) - ord(str[1]) == 1):
    #         #resposta.append(str[0]+":"+str[2])
    #             return [str[0]+":"+str[2]]
    #         else:
    #             return [str[0]+":"+str[1], str[2]+":"+str[2]]
    for i in range(1, len(str)):
        if ord(str[i]) - ord(str[i-1]) > 1:
            resposta.append(str[i]+":"+str[i])
        else:
            resposta.append(str[i-1]+":"+str[i])

    if resposta != '':
        return resposta

    return [str[0]+":"+str[0]]