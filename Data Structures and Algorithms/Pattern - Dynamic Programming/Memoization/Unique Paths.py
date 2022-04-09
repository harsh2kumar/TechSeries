# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the
# bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time. Given the two integers m and n,
# return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# Grokking
# Leetcode https://leetcode.com/problems/unique-paths/
# Solution https://leetcode.com/problems/unique-paths/solution/
# Time Complexity The time complexity of the above algorithm is O(m*n).
# Space Complexity The space complexity of this algorithm is O(m+n).


class Solution:
    def uniquePaths(self, m: int, n: int, memo={}) -> int:
        # calculate key for given cell
        key = str(m) + ", " + str(n)
        # memoization
        if key in memo:
            return memo[key]
        if (m == 1 and n == 1):
            return 1
        if (m == 0 or n == 0):
            return 0
        key_inv = str(n) + ", " + str(m)
        # move right -> decrease m
        # move down -> decrease n
        memo[key] = self.uniquePaths(
            m-1, n, memo) + self.uniquePaths(m, n-1, memo)
        memo[key_inv] = memo[key]
        return memo[key]


sol = Solution()
print("3, 7: ", sol.uniquePaths(3, 7))
print("3, 2: ", sol.uniquePaths(3, 2))
print("18, 18: ", sol.uniquePaths(18, 18))
print("100, 100: ", sol.uniquePaths(100, 100))
print("100, 200: ", sol.uniquePaths(100, 200))
