# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
# You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
# Grokking
# Leetcode https://leetcode.com/problems/sliding-window-maximum/
# Solution https://leetcode.com/problems/sliding-window-maximum/solution/
# Time Complexity O(N), since each element is processed exactly twice - it's index added and then removed from the deque.
# Space Complexity O(N), since O(N−k+1) is used for an output array and O(k) for a deque.


from collections import defaultdict, deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n*k == 0:
            return []
        if k == 1:
            return nums

        def clean_deq(i):
            # remove indexes that are outside the window
            if deq and deq[0] == i-k:
                deq.popleft()

            # remove indexes of all elements that are
            # smaller than the current window
            while deq and nums[i] > deq[-1]:
                deq.pop()

        # initialize deq and output
        # first index of this queue will store the
        # largest element of our window
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deq(i)
            deq.append(i)

            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        for i in range(k, n):
            clean_deq(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output


sol = Solution()
print("[1,3,-1,-3,5,3,6,7], 3: ",
      sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print("[1], 1: ",
      sol.maxSlidingWindow([1], 1))
