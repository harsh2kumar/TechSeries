# You are given an array of integers stones where stones[i] is the weight of the ith stone. Check Notion for Problem Statement.
# Grokking
# Leetcode https://leetcode.com/problems/last-stone-weight/
# Solution https://leetcode.com/problems/last-stone-weight/solution/
# Time Complexity The time complexity of O(NlgN)
# Space Complexity The space complexity is O(N).

from typing import List
from heapq import *


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = [stone*-1 for stone in stones]
        heapify(max_heap)
        while len(max_heap) > 1:
            stone_1, stone_2 = -heappop(max_heap), -heappop(max_heap)
            if stone_1 > stone_2:
                heappush(max_heap, -(stone_1-stone_2))
        return -max_heap[0] if max_heap else 0


sol = Solution()
print("[2,7,4,1,8,1]: ", sol.lastStoneWeight([2, 7, 4, 1, 8, 1]))
print("[1]: ", sol.lastStoneWeight([1]))
