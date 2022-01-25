# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# Grokking
# Leetcode https://leetcode.com/problems/rotate-image/
# Solution https://leetcode.com/problems/rotate-image/solution/
# Time Complexity The time complexity of O(N), where N is the number of cells in the grid
# Space Complexity The space complexity is O(1).

from typing import List


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)
        return matrix

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]


sol = Solution()
print("[[1, 2, 3], [4, 5, 6], [7, 8, 9]]: ", sol.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print("[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]: ", sol.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))
