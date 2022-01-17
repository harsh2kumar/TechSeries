# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Grokking
# Leetcode https://leetcode.com/problems/container-with-most-water/
# Solution https://leetcode.com/problems/container-with-most-water/solution/
# Time Complexity The time complexity of O(N)
# Space Complexity The space complexity is O(1).

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        left, right = 0, len(height)-1
        while left < right:
            water = max(water, (right-left)*min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return water


sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(sol.maxArea([1, 1]))
