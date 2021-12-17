# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
# Grokking
# Leetcode https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
# Solution https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/solution/
# Time Complexity The time complexity of our algorithm will be O(N*logN + KlogN).
# Space Complexity The space complexity will be O(N) as, in the worst case, we need to store all the ‘N’ numbers in the HashMap.
from heapq import *
from collections import Counter


def find_least_distinct_elements(nums, k):
    # if number of elements to be removed is greater than length of array, return 0 as that'll the number of elements remaining
    if k > len(nums):
        return 0
    minheap = []
    # count frequency of elements
    ele_count = Counter(nums)
    distinct_ele_count = len(ele_count)
    # insert in minheap elements
    for ele, freq in ele_count.items():
        heappush(minheap, (freq, ele))
    # remove from minheap greedily
    # for least distinct elements, remove elements with lowest frequency first
    # increase the distinct_ele_count
    while k > 0 and minheap:
        freq, ele = heappop(minheap)
        k -= freq
        if k >= 0:
            distinct_ele_count -= 1
    return distinct_ele_count


def main():

    print("Least distinct numbers after removing K numbers: " +
          str(find_least_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Least distinct numbers after removing K numbers: " +
          str(find_least_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Least distinct numbers after removing K numbers: " +
          str(find_least_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))
    print("Least distinct numbers after removing K numbers: " +
          str(find_least_distinct_elements([5, 5, 4], 1)))
    print("Least distinct numbers after removing K numbers: " +
          str(find_least_distinct_elements([4, 3, 1, 1, 3, 3, 2], 3)))


main()
