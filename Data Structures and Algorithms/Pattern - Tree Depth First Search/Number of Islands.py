# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# Grokking
# Leetcode https://leetcode.com/problems/number-of-islands/
# Solution https://leetcode.com/problems/number-of-islands/solution/
# Time Complexity O(M×N) where M is the number of rows and N is the number of columns.
# Space Complexity O(min(M,N)) because in worst case where the grid is filled with lands, the size of queue can grow up to min(M,N).


from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        # 3- call dfs form main method
        for r in range(rows):
            for c in range(cols):
                islands += self.dfs(grid, r, c)

        return islands

    def dfs(self, grid, row, col):
        # 1- check the terminating condition
        if row < 0 or row >= len(grid):
            return 0
        elif col < 0 or col >= len(grid[0]):
            return 0
        elif grid[row][col] == '0':
            return 0
        # 2- do the dfs
        # elif grid[row][col] == '1': # don't need to this check because its the only condition left
        # set that element to 0 otherwise we'll keep on looping and visiting the same elements
        grid[row][col] = '0'
        self.dfs(grid, row+1, col)
        self.dfs(grid, row-1, col)
        self.dfs(grid, row, col+1)
        self.dfs(grid, row, col-1)
        return 1


sol = Solution()
print(sol.numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], [
      "1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
print(sol.numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], [
      "0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
