# Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers from the array such that we are left with maximum distinct numbers.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/gx6oKY8PGYY
# Leetcode
# Solution
# Time Complexity The time complexity of our algorithm will be O(N*logN + KlogN).
# Space Complexity The space complexity will be O(N) as, in the worst case, we need to store all the ‘N’ numbers in the HashMap.
from heapq import *
from collections import Counter


def find_maximum_distinct_elements(nums, k):
    # if number of elements to be removed is greater than length of array, return 0 as that'll the number of elements remaining
    if k > len(nums):
        return 0
    distinct_ele_count = 0
    minheap = []
    # count frequency of elements
    ele_count = Counter(nums)
    # insert in minheap elements if freq>1
    # increase distinct element count if freq==1
    for ele, freq in ele_count.items():
        if freq == 1:
            distinct_ele_count += 1
        else:
            heappush(minheap, (freq, ele))
    # remove from minheap greedily
    # for maximum distinct elements, remove all duplicate occurrences except one
    # increase the distinct_ele_count
    while k > 0 and minheap:
        freq, ele = heappop(minheap)
        k -= freq-1
        if k >= 0:
            distinct_ele_count += 1
    # if we still need to remove elements, start removing distinct elements
    if k > 0:
        distinct_ele_count -= k
    return distinct_ele_count


def main():

    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()
