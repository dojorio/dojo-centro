#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ScrewFinder:
	def __init__(self, intervals):
		self.intervals = intervals		

	def find(self, screw):
		if screw in self.intervals[0]:
			return [0,0]
		
		return []

