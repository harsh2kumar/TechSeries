# Given a string s, return the longest palindromic substring in s.
# Grokking
# Leetcode https://leetcode.com/problems/longest-palindromic-substring/
# Solution https://leetcode.com/problems/longest-palindromic-substring/solution/
# Time Complexity The time complexity of O(N^2)
# Space Complexity The space complexity is O(1).


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, res_len = "", 0

        def isPalindrome(left, right):
            nonlocal res, res_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > res_len:
                    res = s[left:right+1]
                    res_len = right-left+1
                left -= 1
                right += 1

        for i in range(len(s)):
            # odd length
            left, right = i, i
            isPalindrome(left, right)

            # even length
            left, right = i, i+1
            isPalindrome(left, right)
        return res


sol = Solution()
print("babad: ", sol.longestPalindrome("babad"))
print("cbbd: ", sol.longestPalindrome("cbbd"))
