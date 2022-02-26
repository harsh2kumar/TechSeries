# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
# Grokking
# Leetcode https://leetcode.com/problems/reverse-integer/
# Solution https://leetcode.com/problems/reverse-integer/solution/
# Time Complexity O(log(n)).
# Space Complexity O(log(n)).

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calculate(base, exponent):
            # base case
            if base == 0:
                return 0
            if base == 1 or exponent == 0:
                return 1
            result = calculate(base, exponent//2)
            result = result*result
            return result if exponent % 2 == 0 else result*base
        return calculate(x, abs(n)) if n > 0 else 1/(calculate(x, abs(n)))


sol = Solution()
print("2.00000, 10: ", sol.myPow(2.00000, 10))
print("2.10000, 3: ", sol.myPow(2.10000, 3))
print("2.00000, -2: ", sol.myPow(2.00000, -2))
