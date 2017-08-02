#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ocr(source):	
	if source[1] == "|_ ":
		return 5

	if "|_ " in source:
		return 2

	if " _|" in source:
		return 3

	if "|_|" in source:
		return 4

	if source[2] == "|_|":
		return 6

	return 1