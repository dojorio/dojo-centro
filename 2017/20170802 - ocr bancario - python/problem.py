#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ocr(source):
	if "|_ " in source:
		return 2

	if " _|" in source:
		return 3

	if "|_|" in source:
		return 4
		
	return 1