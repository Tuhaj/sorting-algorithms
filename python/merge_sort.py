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
