# Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.
# You can assume that the array does not have any duplicates.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/R1v4P0R7VZw
# Leetcode https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Solution https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solution/
# Time Complexity Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(logN)
# where ‘N’ is the total elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


def count_rotations(arr):
    # this question actually want us the find the minimum in array, total number of rotations is index of minimum element
    start, end = 0, len(arr)-1
    while start <= end:
        mid = start+(end-start)//2
        # check if element at mid is greater than next element
        if mid < end and arr[mid] > arr[mid+1]:
            # mid+1 is the smallest element, its index is the number of rotations
            return mid+1
        # check if element at mid is smaller than previous element
        elif mid >= start and arr[mid-1] > arr[mid]:
            # mid is the smallest element, its index is the number of rotations
            return mid
        if arr[start] <= arr[mid]:  # if left side is sorted, then pivot is on right side
            start = mid+1
        else:  # if right side is sorted, then pivot is on left side
            end = mid-1
    # array is not rotated
    return 0


def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))


main()
