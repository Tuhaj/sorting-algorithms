require 'rspec'
require_relative 'merge_sort.rb'
describe "Merge sort" do
  it "check for array" do
    expect(merge_sort([1])).to eq([1])
  end

  it "sort simple array" do
    arr = [4,6,2,4,1]
    expect(merge_sort(arr)).to eq(arr.sort)
  end
end
