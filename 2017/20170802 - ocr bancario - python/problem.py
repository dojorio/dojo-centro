#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse(source):
    n = (len(source[0]) + 1) // 4
    result = []
    for i in range(n):
        result.append([])

    for linha in source:
        for i in range(n):
            result[i].append(linha[i * 4:i * 4 + 3])

    return result

    return         [
          [
              "   ",
              "  |",
              "  |"
            ],
          [
              " _ ",
              "| |",
              "|_|"
            ]
         ]

def ocr(source): 

    if source[1] == source[2] == "  |" and source[0] != "   ":
        return 7

    if source[2] == "|_|":
        if source[1] == "|_|":
            return 8
        if source[1] == "| |":
            return 0
        return 6

    if source[1] == "|_ ":
        return 5

    if "|_ " in source:
        return 2

    if " _|" in source:
        if source[1] == "|_|":
            return 9
        return 3

    if "|_|" in source:
        return 4

    if source[2] == "|_|":
        return 6

    if "     _ " in source:
        return 10


    return 1