# Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.
# How do we find the rotation count of a sorted and rotated array that has duplicates too?
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/R1v4P0R7VZw#Problem-1
# Leetcode https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
# Solution https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/solution/
# Time Complexity Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(logN)
# where ‘N’ is the total elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


def count_rotations_with_duplicates(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        # if element at mid is greater than the next element
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid + 1
        # if element at mid is smaller than the previous element
        if mid > start and arr[mid - 1] > arr[mid]:
            return mid

        # this is the only difference from the previous solution
        # if numbers at indices start, mid, and end are same, we can't choose a side
        # the best we can do is to skip one number from both ends if they are not the smallest number
        if arr[start] == arr[mid] and arr[end] == arr[mid]:
            if arr[start] > arr[start + 1]:  # if element at start+1 is not the smallest
                return start + 1
            start += 1
            if arr[end - 1] > arr[end]:  # if the element at end is not the smallest
                return end
            end -= 1
        # left side is sorted, so the pivot is on right side
        elif arr[start] < arr[mid] or (arr[start] == arr[mid] and arr[mid] > arr[end]):
            start = mid + 1
        else:  # right side is sorted, so the pivot is on the left side
            end = mid - 1

    return 0  # the array has not been rotated


def main():
    print(count_rotations_with_duplicates([3, 3, 7, 3]))


main()
