require 'rspec'
require_relative 'merge_sort.rb'
# run with:
# rspec merge_sort_test.rb


describe "Merge sort" do
  it "check for one element array" do
    expect(merge_sort([1])).to eq([1])
  end

  it "sort simple array" do
    arr = [4,6,2,4,1]
    expect(merge_sort(arr)).to eq(arr.sort)
  end

  it "sort reverse sorted array" do
    arr = [8,7,6,5,4,3,2,1]
    expect(merge_sort(arr)).to eq(arr.sort)
  end

  it "merge two arrays" do
    left_side = [1,3,5,7]
    right_side = [2,4,6]
    merged_array = left_side + right_side
    expect(merge(left_side, right_side)).to eq(merged_array.sort)
  end

  it "sort two element array" do
    arr = [2,1]
    expect(merge_sort(arr)).to eq(arr.sort)
  end
end
