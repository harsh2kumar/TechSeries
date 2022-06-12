# Given an integer x, return true if x is palindrome integer.
# Grokking
# Leetcode https://leetcode.com/problems/palindrome-number/
# Solution https://leetcode.com/problems/palindrome-number/solution/
# Time Complexity O(log_100_(n)).
# Space Complexity O(1).

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negative numbers are never palindromes
        if x < 0:
            return False
        # determine the divisor
        div = 1
        while x >= 10*div:
            div *= 10

        # while number is non-zero
        while x:
            right_digit = x % 10
            left_digit = x // div
            if left_digit != right_digit:
                return False
            # update value of number and div
            # remove leftmost and rightmost digit from the number
            x = (x % div) // 10
            # everytime we remove 2 digits from our number, hence we
            # divide our divisor by 100
            div /= 100
        # number is a palindrome
        return True


sol = Solution()
print("121: ", sol.isPalindrome(121))
print("-121: ", sol.isPalindrome(-121))
print("10: ", sol.isPalindrome(10))
