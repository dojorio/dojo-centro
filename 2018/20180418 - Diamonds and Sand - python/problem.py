#!/usr/bin/env python
# -*- coding: utf-8 -*-

pattern = /<.*>/g

def count_diamonds(mine):
	print(pattern.exec(mine))
	return 0
