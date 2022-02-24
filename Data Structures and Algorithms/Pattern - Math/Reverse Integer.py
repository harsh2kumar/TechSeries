# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
# Grokking
# Leetcode https://leetcode.com/problems/reverse-integer/
# Solution https://leetcode.com/problems/reverse-integer/solution/
# Time Complexity  O(log(x)). There are roughly log10 (x) digits in x.
# Space Complexity The space complexity is O(1).

class Solution:
    def reverse(self, x: int) -> int:
        rev, negative = 0, False
        INT_32 = 2**31
        if x < 0:
            negative = True
            x *= -1
        while x != 0:
            pop = x % 10
            x //= 10
            # check for max 32 bit integer
            if (rev > INT_32/10) or (x == INT_32/10 and pop > 7):
                return 0
            # check for min 32 bit integer
            # not necessary to check this condition since we are converting to positive number
            if (rev < (-INT_32-1)/10) or (x == (-INT_32-1)/10 and pop < -8):
                return 0
            rev = rev*10+pop
        if negative:
            rev *= -1
        return rev


sol = Solution()
print("123: ", sol.reverse(123))
print("-123: ", sol.reverse(-123))
print("120: ", sol.reverse(120))
print("1534236469: ", sol.reverse(1534236469))
