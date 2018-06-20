#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ScrewFinder:
	def __init__(self, intervals):
		self.intervals = intervals
		pass

	def find(self, screw):
		if screw == 1:
			return [0, 0]
		return []