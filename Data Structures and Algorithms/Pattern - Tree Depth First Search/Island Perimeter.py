# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# Grokking
# Leetcode https://leetcode.com/problems/number-of-islands/
# Solution https://leetcode.com/problems/number-of-islands/solution/
# Time Complexity O(M×N) where M is the number of rows and N is the number of columns.
# Space Complexity O(1). Only the result variable is updated and there is no other space requirement.


from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    if r == 0:
                        up = 0
                    else:
                        up = grid[r-1][c]

                    if c == 0:
                        left = 0
                    else:
                        left = grid[r][c-1]

                    if r == ROWS-1:
                        down = 0
                    else:
                        down = grid[r+1][c]

                    if c == COLS-1:
                        right = 0
                    else:
                        right = grid[r][c+1]

                    res += 4-(up+down+left+right)
        return res


sol = Solution()
print("[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]: ", sol.islandPerimeter(
    [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
print("[[1]]: ", sol.islandPerimeter([[1]]))
print("[[1,0]]: ", sol.islandPerimeter([[1, 0]]))
