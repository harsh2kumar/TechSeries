# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
# Grokking
# Leetcode https://leetcode.com/problems/largest-rectangle-in-histogram/
# Solution https://leetcode.com/problems/largest-rectangle-in-histogram/solution/
# Time Complexity O(n). n numbers are pushed and popped.
# Space Complexity O(n). Stack is used.

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # pair(index, height)

        for i, h in enumerate(heights):
            start = i  # mark the start of current rectangle
            # use monotonically increasing stack
            # we need to make sure the new bar added is taller than
            # top of stack
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # calculate max_area
                max_area = max(max_area, height*(i-index))
                # push the start index all the way back
                start = index
            stack.append((start, h))

        # recalculate max area for the remaining histograms
        # these were able to be extended all the way through the complete width of
        # our histogram
        for i, h in stack:
            max_area = max(max_area, h*(len(heights)-i))
        return max_area


sol = Solution()
print("[2,1,5,6,2,3]: ", sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))
print("[2,4]: ", sol.largestRectangleArea([2, 4]))
