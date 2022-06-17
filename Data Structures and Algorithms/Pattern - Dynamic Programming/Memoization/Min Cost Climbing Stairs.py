# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1. Return the minimum cost to reach the top of the floor.
# Grokking
# Leetcode https://leetcode.com/problems/min-cost-climbing-stairs/
# Solution https://leetcode.com/problems/min-cost-climbing-stairs/solution/
# Time Complexity The time complexity of the above algorithm is O(n).
# Space Complexity The space complexity of this algorithm is O(1).
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top of stair is one index more than the last index
        # cost to reach top of stair from that stair itself is 0
        cost.append(0)

        # back-calculate the cost for previous two steps from current step
        for i in range(len(cost)-3, -1, -1):
            # cost[i] = min(cost[i]+cost[i+1], cost[i]+cost[i+2])
            # better way of adding current cost
            cost[i] += min(cost[i+1], cost[i+2])
        # we can start either at index 0 or at index 1
        # return the minimum of both
        return min(cost[0], cost[1])


sol = Solution()
print("[10, 15, 20]: ", sol.minCostClimbingStairs([10, 15, 20]))
print("[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]: ",
      sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
