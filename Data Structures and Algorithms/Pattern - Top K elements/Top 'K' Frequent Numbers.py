# Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/B89rvR6XZ3J
# Leetcode https://leetcode.com/problems/top-k-frequent-elements/
# Solution https://leetcode.com/problems/top-k-frequent-elements/solution/
# Time Complexity The time complexity of the above algorithm is O(N+N*logK).
# Space Complexity The space complexity will be O(N). Even though we are storing only ‘K’ numbers in the heap. For the frequency map, however,
# we need to store all the ‘N’ numbers.
from heapq import *
from collections import Counter


def find_k_frequent_numbers(nums, k):

    minheap = []
    top_k = []
    # find frequency of each elemenr
    nums_dict = Counter(nums)

    # add elements from nums_dict in minheap
    # if length of minheap>k, remove element with smallest freq from minheap
    # in the end, we'll have the highest occurring elements
    for ele, freq in nums_dict.items():
        heappush(minheap, (freq, ele))
        if len(minheap) > k:
            heappop(minheap)
    while minheap:
        top_k.append(heappop(minheap)[1])
    return top_k


def main():

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()
