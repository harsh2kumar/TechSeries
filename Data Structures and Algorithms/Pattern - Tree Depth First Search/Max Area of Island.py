# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all
# four edges of the grid are surrounded by water. The area of an island is the number of cells with a value 1 in the island. Return the maximum area of an island in grid.
# If there is no island, return 0.
# Grokking
# Leetcode https://leetcode.com/problems/max-area-of-island/
# Solution https://leetcode.com/problems/max-area-of-island/solution/
# Time Complexity O(R*C), where R is the number of rows in the given grid, and C is the number of columns. We visit every square once.
# Space Complexity O(R*C), the space used by seen to keep track of visited squares, and the space used by the call stack during our recursion.

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        def area(row, col):
            if not (0 <= row < ROWS and 0 <= col < COLS
                    and ((row, col) not in seen) and grid[row][col]):
                return 0
            seen.add((row, col))

            return (1 + area(row+1, col) + area(row-1, col) + area(row, col-1) + area(row, col+1))

        return max(area(r, c)
                   for r in range(ROWS)
                   for c in range(COLS))


sol = Solution()
print("[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]: ", sol.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [
      0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
print("[[0,0,0,0,0,0,0,0]]: ", sol.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]))
