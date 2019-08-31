import unittest
from merge_sort import sort
from merge_sort import merge

class TestMergeSort(unittest.TestCase):
    """run with: python -m unittest merge_sort_test.py"""
    def test_if_sorted(self):
        list = [4,6,2,4,1]
        sorted_list = list.copy()
        sorted_list.sort()
        self.assertEqual(sort(list), sorted_list)

    def test_if_sorted_for_different_list(self):
        list = [8,7,6,5,4,3,2,1]
        sorted_list = list.copy()
        sorted_list.sort()
        self.assertEqual(sort(list), sorted_list)

    def test_two_element_list(self):
        list = [2,1]
        sorted_list = list.copy()
        sorted_list.sort()
        self.assertEqual(sort(list), sorted_list)

    def test_single_element_list(self):
        list = [1]
        sorted_list = list.copy()
        sorted_list.sort()
        self.assertEqual(sort(list), sorted_list)


    def test_merge(self):
        left_side = [1,3,5,7]
        right_side = [2,4,6]
        merged = merge(left_side, right_side)
        self.assertEqual(merged, [i for i in range(1,8)])

if __name__ == '__main__':
    unittest.main()


