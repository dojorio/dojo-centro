#coding: utf-8
import unittest
from quicksort import partition, quicksort

class TestQuicksort(unittest.TestCase):
    def test_sorted_list(self):
        array = [1, 2, 3]
        pivot = partition(array, 1)
        self.assertEqual(pivot, 1)
        self.assertPivot(array, pivot)

    def test_reversed_list(self):
        array = [3, 2, 1]
        pivot = partition(array, 1)
        self.assertEqual(pivot, 1)
        self.assertPivot(array, pivot)

    def test_unsorted_list(self):
        array = [3, 1, 2]
        pivot = partition(array, 2)
        self.assertEqual(pivot, 1)
        self.assertPivot(array, pivot)
    
    def test_sorted_list_pivot_3(self):
        array = [1, 2, 3]
        pivot = partition(array, 2)
        self.assertEqual(pivot, 2)
        self.assertPivot(array, pivot)
        
    def test_sorted_non_contiguous_list(self):
        array = [1, 2, 4]
        pivot = partition(array, 2)
        self.assertEqual(pivot, 2)
        self.assertPivot(array, pivot)
        
    def test_kind_of_unsorted_list_4(self):
        array = [1, 3, 2, 4]
        pivot = partition(array, 2)
        self.assertEqual(pivot, 1)
        self.assertPivot(array, pivot)

    def test_yet_another_unsorted_list_4(self):
        array = [3, 1, 2, 4]
        pivot = partition(array, 2)
        self.assertEqual(pivot, 1)
        self.assertPivot(array, pivot)
        
    def assertPivot(self, array, pivot):
        for i in range(0, pivot):
            self.assertLess(array[i], array[pivot],array)
        for i in range(pivot, len(array)):
            self.assertGreaterEqual(array[i], array[pivot], array)
        
    def test_rotated_list_4(self):
        array = [4, 1, 2, 3]
        pivot = partition(array, 2)
        self.assertEqual(pivot, 1)
        self.assertPivot(array, pivot)

    def test_rotated_list__5(self):
        array = [4, 1, 5, 2, 3]
        pivot = partition(array, 3)
        self.assertEqual(pivot, 1)
        self.assertPivot(array, pivot)   
  
        
unittest.main()
