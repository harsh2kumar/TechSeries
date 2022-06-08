# Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two
# elements of this subarray is less than or equal to limit.
# Grokking
# Leetcode https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
# Solution https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/solution/
# Time Complexity The time complexity of O(N)
# Space Complexity The space complexity is O(N).

import sys
from typing import List
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque, max_deque = deque(), deque()
        l = r = 0
        result = 0

        while r < len(nums):
            # min_deque is monotonically increasing
            # keep on removing elements until that property is maintained
            while min_deque and nums[r] <= nums[min_deque[-1]]:
                min_deque.pop()
            # max_deque is monotonically decreasing
            # keep on removing elements until that property is maintained
            while max_deque and nums[r] >= nums[max_deque[-1]]:
                max_deque.pop()
            # append current index to both queues
            min_deque.append(r)
            max_deque.append(r)

        # if the limit condition is not satisfied, start increasing left pointer
            while nums[max_deque[0]]-nums[min_deque[0]] > limit:
                l += 1
                if l > min_deque[0]:
                    min_deque.popleft()
                if l > max_deque[0]:
                    max_deque.popleft()

            result = max(result, r-l+1)
            r += 1
        return result


sol = Solution()
print("[8,2,4,7], 4: ", sol.longestSubarray([8, 2, 4, 7], 4))
print("[10,1,2,4,7,2], 5: ", sol.longestSubarray([10, 1, 2, 4, 7, 2], 5))
print("[4,2,2,2,4,4,2,2], 0: ", sol.longestSubarray(
    [4, 2, 2, 2, 4, 4, 2, 2], 0))
