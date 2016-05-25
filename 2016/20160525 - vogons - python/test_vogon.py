import unittest
from vogon import vogon_report

class TestVogonReport(unittest.TestCase):
	def test_1(self):
		planet_1 = (0, 0)
		planet_2 = (1, 0)
		other_planets = [
			(0, 1, 1)
		]
		report_output = {
			"deaths": 0
		}
		self.assertEquals(vogon_report(
			planet_1, planet_2, other_planets), 
				report_output)

	def test_2(self):
		planet_1 = (0, 0)
		planet_2 = (1, 0)
		other_planets = [
			(0, 0, 1)
		]
		report_output = {
			"deaths": 1
		}
		self.assertEquals(vogon_report(
			planet_1, planet_2, other_planets), 
				report_output)

unittest.main()