# You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci]. You have an array arr of length length with all zeros, and you
# have some operation to apply on arr. In the ith operation, you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.
# Return arr after applying all the updates.
# Grokking
# Leetcode https://leetcode.com/problems/range-addition/
# Solution https://leetcode.com/problems/range-addition/
# Time Complexity O(n)
# Space Complexity O(1)

from typing import List
import collections


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # brute force
        # result = [0]*length
        # for q in updates:
        #     start, end, val = q
        #     for i in range(start, end+1):
        #         result[i] += val
        # return result

        # prefix sum
        result = [0] * (length+1)
        # Just update the start index with +val and end+1 with -val as we need to see the effect till end. We will use the prefix sum to retrive the actual sum, later
        for start, end, inc in updates:
            result[start] += inc
            result[end+1] -= inc
        # Iterte over the array again and get the prefix sum. This time we need to iterate form second element onwards
        for i in range(1, length+1):
            result[i] += result[i-1]

        # We do not need to return the last element as we have already created this array with one extra size. This extra size was to do the prefix sum
        # and access the end+1 index
        return result[:length]


sol = Solution()
print("5, [[1,3,2],[2,4,3],[0,2,-2]]",
      sol.getModifiedArray(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]))
print("10, [[2,4,6],[5,6,8],[1,9,-4]]",
      sol.getModifiedArray(10, [[2, 4, 6], [5, 6, 8], [1, 9, -4]]))
