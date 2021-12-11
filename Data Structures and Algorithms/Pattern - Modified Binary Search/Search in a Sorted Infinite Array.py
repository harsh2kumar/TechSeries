# Given an infinite sorted array (or an array with unknown size), find if a given number ‘key’ is present in the array.
# Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/B1ZW38kXJB2
# Leetcode https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/
# Solution https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/solution/
# Time Complexity Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(logN)
# where ‘N’ is the total elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


import math


class ArrayReader:

    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):
    # find the proper bounds first
    start, end = 0, 1
    while key > reader.get(end):
        new_start = end+1
        end = (end-start+1)*2
        start = new_start
    return binary_search(reader, start, end, key)


def binary_search(reader, start, end, key):
    while start <= end:
        mid = start+(end-start)//2
        if key < reader.get(mid):
            end = mid-1
        elif key > reader.get(mid):
            start = mid+1
        else:
            return mid
    return -1


def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader, 16))
    print(search_in_infinite_array(reader, 11))
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))


main()
