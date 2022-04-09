# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two
# preceding ones, starting from 0 and 1. Given n, calculate F(n).
# Grokking
# Leetcode https://leetcode.com/problems/fibonacci-number/
# Solution https://leetcode.com/problems/fibonacci-number/solution/
# Time Complexity The time complexity of the above algorithm is O(n).
# Space Complexity The space complexity of this algorithm is O(n).


class Solution:
    def fib(self, n: int, memo={}) -> int:
        # memoization
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n <= 2:
            return 1
        # pass in the memo object
        memo[n] = self.fib(n-1, memo) + self.fib(n-2, memo)
        return memo[n]


sol = Solution()
print("0: ", sol.fib(0))
print("2: ", sol.fib(2))
print("4: ", sol.fib(4))
print("10: ", sol.fib(10))
print("50: ", sol.fib(50))
print("100: ", sol.fib(100))
