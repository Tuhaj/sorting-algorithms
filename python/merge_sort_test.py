import unittest
from merge_sort import sort
from merge_sort import merge

class TestMergeSort(unittest.TestCase):
    """run with: python -m unittest merge_sort_test.py"""
    def test_if_sorted(self):
        array = [4,6,2,4,1]
        sorted_array = array.copy()
        sorted_array.sort()
        self.assertEqual(sort(array), sorted_array)

    def test_if_sorted_for_different_array(self):
        array = [8,7,6,5,4,3,2,1]
        sorted_array = array.copy()
        sorted_array.sort()
        self.assertEqual(sort(array), sorted_array)

    def test_on_small_array(self):
        array = [2,1]
        sorted_array = array.copy()
        sorted_array.sort()
        self.assertEqual(sort(array), sorted_array)


    def test_merge(self):
        left_side = [1,3,5,7]
        right_side = [2,4,6]
        merged = merge(left_side, right_side)
        self.assertEqual(merged, [i for i in range(1,8)])

if __name__ == '__main__':
    unittest.main()


