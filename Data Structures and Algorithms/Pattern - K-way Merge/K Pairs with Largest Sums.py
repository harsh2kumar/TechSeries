# Given two sorted arrays in descending order, find ‘K’ pairs with the largest sum where each pair consists of numbers from both the arrays.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/B1JKxRB8EDJ
# Leetcode
# Solution
# Time Complexity The time complexity of the above algorithm will be O(N*M*logK) where ‘N’ and ‘M’ are the total number of elements in both arrays.
# Space Complexity The space complexity will be O(K) because, at any time, our Min Heap will be storing ‘K’ largest pairs.
from heapq import *


def find_k_largest_pairs(nums1, nums2, k):
    minheap = []
    for i in range(0, min(k, len(nums1))):
        for j in range(min(k, len(nums2))):
            if len(minheap) < k:
                heappush(minheap, (nums1[i] + nums2[j], i, j))
            else:
                # if the sum of the two numbers from the two arrays is smaller than the smallest(top)
                # element of the heap, we can 'break' here. Since the arrays are sorted in the
                # descending order, we'll not be able to find a pair with a higher sum moving forward
                if nums1[i] + nums2[j] < minheap[0][0]:
                    break
                else:  # we have a pair with a larger sum, remove top and insert this pair in the heap
                    heappop(minheap)
                    heappush(minheap, (nums1[i] + nums2[j], i, j))

    result = []
    for (num, i, j) in minheap:
        result.append([nums1[i], nums2[j]])

    return result


def main():
    print("Pairs with largest sum are: " +
          str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()
