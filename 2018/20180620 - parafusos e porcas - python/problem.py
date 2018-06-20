#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ScrewFinder:
	def __init__(self, intervals):
		self.intervals = intervals		

	def find(self, screw):
		if screw in self.intervals[0]:
			if screw == self.intervals[0][0]:
				return [0, 0]
			else:
				return [1, 1]

		

		return []

