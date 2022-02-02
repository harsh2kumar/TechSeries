# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].
# Grokking
# Leetcode https://leetcode.com/problems/flood-fill/
# Solution https://leetcode.com/problems/flood-fill/solution/
# Time Complexity O(N), where N is the number of pixels in the image. We might process every pixel.
# Space Complexity O(N), the size of the implicit call stack when calling dfs.


from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        if image[sr][sc] == newColor:
            return image
        self.dfs(image, sr, sc, image[sr][sc], newColor)
        return image

    def dfs(self, image, row, col, current_color, new_color):
        if row >= 0 and col >= 0 and row < len(image) and col < len(image[0]) and image[row][col] == current_color:
            image[row][col] = new_color
            self.dfs(image, row+1, col, current_color, new_color)
            self.dfs(image, row-1, col, current_color, new_color)
            self.dfs(image, row, col+1, current_color, new_color)
            self.dfs(image, row, col-1, current_color, new_color)


sol = Solution()
print(sol.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
print(sol.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 2))
