import unittest
from katapotter import *

class BookChargerTests(unittest.TestCase):
    def test_no_books(self):
        chart = Chart()
        book_charger = BookCharger(chart)
        self.assertEqual(book_charger.price, 0)
        
    def test_one_book(self):
        chart = Chart()
        chart.add(book)
        book_charger = BookCharger(chart)
        self.assertEqual(book_charger.price, 42.0)
        
    def test_two_books(self):
        chart = Chart()
        chart.add(book)
        chart.add(book)
        book_charger = BookCharger(chart)
        self.assertEqual(book_charger.price, 84.0)
        
    def test_two_different_books(self):
        chart = Chart()
        chart.add(book1)
        chart.add(book2)
        book_charger = BookCharger(chart)
        self.assertEqual(book_charger.price, 84.0 * .95)
        
    def test_two_equal_books_plus_a_different_one(self):
        chart = Chart()
        chart.add(book1)
        chart.add(book1)
        chart.add(book2)
        book_charger = BookCharger(chart)
        self.assertEqual(book_charger.price, 42 * 2 * .95 + 42)

unittest.main()
