#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ScrewFinder:
	def __init__(self, intervals):
		self.intervals = intervals
		self.shelf = []

		for interval in intervals:
		 	self.shelf += self.my_range(interval)

	def my_range(self, tupla):
		first = tupla[0]
		last = tupla[1]+1
		return list(range(first, last))

	def find(self, screw):
		if screw in self.shelf:
			occurrences = self.shelf.count(screw)

			return [self.shelf.index(screw), self.shelf.index(screw)+occurrences-1]

		return []
