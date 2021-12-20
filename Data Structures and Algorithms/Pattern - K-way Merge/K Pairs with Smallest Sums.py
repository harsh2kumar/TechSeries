# Given two sorted arrays in ascending order, find ‘K’ pairs with the smallest sum where each pair consists of numbers from both the arrays.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/B1JKxRB8EDJ
# Leetcode https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
# Solution https://leetcode.com/problems/find-k-pairs-with-smallest-sums/solution/
# Time Complexity The time complexity of the above algorithm will be O(N*M*logK) where ‘N’ and ‘M’ are the total number of elements in both arrays.
# Space Complexity The space complexity will be O(K) because, at any time, our Min Heap will be storing ‘K’ smallest pairs.
from heapq import *


def find_k_largest_pairs(nums1, nums2, k):
    maxheap = []
    for i in range(0, min(k, len(nums1))):
        for j in range(min(k, len(nums2))):
            if len(maxheap) < k:
                heappush(maxheap, (-(nums1[i] + nums2[j]), i, j))
            else:
                # if the sum of the two numbers from the two arrays is greater than the largest(top)
                # element of the heap, we can 'break' here. Since the arrays are sorted in the
                # ascending order, we'll not be able to find a pair with a smaller sum moving forward
                if nums1[i] + nums2[j] > -maxheap[0][0]:
                    break
                else:  # we have a pair with a smaller sum, remove top and insert this pair in the heap
                    heappop(maxheap)
                    heappush(maxheap, (-(nums1[i] + nums2[j]), i, j))

    result = []
    for (num, i, j) in maxheap:
        result.append([nums1[i], nums2[j]])

    return result


def main():
    print("Pairs with largest sum are: " +
          str(find_k_largest_pairs([2, 8, 9], [1, 3, 6], 3)))


main()
