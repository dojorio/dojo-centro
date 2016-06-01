import unittest
from vogon import vogon_report

class TestVogonReport(unittest.TestCase):
	def test_1(self):
		road_start = (0, 0)
		road_end = (1, 0)
		planets = [(0, 1, 1)]
		report_output = { "deaths": 0 }
		self.assertEquals(vogon_report(
			road_start, road_end, planets),
			report_output)

	def test_2(self):
		road_start = (0, 0)
		road_end = (1, 0)
		planets = [(0, 0, 1)]
		report_output = { "deaths": 1 }
		self.assertEquals(vogon_report(
			road_start, road_end, planets),
			report_output)

	def test_3(self):
		road_start = (1, 0)
		road_end = (2, 0)
		planets = [(0, 0, 1)]
		report_output = { "deaths": 0 }
		self.assertEquals(vogon_report(
			road_start, road_end, planets),
			report_output)


	def test_4(self):
		road_start = (0, 0)
		road_end = (1, 0)
		planets = [(0, 0, 2)]
		report_output = { "deaths": 2 }
		self.assertEquals(vogon_report(
			road_start, road_end, planets),
			report_output)

	def test_5(self):
		road_start = (0, 0)
		road_end = (1, 0)
		planets = [(2, 0, 2)]
		report_output = { "deaths": 0 }
		self.assertEquals(vogon_report(
			road_start, road_end, planets),
		    report_output)

	def test_6(self):
		road_start = (0, 0)
		road_end = (1, 0)
		planets = [(3, 0, 2)]
		report_output = { "deaths": 0 }
		self.assertEquals(vogon_report(
			road_start, road_end, planets),
			report_output)

	def test_7(self):
		road_start = (1, 0)
		road_end = (3, 0)
		planets = [(2, 0, 2)]
		report_output = { "deaths": 2 }
		self.assertEquals(vogon_report(
			road_start, road_end, planets),
			report_output)

	def test_8(self):
		road_start = (3, 0)
		road_end = (1, 0)
		planets = [(2, 0, 2)]
		report_output = { "deaths": 2 }
		self.assertEquals(vogon_report(
			road_start, road_end, planets),
			report_output)

	def test_9(self):
		road_start = (0, 1)
		road_end = (0, 2)
		planets = [(0, 0, 1)]
		report_output = { "deaths": 0 }
		self.assertEquals(vogon_report(
			road_start, road_end, planets),
			report_output)

	def test_10(self):
		road_start = (0, 3)
		road_end = (0, 1)
		planets = [(0, 2, 2)]
		report_output = { "deaths": 2 }
		self.assertEquals(vogon_report(
			road_start, road_end, planets),
			report_output)

	def test_11(self):
		road_start = (0, 0)
		road_end = (2, 2)
		planets = [(1, 1, 2)]
		report_output = { "deaths": 2 }
		self.assertEquals(vogon_report(
			road_start, road_end, planets),
			report_output)

	def test_12(self):
		road_start = (0, 0)
		road_end = (4, 4)
		planets = [(1, 3, 2)]
		report_output = { "deaths": 0 }
		self.assertEquals(vogon_report(
			road_start, road_end, planets),
			report_output)

unittest.main()