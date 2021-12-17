# Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. Return the numbers in the sorted order.
# ‘X’ is not necessarily present in the array.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/N8MJQNYyJPL
# Leetcode https://leetcode.com/problems/find-k-closest-elements/
# Solution https://leetcode.com/problems/find-k-closest-elements/solution/
# Time Complexity The time complexity of the above algorithm is O(logN + K). We need O(logN) for Binary Search and O(K) for finding the ‘K’ closest numbers
# using the two pointers.
# Space Complexity If we ignoring the space required for the output list, the algorithm runs in constant space O(1).
from heapq import *
from collections import deque


def find_closest_elements(arr, K, X):
    index = binary_search(arr, X)
    result = deque()
    left_pointer, right_pointer = index, index+1
    n = len(arr)
    for i in range(K):
        # check if two pointers satisfy given bounds
        # to maintain sorted order, we'll use appendleft and append for left_pointer and right_pointer
        if left_pointer >= 0 and right_pointer < n:
            diff_l = abs(arr[left_pointer]-X)
            diff_r = abs(arr[right_pointer]-X)
            if diff_l <= diff_r:
                result.appendleft(arr[left_pointer])
                left_pointer -= 1
            else:
                result.append(arr[right_pointer])
                right_pointer += 1
        elif left_pointer >= 0:
            result.appendleft(arr[left_pointer])
            left_pointer -= 1
        elif right_pointer < n:
            result.append(arr[right_pointer])
            right_pointer += 1
    return result


def binary_search(nums, target):
    start, end = 0, len(nums)-1
    while start <= end:
        mid = start+(end-start)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid+1
        else:
            end = mid-1
    if start > 0:
        return start-1
    return start


def main():
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
