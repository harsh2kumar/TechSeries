# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large,
# return the answer modulo 10^9 + 7.
# Grokking
# Leetcode https://leetcode.com/problems/sum-of-subarray-minimums/
# Solution https://leetcode.com/problems/sum-of-subarray-minimums/solution/
# Time Complexity The time complexity of O(N)
# Space Complexity The space complexity is O(N).

from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        result = 0
        arr.append(0)
        # we use monotonically increasing stack
        for i, ele in enumerate(arr):
            while stack and (ele < stack[-1][1] or i == len(arr)-1):
                index, num = stack.pop()
                # left length is from to the second last element's index
                # this is because after the second last element, it is the new minimum
                # for all previous subarrays
                if stack:
                    left_length = index - stack[-1][0]
                else:
                    left_length = index + 1
                right_length = i - index

                result += left_length*right_length*num
            stack.append((i, ele))
        return result % (10**9+7)


sol = Solution()
print("[3,1,2,4]: ", sol.sumSubarrayMins([3, 1, 2, 4]))
print("[11,81,94,43,3]: ", sol.sumSubarrayMins([11, 81, 94, 43, 3]))
