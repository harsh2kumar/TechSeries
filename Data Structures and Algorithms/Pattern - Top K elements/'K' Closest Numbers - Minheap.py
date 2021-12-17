# Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. Return the numbers in the sorted order.
# ‘X’ is not necessarily present in the array.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/N8MJQNYyJPL
# Leetcode https://leetcode.com/problems/find-k-closest-elements/
# Solution https://leetcode.com/problems/find-k-closest-elements/solution/
# Time Complexity The time complexity of the add() function will be O(logK) since we are inserting the new number in the heap.
# Space Complexity The space complexity will be O(K) for storing numbers in the heap.
from heapq import *


def find_closest_elements(arr, K, X):
    index = binary_search(arr, X)
    low, high = index-K, index+K

    low = max(low, 0)  # 'low' should not be less than zero
    # 'high' should not be greater the size of the array
    high = min(high, len(arr) - 1)

    minheap = []
    # add all candidate elements to the min heap, sorted by their absolute difference from 'X'
    for i in range(low, high+1):
        heappush(minheap, (abs(arr[i]-X), arr[i]))

    # we need the top 'K' elements having smallest difference from 'X'
    result = []
    for _ in range(K):
        result.append(heappop(minheap)[1])

    result.sort()
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
