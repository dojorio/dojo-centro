import unittest
from vogon import vogon_report

class TestVogonReport(unittest.TestCase):
	def test_1(self):
		road_start = (0, 0)
		road_end = (1, 0)
		other_planets = [
			(0, 1, 1)
		]
		report_output = {
			"deaths": 0
		}
		self.assertEquals(vogon_report(
			road_start, road_end, other_planets), 
				report_output)

	def test_2(self):
		road_start = (0, 0)
		road_end = (1, 0)
		other_planets = [
			(0, 0, 1)
		]
		report_output = {
			"deaths": 1
		}
		self.assertEquals(vogon_report(
			road_start, road_end, other_planets), 
				report_output)

	def test_3(self):
		road_start = (1, 0)
		road_end = (2, 0)
		other_planets = [
			(0, 0, 1)
		]
		report_output = {
			"deaths": 0
		}
		self.assertEquals(vogon_report(
			road_start, road_end, other_planets), 
				report_output)


	def test_4(self):
		road_start = (0, 0)
		road_end = (1, 0)
		other_planets = [
			(0, 0, 2)
		]
		report_output = {
			"deaths": 2
		}
		self.assertEquals(vogon_report(
			road_start, road_end, other_planets), 
				report_output)

unittest.main()