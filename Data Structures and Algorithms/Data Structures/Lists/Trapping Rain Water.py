# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# Grokking
# Leetcode https://leetcode.com/problems/trapping-rain-water/
# Solution https://leetcode.com/problems/trapping-rain-water/solution/
# Time Complexity O(N)
# Space Complexity O(1)


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        ans = 0
        left_max, right_max = 0, 0

        while left < right:
            # a taller bar exists on left pointers right side
            # hence water trapped will be on the shorter side i.e. left side
            if height[left] < height[right]:
                # is there a taller bar on left side
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max-height[left]
                left += 1
            # a taller bar exists on right pointers left side
            # hence water trapped will be on the shorter side i.e. right side
            else:
                # is there a taller bar on right side
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max-height[right]
                right -= 1
        return ans


sol = Solution()


print([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], ": ",
      sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print([4, 2, 0, 3, 2, 5], ": ", sol.trap([4, 2, 0, 3, 2, 5]))
