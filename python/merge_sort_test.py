import unittest

def merge(left_side, right_side):
    array = []
    left = 0
    right = 0
    while left < len(left_side) and right < len(right_side):
        left_el = left_side[left]
        right_el = right_side[right]
        if left_el < right_el:
            array.append(left_el)
            left += 1
        else:
            array.append(right_el)
            right += 1
    array += left_side[left:]
    array += right_side[right:]
    return array


def sort(array):
    if (len(array) == 1):
        return array
    mid = len(array) // 2
    left_side = sort(array[:mid])
    right_side = sort(array[mid:])
    return merge(left_side, right_side)


class TestMergeSort(unittest.TestCase):
    """docstring for TestMergeSort"""
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


