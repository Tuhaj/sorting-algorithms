
def merge(left_side, right_side)
  arr = []
  left = right = 0
  max_left = left_side.size - 1
  max_right = right_side.size - 1

  while left <= max_left and right <= max_right
    if left_side[left] <= right_side[right]
      arr << left_side[left]
      left += 1
    else
      arr << right_side[right]
      right += 1
    end
  end
  arr += Array(left_side[left..-1])
  arr += Array(right_side[right..-1])
end

def merge_sort(arr)
  return arr if arr.size < 2
  mid = arr.size / 2
  left_side = merge_sort(arr[0...mid])
  right_side = merge_sort(arr[mid..-1])
  merge(left_side, right_side)
end
