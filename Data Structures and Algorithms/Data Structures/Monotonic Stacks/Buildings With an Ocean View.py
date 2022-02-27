# There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line. The ocean is to the right
# of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to
# its right have a smaller height. Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.
# Grokking
# Leetcode https://leetcode.com/problems/buildings-with-an-ocean-view/
# Solution https://leetcode.com/problems/buildings-with-an-ocean-view/solution/
# Time Complexity The time complexity of O(N)
# Space Complexity The space complexity is O(N).

from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        view = []
        stack = []
        n = len(heights)
        # use monnotonically decreasing stacks
        # start from the right most building
        for i in reversed(range(n)):
            # pop off buildings with height smaller than
            # current building
            while stack and heights[i] > heights[stack[-1]]:
                stack.pop()
            # if stack is empty, then no building is blocking the view of current building
            # add it to list of buildings with ocean view
            if not stack:
                view.append(i)
            # add current building to stack as it could block view of a building to its left
            stack.append(i)
        # return reversed list of views
        view.reverse()
        return view


sol = Solution()
print("[4,2,3,1]: ", sol.findBuildings([4, 2, 3, 1]))
print("[4,3,2,1]: ", sol.findBuildings([4, 3, 2, 1]))
print("[1,3,2,4]: ", sol.findBuildings([1, 3, 2, 4]))
