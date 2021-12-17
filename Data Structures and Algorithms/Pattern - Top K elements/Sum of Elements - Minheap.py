
# Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/qVljv3Plr67
# Leetcode
# Solution
# Time Complexity Since we need to put all the numbers in a min-heap, the time complexity of the above algorithm will be O(N*logN) where ‘N’ is the total input numbers.
# Space Complexity The space complexity will be O(N), as we need to store all the ‘N’ numbers in the heap.
from heapq import *

# minheap based solution


def find_sum_of_elements_minheap(nums, k1, k2):
    minheap = []
    range_sum = 0
    # add all elements in minheap
    for i in nums:
        heappush(minheap, i)
    # remove K1 smallest elements from minheap
    for _ in range(k1):
        heappop(minheap)
    # add elements between K1 and K2, i.e. sum next K2-K1-1 numbers
    for _ in range(k2-k1-1):
        range_sum += heappop(minheap)
    return range_sum


def main():

    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements_minheap([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements_minheap([3, 5, 8, 7], 1, 4)))


main()
