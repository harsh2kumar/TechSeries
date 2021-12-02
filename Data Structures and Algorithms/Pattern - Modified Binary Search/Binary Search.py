# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. 
# Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity.
# Grokking 
# Leetcode https://leetcode.com/problems/binary-search/
# Solution https://leetcode.com/problems/binary-search/solution/
# Time Complexity Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(logN)
# where ‘N’ is the total elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


def binary_search(arr, key):
    start, end = 0, len(arr)-1
    # check if the array is ascending or descending
    is_ascending = arr[start] < arr[end]

    while start <= end:
        # calculate the middle of the current range
        mid = start + (end-start)//2
        if arr[mid] == key:
            return mid
        if key < arr[mid]:
            end = mid - 1  # the 'key' can be in the first half
        else:  # key > arr[mid]
            start = mid + 1  # the 'key' can be in the second half
    return -1


def main():
    print(binary_search([-1, 0, 3, 5, 9, 12], 9))
    print(binary_search([-1, 0, 3, 5, 9, 12], 2))


main()
