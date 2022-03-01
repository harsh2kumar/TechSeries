# Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such
# subarray, return -1. A subarray is a contiguous part of an array.
# Grokking
# Leetcode https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
# Solution https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/solution/
# Time Complexity The time complexity of O(N)
# Space Complexity The space complexity is O(N).

import sys
from typing import List
from collections import deque


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        # sliding window won't work because we have negative numbers
        # when a number is removed from our window, we don't know whether
        # the total sum will increase(negative num) or decrease(positive num).

        # Hence, we need to use increasing monotonic queue
        # we calculate pre-sum/ prefix sum for all elements in our array
        n = len(A)

        # initialize prefix sum with first element of A
        prefix_sum = [0]
        # populate prefix_sum
        for i in range(n):
            prefix_sum.append(prefix_sum[-1]+A[i])

        # initialize answer and inc_mono_q
        min_window = sys.maxsize
        inc_mono_q = deque()
        # calculate shortest window where the sum is at least K
        for window_end, ele in enumerate(prefix_sum):
            # if the sum is greater than or equal to K
            # we can shrink our window
            while inc_mono_q and ele-prefix_sum[inc_mono_q[0]] >= K:
                min_window = min(min_window, window_end-inc_mono_q.popleft())

            # remove all elements in mono queue which are less than current element
            while inc_mono_q and ele <= prefix_sum[inc_mono_q[-1]]:
                inc_mono_q.pop()

            inc_mono_q.append(window_end)

        return min_window if min_window < sys.maxsize else -1


sol = Solution()
print("[1], 1: ", sol.shortestSubarray([1], 1))
print("[1,2], 4: ", sol.shortestSubarray([1, 2], 4))
print("[2,-1,2], 3: ", sol.shortestSubarray([2, -1, 2], 3))
print("[84,-37,32,40,95], 167: ",
      sol.shortestSubarray([84, -37, 32, 40, 95], 167))
