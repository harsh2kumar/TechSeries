# Given an m x n matrix, return all elements of the matrix in spiral order.
# Grokking
# Leetcode https://leetcode.com/problems/spiral-matrix/
# Solution https://leetcode.com/problems/spiral-matrix/solution/
# Time Complexity The time complexity of O(M.N)
# Space Complexity The space complexity is O(1).

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows, columns = len(matrix), len(matrix[0])

        up, left = 0, 0
        down, right = rows-1, columns-1

        while len(result) < rows*columns:
            # Traverse from left to right
            for col in range(left, right+1):
                result.append(matrix[up][col])

            # Traverse downwards
            # up+1 because we have already traversed the upper row once
            for row in range(up+1, down+1):
                result.append(matrix[row][right])

            # Traverse from right to left
            # make sure that we are on a different row
            if up != down:
                for col in range(right-1, left-1, -1):
                    result.append(matrix[down][col])

            # Traverse upwards
            # make sure that we are on a different column
            # we don't use (up-1) in for loop because, we've
            # already traversed it once from left to right
            if left != right:
                for row in range(down-1, up, -1):
                    result.append(matrix[row][left])

            # update the boundaries
            up += 1
            left += 1
            right -= 1
            down -= 1

        return result


sol = Solution()


print("[[1,2,3],[4,5,6],[7,8,9]]: ", sol.spiralOrder(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print("[[1,2,3,4],[5,6,7,8],[9,10,11,12]]: ", sol.spiralOrder(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
