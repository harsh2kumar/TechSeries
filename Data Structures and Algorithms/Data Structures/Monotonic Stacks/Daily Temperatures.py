# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait
# after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
# Grokking
# Leetcode https://leetcode.com/problems/daily-temperatures/
# Solution https://leetcode.com/problems/daily-temperatures/solution/
# Time Complexity The time complexity of O(N)
# Space Complexity The space complexity is O(N).

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        # we'll use Monotonically decreasing stacks to find the next greater temperature in future
        stack = []  # contains tuple (temperature, index)

        for i, current_temp in enumerate(temperatures):
            # if current temp is greater than top of stack temperature
            while stack and current_temp > stack[-1][0]:
                temp, index = stack.pop()
                # calculate num of days till next higher temperature
                res[index] = i-index
            # append current temperature and index to stack
            stack.append((current_temp, i))
        return res


sol = Solution()
print("[73,74,75,71,69,72,76,73]: ", sol.dailyTemperatures(
    [73, 74, 75, 71, 69, 72, 76, 73]))
print("[30,40,50,60]: ", sol.dailyTemperatures([30, 40, 50, 60]))
print("[30,60,90]: ", sol.dailyTemperatures([30, 60, 90]))
