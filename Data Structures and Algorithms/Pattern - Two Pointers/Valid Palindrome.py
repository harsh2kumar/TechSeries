# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same
# forward and backward. Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, or false otherwise.
# Grokking
# Leetcode https://leetcode.com/problems/valid-palindrome/
# Solution https://leetcode.com/problems/valid-palindrome/solution/
# Time Complexity The time complexity of the above algorithm will be O(N), where ‘N’ is the total number of alphanumeric characters in the given array.
# Space Complexity The algorithm runs in constant space O(1).


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1

        while i < j:
            while i < j and not self.isAlphaNum(s[i]):
                i += 1
            while i < j and not self.isAlphaNum(s[j]):
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1
        return True

    def isAlphaNum(self, c: str) -> bool:
        if (ord('a') <= ord(c) <= ord('z') or
            ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9')):
            return True
        return False


sol = Solution()


print("'A man, a plan, a canal: Panama': ",
      sol.isPalindrome("A man, a plan, a canal: Panama"))
print("'race a car': ", sol.isPalindrome("race a car"))
print("' ': ", sol.isPalindrome(" "))
