
# Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/qVljv3Plr67
# Leetcode
# Solution
# Time Complexity Since we need to put only the top K2 numbers in the max-heap at any time, the time complexity of the above algorithm will be O(N*logK2).
# Space Complexity The space complexity will be O(K2), as we need to store the smallest ‘K2’ numbers in the heap.
from heapq import *

# maxheap based solution


def find_sum_of_elements_maxheap(nums, k1, k2):
    maxheap = []
    range_sum = 0
    # add smallest K2 elements in maxheap
    for i in range(len(nums)):
        if i < k2-1:
            heappush(maxheap, -nums[i])
        # if size of maxheap is greater than K2, keep only the smallest elements
        elif nums[i] < -maxheap[0]:
            heappop(maxheap)
            heappush(maxheap, -nums[i])
    # sum next K2-K1-1
    for _ in range(k2-k1-1):
        range_sum += -heappop(maxheap)
    return range_sum


def main():

    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements_maxheap([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements_maxheap([3, 5, 8, 7], 1, 4)))


main()
